def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.5: 
      return 1*mass**-1.3
    elif mass < 1: 
      return 0.5358867312681466*mass**-2.2
    else: 
      return 0.5358867312681466*mass**-1.5
