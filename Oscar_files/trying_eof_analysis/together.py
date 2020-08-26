from eofs.xarray import Eof
from eofs.examples import example_data_path
from netCDF4 import Dataset as NetCDFFile
import pandas as pd
import netCDF4
import numpy as np
import xarray as xr
from datetime import datetime as dt
import matplotlib.pyplot as plt
mydirectory = '/users/dullman1/data/dullman1/EPSCOR/2017_mod8_run1_NAM'
oceansets = []
for i in range(1, 2):
        if i<10:
                oceansets.append('/ocean_his_000'+str(i)+'.nc')
        elif 10<=i<100:
                oceansets.append('/ocean_his_00'+str(i)+'.nc')
        elif i>=100:
                oceansets.append('/ocean_his_0'+str(i)+'.nc')
print(oceansets)
print('that was oceansets')
timearray = []
gridfile = '/gpfs/data/epscor/asane/forcefiles/ngbay_grd.nc'
myotherdirectory = '/users/asmit101/data/stuff/netcdf/'
ncgrid = NetCDFFile(gridfile)
lat = ncgrid.variables['lat_rho']
lon = ncgrid.variables['lon_rho']
print('sup')
dataset = xr.open_mfdataset([mydirectory+i for i in oceansets]).load()
dataset.close()
#dataset = xr.open_mfdataset('/users/asmit101/data/stuff/netcdf/*.nc')
#dataset = xr.open_mfdataset('{}/*.nc'.format(myotherdirectory))
chlorophyll = dataset.variables['chlorophyll1']
print(chlorophyll.dims[0])
dimensionlist = list(chlorophyll.dims)
dimensionlist[0] = 'time'
print(dimensionlist)
chlorophyll.dims = tuple(dimensionlist)
print(chlorophyll.dims)
surfchl = chlorophyll[:,14,:,:]
print(xr.DataArray(surfchl).shape)
chl_mean = surfchl.mean(dim='time')
print(xr.DataArray(chl_mean).shape)
anomaly = surfchl-chl_mean
print(xr.DataArray(anomaly).shape)
solver = Eof(xr.DataArray(anomaly))
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
