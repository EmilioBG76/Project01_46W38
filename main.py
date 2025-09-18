import numpy as np
import matplotlib.pyplot as plt

## Variables
# Power output P [MW]
# Wind speed at hub height v [m/s]
# Cp power coefficient that itself is a function of the v
# Rotor area of the turbine A [m2]
# Power rated of the turbine Prated [MW]
# Cut-in wind speed that denotes the minimal wind speed the turbine starts to 
# generate power v_in [m/s] 
# Cut-out wind speed that denotes the wind speed the turbine stops generating 
# power v_out [m/s]
# Rated wind speed that denotes the wind speed the turbine reaches the rated 
# power v_rated [m/s]
# Weighting function g(v) denotes the ratio of generated power to the rated power
# For linear interpolation g(v)=(v−v_in)/(v_rated−vin)
# For cubic interpolation g(v)=v^3/v^3_rated

## Write a function to calculate the power output by implementing the model 
# defined in the last section. 
# Your function need to fullfil the following requirements:
# wind speed (we assume it will be a float number)
# rated power, with a default value: 15,
# cut-in wind speed, with a default value: 3,
# rated wind speed, with a default value: 11,
# cut-out wind speed, with a default value: 25,
# interpolation option, a string to define the interpolation method, can only be
# "linear" or "cubic", with a default value: "linear".

# Assigment values to variables
P_rated = 15 # [MW] units
v_in = 3 # cut-in wind speed [m/s] units
v_rated = 11 # rated wind speed [m/s] units
v_out = 25 # cut-out wind speed [m/s] units

# Initializing variable for power curve
P_v = O 

# Asking the user to enter the wind speed [m/s]

v = float(input('Please enter the wind speed v[m/s]:'))

# Asking the user if he/she wish to use cubic interpolation

interporlation = input('Type "cubic" if you do not wish to use linear interpolation?')

# For cubic interpolation the weighting function is calculated like this:
        if interpolation == "cubic":
            g_v = v**3 / v_rated**3
    
# For linear interpolation the weighting function is calculated like this:
        else:
            g_v = (v-v_in) / (v_rated - v_in)


    if v < v_in or v >= v_out:
        P_v = O
    elif v_in <= v < v_rated:
        P_v = g_v * P_rated
    elif v_rated <= v < v_out
        P_v = P_rated
        
# Returns the computed power output using the model and the inputs.
    print(f'Then the power output is: {P_v} [MW]')
    
# Returns the computed power output using the model and the inputs.
# Have proper docstring and several (at least 3) comments to explain the 
# function.
# Include error handling by raising proper error when the user gives an invalid 
# input 
# for the string defining the interpolation option.

# You should also write the main script to run your function for at least one 
# example. 
# These can be done in one script that looks like the following:

def add_two(x, y):
    """
    Docstring here.
    """
    # Add comment if needed.
    result = x +  y # Add comment if needed.

    return result

if __name__ == '__main__':
    # Write the main script to use the function here:
    x = 1
    y = 1

    # Add comments to explain if needed.
    z = add_two(x, y)
    print(f'x + y = {z}')  # Add comment when needed