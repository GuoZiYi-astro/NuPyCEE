def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return mass**-3.577777777777778
    elif mass < 0.5: 
      return 1.0*mass**-3.577777777777778
    else: 
      return 1.0*mass**-3.577777777777778
