import numpy as np
import json

record = []
for i in range(400):
    position_red = [np.random.rand() * 6000 - 3000,
                    np.random.rand() * 6000 - 3000,
                    np.random.rand() * 5000 - 8000]
    position_blue = [np.random.rand() * 6000 - 3000,
                     np.random.rand() * 6000 - 3000,
                     np.random.rand() * 5000 - 8000]
    euler_red = [0, -0, (np.random.rand() * 2 - 1) * 180]
    euler_blue = [0, -0, (np.random.rand() * 2 - 1) * 180]
    mach_red = 0.9 - np.random.rand() * 0.6
    mach_blue = 0.9 - np.random.rand() * 0.6

    if np.linalg.norm(np.array(position_red) - np.array(position_blue)) <= 500:
        continue

    record.append([[position_red, euler_red, mach_red],
                   [position_blue, euler_blue, mach_blue]])

with open('./test_record.json', 'w') as f:
    json.dump(record, f)
