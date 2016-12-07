from multiprocessing import Pool
import numpy as np
import time


def test_function(x):
	return np.sin(x)

args=np.linspace(0,100,1e6)

start_time=time.time()
results=test_function(args)
print str(time.time()-start_time)+" s"
