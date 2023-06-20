# %% [markdown]
# # The purpose of this script is show how to convert .grib files to NetCDF4. This script is designed for users who are programming on Windows computer and using Ananconda.
# 
# # Before running the script, ensure to have followed the following steps:
# 
# 1. Open Anaconda prompt
# 
# 2. Create a new environment (using the code below) to avoid any potential package conflict. Python 3.9 works well for me.
# 
#           conda create --name gribenv python=3.9
# 
# 3. Activate the newly created environnment in order to install the required packages
# 
#           conda activate gribenv
# 
# 4. Install the following packages by following the order below
# 
#           pip install ecmwflibs (version 0.5.1)
# 
#           pip install eccodes==1.3.1
# 
#           pip install cfgrib (version 0.9.10.4)
# 
#           conda install ipykernel
# 
#           conda install xarray
# 
# 5. Go to Jupyter notebook (or Spyder), and connect to to the newly created environment (gribenv)
# 
# 6. Run the script as described below

# %%
# Importing the xarray library

import xarray

# %%
# Creating a function that will execute the conversion from grib to NetCDF

def grib_to_nc (grib_file, output_file):

    data = xr.open_dataset(grib_file, engine = "cfgrib")

    data.to_netcdf(output_file, format = "NETCDF4")


# grib_file is the input .grib file and output_file is the NetCDF file to be created

# %%
# Writting the path of the input grib file and the output NetCDF file

grib_file = "C:/Users/public/documents/temperature.grib" # This is where the grib file is located

output_file = "C:/Users/public/documents/converted_temperature.nc" # This is where you want to store the NetCDF file and specify the name of the file

# Launching the conversion process

grib_to_nc(grib_file, output_file)


