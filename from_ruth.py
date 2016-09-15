import numpy as np


def teff2bv(teff, logg, feh):
    """
    Relation from Sekiguchi & Fukugita (2000).
    
    original here:
    https://gist.github.com/RuthAngus/53c90cb5e55b8467198d7d33a9fec424
    """
    t = [-813.3175, 684.4585, -189.923, 17.40875]
    f = [1.2136, 0.0209]
    d1, g1, e1 = -0.294, -1.166, 0.3125
    return t[0] + t[1]*np.log10(teff) + t[2]*(np.log10(teff))**2 + \
            t[3]*(np.log10(teff))**3 + f[0]*feh + f[1]*feh**2 \
            + d1*feh*np.log10(teff) + g1*logg + e1*logg*np.log10(teff)

        
def gyro(B_V, age):
    '''
    Compute the rotation period expected for a star of a given color (temp) and age
    
    NOTE: Age is in MYr
    
    Eqn 15 from Angus+2015
    '''
    P = (age**0.55) * 0.4 * ((B_V - 0.45)**0.31)
    
    return P