from matplotlib import pyplot as plt
import sys
import numpy as np

for w in [# 1,
          # 10,
          50,
          # 100,
          # 200,
          # 400
          ]:
 for z, i in enumerate(sys.argv[1:]):
  x = eval(open(f"loss-{i}.txt").read())
  x = [np.convolve(np.array(b), np.ones(w), 'valid') / w for b in zip(*x)] 
  f = ['-', '--', '+'][(z-1) % 1# 3
                               ]
  for j, s in enumerate(x):
   if j != 5: continue
   #s = np.array(s)
   #s = np.convolve(s, np.ones(w), 'valid') / w
   plt.plot(s, f, label=i+'-'+str(j))
   # plt.loglog(s, f, label=i+'-'+str(j))
   #  plt.plot(np.mean(x, axis=0), f, label=i+' total')
 plt.legend()
 plt.show()
