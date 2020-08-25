# **Introduction**
This repository contains code from an undergraduate research project conducted during the Summer of 2020, in collaboration with other members of the Fox-Kemper research group at Brown University. The project is centered around the [Rhode Island Data Discovery Center](http://ridatadiscovery.org/#/) (RIDDC) and the Ocean State Ocean Model (OSOM). As part of RIDDC, there is an [ERDDAP server](https://pricaimcit.services.brown.edu/erddap/index.html) with a wealth of datasets relating to Narragansett Bay and surrounding waters. OSOM was built primarily by Professor Dave Ullman at the University of Rhode Island using the Regional Ocean Modeling System (ROMS). OSOM models a relatively small part of the ocean that includes Narragansett Bay and waters near Long Island, Martha’s Vineyard, and Nantucket Island.

Here is a brief summary of things you can explore through code in this repository:<br/>
•	Examples of how to visualize and analyze data stored in the RIDDC ERDDAP server<br/>
•	Spatial averages, climatologies, and anomalies for plankton-related variables in the ERDDAP server<br/>
•	EOF analyses of these variables<br/>
•	Comparisons data produced by different satellites<br/>
•	Comparisons between observations available in the ERDDAP server and OSOM output<br/>
•	Other types of RIDDC ERDDAP data such as salinity, sea surface temperature, and wind stress

# **How well does OSOM model Chlorophyll?**

One of the key products of this summer research project was a comparison between model runs conducted by Professor Ullman and data available on the RIDDC ERDDAP server. In particular, I have focused on variables relating to phytoplankton. The RIDDC ERDDAP server contains satellite data from two different instruments, the MODIS satellite and Suomi-NPP/VIIRS. Both of the satellites measure chlorophyll a, K490 (the diffuse attenuation coefficient at 490 nm), and PAR (photosynthetically available radiation). Additionally, MODIS alone measures Fluorescence Line Height, while Suomi-NPP/VIIRS measures Particulate Inorganic Carbon (PIC), Particulate Organic Carbon (POC), and Reflectance at 671 nm. Professor Ullman’s OSOM runs, on the other hand, model two different chlorophyll variables, named “Chlorophyll 1” and “Chlorophyll 2.” The biological components of his OSOM runs are produced using the [Carbon, Silicate, Nitrogen Ecosystem (CoSiNE)](http://ccrm.vims.edu/schismweb/CoSiNE_manual_ZG_v5.pdf) model, and the Chlorophyll 1 and 2 variables in Professor Ullman’s OSOM runs are derived from CoSiNE’s Small Phytoplankton and Diatom variables, respectively. Through this summer project, I sought to learn how well OSOM captures the real patterns in chlorophyll throughout the ocean and across time.

To make this comparison, I looked at OSOM runs for 2006, 2017, and 2018. I constrained latitute and longitude in both the OSOM runs and the satellite data to get an approximate match between the grids and regions (however, the match between datasets is not perfect due to a curvilinear grid used by OSOM and differing resolutions). The 2006 and 2017 runs are one year runs, while the 2018 run is spun up with a 2017 run, and thus has 2 years' worth of data. In the figures below, you can see what the satellite data has to say about these years. Based on monthly averages, it seems that in 2006 there were large concentrations of chlorophyll in the winter, a bit of a Spring bloom, and a Fall bloom. In 2017, chlorophyll concentrations are mostly flat except for a large Fall bloom. Finally, 2018 shows a large Spring bloom and a smaller Fall bloom. The pattern we see in 2018 seems to be most typical, based on the climatology.

<img width="783" alt="Screen Shot 2020-08-25 at 11 50 56 AM" src="https://user-images.githubusercontent.com/69660053/91212196-e1e0fa00-e6dd-11ea-9bf5-065b409c1a3b.png">

## **Author**
Benny Smith<br/>
Undergraduate, Brown University<br/>
austin_smith@brown.edu
