from eofs.xarray import Eof
from eofs.examples import example_data_path
from netCDF4 import Dataset as NetCDFFile
import pandas as pd
import netCDF4 as nc
import numpy as np
import xarray as xr
from datetime import datetime as dt
import matplotlib.pyplot as plt
mydirectory = '/users/dullman1/data/dullman1/EPSCOR/2017_mod8_run1_NAM'
oceansets = []
'''for i in range(1, 3):
        if i<10:
                oceansets.append('/ocean_his_000'+str(i)+'.nc')
        elif 10<=i<100:
                oceansets.append('/ocean_his_00'+str(i)+'.nc')
        elif i>=100:
                oceansets.append('/ocean_his_0'+str(i)+'.nc')'''
timearray = []
gridfile = '/gpfs/data/epscor/asane/forcefiles/ngbay_grd.nc'
ncgrid = NetCDFFile(gridfile)
lat = ncgrid.variables['lat_rho']
lon = ncgrid.variables['lon_rho']
print('sup')
dataset = nc.MFDataset([mydirectory+oceansets)
#df = dataset.to_dataframe()

