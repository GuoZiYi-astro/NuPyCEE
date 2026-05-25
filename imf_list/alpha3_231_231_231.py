def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return mass**-2.3111111111111113
    elif mass < 0.5: 
      return 1.0*mass**-2.3111111111111113
    else: 
      return 1.0*mass**-2.3111111111111113
