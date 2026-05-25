def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 1*mass**-0.3
    elif mass < 0.5: 
      return 0.07999999999999999*mass**-1.3
    else: 
      return 0.049245776533796644*mass**-2.0
