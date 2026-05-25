def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.5: 
      return 1*mass**-0.3
    elif mass < 1: 
      return 0.5*mass**-1.3
    else: 
      return 0.5*mass**-2.7
