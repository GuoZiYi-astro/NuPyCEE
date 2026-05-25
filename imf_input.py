def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return mass**-0.3
    elif mass < 0.5: 
      return mass**-1.3
    else: 
      return mass**-2.3
