This file explains the data, the calculations, and the resolt.
The data is a real example from our lab, which investigates chaos.

IN SIMPLE WORDS- There are certain conditions under which a particle create a shape that has a non integer dimension, differently from the common values we familiar with, such as 1, 2 or 3 dimenstional shapes.
This special shape is the "trajectory" ploted in the graph.

The Output- is the incomplete DIMENSION.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Data & Calculations: 

The data splites into 2 parts:
    1. part 1 (Trajectory)
        a. "x" - position of a particle 
        b. "p" - momentum of the particle (like velocity)
    2. part 2 (Data)
        c. "N_axis" 
        d. "n_unique" 
        this data is yielded by an algorithm developed in our lab, which apllied to the "x" and "p", returning 2 vectors c and d. 

The calculation steps which done on c and d :
    1. taking the logarithm in exponential basis of c and d
    2. Calculating the derivative (change) of one in respect to another 
    3. Truncate all the values smaller then 1 
    4. Taking the average value, this value it the dimension