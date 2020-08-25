#SURFACE LEVEL ONLY:

'''print('2017 OSOM Small Phytoplankton, Surface')
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
mydirectory = '/users/dullman1/data/dullman1/EPSCOR/2017_mod8_run1_NAM'
print(mydirectory)
oceansets = []
start_day = 1
end_day = 366
for i in range(start_day, end_day):
        if i<10:
                oceansets.append('/ocean_his_000'+str(i)+'.nc')
        elif 10<=i<100:
                oceansets.append('/ocean_his_00'+str(i)+'.nc')
        elif i>=100:
                oceansets.append('/ocean_his_0'+str(i)+'.nc')
avg_list = []
day_list = []
for i in range(len(oceansets)):
        day_list.append(i+start_day)
for j in range(len(oceansets)):
        nc = NetCDFFile(mydirectory+oceansets[j])
        time = nc.variables['ocean_time']
        chlorophyll = nc.variables['smallphytoplankton']
        timearray = []
        for i in time:
                timearray.append(dt.fromtimestamp(i+1483228800))
        dstart = nc.variables['dstart'][:]
        for i in timearray:
                print(i)
        print(chlorophyll.ndim)
        surfchl = chlorophyll[:,14,:,:]
        chl_mean = surfchl.mean()
        avg_list.append(chl_mean)
print(day_list)
print(avg_list)'''
'''plt.plot(day_list, avg_list)
plt.title('OSOM Small Phytoplankton,  2017')
plt.xlabel('Day')
plt.ylabel('Small Phytoplankton (mmol m^-3)')
plt.savefig('smallphytoplankton_2017.png')
plt.show()'''

#ALL DEPTH LEVELS:

print('2017 OSOM Small Phytoplankton, depths 9-15')
from netCDF4 import Dataset as NetCDFFile
import numpy as np
from datetime import datetime as dt
import matplotlib.pyplot as plt
mydirectory = '/users/dullman1/data/dullman1/EPSCOR/2017_mod8_run1_NAM'
print(mydirectory)
oceansets = []
start_day = 1
end_day = 366
for i in range(start_day, end_day):
        if i<10:
                oceansets.append('/ocean_his_000'+str(i)+'.nc')
        elif 10<=i<100:
                oceansets.append('/ocean_his_00'+str(i)+'.nc')
        elif i>=100:
                oceansets.append('/ocean_his_0'+str(i)+'.nc')
avg_list = []
day_list = []
for i in range(len(oceansets)):
        day_list.append(i+start_day)
for k in range(8, 15):
	for j in range(len(oceansets)):
        	nc = NetCDFFile(mydirectory+oceansets[j])
        	time = nc.variables['ocean_time']
        	chlorophyll = nc.variables['smallphytoplankton']
        	timearray = []
        	for i in time:
                	timearray.append(dt.fromtimestamp(i+1483228800))
        	print(chlorophyll.ndim)
        	surfchl = chlorophyll[:,k,:,:]
        	chl_mean = surfchl.mean()
        	avg_list.append(chl_mean)
	print('Depth Level '+str(k+1))
	print(day_list)
	print(avg_list)
'''plt.plot(day_list, avg_list)
plt.title('OSOM Small Phytoplankton,  2017')
plt.xlabel('Day')
plt.ylabel('Small Phytoplankton (mmol m^-3)')
plt.savefig('smallphytoplankton_2017.png')
plt.show()'''
