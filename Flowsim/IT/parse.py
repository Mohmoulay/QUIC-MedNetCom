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



f = open("QUIC_1M_IT.json")
text = f.read()
loaded_json = json.loads(text)
# print(loaded_json)
# for distro in loaded_json:
#     print(distro['metrics_updated'])
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

KPI = ['smoothed_rtt', 'min_rtt','latest_rtt','rtt_variance','congestion_window','bytes_in_flight','packets_in_flight']

metric = extract_values(loaded_json, KPI[1])
print(len(metric))
# time_sta = extract_values(loaded_json, KPI[4])
# dt_object = datetime.fromtimestamp(timestamp)

# print(names)
s_rtt = np.transpose(metric)
plt.hist(s_rtt)
plt.show()
ecdf = ECDF(s_rtt)
# get cumulative probability for values
print('P(x<20): %.3f' % ecdf(20))
print('P(x<40): %.3f' % ecdf(40))
print('P(x<60): %.3f' % ecdf(60))
plt.plot(ecdf.x,ecdf.y)
plt.xlabel(KPI[1])
plt.ylabel("ECDF")

plt.show()
