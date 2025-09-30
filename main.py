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
# - wind speed (we assume it will be a float number)
# - rated power, with a default value: 15,
# - cut-in wind speed, with a default value: 3,
# - rated wind speed, with a default value: 11,
# - cut-out wind speed, with a default value: 25,
# - interpolation option, a string to define the interpolation method, can only be
# - "linear" or "cubic", with a default value: "linear".


def output_WTpower(v: float | int,
                   rated_power: float = 15, # Rated power in [MW] units
                   cutin_ws: float = 3, # cut-in wind speed [m/s] units
                   rated_ws: float = 11, # rated wind speed [m/s] units
                   cutout_ws: float = 25, # cut-out wind speed [m/s] units
                   interp_method: str = "linear") -> float:
    
    """Calculation of the power output of a wind turbine with the arguments provided
    taking into account two interpolation options: linear or cubic. If the interpolation
    chosen is not linear or cubic shows a message error"""

# Asking the user if he/she wishes to use cubic interpolation 
# or linear as default. Error message if is not a linear/cubic interpolation 
# answered by user
    if interp_method.lower() not in ["linear", "cubic"]:
        raise ValueError("Incorrect interpolation, please choose linear or cubic")
    
    power_output = 0 # Initialization of the variable, [MW] units
    
# For cubic interpolation the weighting function is calculated like this:
    if interp_method == "cubic":
        g_v = v**3 / rated_ws**3
    
# For linear interpolation the weighting function is calculated like this:
    elif interp_method == "linear":
        g_v = (v-cutin_ws) / (rated_ws - cutin_ws)

# Calculating power output depending on wind speed value provided by the user
    if v < cutin_ws or v >= cutout_ws: # Turbine stopped due to low wind
        power_output = O
        
    elif cutin_ws <= v < rated_ws:  # Turbine generating below rated power
        power_output = g_v * rated_power
        
    elif rated_ws <= v < cutout_ws:  # Turbine generating rated power
        power_output = rated_power
    
    return power_output

if __name__ == '__main__':
    
    # Calculation of power output with linear interpolation, v=9 [m/s] units 
    v = float(input(f'Please enter a wind speed value:'))       
    #v = 9 # wind speed test value, in [m/s] units
    
    power_output_lin = output_WTpower(v, interp_method = "linear")
    print(f'For a wind speed of {v} [m/s] using linear interpolation, the power output is: {power_output_lin:.2f} [MW] units')
    
    # Calculation of power output with cubic interpolation, v=9 [m/s] units
    power_output_cub = output_WTpower(v, interp_method = "cubic")
    print(f'For a wind speed of {v} [m/s] using cubic interpolation, the power output is: {power_output_cub:.2f} [MW] units')
    

# Pendent, what happens for ws < cut-in value and ws > cut-out value



## Script requirements    
# Returns the computed power output using the model and the inputs.
# Have proper docstring and several (at least 3) comments to explain the 
# function.
# Include error handling by raising proper error when the user gives an invalid 
# input 
# for the string defining the interpolation option.
# You should also write the main script to run your function for at least one 
# example. 
# These can be done in one script that looks like the following:

# def add_two(x, y):
#    """
#    Docstring here.
#    """
#    # Add comment if needed.
#    result = x +  y # Add comment if needed.

#    return result

#if __name__ == '__main__':
    # Write the main script to use the function here:
#    x = 1
#    y = 1

    # Add comments to explain if needed.
#    z = add_two(x, y)
#    print(f'x + y = {z}')  # Add comment when needed