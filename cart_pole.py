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

def random_guessing(env, n=10000):
    random_parameters = np.random.normal(size=(n,4))
    best_config = BestConfig(None, -float("inf"))
    for config in random_parameters:
        policy = lambda x : 1 if np.dot(config, x) > 0 else 0
        episode_return = run_episode(env, policy)
        if episode_return > best_config.episode_return:
            best_config = BestConfig(config, episode_return)
    best_policy = lambda x : 1 if np.dot(best_config.config, x) > 0 else 0
    run_episode(env, best_policy, render=True)


def hill_climbing(env):
    pass

def policy_gradient(env):
    pass

def main(algorithm_type):
    env = gym.make('CartPole-v0')
    if algorithm_type == 'random_guessing':
        random_guessing(env)
    elif algorithm_type == 'hill_climbing':
        hill_climbing(env)
    elif algorithm_type == 'policy_gradient':
        policy_gradient(env)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm_type', type=str, default='random_guessing',
                      help='identifies algorithm to run on CartPole-v0')
    args = parser.parse_args()
    main(args.algorithm_type)
