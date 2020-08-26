#!/bin/bash
#SBATCH -n 12
#SBATCH --mem=64G
#SBATCH -t 48:00:00
export PYTHONUNBUFFERED=TRUE
python /users/asmit101/data/stuff/surfchl_2018.py
