import matplotlib.pyplot as plt

from Env import Env
from Agent import DoubleDQN
import numpy as np
import os
import time


def main(index):
    start_time_total = time.time()
    path = os.path.dirname(os.path.realpath(__file__))
    path = path + '/Record' + str(index)
    if not os.path.exists(path):
        os.makedirs(path)

    agent = DoubleDQN(path)
    env = Env()
    total_steps = 0
    episode = 0
    store_index = 0
    win_count = 0
    loss_count = 0
    tight_count = 0

    win_loss_tight_record = []

    while agent.train_it < 50000:
        episode += 1
        attitude_record = 0
        reward_record = []

        # METRİK LOG'LARI
        ata_log = []
        distance_log = []
        mach_log = []
        height_log = []

        s = env.reset()
        if s is None:
            print("Episode skipped (reset returned None)")
            continue

        print(f"Episode {episode} started.")
        start_time = time.time()

        for ep_step in range(300):
            a = agent.get_action(s)
            if a == 4:
                attitude_record += 1

            s_, r, done, info = env.step(a)

            # METRİKLERİ LOG'LA
            ata_log.append(info["ata_blue"])
            distance_log.append(info["distance"])
            mach_log.append(info["mach_blue"])
            height_log.append(info["height_blue"])

            agent.store_transition(s, a, s_, r, done)

            # DEBUG LOG
            print(f"Step {ep_step} | Memory: {agent.memory.counter} | Train it: {agent.train_it}")

            reward_record.append(r)
            s = s_
            total_steps += 1

            if agent.train_it % 1000 == 1:
                print(f"Model checkpoint stored at step {agent.train_it}")
                win_loss_tight_record.append([win_count, loss_count, tight_count])
                agent.store_net(str(store_index))
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
                      ' train_step:', agent.train_it,
                      'left_blood:', env.red_blood, env.blue_blood,
                      ' attitude record: ', attitude_record,
                      ' win,loss,tight: ', win_count, loss_count, tight_count,
                      time.time() - start_time)
                break

        # EPİZOD METRİKLERİNİ KAYDET
        np.savez(path + f'/episode_{episode}_metrics.npz',
                 ata=np.array(ata_log),
                 distance=np.array(distance_log),
                 mach=np.array(mach_log),
                 height=np.array(height_log))

    np.save(path + '/win_loss_tight.npy', np.array(win_loss_tight_record))
    print("Eğitim tamamlandı.")
    print("Toplam süre:", time.time() - start_time_total)


if __name__ == '__main__':
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
    for i in range(1):  # 1 deney çalıştırılması yeterli
        main(i)


    