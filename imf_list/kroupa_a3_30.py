def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 1*mass** -0.3
    elif mass < 0.5: 
      return 0.08*mass**-1.3
    else: 
      return 0.024622888266898325*mass**-3.0
