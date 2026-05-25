def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 946172590.933352*mass**-1.8
    elif mass < 0.5: 
      return 946172590.933352*mass**-1.8
    else: 
      return 946172590.933352*mass**-1.8
