# grib_to_netcdf4

Python script to convert grib files to NetCDF using xarray


The purpose of this script is show how to convert .grib files to NetCDF4 using Xarray. This script is designed for users who are programming on Windows computer and using Ananconda.

Before running the script, ensure to have follow the following step:

1. Open Anaconda prompt

2. Create a new environment (using the code below) to avoid any potential package conflict. Python 3.9 works well for me.

          conda create --name gribenv python=3.9

3. Activate the newly created environnment in order to install the required packages

          conda activate gribenv

4. Install the following packages by following the order below

          pip install ecmwflibs

          pip install eccodes==1.3.1

          pip install cfgrib

          conda install ipykernel

          conda install xarray

5. Go to Jupyter notebook (or Spyder), and connect to to the newly created environment (gribenv)

6. Run the script as described below
