
import numpy as np
import matplotlib.pyplot as plt
import h5py
from scipy.signal import find_peaks


#%%


dict_data = {}
def load_h5(files):

    """ Lädt Daten, öffnet bestimmtes Datanset und macht ein np array draus """
    with h5py.File(files, 'r') as hdf:
        G1 = hdf.get('/0')
        G1_items = list(G1.items())
        #print('Items in Group1: ', G1_items)

        for item in G1:
            data = G1.get(item)
            np_dataset = np.array(data.get('E'))
            dict_data.update({item: np_dataset} )
            #print(item)
            #return dict_data



#%%

load_h5('056_ev.h5')
print(dict_data)

#%%
dict_kurz = {'290': dict_data['290.0'], '300':dict_data['300.0']}
print(dict_kurz)

#%%
plt.clf()
def plot_tof_all(data):
    """ Funktion die alle Daten gelichzetig plottet"""
    figs= {}
    for energy, array in data.items():
        plt.figure() # damit mehrere Fenster geöffnet werden
        xaxis_scale = array * 0.025   # 25 ps (in ns) Genauigkeit der TDCs
        N, bins, patches = plt.hist(xaxis_scale, bins=1592)  # 1592 bins, weil 1592 ns aufgenommen wurde (2 Bunche)
        plt.xlabel('Time of flight [ns]' )
        plt.ylabel('Intensity [arb. unit]')
        plt.title('Time of flight of the electrons by ' + str(energy) +' eV')
        peaks, peak_height_array = find_peaks(N, height=250, distance=12)
        plt.plot(bins[:-1], N)
        plt.plot(bins[peaks], N[peaks], "x")
        plt.show()
        #print(peaks, N[peaks])
        tupelt_peaks = (peaks)
        print(tupelt_peaks)

#%
plot_tof_all(dict_kurz)
#%%

import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
import h5py
#%%

with h5py.File('056_ev.h5', 'r') as hdf:
    ls = list(hdf.keys())
    print('Liste der Datasets in der Datei: ', ls )
    #base_items = list(hdf.items())
    #print('Items in the base directory: ', base_items)
    G1 = hdf.get('/0/310.0')                                             #in den erste Ordner gegangen "0"
    #G1_items = list(G1.items())
    #print('Items in Group1: ', G1_items)
    #data290 =G1.get('/0/290.0')                                   # in den Unterordner "290.0" gegangen
    #data290_items = list(data290.items())
    np_dataset = np.array(G1.get('E'))

                        # in die jeweilige Datenbas (z.B. "EE") gegangen


    print(np_dataset)

#%%
plt.clf()
from scipy.signal import find_peaks
#xaxis_scale = np_dataset/(np.max(np_dataset)/1600)
xaxis_scale = np_dataset * 0.025   # 25 ps Genauigkeit haben die TDCs


N, bins, patches = plt.hist(xaxis_scale, bins=1600)
#plt.hist(xaxis_scale, bins=800)
plt.xlabel('Time of flight [ns]' )
plt.ylabel('Intensity [arb. unit]')
plt.title('Time of flight of the electrons' )

#N1 = N [:10]
N2 = N[1:-1]
N3 = N[2:-2]
#x1 = bins[:10]
x2 = bins[1:-2]
#plt.clf()
maxima = (N2 > 800) & (N2 > N[:-2]) & (N2 > N[2:]) # & operator -> bitwise operators
#maxima_opt = maxima[:-2] & (N3 > N[4:])

maxima = np.logical_and.reduce([N2 > 800, N2 > N[:-2], N2 > N[2:]])

plt.plot(x2[maxima], N2[maxima], "o")
plt.show()

print(x2[maxima], N2[maxima])

