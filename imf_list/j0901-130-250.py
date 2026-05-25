def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.5: 
      return 1*mass**-1.3
    elif mass < 1: 
      return 0.5743491774985175*mass**-2.1
    else: 
      return 0.5743491774985175*mass**-2.5
