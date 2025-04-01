import numpy as np
import matplotlib.pyplot as plt

class HubbleFunction:
    def __init__(self,H0,omega_m,omega_lambda,omega_rad):
        
        self.H0=H0
        self.omega_m=omega_m
        self.omega_lambda=omega_lambda
        self.omega_rad=omega_rad

    def __call__(self, z):
        
        return self.H0*np.sqrt(self.omega_m*(1+z)**3+self.omega_lambda+self.omega_rad*(1+z)**4)
    