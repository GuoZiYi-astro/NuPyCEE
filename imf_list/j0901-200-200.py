def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.5: 
      return 1*mass**-2
    elif mass < 1: 
      return 1.0*mass**-2
    else: 
      return 1.0*mass**-2
