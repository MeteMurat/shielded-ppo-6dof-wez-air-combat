import matplotlib.pyplot as plt

from Env import Env
from Agent import DoubleDQN
import numpy as np
import os
import time


def main(index):
    start_time_total = time.time()
    path = os.path.dirname(os.path.realpath(__file__))
    path = path+'/Record'+str(index)
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
        s = env.reset()
        if s is None:
            continue
        start_time = time.time()
        for ep_step in range(300):
            a = agent.get_action(s)
            if a == 4:
                attitude_record += 1
            s_, r, done = env.step(a)
            agent.store_transition(s, a, s_, r, done)
            reward_record.append(r)
            s = s_
            total_steps += 1
            if agent.train_it % 1000 == 1:
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

                # print(reward_record)
                print(' episode:', episode,
                      'ep_step:', ep_step,
                      ' train_step:', agent.train_it,
                      'left_blood:', env.red_blood, env.blue_blood,
                      ' attitude record: ', attitude_record,
                      ' win,loss,tight: ', win_count, loss_count, tight_count,
                      time.time() - start_time)
                break
    np.save(path+'/win_loss_tight.npy', np.array(win_loss_tight_record))
    print(time.time() - start_time_total)


if __name__ == '__main__':
    # process on i7-11700, simulation 0.67s, plus train 0.85s
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
    for i in range(10):
        main(i)
    # import matplotlib.pyplot as plt
   #  x = np.load('./Record0/win_loss_tight.npy')
     #print(x.shape)
    # win = x[:, 0]
    # loss = x[:, 1]
    # tight = x[:, 2]
    # plt.plot(win)
    # plt.plot(loss)
    # plt.plot(tight)
    #
    # plt.plot(win[1:] - win[:-1])
    # plt.show()