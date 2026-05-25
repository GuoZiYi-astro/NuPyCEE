def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 45124734416.3693*mass**-0.3
    elif mass < 0.5: 
      return 4647245838.12625*mass**-1.2
    else: 
      return 2168016843.37696*mass**-2.3
