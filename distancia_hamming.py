from scipy.spatial.distance import pdist
samp_data = [(10, 8),
          (10, 12),
          (10, 15),
          (19, 16)]
print(pdist(samp_data,'hamming'))