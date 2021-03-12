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



f = open("QUIC_fernando.json")
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
# RTT min
metric = extract_values(loaded_json, KPI[1])
print(len(metric))
min_rtt = np.transpose(metric)
#v3 = plt.hist(s_rtt)
#sns.catplot(v3)
#plt.show()
ecdf_min = ECDF(min_rtt)
# get cumulative probability for values
# print('P(x<20): %.3f' % ecdf(20))
# print('P(x<40): %.3f' % ecdf(40))
# print('P(x<60): %.3f' % ecdf(60))
# plt.plot(ecdf.x,ecdf.y)
# plt.xlabel(KPI[3])
# plt.ylabel("ECDF")

# plt.show()

# Smoothed RTT
metric_s = extract_values(loaded_json, KPI[0])
print(len(metric))
s_rtt = np.transpose(metric_s)
ecdf_s = ECDF(s_rtt)
# latest RTT
metric_l = extract_values(loaded_json, KPI[2])
# print(len(metric))
l_rtt = np.transpose(metric_l)
ecdf_l = ECDF(l_rtt)

# Congestion
metric_c = extract_values(loaded_json, KPI[4])
# print(len(metric))
c_rtt = np.transpose(metric_c)
ecdf_c = ECDF(c_rtt)

# Byte in flight
metric_b = extract_values(loaded_json, KPI[5])
# print(len(metric))
b_rtt = np.transpose(metric_b)
ecdf_b = ECDF(b_rtt)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(ecdf_s.x, ecdf_s.y)
axs[0, 0].set_title('RTT_min [ms]')
axs[0, 1].plot(ecdf_l.x, ecdf_l.y, 'tab:orange')
axs[0, 1].set_title('Latest RTT [RTT]')
axs[1, 0].plot(ecdf_c.x, ecdf_c.y, 'tab:green')
axs[1, 0].set_title('Congestion Window')
axs[1, 1].plot(ecdf_b.x, ecdf_b.y, 'tab:red')
axs[1, 1].set_title('Byte in fligths')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='ECDF')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.savefig("all.pdf")
plt.show()
