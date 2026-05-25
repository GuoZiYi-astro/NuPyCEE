def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 0.468242584506758*mass**-0.3
    elif mass < 0.5: 
      return 0.0374594067605407*mass**-1.3
    else: 
      return 0.0187297033802703*mass**-2.3
