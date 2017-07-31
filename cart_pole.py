import argparse
import numpy as np
import gym

class BestConfig:

    def __init__(self, config, episode_return):
        self.config = config
        self.episode_return = episode_return

def run_episode(env, policy, render=False):
    done = False
    state = env.reset()
    cumulative_reward = 0
    while not done:
        if render:
            env.render()
        action = policy(state)
        (state, reward, done, _) = env.step(action)
        cumulative_reward += reward
    return cumulative_reward

def random_guessing(env, n=100):
    random_parameters = np.random.normal(size=(n,4))
    best_config = BestConfig(None, -float("inf"))
    for config in random_parameters:
        policy = lambda x : 1 if np.dot(config, x) > 0 else 0
        episode_return = run_episode(env, policy)
        if episode_return > best_config.episode_return:
            best_config = BestConfig(config, episode_return)
    best_policy = lambda x : 1 if np.dot(best_config.config, x) > 0 else 0
    run_episode(env, best_policy, render=True)

def hill_climbing(env, n=100):
    config = np.random.normal(scale=0.25, size=4)
    policy = lambda x : 1 if np.dot(config, x) > 0 else 0
    episode_return = run_episode(env, policy)
    for episode_i in range(n):
        noise = np.random.normal(scale=0.25, size=4)
        updated_config = config + noise
        updated_policy = lambda x : 1 if np.dot(updated_config, x) > 0 else 0
        updated_episode_return = run_episode(env, updated_policy)
        if updated_episode_return > episode_return:
            config = updated_config
            episode_return = updated_episode_return
    run_episode(env, policy, render=True)

def policy_gradient(env):
    pass

def main(algorithm_type):
    env = gym.make('CartPole-v0')
    if algorithm_type == 'guess':
        random_guessing(env)
    elif algorithm_type == 'climb':
        hill_climbing(env)
    elif algorithm_type == 'gradient':
        policy_gradient(env)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm_type', type=str, default='guess',
                      help='identifies algorithm to run on CartPole-v0')
    args = parser.parse_args()
    main(args.algorithm_type)
