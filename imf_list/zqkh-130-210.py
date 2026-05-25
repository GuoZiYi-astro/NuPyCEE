def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 9459339612.74036*mass**-1.3
    elif mass < 0.5: 
      return 1254101847.23322*mass**-2.1
    else: 
      return 1254101847.23322*mass**-2.1
