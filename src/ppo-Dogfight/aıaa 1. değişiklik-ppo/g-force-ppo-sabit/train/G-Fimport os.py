import os
import numpy as np
from Env import Env
from Agent import DoubleDQN
import time

def evaluate_g_force(model_prefix, model_path="Record9", record_dir="GForceTestResults", num_episodes=50):
    os.makedirs(record_dir, exist_ok=True)

    agent = DoubleDQN(path=model_path)
    agent.load_net(model_prefix)

    env = Env()

    for episode in range(1, num_episodes + 1):
        s = env.reset()
        if s is None:
            print(f"Episode {episode} skipped (invalid reset)")
            continue

        g_force_z_log = []
        g_force_y_log = []
        ata_log = []
        distance_log = []
        mach_log = []
        height_log = []

        for ep_step in range(300):
            a = agent.get_action(s)
            s_, r, done, info = env.step(a)

            g_force_z_log.append(info["g_force_z"])
            g_force_y_log.append(info["g_force_y"])
            ata_log.append(info["ata_blue"])
            distance_log.append(info["distance"])
            mach_log.append(info["mach_blue"])
            height_log.append(info["height_blue"])

            s = s_

            if done:
                break

        # Kaydet
        np.savez(os.path.join(record_dir, f"episode_{episode}_metrics.npz"),
                 g_force_z=np.array(g_force_z_log),
                 g_force_y=np.array(g_force_y_log),
                 ata=np.array(ata_log),
                 distance=np.array(distance_log),
                 mach=np.array(mach_log),
                 height=np.array(height_log))

        print(f"Episode {episode} finished and saved.")

if __name__ == "__main__":
    evaluate_g_force(model_prefix="30", model_path="Record5", record_dir="GForceTestResults", num_episodes=50)


