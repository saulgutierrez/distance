# Using scipy to Calculate the Manhattan Distance
# The Manhattan distance is often referred to as the city block distance or the taxi cab distance. The Manhattan distance can be a helpful measure when
# working with high dimensional datasets.
# The Manhattan distance represents the sum of the absolute differences between coordinates of two points.
# While the Euclidian distance represents the shortest distance, the Manhattan distance represents the distance a taxi cab would have to take
from scipy.spatial.distance import cityblock
# Driver code
x1 = [1,2,3,4,5,6]
x2 = [10,20,30,1,2,3]
print(cityblock(x1, x2))