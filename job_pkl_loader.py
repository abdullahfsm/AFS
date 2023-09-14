import pickle
import os, sys
import matplotlib.pyplot as plt
from sim import Job
import numpy as np

def sched_history_marker(job):
	sched_history = job.sched_history
	gpus = [sh[1] for sh in sched_history]
	times = [sh[0] for sh in sched_history] + [job.ts_current]

	m1 = (np.diff(gpus) < 0).any()

	area_under_curve = np.dot(gpus[1:],np.diff(times)[1:])
	max_area = sum(np.diff(times)[1:])*max(gpus[1:]) 

	m2 = area_under_curve/max_area < 0.75


	m3 = len(gpus) < 10

	# print(np.diff(times)[1:])

	return m1 and m2 and True


if __name__ == '__main__':

	vc = "ee9e8c"
	alg = "SRSF_ELASTIC"

	path = f'/users/abdffsm/schedsim/job_sched_history_{vc}_{alg}.pkl'
	path2 = f'/users/abdffsm/schedsim/sched_sched_history_{vc}_{alg}.pkl'



	with open(path2,'rb') as fp:
		availability_history = pickle.load(fp)


	# FIFO
	# file = "job=12590"
	# file = "job=14133"
	# file = "job=11627"
	# file = "job=12693"
	

	# SRSF
	# job=1004
	# job=1128
	# job=130
	# job=1349
	# job=1087


	# job loader
	with open(path,'rb') as fp:
		jobs = pickle.load(fp)


	print(len(jobs))

	# jobs = list(filter(lambda j: len(j.sched_history) == 5, jobs))
	
	# jobs = list(filter(lambda j: j.max_gpus > 3, jobs))
	jobs = list(filter(lambda j: sched_history_marker(j), jobs))

	jobs_dict = {}

	for job in jobs:
		jobs_dict[job.jid] = job

	print(len(jobs))

	job = np.random.choice(jobs)
	# job = jobs_dict[1727]
	# job = jobs_dict[1774]

	print(job.jid)

	X = []
	Y = []
	
	# for entry in job.sched_history[1:]:

	sidx = None
	for i, entry in enumerate(job.sched_history):
		if entry[0] == job.ts_init_scheduled:
			sidx = i
			break
	
	for entry in job.sched_history[sidx:]:
		X.append(entry[0])
		Y.append(entry[1])


	X.append(job.ts_current)
	Y.append(Y[-1])


	min_x, max_x = X[0], X[-1]
	

	X = [int((x)/60.0) for x in X]
	

	availability_history = list(filter(lambda t: t[0] >= min_x, availability_history))
	availability_history = list(filter(lambda t: t[0] <= max_x, availability_history))

	X2 = []
	Y2 = []
	for entry in availability_history:
		X2.append(entry[0])
		Y2.append(entry[1])


	X2 = [int((x)/60.0) for x in X2]

	
	# plt.xticks(X,rotation='vertical')
	# plt.yticks(Y)

	plt.step(X,Y,where='post',color='red')
	
	print(np.diff(X)[1:])
	print(Y[1:-1])

	plt.step(X2,Y2,where='post',color='grey')
	# plt.title(f"Sched History Job={job.jid}")
	

	plt.savefig("/users/abdffsm/schedsim/job_sched_history.png",dpi=300)
	# plt.savefig(path.replace('pkl','png'),dpi=300)






