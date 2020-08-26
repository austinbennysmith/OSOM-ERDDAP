#!/bin/bash
#SBATCH -n 12
#SBATCH --mem=64G
#SBATCH -t 48:00:00
module load nco/4.9.3
cd /users/dullman1/data/dullman1/EPSCOR/2006_mod8_run6a_NAM
for file in ocean_his_*.nc ; do
	cd /users/dullman1/data/dullman1/EPSCOR/2006_mod8_run6a_NAM
	cp $file /users/asmit101/data/stuff/2006_mod8_run6a_NAM
	cd /users/asmit101/data/stuff/2006_mod8_run6a_NAM
	ncks -d s_rho,-1 -d eta_rho,0,600 -v chlorophyll1,chlorophyll2 $file surfchl_$file
	rm $file
	cd /users/dullman1/data/dullman1/EPSCOR/2006_mod8_run6a_NAM
	echo "Processing $file"
done
