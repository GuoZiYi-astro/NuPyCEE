def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 279117390.639770*mass**-2.7
    elif mass < 0.5: 
      return 279117390.639770*mass**-2.7
    else: 
      return 279117390.639770*mass**-2.7
