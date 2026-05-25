def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 19124735410.2952*mass**-0.3
    elif mass < 0.5: 
      return 1529978832.82362*mass**-1.3
    else: 
      return 1081858407.76146*mass**-1.8
