import pickle
import os, sys
import matplotlib.pyplot as plt
from sim import Job
import numpy as np

if __name__ == '__main__':

	path = '/users/abdffsm/schedsim/'

	files = list(filter(lambda f: "job=" in f, os.listdir(path)))


	file = np.random.choice(files)

	# FIFO
	# file = "job=12590"
	# file = "job=14133"
	# file = "job=11627"
	# file = "job=12693"
	

	print(path+file)
	with open(path+file,'rb') as fp:
		job = pickle.load(fp)

	X = []
	Y = []
	
	for entry in job.sched_history[1:]:
		X.append(entry[0])
		Y.append(entry[1])


	X.append(job.ts_current)
	Y.append(Y[-1])

	X = [int((x - X[0])/60.0) for x in X]

	
	plt.xticks(X,rotation='vertical')
	plt.yticks(Y)
	plt.step(X,Y,where='post',color='red')
	plt.title(f"Sched History Job={job.jid}")
	plt.savefig(f"{path}job_sched_history.png",dpi=300)






