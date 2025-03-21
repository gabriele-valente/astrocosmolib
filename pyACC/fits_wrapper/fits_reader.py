import numpy as np 

from astropy.io import fits

from ..helpers.logger import Logger

class FitsManager:
    "A class to manage FITS files, using astopy.io.fits module"
    
    def __init__(self, imput_file):
    
        "Constructor of thr class"
        self.imput_files=imput_file
        self.hdulist=fits.open(imput_file) 

        self.logger= Logger("FitsManager")
        self.logger("FITS file opened correctly")

    def get_header(self,hdu_index):

        if hdu_index <0 or hdu_index >= len(self.hdulist):

            self.logger.error("invalid hdu index")
            raise ValueError("Invalid hdu index")

        return self.hdulist[hdu_index].header
    
    def get_data(self,hdu_index):

        if hdu_index <0 or hdu_index >= len(self.hdulist):

            self.logger.error("invalid hdu index")
            raise ValueError("Invalid hdu index")

        return self.hdulist[hdu_index].data
    
    def get_hdu_count(self):

        return len(self.hdulist)

