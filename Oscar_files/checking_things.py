#This one for all depth levels, to see the s_rho stuff
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
import xarray as xr
mydirectory = '/users/asmit101/data/stuff/netcdf'
nc = xr.open_dataset(mydirectory+'/ocean_his_0001.nc')
print(nc.variables.keys())
chlorophyll1 = nc.variables['chlorophyll1'][:]
s_rho = nc.variables['s_rho'][:]
print(chlorophyll1.ndim)
print(chlorophyll1.dims)
print(list(s_rho))

# This one for one depth level
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
import xarray as xr
mydirectory = '/users/asmit101/data/stuff/surfchl_2017_mod8_run1_NAM'
nc = xr.open_dataset(mydirectory+'/surfchl_ocean_his_0075.nc')
print(nc.variables.keys())
chlorophyll1 = nc.variables['chlorophyll1'][:]
s_rho = nc.variables['s_rho'][:]
print(chlorophyll1.ndim)
print(chlorophyll1.dims)
print(list(s_rho))
