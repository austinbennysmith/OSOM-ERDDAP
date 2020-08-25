print('this one is for Chlorophyll 2 in 2018')
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
mydirectory = '/users/asmit101/data/stuff/2018_mod8_run1_NAM'
nc = NetCDFFile(mydirectory+'/surfchl_whole_year.nc')
print(nc.variables.keys())
chlorophyll2 = nc.variables['chlorophyll2'][:]
s_rho = nc.variables['s_rho'][:]
time = nc.variables['ocean_time'][:]
timearray = []
for i in time:
	timearray.append(dt.fromtimestamp(i))
for j in timearray:
        print(j)
print(chlorophyll2.ndim)
print(list(s_rho))
gridfile = '/users/asmit101/data/stuff/myngbay_grd.nc'
ncgrid = NetCDFFile(gridfile)
lat = ncgrid.variables['lat_rho']
lon = ncgrid.variables['lon_rho']
chlorophyll2 = chlorophyll2.mean(axis = tuple(range(2,4)))
'''plt.pcolormesh(lon, lat,  chlorophyll2[0,0,:,:])
plt.title('Chlorophyll 2, day 75, OSOM 2017 run')
cbar = plt.colorbar()
cbar.set_label('mg m^-3', rotation = 270)
plt.show()'''
chlorophyll2array = []
for i in chlorophyll2:
        chlorophyll2array.append(float(i))
print(chlorophyll2array)
print(timearray)
