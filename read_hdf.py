
from pyhdf.SD import SD, SDC
from numpy import *

class read_hdf:

#   this script is to read the hdf data from the HDF4 file for MACER2D

    __version__ = 0.2
    
    def __init__(self,filename):
    
        self.filename = filename
        self.data     = SD(filename,SDC.READ)
        self.vardic   = self.data.datasets()
    
        info = self.data.select('Data-Set-5').getdatastrs()
        self.time  = float(info[0].split('AT TIME=')[-1])
        self.geom  = info[-1]
    
        print ('Reading',filename, 'of time =',self.time)
    
        self.x1b   = self.data.select('fakeDim2').get() 
        self.x2b   = self.data.select('fakeDim1').get()
        self.x3b   = self.data.select('fakeDim0').get()
    
        self.v1    = self.data.select('Data-Set-2').get()[0]
        self.v2    = self.data.select('Data-Set-3').get()[0]
        self.v3    = self.data.select('Data-Set-4').get()[0]
    
        self.dims  = shape(self.v1)
    
        if 'DENSITY' in info[0]:
            self.d  = self.data.select('Data-Set-5').get()[0]
            self.e  = self.data.select('Data-Set-6').get()[0]
            
    #        if 'SFR' in self.data.select('Data-Set-7').getdatastrs()[0]:
    #            self.sfr = self.data.select('Data-Set-7').get()[0]
    #        if 'DNEWSTAR' in self.data.select('Data-Set-8').getdatastrs()[0]:
    #            self.d_nstar = self.data.select('Data-Set-8').get()[0]
        else:
           self.b1 = self.data.select('Data-Set-5').get()[0]
           self.b2 = self.data.select('Data-Set-6').get()[0]
           self.b3 = self.data.select('Data-Set-7').get()[0]
           self.d  = self.data.select('Data-Set-8').get()[0]
           self.e  = self.data.select('Data-Set-9').get()[0]
        self.T     = self.e/self.d * 93 
    
    def x(self):
        return array([self.x1b*sin(theta) for theta in self.x2b])
    
    def y(self):
        return array([self.x1b*cos(theta) for theta in self.x2b])




