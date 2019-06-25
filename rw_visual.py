import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
point_numbers = list(range(rw.num_points))

# alpha 设置透明度
plt.scatter(rw.x_val, rw.y_val, c=point_numbers, cmap=plt.cm.plasma, edgecolor='none', alpha=0.1, s=55)
plt.show()
