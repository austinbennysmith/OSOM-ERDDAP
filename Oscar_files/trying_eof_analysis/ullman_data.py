from eofs.standard import Eof
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from datetime import datetime as dt
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import xarray as xr

nc = xr.open_dataset('/users/asmit101/data/stuff/surfchl_2017_mod8_run1_NAM/surfchl_ocean_his_0129.nc')
time = nc.variables['ocean_time']
chlorophyll1 = nc.variables['chlorophyll1']
chlorophyll2 = nc.variables['chlorophyll2']
timearray = []
#for i in time:
	#timearray.append(dt.fromtimestamp(i))
for i in timearray:
	print(i)
gridfile = '/users/asmit101/data/stuff/myngbay_grd.nc'
ncgrid = NetCDFFile(gridfile)
lat = ncgrid.variables['lat_rho']
lon = ncgrid.variables['lon_rho']
print(chlorophyll1.ndim)
print(chlorophyll1.dims)



surfchl = chlorophyll1[:,14,:,:]
chl_mean = surfchl.mean(axis=0)
anomaly = surfchl-chl_mean
solver = Eof(anomaly)
eof1 = solver.eofsAsCorrelation(neofs=1)
pc1 = solver.pcs(npcs=1, pcscaling=1)
plt.pcolormesh(lon, lat, eof1[0], cmap=plt.cm.RdBu_r)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('EOF1 expressed as Correlation')
cbar = plt.colorbar()
cbar.set_label('Correlation Coefficient', rotation=270)
plt.show()
plt.plot(timearray, pc1[:, 0])
plt.xlabel('Year')
plt.ylabel('Normalized Units')
plt.title('PC1 Time Series')
plt.show()
vF1 = solver.varianceFraction(neigs=6)
percentarray = vF1*100
array1 = [1,2,3,4,5,6]
plt.bar(array1, percentarray)
plt.title('Scree Plot')
plt.xlabel('Mode')
plt.ylabel('Percent of Variance Explained')
plt.show()

