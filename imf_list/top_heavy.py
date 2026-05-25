def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 1.22801837508159*mass**-0.3 
    elif mass < 0.5: 
      return 0.0982414700065269*mass**-1.3 
    else: 
      return 0.451399259955952*mass**-0.9
