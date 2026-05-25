def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return mass**-0.3
    elif mass < 0.5: 
      return 0.08*mass**-1.3
    else: 
      return 0.04924577653379665*mass**-2.0
