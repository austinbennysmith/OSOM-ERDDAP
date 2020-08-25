print('this one is for chlorophyll 1 in 2018')
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from datetime import datetime as dt
mydirectory = '/users/asmit101/data/stuff/2018_mod8_run1_NAM'
nc = NetCDFFile(mydirectory+'/surfchl_whole_year.nc')
print(nc.variables.keys())
chlorophyll1 = nc.variables['chlorophyll1'][:]
time = nc.variables['ocean_time'][:]
timearray = []
for i in time:
	timearray.append(dt.fromtimestamp(i))
for j in timearray:
        print(j)
print(chlorophyll1.ndim)
chlorophyll1array = []
chlorophyll1 = chlorophyll1.mean(axis = tuple(range(2,4)))
for i in chlorophyll1:
        chlorophyll1array.append(float(i))
print(chlorophyll1array)
print(timearray)
