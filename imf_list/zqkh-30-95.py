def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 430802486.285260*mass**-0.3
    elif mass < 0.5: 
      return 83423170.7725248*mass**-0.95
    else: 
      return 83423170.7725248*mass**-0.95
