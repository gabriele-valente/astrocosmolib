import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import trapezoid, simpson, quad

class Distances:
    "Class to calculate cosmological distances."

    def __init__(self, hubble_function):
        """
        Initialize the Distances class.

        Parameters
        ----------
        hubble_function : callable
            Function to calculate the Hubble parameter as a function of redshift.
        """
        self.hubble_function = hubble_function

    def comoving_distance(self, z, method="trapezoid", err_ass=1.e-4, err_rel=1.e-4):
        """
        Calculate the comoving distance.
        Parameters----------z : float or array-like Redshift.
        Returns ------- float or array-like Comoving distance in Mpc.
        """
        c = 299792.458   #km/s

        if np.isscalar(z):

            integral=0

        # Integrate the inverse of the Hubble parameter to get the comoving distance
            if method == "trapezoid":

                integral = trapezoid(1 / self.hubble_function(np.linspace(0, z, 100)), np.linspace(0, z, 100))
        
            if method == "quad":    

                def func(x):
                    return 1/self.hubble_function(x)

                integral,_ = quad(func, a=0, b=z, epsabs=err_ass, epsrel=err_rel)

            if method == "simpson":

                integral = simpson(1 / self.hubble_function(np.linspace(0, z, 100)), x=np.linspace(0, z, 100))

            return c*integral
        
        elif isinstance(z, (list, np.ndarray)):
            return np.array([self.comoving_distance(zi, method, err_ass, err_rel) for zi in z])
    
    
    def luminosity_distance(self,z,method="trapezoid",err_ass=1.e-4,err_rel=1.e-4):
        return (1+z)*self.comoving_distance(z,method,err_ass,err_rel)

    def angular_diameter_distance(self,z,method="trapezoid",err_ass=1.e-4,err_rel=1.e-4):
        return self.comoving_distance(z,method,err_ass,err_rel)*(1/(1+z))