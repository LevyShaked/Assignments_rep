import csv # to read csv data files accepted from the algorythm
import numpy as np # mathematical tool like logarithm
import matplotlib.pyplot as plt # ploting (the trajectory, which is the subject for the calculations)

#######################################
# data reader function
def file_reder(file,data) :
    with open(file) as csvfile :
        reader = csv.reader(csvfile)
        for row in reader:
            for value in row:
                data.append((float(value)))

######################################
# saving the data on vectors #

# the trajectory that the particle creats
x = [] # (position in time)
p = [] # (momentum (like velocity) in time)

# the data from the algorythm that analyze the trajectory
N_axis_vec = [] 
n_unique_vec = []

#######################################
# reding and placing the data on vectors
file_reder("N_axis_test.csv",N_axis_vec)
file_reder("n_unique_test.csv",n_unique_vec)
file_reder("x_test.csv",x)
file_reder("p_test.csv",p)

#######################################
# calculating the logarythm of each vector

log_N_axis = np.log(N_axis_vec)
log_n_unique = np.log(n_unique_vec)

#######################################
# calculating the derivative (the change itself) of log_n_unique in respect to log_n_unique

der_log_n_unique = (log_n_unique[1:] - log_n_unique[0:len(log_n_unique)-1])/(log_N_axis[1:]-log_N_axis[0:len(log_N_axis)-1])

#######################################
# calculating the dimension
# the dimension of the shape will be the mean value of the truncated decresed data (minimal value biger then ~1)

reduced_dim = []
for dim in der_log_n_unique :
    if dim > 0.95 :
        reduced_dim.append(dim)
    else :
        break

dimension = np.mean(reduced_dim)
dimension = round(dimension, 3)

def test():
    assert(abs(1-dimension) <0.05)

#######################################
# ploting the trajectory and presenting the dimension

plt.plot(x, p)
x = np.array(x)
p = np.array(p)
plt.xlabel('Position')
plt.ylabel('Momentum')
plt.title(f'Trajectory, Dimension = {dimension}')
plt.show()