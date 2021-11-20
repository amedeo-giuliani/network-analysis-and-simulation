import numpy as np

n = 100
data = np.random.uniform(0,1,n)
r = 10000
alpha = 0.05
lb_arr = []
ub_arr = []

for i in range(r):
    x = np.random.choice(data,size=100,replace=True)
    x = np.sort(x)
    lb_arr.append(x[int(np.floor((n+1)*alpha/2))])
    ub_arr.append(x[int(np.ceil((n+1)*(1-alpha/2)))])

print('bootstrap results')
lb = np.mean(lb_arr)
ub = np.mean(ub_arr)
print(lb)
print(ub)

print('from theory')
data = np.sort(data)
lb = data[int(np.floor((n+1)*alpha/2))]
ub = data[int(np.ceil((n+1)*(1-alpha/2)))]
print(lb)
print(ub)