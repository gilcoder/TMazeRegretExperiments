from ai4u.gmproc.ga3c import A3CMaster, A3CWorker, Runner
from ai4u.gmproc import ClientServer
import gym
import os
import shutil
import setup
import numpy as np

def env_maker(name):
	return gym.make(name, max_steps=200, rewards={(1, 2): -30, (2, 2): 20}) #rewards={(1, 2): 30, (2, 2): 20} | rewards={(1, 2): -30, (2, 2): 20}

def train(n_workers = 4, use_saved_model=False, max_ep = 10000):
	if os.path.exists('./logs'):
		shutil.rmtree('./logs')
	os.mkdir('logs')
	params = {}
	params['env_name'] = "TMazeRLEnv-v0"
	env = gym.make(params['env_name'])
	params['state_size'] = env.observation_space.shape[0]
	params['action_size'] = env.action_space.n
	params['update_freq'] = 30
	params['entropy_bonus'] = 0.01
	params['value_loss_coef'] = 0.5
	params['learning_rate'] = 0.001
	params['max_grad_norm'] = 5
	params['gamma'] = 0.90
	params['env_maker'] = env_maker
	params['debug_freq'] = 10
	params['log_bsize'] = 1000
	params['log_verbose'] = True
	params['max_ep'] = max_ep
	params['model_save_freq'] = 1
	if use_saved_model:
		params['load_model'] = "model"
	cs = ClientServer(A3CMaster)
	cs.new_workers(n_workers, A3CWorker, params=params)
	cs.run(params=params)

def test():
	params = {}
	params['env_name'] = "TMazeRLEnv-v0"
	env = gym.make(params['env_name'])
	params['state_size'] = env.observation_space.shape[0]
	params['action_size'] = env.action_space.n
	params['load_model'] = "model"
	params['env_maker'] = env_maker
	runner = Runner(params=params)
	runner.run()

	states = [(0, 0), (0, 1), (0, 2), (0, 3),  (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0,9), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
	for s in states:
		l, v = runner.get_model_output( np.array(list(s)) )
		p = runner.get_actions_prob(l)
		print(s, ': ', v.numpy(), ", ", p.numpy())

if __name__=="__main__":
	#train(max_ep=2400)
	#train(1, True, 90)
	test()
