def custom_imf(mass): 
    if mass == 0: 
      return 0 
    elif mass < 0.08: 
      return 47830485165.7916*mass**-0.7
    elif mass < 0.5: 
      return 3826438813.26333*mass**-1.7
    else: 
      return 1913219406.63166*mass**-2.7
