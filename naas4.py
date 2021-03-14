import numpy as np

n = 11
a = 0
b = 1
true_mean = (a+b)/2
true_variance = np.power(b-a,2)/12
chi_avg_points1 = [18.307,31.41,43.773,55.758,67.505,79.082,90.531,101.879,113.145,124.342]
chi_avg_points2 = [3.94,10.851,18.493,26.509,34.764,43.188,51.739,60.391,69.126,77.929]

i = 0
while n<=101:
	x = np.random.uniform(a,b,n) #generate n uniform and independent RVs
	sample_mean = np.sum(x)/n
	sample_variance = np.sum(np.power(x-sample_mean,2))/(n-1)
	print("Sample mean:",sample_mean,"and sample variance:",sample_variance)
	#mse_sample_mean = 1/n * np.sum(np.power(sample_mean-true_mean,2))
	#print("MSE of sample mean:",mse_sample_mean)
	#mse_sample_variance = 1/n * np.sum(np.power(sample_variance-true_variance,2))
	#print("MSE of sample_variance:",mse_sample_variance)
	#upper and lower bound for 95% CI of variance
	lb = (n-1)*sample_variance/chi_avg_points1[i]
	ub = (n-1)*sample_variance/chi_avg_points2[i]
	print("Variance CI: [",lb,";",ub,"]")
	n += 10
	i += 1
