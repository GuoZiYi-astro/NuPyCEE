def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return mass**-0.3
    elif mass < 0.5: 
      return 0.10298666348361793*mass**-1.2
    else: 
      return 0.11037837291689721*mass**-1.1
