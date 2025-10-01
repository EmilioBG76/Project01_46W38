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
    
    """ Calculation of the power output of a wind turbine with the arguments provided
    taking into account two interpolation options to be chosen: linear or cubic. 
    If the interpolation method chosen is not linear or cubic asks again to the user
    to enter a correct interpolation method.
    
        Returning the power output in [MW] units.
        
        Raising a ValueError when user types a wrong interpolation method"""
# Asking the user if he/she wishes to use cubic interpolation 
# or linear as default. if is not a linear/cubic interpolation answered by user
# Then user is asked to enter/choose again one of the two interpolation methods
    power_output = 0 # Initialization of the variable, [MW] units
    
# For cubic interpolation the weighting function is calculated like this:
    if interp_method == "cubic":
        g_v = v**3 / rated_ws**3
    
# For linear interpolation the weighting function is calculated like this:
    elif interp_method == "linear":
        g_v = (v-cutin_ws) / (rated_ws - cutin_ws)

# Calculating power output depending on wind speed value provided by the user
    if v < cutin_ws or v >= cutout_ws: # Turbine stopped due to low wind
        return 0 # When wind speed is below cut-in or above cut-out power is 0[MW] 
        
    elif cutin_ws <= v < rated_ws:  # Turbine generating below rated power
        power_output = g_v * rated_power
        
    elif rated_ws <= v < cutout_ws:  # Turbine generating rated power
        power_output = rated_power
        
    elif v < 0:
        raise ValueError(f'wind speed v should be positive, please enter a valid value') 
    
    return power_output

if __name__ == '__main__':   
    # Calculation of power output with linear interpolation, asking for v to user
    # If value entered is a mistake then show wrong input message
    try:
        print("Welcome! We're going now to calculate the output power of a wind turbine for a given wind speed")    
        v = float(input(f'Please enter a wind speed value in [m/s] units:'))      
    except ValueError: # If the user types wrong the wind speed wrong message shown
        # Asking the user to enter again a correct value for wind speed
        print("Wrong input. Please enter again a value for wind speed.")
        v = float(input(f'Please enter a wind speed value:')) 
    #    exit()
    # Asking the user for a linear or cubic interp. method to use
    while True:
        interp_method = input("Please choose now between linear or cubic interpolation method to be applied (linear by default):") 
    # Calculation of power output with linear interpolation
        if interp_method.lower() == "linear" or interp_method == "" or interp_method.lower() == "l":
            power_output_lin = output_WTpower(v, interp_method = "linear")
            print(f'For a wind speed of {v} [m/s] using linear interpolation, the power output calculated is: {power_output_lin:.2f} [MW]')
            # Asking the user about re-calculating power output for another wind speed given
            answer = str(input("Do you wish to calculate another power output for a given wind speed value (Yes/No)?:"))
            
            if answer.lower() == "yes" or answer.lower() == "y":
                v = float(input(f'Please enter another wind speed value:')) 
            else:             
                break
    # Calculation of power output with cubic interpolation
        elif interp_method.lower()  == "cubic" or interp_method.lower() == "c":
            power_output_cub = output_WTpower(v, interp_method = "cubic")
            print(f'For a wind speed of {v} [m/s] using cubic interpolation, the power output calculated is: {power_output_cub:.2f} [MW]')
            # Asking the user about re-calculating power output for another wind speed given
            answer = str(input("Do you wish to calculate another power output for a given wind speed value (Yes/No)?:"))
            
            if answer.lower() == "yes" or answer.lower() == "y":
                v = float(input(f'Please enter another wind speed value:')) 
            else:             
                break
    



