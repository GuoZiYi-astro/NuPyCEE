def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 804314759.959931*mass**-2.3
    elif mass < 0.5: 
      return 804314759.959931*mass**-2.3
    else: 
      return 804314759.959931*mass**-2.3
