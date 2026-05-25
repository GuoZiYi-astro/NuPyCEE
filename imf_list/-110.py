def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 1076750751.87094*mass**-0.3
    elif mass < 0.5: 
      return 142753634.208499*mass**-1.1
    else: 
      return 142753634.208499*mass**-1.1
