def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 804314759.959925*mass**-1.7
    elif mass < 0.5: 
      return 804314759.959925*mass**-1.7
    else: 
      return 804314759.959925*mass**-1.7
