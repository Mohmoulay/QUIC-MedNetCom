import json
import time
import json
import re
import argparse
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
from datetime import datetime



f = open("HTTP.json")
text = f.read()
loaded_json = json.loads(text)
# print(loaded_json)
# for distro in loaded_json:
#     print(distro['metrics_updated'])
# data = [json.loads(line) for line in open('HTTP3.json', 'r')]

def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

KPI = ['XferTime', 'min_rtt','latest_rtt','rtt_variance','congestion_window','bytes_in_flight','packets_in_flight']
# RTT min
metric = extract_values(loaded_json, KPI[0])
# print(metric)
res = list(map(lambda st: str.replace(st, "ms", ""), metric))
res1 = list(map(float, res))
# print(res)
# print(res1)
# min_rtt = np.transpose(res1)
min_rtt = res1
print(min_rtt)

ecdf_min = ECDF(min_rtt)
plt.plot(ecdf_min.x, ecdf_min.y)
data = np.column_stack((ecdf_min.x, ecdf_min.y))

print(ecdf_min.y)
# plt.show()
np.savetxt('HTTP.dat', data)