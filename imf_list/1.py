def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 0.260205831350083*mass**-0.3
    elif mass < 0.5: 
      return 0.0208164665080066*mass**-1.3
    else: 
      return 0.0104082332540033*mass**-2.9
