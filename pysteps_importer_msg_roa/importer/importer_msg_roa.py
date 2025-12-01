# -*- coding: utf-8 -*-
"""
One-line description of this module. E.g.

This is a more extensive description (optional) that describes the readers implemented
in this module and other relevant information.
"""

# Import the needed libraries
import numpy as np

## Uncomment the next lines if pyproj is needed for the importer.
 try:
     import pyproj

     PYPROJ_IMPORTED = True
 except ImportError:
     PYPROJ_IMPORTED = False

from pysteps.decorators import postprocess_import

# Function import_abc_xxx to import XXX-format
# files from the ABC institution

@postprocess_import()
def import_msg_roa(filename, var="precipitation"):
    """
    Import precipitation field from Rain over Africa product generated using meteosat
    second generation data.

    Parameters
    ----------
    filename : str
        Name of the file to import.

    var : str
        Variable to be read from the file, for the Leeds generated files this is simply precipitation.

    Returns
    -------
    out : tuple
        A three-element tuple containing the precipitation field, quality field and metadata.
        The quality field is currently set to None.
    """

    import netCDF4

    ds_rainfall = netCDF4.Dataset(filename)
    metadata = {}
    if var in ds_rainfall.variables.keys():
        precipitation = ds_rainfall.variables[var][:]
        lat = ds_rainfall.variables["latitude"][:]
        lon = ds_rainfall.variables["longitude"][:]
        x = ds.variables["x"][:]
        y = ds.variables["y"][:]
        metadata["unit"] = ds_rainfall.variables[var].units
    else:
        precipitation = None
        latitude = None
        longitude = None
        x = None
        y = None

    ds.close

    metadata["institution"] = "Rain over Africa"
    metadata["projection"] = (
        "+proj=geos "
        "+h=35785831.0 "
        "+lon_0=0 "
        "+x_0=0 +y_0=0 "
        "+sweep=y "
        "+units=m +no_defs"
    )
    metadata["cartesian_unit"] = "m"

    # --- domain bounding box ---
    metadata["x1"] = float(x.min())
    metadata["x2"] = float(x.max())
    metadata["y1"] = float(y.min())
    metadata["y2"] = float(y.max())

    # --- pixel size ---
    metadata["xpixelsize"] = abs(x[1] - x[0])
    metadata["ypixelsize"] = abs(y[1] - y[0])

    # MSG has origin at upper-left (y decreases as row increases):
    if y[0] > y[-1]:
        metadata["yorigin"] = "upper"
    else:
        metadata["yorigin"] = "lower"

    # --- extra pysteps metadata ---
    metadata["transform"] = None
    metadata["accutime"] = None
    metadata["threshold"] = np.nanmin(precip[precip > -9999])  # or adapt
    metadata["zero_value"] = 0.0
    quality = None

    return precip, quality, metadata

