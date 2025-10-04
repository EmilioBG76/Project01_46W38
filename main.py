
# Defining a function that calculates the power output of a wind turbine based 
# on the arguments provided: power rated, wind speed, cut-in wind speed, 
# rated wind speed, cut-out wind speed and interpolation method: linear or cubic
# default is linear interpolation method

def output_WTpower(v: float | int,
                   power_rated: float = 15, # Rated power in [MW] units
                   ws_cutin: float = 3, # cut-in wind speed [m/s] units
                   ws_rated: float = 11, # rated wind speed [m/s] units
                   ws_cutout: float = 25, # cut-out wind speed [m/s] units
                   interp_method: str = "linear") -> float:
    
    """ Calculation of the power output of a wind turbine with the arguments 
    provided taking into account two interpolation options to be chosen: linear 
    or cubic. 
    If the interpolation method chosen is not linear or cubic asks again to the 
    user to enter a correct interpolation method.
    
    Args:
        v (float | int): _description_
        power_rated (float, optional): rated power. Defaults to 15 [MW]
        ws_cutin (float, optional): cut-in wind speed. Defaults to 3 [m/s] 
        ws_rated (float, optional): rated wind speed. Defaults to 11 [m/s]
        ws_cutout (float, optional): cut-out wind speed. Defaults to 25 [m/s]
        interp_method (str, optional): interpolation method. Defaults to "linear"
        Returning the power output in [MW] units.
        
    Raising a ValueError when user types a wrong interpolation method
    
    Output: Power output of a wind turbine"""
# Asking the user if he/she wishes to use cubic interpolation 
# or linear as default. if is not a linear/cubic interpolation answered by user
# Then user is asked to enter/choose again one of the two interpolation methods
    power_output = 0 # Initialization of the variable, [MW] units
    
# For cubic interpolation the weighting function is calculated like this:
    if interp_method == "cubic":
        g_v = v**3 / ws_rated**3
    
# For linear interpolation the weighting function is calculated like this:
    elif interp_method == "linear":
        g_v = (v - ws_cutin) / (ws_rated - ws_cutin)

# Calculating power output depending on wind speed value provided by the user
    if 0 < v < ws_cutin or v >= ws_cutout: # Turbine stopped due to low wind
        return 0 # When wind speed is below cut-in or above cut-out power is 0[MW] 
        
    elif ws_cutin <= v < ws_rated:  # Turbine generating below rated power
        power_output = g_v * power_rated
        
    elif ws_rated <= v < ws_cutout:  # Turbine generating rated power
        power_output = power_rated   
    return power_output

if __name__ == '__main__':   
    # Calculation of power output with linear interpolation, asking for v to user
    # If wind speed value entered is a mistake then show wrong input message
    while True:
        try:
            print("Welcome! We're going now to calculate the output power of a"\
" wind turbine for a given wind speed")    
            v = float(input(f'Please enter a wind speed value in [m/s] units:'))
            break      
        except ValueError: # If the user types wrong the ws wrong message shown
            print("Wrong input. Please enter again a value for wind speed.")
    # Asking the user for a linear or cubic interpolation method to be used
    while True:
        interp_method = input("Please choose now between linear or cubic"\
" interpolation method to be applied (linear by default):") 
    # Calculation of power output with linear interpolation
        if interp_method.lower() == "linear" or interp_method == "" or \
        interp_method.lower() == "l":
            power_output_lin = output_WTpower(v, interp_method = "linear")
            print(f'For a wind speed of {v} [m/s] using linear interpolation, \
the power output calculated is: {power_output_lin:.2f} [MW]')
    # Calculation of power output using cubic interpolation
        elif interp_method.lower() == "cubic" or interp_method.lower() == "c":
            power_output_cub = output_WTpower(v, interp_method = "cubic")
            print(f'For a wind speed of {v} [m/s] using cubic interpolation, \
the power output calculated is: {power_output_cub:.2f} [MW]')
        else:
            print("Invalid method. Please choose linear or cubic")
            continue
    # Asking the user if he/she wishes to calculate another power output
        while True:
            answer = str(input("Do yo wish to calculate another power output"\
" for a given wind speed value (Yes/No)?:)"))            
            if answer.lower() == "yes" or answer.lower() == "y":
                while True:
                    try:
                        v = float(input(f'Please enter another wind speed value:'))
                        break
                    except ValueError:
                        print("Wrong input. Please enter a valid wind speed value")
                break
            elif answer.lower() == "no" or answer.lower() == "n":
                break
            else:             
                print("Invalid input. Please answer Yes or No, thank you.")
        if answer.lower() == "no" or answer.lower() == "n":
            print("Thank you for using this program for power output calculation")
            break
    
