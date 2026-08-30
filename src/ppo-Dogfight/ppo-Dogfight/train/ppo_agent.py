import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

class PolicyNetwork(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )

    def forward(self, x):
        return self.fc(x)

class ValueNetwork(nn.Module):
    def __init__(self, state_dim):
        super(ValueNetwork, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        return self.fc(x)

class PPOAgent:
    def __init__(self, state_dim, action_dim, clip_epsilon=0.3, gamma=0.95, lr=5e-4):
        self.policy_net = PolicyNetwork(state_dim, action_dim)
        self.value_net = ValueNetwork(state_dim)
        self.optimizer_policy = optim.Adam(self.policy_net.parameters(), lr=lr)
        self.optimizer_value = optim.Adam(self.value_net.parameters(), lr=lr)
        self.clip_epsilon = clip_epsilon
        self.gamma = gamma
        self.memory = []

    def store_transition(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def compute_advantages(self, rewards, values, dones):
        advantages = []
        gae = 0
        for i in reversed(range(len(rewards))):
            delta = rewards[i] + self.gamma * values[i + 1] * (1 - dones[i]) - values[i]
            gae = delta + self.gamma * gae * (1 - dones[i])
            advantages.insert(0, gae)
        return advantages

    def learn(self):
        states, actions, rewards, next_states, dones = zip(*self.memory)
        self.memory = []

        states = torch.tensor(np.array(states), dtype=torch.float32)
        actions = torch.tensor(actions, dtype=torch.long)
        rewards = torch.tensor(rewards, dtype=torch.float32)
        next_states = torch.tensor(np.array(next_states), dtype=torch.float32)
        dones = torch.tensor(dones, dtype=torch.float32)

        values = self.value_net(states).squeeze()
        next_values = self.value_net(next_states).squeeze()

        advantages = self.compute_advantages(rewards, torch.cat([values, next_values[-1:]]), dones)
        advantages = torch.tensor(advantages, dtype=torch.float32).detach()
        returns = (advantages + values).detach()

        old_probs = self.policy_net(states).gather(1, actions.unsqueeze(1)).detach()

        # Optimize Policy Loss
        for _ in range(10):
            probs = self.policy_net(states).gather(1, actions.unsqueeze(1))
            ratio = (probs / old_probs).squeeze()

            surr1 = ratio * advantages
            surr2 = torch.clamp(ratio, 1 - self.clip_epsilon, 1 + self.clip_epsilon) * advantages

            policy_loss = -torch.min(surr1, surr2).mean()

            self.optimizer_policy.zero_grad()
            policy_loss.backward()
            self.optimizer_policy.step()

        # Optimize Value Loss
        for _ in range(10):
            value_loss = nn.MSELoss()(self.value_net(states).squeeze(), returns)

            self.optimizer_value.zero_grad()
            value_loss.backward()
            self.optimizer_value.step()

    def select_action(self, state):
        state = torch.tensor(state, dtype=torch.float32).unsqueeze(0)
        probs = self.policy_net(state).detach().numpy().flatten()
        action = np.random.choice(len(probs), p=probs)
        return action
