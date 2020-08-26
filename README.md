# **Introduction**
This repository contains code from an undergraduate research project conducted during the Summer of 2020, in collaboration with other members of the Fox-Kemper research group at Brown University. The project is centered around the [Rhode Island Data Discovery Center](http://ridatadiscovery.org/#/) (RIDDC) and the Ocean State Ocean Model (OSOM). As part of RIDDC, there is an [ERDDAP server](https://pricaimcit.services.brown.edu/erddap/index.html) with a wealth of datasets relating to Narragansett Bay and surrounding waters. OSOM was built primarily by Professor Dave Ullman at the University of Rhode Island using the Regional Ocean Modeling System (ROMS). OSOM models a relatively small part of the ocean that includes Narragansett Bay and waters near Long Island, Martha’s Vineyard, and Nantucket Island.

Here is a brief summary of things you can explore through code in this repository:<br/>
•	[Examples](https://github.com/austinbennysmith/OSOM-ERDDAP/tree/master/ERDDAP_examples) of how to visualize and analyze data stored in the RIDDC ERDDAP server<br/>
•	[Spatial averages, climatologies, and anomalies](https://github.com/austinbennysmith/OSOM-ERDDAP/tree/master/plankton/averages_climatologies_anomalies) for plankton-related variables in the ERDDAP server<br/>
•	[EOF analyses](https://github.com/austinbennysmith/OSOM-ERDDAP/blob/master/plankton/EOF_Analysis.ipynb) of these variables<br/>
•	[Comparisons of data](https://github.com/austinbennysmith/OSOM-ERDDAP/tree/master/plankton/averages_climatologies_anomalies) produced by different satellites<br/>
•	Comparisons between observations available in the ERDDAP server and OSOM output<br/>
•	Other types of RIDDC ERDDAP data such as salinity, sea surface temperature, and wind stress

# **How well does OSOM model Chlorophyll?**

One of the key products of this summer research project was a comparison between model runs conducted by Professor Ullman and data available on the RIDDC ERDDAP server. In particular, I have focused on variables relating to phytoplankton. The RIDDC ERDDAP server contains satellite data from two different instruments, the MODIS satellite and Suomi-NPP/VIIRS. Both of the satellites measure chlorophyll a, K490 (the diffuse attenuation coefficient at 490 nm), and PAR (photosynthetically available radiation). Additionally, MODIS alone measures Fluorescence Line Height, while Suomi-NPP/VIIRS measures Particulate Inorganic Carbon (PIC), Particulate Organic Carbon (POC), and Reflectance at 671 nm. Professor Ullman’s OSOM runs, on the other hand, model two different chlorophyll variables, named “Chlorophyll 1” and “Chlorophyll 2.” The biological components of his OSOM runs are produced using the [Carbon, Silicate, Nitrogen Ecosystem (CoSiNE)](http://ccrm.vims.edu/schismweb/CoSiNE_manual_ZG_v5.pdf) model, and the Chlorophyll 1 and 2 variables in Professor Ullman’s OSOM runs are derived from CoSiNE’s Small Phytoplankton and Diatom variables, respectively. Through this summer project, I sought to learn how well OSOM captures the real patterns in chlorophyll throughout the ocean and across time.

To make this comparison, I looked at OSOM runs for 2006, 2017, and 2018. I constrained latitute and longitude in both the OSOM runs and the satellite data to get an approximate match between the grids and regions (however, the match is not perfect due to a curvilinear grid used by OSOM and differing resolutions). Satellite data was constrained to latitudes between 40.5 and 41.5, and longitudes between -72.65 and -70.25. OSOM output was constrained to eta_rho values between 0 and 600. Constraining OSOM output in this way prevented averages from being biased by data from Narragansett Bay itself, which is not captured by relatively low-resolution satellite data. The 2006 and 2017 runs are one year runs, while the 2018 run is spun up with a 2017 run, and thus has 2 years' worth of data. In the figures below, you can see what the satellite data has to say about these years. Based on monthly averages, it seems that in 2006 there were large concentrations of chlorophyll in the winter, a bit of a Spring bloom, and a Fall bloom. In 2017, chlorophyll concentrations are mostly flat except for a large Fall bloom. Finally, 2018 shows a large Spring bloom and a smaller Fall bloom. The pattern we see in 2018 seems to be most typical, based on the climatology.

<img width="783" alt="Screen Shot 2020-08-25 at 11 50 56 AM" src="https://user-images.githubusercontent.com/69660053/91212196-e1e0fa00-e6dd-11ea-9bf5-065b409c1a3b.png">

If we compare this to all of the one-year runs, it looks like OSOM is not modelling the chlorophyll very well. Below I have graphed the sum of OSOM's "Chlorophyll 1" and "Chlorophyll 2" variables for each of the runs (including just the 1 year spinup for the 2018 run), along with an average of the three years. Here we see a large Spring bloom, a huge Summer bloom, and a smaller Fall bloom. Chlorophyll concentrations are drastically higher in the OSOM runs than anything we see in the satellite data, reaching 16 mg/m^3 in July.

<img width="783" alt="Screen Shot 2020-08-25 at 11 51 19 AM" src="https://user-images.githubusercontent.com/69660053/91213110-202ae900-e6df-11ea-891c-eafb3aabf713.png">

Since all three of these runs look so similar, it is likely that the results are being severely biased by the initial conditions. Below we see that in the 2-year 2018 run, the second year begins to show different behavior. In the future we hope to improve how OSOM models the real ecological patterns observed from satellites.

<img width="844" alt="Screen Shot 2020-08-25 at 2 41 04 PM" src="https://user-images.githubusercontent.com/69660053/91214577-4487c500-e6e1-11ea-9397-71234d937d48.png">

See the various Python notebooks above for higher-resolution averages and climatologies, scaling between the MODIS and Suomi-NPP/VIIRS data, code for working with the OSOM output, and other types of analysis such as Empirical Orthogonal Functions.

## **Author**
Benny Smith<br/>
Undergraduate, Brown University<br/>
austin_smith@brown.edu
