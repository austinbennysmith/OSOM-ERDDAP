# **Introduction**
This repository contains code from an undergraduate research project conducted during the Summer of 2020, in collaboration with other members of the Fox-Kemper research group at Brown University. The project is centered around the [Rhode Island Data Discovery Center](http://ridatadiscovery.org/#/) (RIDDC) and the Ocean State Ocean Model (OSOM). As part of RIDDC, there is an [ERDDAP server](https://pricaimcit.services.brown.edu/erddap/index.html) with a wealth of datasets relating to Narragansett Bay and surrounding waters. OSOM was built primarily by Professor Dave Ullman at the University of Rhode Island using the Regional Ocean Modeling System (ROMS). OSOM models a relatively small part of the ocean that includes Narragansett Bay and waters near Long Island, Martha’s Vineyard, and Nantucket Island.

Here is a brief summary of things you can explore through code in this repository:
•	Examples of how to visualize and analyze data stored in the RIDDC ERDDAP server<br/>
•	Spatial averages, climatologies, and anomalies for plankton-related variables in the ERDDAP server<br/>
•	EOF analyses of these variables<br/>
•	Comparisons data produced by different satellites<br/>
•	Comparisons between observations available in the ERDDAP server and OSOM output<br/>
•	Other types of RIDDC ERDDAP data such as salinity, sea surface temperature, and wind stress

# **How well does OSOM model Chlorophyll?**

One of the key products of this summer research project was a comparison between model runs conducted by Professor Ullman and data available on the RIDDC ERDDAP server. In particular, I have focused on variables relating to phytoplankton. The RIDDC ERDDAP server contains satellite data from two different instruments, the MODIS satellite and Suomi-NPP/VIIRS. Both of the satellites measure chlorophyll a, K490 (the diffuse attenuation coefficient at 490 nm), and PAR (photosynthetically available radiation). Additionally, MODIS alone measures Fluorescence Line Height, while Suomi-NPP/VIIRS measures Particulate Inorganic Carbon (PIC), Particulate Organic Carbon (POC), and Reflectance at 671 nm. Professor Ullman’s OSOM runs, on the other hand, model two different chlorophyll variables, named “Chlorophyll 1” and “Chlorophyll 2.” His OSOM runs are produced using CoSiNE, and the Chlorophyll 1 and 2 variables in Professor Ullman’s OSOM runs are derived from CoSiNE’s small phytoplankton and diatoms, respectively. Through this summer project, I sought to learn how well OSOM captures the real patterns in chlorophyll throughout the ocean and across time.

## **Author**
Benny Smith<br/>
Undergraduate, Brown University<br/>
austin_smith@brown.edu
