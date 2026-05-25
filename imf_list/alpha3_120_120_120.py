def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return mass**-1.2000000000000002
    elif mass < 0.5: 
      return 1.0*mass**-1.2000000000000002
    else: 
      return 1.0*mass**-1.2000000000000002
