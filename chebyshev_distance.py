from scipy.spatial.distance import pdist
# Driver code
samp_data = [(3, 3.5),(-5.1, -5.2)]

print(pdist(samp_data,'chebyshev'))