def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 1*mass** -0.3
    elif mass < 0.5: 
      return 0.08*mass**-1.3
    else: 
      return 0.03031433133020797*mass**-2.6999999999999997
def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 1*mass** -0.3
    elif mass < 0.5: 
      return 0.08*mass**-1.3
    else: 
      return 0.03031433133020797*mass**-2.6999999999999997
