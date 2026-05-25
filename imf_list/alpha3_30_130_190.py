def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return mass**-0.3
    elif mass < 0.5: 
      return 0.08*mass**-1.3
    else: 
      return 0.052780316430915776*mass**-1.9
