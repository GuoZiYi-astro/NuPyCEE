def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 14305181219.1217*mass**-0.3
    elif mass < 0.5: 
      return 1144414497.52973*mass**-1.3
    else: 
      return 867304006.430246*mass**-1.7
