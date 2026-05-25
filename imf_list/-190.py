def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 24832564038.1186*mass**-0.3
    elif mass < 0.5: 
      return 1986605123.04949*mass**-1.3
    else: 
      return 1310670587.72288*mass**-1.9
