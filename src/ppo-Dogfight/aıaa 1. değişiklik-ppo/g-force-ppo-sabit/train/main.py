import matplotlib.pyplot as plt

from Env import Env
from Agent import DoubleDQN
from ppo_agent import PPOAgent  # PPO Agent sınıfını ekledik
import numpy as np
import os
import time

def main(index):
    start_time_total = time.time()
    path = os.path.dirname(os.path.realpath(__file__))
    path = path+'/Record'+str(index)
    if not os.path.exists(path):
        os.makedirs(path)

    agent_dqn = DoubleDQN(path)  # Mevcut DoubleDQN ajanı
    agent_ppo = PPOAgent(state_dim=13, action_dim=8)  # PPO ajanını tanımladık
    env = Env()
    total_steps = 0
    episode = 0
    store_index = 0
    win_count = 0
    loss_count = 0
    tight_count = 0

    win_loss_tight_record = []

    while agent_dqn.train_it < 30000:
        episode += 1
        attitude_record = 0
        reward_record = []
        s = env.reset()
        if s is None:
            continue
        start_time = time.time()
        for ep_step in range(300):
            # PPO ajanı ile eylem seçimi
            a_ppo = agent_ppo.select_action(s)
            a_dqn = agent_dqn.get_action(s)
            
            # PPO ajanının seçimiyle adım atma
            s_, r, done = env.step(a_ppo)
            agent_ppo.store_transition(s, a_ppo, r, s_, done)

            # DQN ajanının seçimiyle adım atma
            s_, r, done = env.step(a_dqn)
            agent_dqn.store_transition(s, a_dqn, s_, r, done)

            reward_record.append(r)
            s = s_
            total_steps += 1

            if agent_dqn.train_it % 1000 == 1:
                win_loss_tight_record.append([win_count, loss_count, tight_count])
                agent_dqn.store_net(str(store_index))
                store_index += 1

            if done:
                if env.red_blood <= 0:
                    if env.blue_blood <= 0:
                        tight_count += 1
                    else:
                        win_count += 1
                else:
                    loss_count += 1

                print()
                print(' episode:', episode,
                      'ep_step:', ep_step,
                      ' train_step:', agent_dqn.train_it,
                      'left_blood:', env.red_blood, env.blue_blood,
                      ' attitude record: ', attitude_record,
                      ' win,loss,tight: ', win_count, loss_count, tight_count,
                      time.time() - start_time)
                break

        # PPO ajanını eğit
        agent_ppo.learn()

    np.save(path+'/win_loss_tight.npy', np.array(win_loss_tight_record))
    print(time.time() - start_time_total)

if __name__ == '__main__':
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
    for i in range(10):
        main(i)
