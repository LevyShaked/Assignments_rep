import csv # to read csv data files accepted from the algorythm
import numpy as np # mathematical toold like logarythm
import matplotlib.pyplot as plt # ploting (the trajectory, which is the subject for the calculations)

# file to variables
def file_to_var():
    
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
    print("Please enter the relevant 4 csv files at the following order: \n\
        N_axis... .csv \n\
        n_unique... .csv \n\
        x... .csv \n\
        p... .csv ")

    N_axis_file = input("N_axis... .csv : ")
    n_unique_file = input("n_unique... .csv : ")
    x_file = input("x... .csv : ")
    p_file = input("p... .csv : ")

    file_reader(N_axis_file,N_axis_vec)
    file_reader(n_unique_file,n_unique_vec)
    file_reader(x_file,x)
    file_reader(p_file,p)

    return(N_axis_vec, n_unique_vec, x, p)
    
#######################################
# data reader function
def file_reader(file,data) :
    with open(file) as csvfile :
        reader = csv.reader(csvfile)
        for row in reader:
            for value in row:
                data.append((float(value)))

#######################################
# calculating the logarythm of each vector
def calculations(N_axis_vec, n_unique_vec):
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
    return(dimension)

def print_plot(dimension, x, p) :
    print(f'Dimension = {dimension}')

    #######################################
    # ploting the trajectory and presenting the dimension

    plt.plot(x, p)
    x = np.array(x)
    p = np.array(p)
    plt.xlabel('Position')
    plt.ylabel('Momentum')
    plt.title(f'Trajectory, Dimension = {dimension}')
    print("CLOSE THE PLOT TO EXIT PROGRAM")
    plt.show()