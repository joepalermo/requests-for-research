import argparse
import gym

def random_guessing():
    pass

def hill_climbing():
    pass

def policy_gradient():
    pass

def main(algorithm_type):
    env = gym.make('CartPole-v0')
    if algorithm_type == 'random_guessing':
        random_guessing()
    elif algorithm_type == 'hill_climbing':
        hill_climbing()
    elif algorithm_type == 'policy_gradient':
        policy_gradient()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm_type', type=str, default='random_guessing',
                      help='identifies algorithm to run on CartPole-v0')
    args = parser.parse_args()
    main(args.algorithm_type)
