import numpy as np

n = 48
k = 1000
sample_mean = [0]*k
sample_variance = [0]*k
sample_stddev = [0]*k
count = 0

for i in range(k):
	x = np.random.uniform(0,1,n)
	sample_mean[i] = np.sum(x)/n
	quad_err = np.power(x-sample_mean[i],2)
	sample_variance[i] = np.sum(quad_err)/(n-1)
	sample_stddev[i] = np.sqrt(sample_variance[i])
	#confidence interval at gamma=0.95
	eta = 1.96
	bound = eta*sample_stddev[i]/np.sqrt(n)
	#count how many times the true mean falls outside the CI
	if 0.5 < sample_mean[i]-bound or 0.5 > sample_mean[i]+bound:
		count += 1

print("Probability for the true mean to be outside the CI:",count*100/k,"%")
