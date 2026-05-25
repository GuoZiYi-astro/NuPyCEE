def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.5: 
      return 1*mass**-2.7
    elif mass < 1: 
      return 1.5157165665103982*mass**-2.1
    else: 
      return 1.5157165665103982*mass**-2.5
