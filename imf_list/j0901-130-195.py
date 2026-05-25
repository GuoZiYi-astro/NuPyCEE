def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.5: 
      return 1*mass**-1.3
    elif mass < 1: 
      return 0.6372803136596311*mass**-1.95
    else: 
      return 0.6372803136596311*mass**-1.95
