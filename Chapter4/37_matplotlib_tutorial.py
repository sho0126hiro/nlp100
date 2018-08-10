# -*- coding: utf-8 -*-
# 参考：http://www.mwsoft.jp/programming/numpy/plot_cui.html
import matplotlib
matplotlib.use('Agg') # error除去のため

import matplotlib.pylab as plt
plt.plot( [1, 2, 3] )
plt.savefig( '37_tutorial.png' )