import numpy as np
import matplotlib.pyplot as plt

mu_0 = 0.000001256637061
m = 80500000000000000000000
#




#
atis = np.array([

    [0, 0, 6370000],
    [10, 10, 10000000],
    [2000000, 3000000, 10000000],

])
#
B_guc = []
for i in atis:
    r = np.linalg.norm(i)
    theta = np.arccos(i[2] / r)
    B_r = (mu_0 / (4 * np.pi)) * (m / r ** 3) * (2 * np.cos(theta))
    B_theta = (mu_0/ (4 * np.pi)) * (m / r ** 3) * (np.sin(theta))
    B_tot= np.sqrt(B_r ** 2 + B_theta ** 2)
    B_guc.append(B_tot)

plt.plot(np.arange(len(B_guc)), B_guc)
plt.xlabel('Zaman')
plt.ylabel('Manyetik Alan Gücü (T)')
plt.title('Apollo 11\'in Hareketi Boyunca Maruz Kaldığı Manyetik Alan Kuvveti')
plt.show()
