def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 7390805413.22325*mass**-0.3
    elif mass < 0.5: 
      return 591264433.057860*mass**-1.3
    else: 
      return 514725585.255483*mass**-1.5
