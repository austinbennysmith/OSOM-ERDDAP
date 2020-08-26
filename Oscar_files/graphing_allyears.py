import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from matplotlib.dates import DateFormatter

#getting into the output files:
file2006_1 = open('/users/asmit101/data/stuff/Chlorophyll1_2006_surf.out', 'r')
file2006_2 = open('/users/asmit101/data/stuff/Chlorophyll2_2006_surf.out', 'r')
file2017_1 = open('/users/asmit101/data/stuff/Chlorophyll1_2017_surf.out', 'r')
file2017_2 = open('/users/asmit101/data/stuff/Chlorophyll2_2017_surf.out', 'r')
file2018_1 = open('/users/asmit101/data/stuff/Chlorophyll1_2018_surf.out', 'r')
file2018_2 = open('/users/asmit101/data/stuff/Chlorophyll2_2018_surf.out', 'r')

#stringlist will be useful for organizing the datasets
stringlist = ['Chlorophyll1_2006_surf', 'Chlorophyll2_2006_surf', 'Chlorophyll1_2017_surf', 'Chlorophyll2_2017_surf', 'Chlorophyll1_2018_surf', 'Chlorophyll2_2018_surf']
yearlist = ['2006', '2017', '2018'] #this helps for for loops and stuff
allmyfiles = [file2006_1, file2006_2, file2017_1, file2017_2, file2018_1, file2018_2] #I'll want to loop through the files
for z in range(len(allmyfiles)):
	allmyfiles[z] = allmyfiles[z].readlines() #the .readlines() function makes a list whose items are the lines of the file. I think this should have a bunch of elements,  but almost all of them are datetimes that were printed by the Python script that produced the output file. The second-to-last line is a list of chlorophyll averages, and the last line is a list of datetimes. Those are the lines we care about.
print(len(allmyfiles))
filedictionary = {} #the keys of this dictionary will be the filenames as listed in stringlist. The values will be lists of the time lists and chlorophyll lists
for x in range(len(allmyfiles)): #looping through the files
	if x == 0 or x == 1: #this helps with datetime stuff. I need to convert time stamp from "years since" to the actual date. 2 of the files are 2006, which is 36 years after 1970
		howmanyyears = 36
	else: #the other files start in 2017 (though obviously the 2018 run goes through 2018 too, after being spun up with a 2017 run)
		howmanyyears = 47
	li = list(allmyfiles[x][-1].split(', d')) #making a list of times by splitting up the datetime.datetime element in allmyfiles[x] in the spots where there's a ', d'. See the output files to see what I mean.
	chl = list(allmyfiles[x][-2].split(', ')) #making a list of chlorophyll averages by splitting up the chlorophyll element in allmyfiles[x] in the spots where there's a comma. See the output files to see what I mean.
	for j in range(len(chl)): #formatting the lists so that I can use them for graphing
        	chl[j] = chl[j].replace('[', '')
        	chl[j] = chl[j].replace(']\n', '')
        	chl[j] = float(chl[j])
        	li[j] = li[j].replace('[', '')
        	li[j] = li[j].replace(']\n', '')
        	li[j] = li[j].replace('atetime.datetime', '')
        	li[j] = li[j].replace('(', '')
        	li[j] = li[j].replace('d', '')
        	li[j] = li[j].replace(')', '')
        	li[j] = datetime.strptime(li[j], "%Y, %m, %d, %H, %M")
        	li[j] = li[j] + timedelta(hours=5) #due to time zone weirdness, you need to add 5 hours to the output
        	li[j] = li[j] + relativedelta(years=howmanyyears) #the relativedelta module is helpful for working with years in datetime.
	filedictionary[stringlist[x]] = [li, chl]

#below I make graphs for each of the years, and also graph the sum of Chlorophyll 1 and 2 (calculated within the following lines)
'''for k in yearlist:
	for j in filedictionary:
		if k in j:
			timearray = filedictionary[j][0]
		if k in j and 'Chlorophyll1' in j:
			chlorophyll1 = filedictionary[j][1]
		if k in j and 'Chlorophyll2' in j:
			chlorophyll2 = filedictionary[j][1]
	chlorophyllsum = []
	for m in range(len(chlorophyll1)):
		chlorophyllsum.append(chlorophyll1[m] + chlorophyll2[m])
	plt.figure()
	plt.plot(timearray, chlorophyll1, label = 'Chlorophyll 1')
	plt.plot(timearray, chlorophyll2, label = 'Chlorophyll 2')	
	plt.plot(timearray, chlorophyllsum, label = 'sum')
	plt.xlabel('Date')
	plt.ylabel('Chlorophyll (mg m^-3)')
	plt.legend(loc='best')
	plt.title('OSOM Chlorophyll, '+k+' run')
	plt.savefig('/users/asmit101/data/stuff/OSOM_Chlorophyll_'+k+'.png')'''

#below I make the graph again for 2018, with a formatting tweak
'''fig, ax = plt.subplots()
fig.autofmt_xdate()
plt.plot(filedictionary['Chlorophyll1_2018_surf'][0], filedictionary['Chlorophyll1_2018_surf'][1], label = 'Chlorophyll 1')
plt.plot(filedictionary['Chlorophyll2_2018_surf'][0], filedictionary['Chlorophyll2_2018_surf'][1],  label = 'Chlorophyll 2')
chlorophyllsum = []
for m in range(len(filedictionary['Chlorophyll1_2018_surf'][1])):
	chlorophyllsum.append(filedictionary['Chlorophyll1_2018_surf'][1][m] + filedictionary['Chlorophyll2_2018_surf'][1][m])
plt.plot(filedictionary['Chlorophyll1_2018_surf'][0], chlorophyllsum, label = 'sum')
plt.legend(loc='best')
plt.xlabel('Date')
plt.ylabel('Chlorophyll (mg m^-3)')
plt.title('OSOM Chlorophyll, 2018 run')
plt.show()'''

#I think the following just 
'''timearray = filedictionary['Chlorophyll1_2018_surf'][0]
chlorophyll1 = filedictionary['Chlorophyll1_2018_surf'][1]
chlorophyll2 = filedictionary['Chlorophyll2_2018_surf'][1]
timearray_2017 = timearray[:int(len(timearray)/2)]
timearray_2018 = timearray[int(len(timearray)/2):]
chlorophyll1_2017 = chlorophyll1[:int(len(chlorophyll1)/2)]
chlorophyll1_2018 = chlorophyll1[int(len(chlorophyll1)/2):]
chlorophyll2_2017 = chlorophyll2[:int(len(chlorophyll2)/2)]
chlorophyll2_2018 = chlorophyll2[int(len(chlorophyll2)/2):]
chlorophyllsum = []
for m in range(len(timearray)):
	chlorophyllsum.append(chlorophyll1[m] + chlorophyll2[m])
chlorophyllsum_2017 = chlorophyllsum[:int(len(chlorophyllsum)/2)]
chlorophyllsum_2018 = chlorophyllsum[int(len(chlorophyllsum)/2):]
graphing_dict = {'both_years':[timearray, chlorophyll1, chlorophyll2, chlorophyllsum, 'OSOM Chlorophyll, 2018 run with 2017'],
		 'year_2017':[timearray_2017, chlorophyll1_2017, chlorophyll2_2017, chlorophyllsum_2017, 'OSOM Chlorophyll, 2018 run spinup'],
		 'year_2018':[timearray_2018, chlorophyll1_2018, chlorophyll2_2018, chlorophyllsum_2018, 'OSOM Chlorophyll, 2018 run without 2017']
}
for w in graphing_dict:
	time_now = graphing_dict[w][0]
	chlorophyll1_now = graphing_dict[w][1]
	chlorophyll2_now = graphing_dict[w][2]
	chlorophyllsum_now = graphing_dict[w][3]
	fig, ax = plt.subplots()
	fig.autofmt_xdate()
	plt.plot(time_now, chlorophyll1_now, label = 'Chlorophyll 1')
	plt.plot(time_now, chlorophyll2_now, label = 'Chlorophyll 2')
	plt.plot(time_now, chlorophyllsum_now, label = 'sum')
	plt.legend(loc='best')
	plt.xlabel('Date')
	plt.ylabel('Chlorophyll (mg m^-3)')
	plt.title(graphing_dict[w][4])
	plt.savefig('/users/asmit101/data/stuff/'+w+'.png')'''

graph_dictionary = {'2006':{},
		    '2017':{},
		    '2018':{}		
}
for k in yearlist:
        for j in filedictionary:
                if k in j:
                        graph_dictionary[k]['time'] = filedictionary[j][0]
                if k in j and 'Chlorophyll1' in j:
                        graph_dictionary[k]['chlorophyll1'] = filedictionary[j][1]
                if k in j and 'Chlorophyll2' in j:
                        graph_dictionary[k]['chlorophyll2'] = filedictionary[j][1]
for w in graph_dictionary:
	graph_dictionary[w]['chlorophyllsum'] = []
	for m in range(len(graph_dictionary[w]['time'])):
		graph_dictionary[w]['chlorophyllsum'].append(graph_dictionary[w]['chlorophyll1'][m] + graph_dictionary[w]['chlorophyll2'][m])
for z in graph_dictionary['2018']:
	graph_dictionary['2018'][z] = graph_dictionary['2018'][z][:int(len(graph_dictionary['2018'][z])/2)]
for v in graph_dictionary:
	for b in range(len(graph_dictionary[v]['time'])):
		if int(v)==2006 or int(v)==2017:
			graph_dictionary[v]['time'][b] = graph_dictionary[v]['time'][b] + relativedelta(years=1900-int(v))
		elif int(v)==2018:
			graph_dictionary[v]['time'][b] = graph_dictionary[v]['time'][b] + relativedelta(years=1900-2017)
meanlist = []
for t in range(len(graph_dictionary['2006']['time'])): #I'm using 2006 here because it's the shortest dataset (only goes until 12/25ish). I'm averaging them until the end of the 2006 run
	myvalue_2006 = graph_dictionary['2006']['chlorophyllsum'][t]
	myvalue_2017 = graph_dictionary['2017']['chlorophyllsum'][t]
	myvalue_2018 = graph_dictionary['2018']['chlorophyllsum'][t]
	meanlist.append((myvalue_2006 + myvalue_2017 + myvalue_2018)/3)

fig, ax = plt.subplots()
plt.plot(graph_dictionary['2006']['time'], graph_dictionary['2006']['chlorophyllsum'], color='m', label='2006')
plt.plot(graph_dictionary['2017']['time'], graph_dictionary['2017']['chlorophyllsum'], color='c', label='2017')
plt.plot(graph_dictionary['2018']['time'], graph_dictionary['2018']['chlorophyllsum'], color='k', label='2017 run for 2018 spinup')
plt.plot(graph_dictionary['2006']['time'], meanlist, color='g', label='average')
plt.title('OSOM Chlorophyll sums of three different runs')
plt.xlabel('Date')
plt.ylabel('Chlorophyll (mg m^-3)')
plt.legend(loc='best')
my_date_format = DateFormatter('%m-%d')
ax.xaxis.set_major_formatter(my_date_format)
plt.show()
