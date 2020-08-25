#!/bin/bash
#SBATCH -n 12
#SBATCH --mem=64G
#SBATCH -t 24:00:00
export PYTHONUNBUFFERED=TRUE
python /users/asmit101/data/stuff/surfchl_2006.py
