def custom_imf(mass): 
    import numpy as np 
    if mass == 0: 
      return 0 
    elif mass <= 1: 
      return 0.158/mass/np.log(10)*np.exp(-(np.log10(mass/0.079)**2/2/0.69**2)) 
    else: 
      return 4.43*10**(-2)*mass**(-1.3)/mass/np.log(10) 
