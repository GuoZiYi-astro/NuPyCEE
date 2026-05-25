def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 88577126772.9604*mass**-0.3
    elif mass < 0.5: 
      return 7086170141.83683*mass**-1.3
    else: 
      return 2337564389.80910*mass**-2.9
