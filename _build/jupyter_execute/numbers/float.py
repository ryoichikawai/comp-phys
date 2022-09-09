#!/usr/bin/env python
# coding: utf-8

# (sec-float)=
# # Floating Point Numbers

# There is no way to express real numbers in discrete systems. For example, we cannot express any irrational number using a finite number of letters 0-9.  Therefore, we express real number approximately using scientific notation such as $1.32567 \times 10^{12}$.  Similarly digital computers use so-called *floating point* representation.  A *single precision* floating point stores a real number in a 32-bit string, of which 24 bits are used for mantissa.  The corresponding significant figure is $\log_{10} 2^{24} \approx 7$.  The exponent part is $2^{2^7}=2^{-128}$ to $2^{2^7-1}=2^{127}$ which is approximately $10^{-38}$ to $10^{+38}$.  One bit is used for the sign, which results in $-0.$ and $+0.$.  They are treated as two different number.
# 
# Usually, the single precision is not accurate enough for computational physics. A *double precision floating point* uses a 64-bit string, 54 bits for mantissa and 10 bits for exponent as shown in {numref}`fig-double-float`.  The largest value the mantissa can express  is $2^{53} = 9007,199,254,740,992$, which corresponds to significant figure 16.  The maximum exponent part is between $2^{-2^9} = 2^{-512} \approx 10^{-308}$ and $2^{2^9-1} = 2^{511} \approx 10^{308}$.[^denormalized]  Any value above the largest floating point number is treated as infinity, which appears as `inf` in output.
# 
# Common CPUs used in desktop and laptop computers are capable of double precision floating point arithmetic.  The default size of floating point in python is 64.
# 
# ```{figure} double-float.png
# :name: fig-double-float
# 
# 64-bit string for floating point expression.  The last bit is used for the sign and 11 bits from $b_{52}$ to $b_{62}$ express the exponent.  The remaining 52 bits express the mantissa.
# ```
# 
# Since the floating point numbers are *quantized*, there is always a gap between the nearest two floating point numbers.  Any values inside the gap cannot be expressed in standard computer languages, which may causes inaccurate results due to quantization error. The positive value next to zero is $1.1754944 \times 10^{-38}$ for single precision. (See {numref}`fig-loating-point-line`.)  If we try to use a number between zero and the smallest floating point value, *underflow error* occurs. 
# Another gap we should pay attention to is the machine epsilon $\epsilon$, the gap between 1 and next number above it.  There is no floating point value between $1$ and $1+\epsilon$. (See  {numref}`fig-loating-point-line`.) 
# 
# ```{figure} floating-point-line.png
# :name: fig-loating-point-line
# 
# Discreteness of floating point numbers.
# ```
# In some cases such as $\sqrt{-1}$, the value is not defined as a real number.  The outcome of such calculation is expressed as `nan`  (not a number).
# 

# [^denormalized]: There is a slightly better enconding known as *denormalized float*.  The smallest value in the denormalized float method is $4.9406564584124654 \times 10^{-324}$ for double and $1.401298 \times 10^{-45}$ for single  which is smaller than the smallest value in the standard floating point method.  Most of modern computer programming language use denormalized float for very small number.  However, if the smallest possible value is asked, the system still returns the value in the standard floating point.

# ## Numpy
# 
# [NumPy](https://numpy.org/doc/stable/user/whatisnumpy.html) is the fundamental package for scientific computing in Python. Although there are other math packages, we use numpy exclusively. See [Numpy documentation](https://numpy.org/doc/stable/) for its usage. A book by Oliphant{cite}`Oliphant2015` is also recommneded.
# 
# 
# In order to use it, we must first load the package.  In this lecture, we load it as
# 
# ```
# import numpy  as np
# ```
# 
# where `np` is a shorthand name of numpy.  This is fairly standard.
# 
# 

# **Example** {numref}`%s <sec-float>`.1   Range of floating point numbers
# 
# Let us try to find the largest and smallest numbers in your computer system.  We use the `float_info` class in `sys` library.

# In[1]:


# load sys package for system information
import sys

fmin = sys.float_info.min
fmax = sys.float_info.max
print("Smallest float =",fmin)
print(" Largest float =",fmax)


# **Example** {numref}`%s <sec-float>`.2   Special value `inf`
# 
# Find what is the outcome of a number larger than the maximum or smaller than minimum.

# In[2]:


print("max * 10 =", fmax*10.)
print("min / 10 =", fmin/10.)
print("min * 10^{-20} =", fmin * 1.e-20)


# Note that the value smaller than the smallest float is obtained.  This means that *denormalized float* [^denormalized] is used below the smallest in the standard float.  However, if the value is even smaller than the smallest in denormalized float, th e anser is replaced with 0.

# **Example** {numref}`%s <sec-float>`.3   Special value `nan`
# 
# See the outcome of $\sqrt{-1}$.

# In[3]:


import numpy as np

print("sqrt(-1)=",np.sqrt(-1))


# In[4]:


import sys

sys.float_info.min
sys.float_info.max


# In[ ]:




