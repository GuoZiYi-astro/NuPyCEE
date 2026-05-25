def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 52825104757.1865*mass**-0.3
    elif mass < 0.5: 
      return 4226008380.57492*mass**-1.3
    else: 
      return 2113004190.28746*mass**-2.3
