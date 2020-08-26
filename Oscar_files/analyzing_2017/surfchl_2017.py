print('this one is for Chlorophyll 1')
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
import xarray as xr
mydirectory = '/users/asmit101/data/stuff/surfchl_2017_mod8_run1_NAM'
nc = xr.open_dataset(mydirectory+'/surfchl_ocean_his_0129.nc')
print(nc.variables.keys())
chlorophyll1 = nc.variables['chlorophyll1'][:]
print(chlorophyll1.dims)
s_rho = nc.variables['s_rho'][:]
time = nc.variables['ocean_time'][:]
timearray = []
for i in time:
	timearray.append(dt.fromtimestamp(i))
for j in timearray:
	print(j)
print(chlorophyll1.ndim)
print(list(s_rho))
gridfile = '/users/asmit101/data/stuff/myngbay_grd.nc'
#gridfile = '/gpfs/data/epscor/asane/forcefiles/ngbay_grd.nc'
ncgrid = NetCDFFile(gridfile)
lat = ncgrid.variables['lat_rho']
lon = ncgrid.variables['lon_rho']
chlorophyll1 = chlorophyll1.mean(axis = tuple(range(2,4)))
'''plt.pcolormesh(lon, lat,  chlorophyll1[0,0,:,:])
plt.title('Chlorophyll 1, day 75, OSOM 2017 run')
cbar = plt.colorbar()
cbar.set_label('mg m^-3', rotation = 270)
plt.show()'''
chlorophyll1array = []
for i in chlorophyll1:
	chlorophyll1array.append(float(i))
print(chlorophyll1array)
print(timearray)
