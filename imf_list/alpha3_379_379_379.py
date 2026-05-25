def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return mass**-3.7888888888888888
    elif mass < 0.5: 
      return 1.0*mass**-3.7888888888888888
    else: 
      return 1.0*mass**-3.7888888888888888
