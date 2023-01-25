import cartopy
import cartopy.mpl.geoaxes
import cartopy.crs as ccrs

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

ax = plt.axes(projection=ccrs.Robinson())
ax.coastlines()
plt.savefig('working.png')
