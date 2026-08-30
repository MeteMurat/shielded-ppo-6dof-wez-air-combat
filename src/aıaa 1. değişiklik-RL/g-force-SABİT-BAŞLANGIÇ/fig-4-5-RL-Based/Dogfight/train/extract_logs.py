import numpy as np
import os
from Env import Env
from Agent import DoubleDQN

def extract_episode(record_index=8, model_file='49.pth', episode=1):
    path = os.path.dirname(os.path.realpath(__file__))
    record_path = os.path.join(path, f'Record{record_index}')
    agent = DoubleDQN(record_path)

    # Özel model dosyasını yükle
    agent.load_net('49')  # sadece prefix olarak ver


    env = Env()
    s = env.reset()
    if s is None:
        print("Reset failed, try again.")
        return

    for step in range(300):
        a = agent.get_action(s)
        s_, r, done = env.step(a)
        s = s_
        if done:
            break

    if all(len(log) > 0 for log in [
        env.ata_red_log, env.ata_blue_log, env.distance_log,
        env.mach_red_log, env.mach_blue_log,
        env.height_red_log, env.height_blue_log]):

        np.save(record_path + f'/ATA_red_ep{episode}.npy', np.array(env.ata_red_log))
        np.save(record_path + f'/ATA_blue_ep{episode}.npy', np.array(env.ata_blue_log))
        np.save(record_path + f'/distance_ep{episode}.npy', np.array(env.distance_log))
        np.save(record_path + f'/mach_red_ep{episode}.npy', np.array(env.mach_red_log))
        np.save(record_path + f'/mach_blue_ep{episode}.npy', np.array(env.mach_blue_log))
        np.save(record_path + f'/height_red_ep{episode}.npy', np.array(env.height_red_log))
        np.save(record_path + f'/height_blue_ep{episode}.npy', np.array(env.height_blue_log))

        print(f"Log files saved to Record{record_index}/ for episode {episode}")
    else:
        print("Warning: Logs are empty, nothing saved.")

if __name__ == '__main__':
    extract_episode(record_index=8, model_file='49.pth', episode=1)
