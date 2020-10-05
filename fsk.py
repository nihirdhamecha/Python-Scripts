import numpy as np
from matplotlib import pyplot as plt


n = 2000
fs = 10000
fc = 100
fm = 10
fd = 40


N = np.arange(n)

cr = np.sin(2*np.pi*(fc/fs)*N)

m_t = np.sin(2*np.pi*(fm/fs)*N)
m_t = [1 if i > 0 else -1 for i in m_t]
i_m_t = []
sm = 0
for i in m_t:
    sm += i
    i_m_t.append(sm/fs)

i_m_t = np.array(i_m_t)
s_t = np.cos(2*np.pi*(fc/fs)*N + 2*np.pi*fd*i_m_t)


fig, ax = plt.subplots(2, 2)
ax[0, 0].plot(N, cr)
ax[0, 1].plot(N, m_t)
ax[1, 0].plot(N, i_m_t)
ax[1, 1].plot(N, s_t)

plt.grid()
plt.show()
