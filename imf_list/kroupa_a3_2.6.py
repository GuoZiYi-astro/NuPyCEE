def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 1*mass** -0.3
    elif mass < 0.5: 
      return 0.08*mass**-1.3
    else: 
      return 0.03249009585424943*mass**-2.5999999999999996
def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 1*mass** -0.3
    elif mass < 0.5: 
      return 0.08*mass**-1.3
    else: 
      return 0.03249009585424943*mass**-2.5999999999999996
