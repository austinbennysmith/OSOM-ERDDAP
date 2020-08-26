# Overview of code in this folder

This folder contains code I used to work with OSOM output using Oscar, the Brown University supercomputer. The primary product of this code is graphs of spatial averages of chlorophyll against time. To produce these graphs, the first thing I had to do was go into Professor Ullman's OSOM runs, extract the variables I wanted (Chlorophyll1 and Chlorophyll2) and put them in a folder in my own directory on Oscar. Then I used [NetCDF Operators (NCO)](http://nco.sourceforge.net/nco.html) to combine those files in my own directory into a single file that could be analyzed with a python notebook.

