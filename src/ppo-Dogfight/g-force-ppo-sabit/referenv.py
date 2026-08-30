import numpy as np
from f16Model import F16
from controller import Controller
from strategy import Strategy
from util import feet2meter, rad2degree, xyz2llh, angle_error


class Env:
    def __init__(self, time_step=0.01):
        self.time_step = time_step
        self.red_fighter = F16(time_step=self.time_step)
        self.blue_fighter = F16(time_step=self.time_step)
        self.red_controller = Controller()
        self.blue_controller = Controller()
        self.red_strategy = Strategy()
        self.blue_strategy = Strategy()

        self.red_blood = self.red_blood_last = 1
        self.blue_blood = self.blue_blood_last = 1
        # only use for testing
        # self.record = []

    def reset(self, initial_condition=None, strategy_num=None):
        if initial_condition is None:
            fixed_mach = 0.7
        # Sabit pozisyonlar ve sabit yönler
            self.red_fighter.reset(
            position=np.array([0, -3000, -7000]),     # Red solda
            euler=np.array([0, 0, 45]),               # Kuzeydoğu
            mach=fixed_mach
            )
            self.blue_fighter.reset(
            position=np.array([-4000, 2000, -7000]),  # Blue sağda
            euler=np.array([0, 0, -135]),             # Güneybatı
            mach=fixed_mach
            )
        else:
            self.red_fighter.reset(position=np.array(initial_condition[0][0]),
                               euler=np.array(initial_condition[0][1]),
                               mach=initial_condition[0][2])
            self.blue_fighter.reset(position=np.array(initial_condition[1][0]),
                                euler=np.array(initial_condition[1][1]),
                                mach=initial_condition[1][2])

        red_position = self.red_fighter.position * feet2meter
        blue_position = self.blue_fighter.position * feet2meter
        los = red_position - blue_position
        distance = np.linalg.norm(los)
        if distance < 10:
            return None

        self.red_controller.reset()
        self.blue_controller.reset()
        if strategy_num is None:
            self.red_strategy.reset(strategy_num=[True, True, True, True])
            self.blue_strategy.reset(strategy_num=[True, True, True, True])
        else:
            self.red_strategy.reset(strategy_num=strategy_num)
            self.blue_strategy.reset(strategy_num=strategy_num)

        self.red_blood = self.red_blood_last = 1
        self.blue_blood = self.blue_blood_last = 1

        state, _ = self._state_reward(red_done=False, blue_done=False)
        return state


    def step(self, action):
        red_mode = self.red_strategy.process(self_fighter=self.red_fighter, target_fighter=self.blue_fighter)
        blue_mode = action + 1
        red_position = self.red_fighter.position * feet2meter
        blue_position = self.blue_fighter.position * feet2meter

        red_done = blue_done = False
        for i in range(100):
            red_u = self.red_controller.control(f16=self.red_fighter, position_target=blue_position, mode=red_mode)
            blue_u = self.blue_controller.control(f16=self.blue_fighter, position_target=red_position, mode=blue_mode)
            self.red_fighter.step(u=red_u)
            self.blue_fighter.step(u=blue_u)

            red_position = self.red_fighter.position * feet2meter
            blue_position = self.blue_fighter.position * feet2meter
            los = red_position - blue_position
            distance = (los[0] ** 2 + los[1] ** 2 + los[2] ** 2)**0.5

            if distance < 10:
                self.red_blood = self.blue_blood = 0
                red_done = blue_done = True
                break

            red_done = self.red_fighter.alpha * rad2degree > 45 or self.red_fighter.height < 10
            blue_done = self.blue_fighter.alpha * rad2degree > 45 or self.blue_fighter.height < 10
            if red_done or blue_done:
                self.red_blood = 0 if red_done else self.red_blood
                self.blue_blood = 0 if blue_done else self.blue_blood
                break

            if 100 < distance < 1000:
                red_ata = np.arccos(np.dot(self.red_fighter.heading, -los) / distance) * rad2degree
                blue_ata = np.arccos(np.dot(self.blue_fighter.heading, los) / distance) * rad2degree
                if red_ata < 2:
                    self.blue_blood -= self.time_step
                if blue_ata < 2:
                    self.red_blood -= self.time_step
                red_done = self.red_blood < 0
                blue_done = self.blue_blood < 0
                if red_done or blue_done:
                    break

        state, reward = self._state_reward(red_done=red_done, blue_done=blue_done)

        los = (self.red_fighter.position - self.blue_fighter.position) * feet2meter
        distance = np.linalg.norm(los)
        red_ata = np.arccos(np.dot(self.red_fighter.heading, -los) / distance) * rad2degree
        blue_ata = np.arccos(np.dot(self.blue_fighter.heading, los) / distance) * rad2degree
        mach_red = self.red_fighter.mach
        mach_blue = self.blue_fighter.mach
        height_red = self.red_fighter.height
        height_blue = self.blue_fighter.height

        info = {
            "distance": distance,
            "ata_red": red_ata,
            "ata_blue": blue_ata,
            "mach_red": mach_red,
            "mach_blue": mach_blue,
            "height_red": height_red,
            "height_blue": height_blue
        }

        return state, reward, red_done or blue_done, info

    def _state_reward(self, red_done, blue_done):
        los = (self.red_fighter.position - self.blue_fighter.position) * feet2meter
        distance = np.linalg.norm(los)

        hca = np.arccos(np.dot(self.red_fighter.heading, self.blue_fighter.heading))
        ata = np.arccos(np.dot(self.blue_fighter.heading, los) / distance)
        aa = np.arccos(np.inner(self.red_fighter.heading, los) / distance)

        pitch_d = np.arctan2(-los[2], (los[0]**2 + los[1]**2)**0.5)
        yaw_d = np.arctan2(los[1], los[0]) * rad2degree

        angle_self = np.array([self.blue_fighter.euler[0],
                               self.blue_fighter.euler[1],
                               self.blue_fighter.path_pitch])
        angle_relation1 = np.array([
            angle_error(self.blue_fighter.euler[2] * rad2degree, yaw_d),
            angle_error(self.blue_fighter.path_yaw * rad2degree, yaw_d)
        ])
        angle_relation2 = np.array([pitch_d, hca, ata, aa])

        state = np.concatenate([
            np.array([self.blue_fighter.height * feet2meter / 2000,
                      self.blue_fighter.ground_speed * feet2meter / 200]),
            angle_self / np.pi,
            angle_relation1 / 180,
            angle_relation2 / np.pi,
            np.array([distance / 2000,
                      self.red_fighter.ground_speed * feet2meter / 200])
        ])

        reward = 0
        if red_done or blue_done:
            if red_done:
                reward += 20
            if blue_done:
                reward -= 20
        else:
            reward += (self.red_blood_last - self.red_blood)
            reward -= (self.blue_blood_last - self.blue_blood)
            reward += (np.pi - ata - aa) / np.pi

        self.red_blood_last = self.red_blood
        self.blue_blood_last = self.blue_blood

        return state, reward

