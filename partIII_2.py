# uncomment this line if you need to
#from __future__ import division # make division act like python3 even if 2.7

import numpy.random as npr
import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt

# notes: probability distribution, its integral, and its reverse lookup
#### next 3 lines are pseudo-code, do not uncomment but use for reference
#### p_g=exp((-1.*u**2)/(2.*sigma**2))/(sigma*sqrt(2.*3.14159))
#### intp_g=0.5+0.5*erf(u/sqrt(2.))
#### u_at_given_intp_g= ??? can't solve analytically, create lookup table

# choose nran random numbers in uniform interval 0-1
nran = 10000
xvals = npr.random(nran)

# the integral of uniform distribution p_u*dx (=1*dx) from 0 to x is just x
intp_uni = xvals # rename variable for clarity

# solve for u that gives the same integrated area under p_g
intp_g = intp_uni # rename variable for clarity
u = (np.array([range(0,10000)])-5000)/1000. 
int_u = 0.5+0.5*erf(u/np.sqrt(2.)) # fill in integral of p_g
uvals = 0.*intp_g # creating zero array of same size
for i in range(0,nran):
    diffs = abs(int_u-intp_g[i])
    uvals[i] = u[np.where(diffs == diffs.min())]

# make a histogram
n1, bins1, patches1 = plt.hist(uvals,bins=50,normed=1,histtype='stepfilled')
plt.setp(patches1,'facecolor','g','alpha',0.75)

#overplot expected Gaussian distribution on histogram
#must uncomment "import numpy as np" above to be able to use np.exp and np.sqrt
sigma = 1
gaussfunct = (1/(sigma*np.sqrt(2*np.pi)))*np.exp((-1)*(bins1**2/(2*sigma**2))) # fill in using equation
plt.plot(bins1,gaussfunct,'k--',linewidth=1.5)
