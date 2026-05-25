def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 16295596605.2083*mass**-1.3
    elif mass < 0.5: 
      return 1678229123.84538*mass**-2.2
    else: 
      return 1186687193.85582*mass**-2.7
