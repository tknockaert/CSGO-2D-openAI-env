import gym
import ma_gym

env = gym.make('Combat-v0')
done_n = [False for _ in range(env.n_agents)]
ep_reward = 0

obs_n = env.reset()
for i in range (0,10000):
    while not all(done_n):
        env.render()
        obs_n, reward_n, done_n, info = env.step(env.action_space.sample())
        ep_reward += sum(reward_n)
    obs_n = env.reset()
    done_n = [False for _ in range(env.n_agents)]
env.close()