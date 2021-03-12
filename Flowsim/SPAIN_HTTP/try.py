import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HTTPS = pd.read_table("HTTPS.dat", sep="\s+", usecols=['x', 'y'])
HTTP = pd.read_table("HTTP.dat", sep="\s+", usecols=['x', 'y'])
HTTP3 = pd.read_table("HTTP3.dat", sep="\s+", usecols=['x', 'y'])

plt.rcParams.update({'font.size': 22})
plt.plot(HTTP3.x, HTTP3.y, label="HTTP3")
plt.plot(HTTPS.x, HTTPS.y, label="HTTPS", color="gold")
plt.plot(HTTP.x, HTTP.y, label="HTTP", color="red")
plt.xlabel("Download[ms]")
plt.ylabel("ECDF")
plt.legend(framealpha=1, frameon=True)
plt.savefig("es.pdf", dpi=500, bbox_inches='tight')
plt.show()