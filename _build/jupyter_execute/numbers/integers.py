#!/usr/bin/env python
# coding: utf-8

# (sec-integers)=
# # Integers
# 

# Digital computers express everything as bit strings, which are discrete.  Hence, it is not possible to express continuous numbers.
# Integers are discrete and their exact enumeration is possible.  In principle, huge integer can be implemented as long as there is enough memory.   Since version 3, python does not have a limit of integer and it dynamically changes the size of integer  as needed.  However, this feature is rather unique to python and most of common computer languages such as C++ impose a hard limit. If you want to write a transportable code, you need to know the upper limit used in other languages, which we discuss here briefly.
# 
# Encoding integers are relatively simple. First, we express them in binary form $I = \sum_{k=0}^{N-1} 2^k b_k$.
# Then the corresponding binary string $b_{N-1} \cdots b_2 b_1 b_0$ is uniquely express the integer.
# For example, binary number $101$ corresponds to integer $1\times 1+ 2 \times 0 + 4 \times 1 =5$.   Noting that an 8-bit binary string can express $256$ different integers, it expresses integers from 0 to 255. In general, an $N$-bit string encodes integers from 0 to $2^N-1$.  Since negative integer is not included, this type of integer is called *unsigned integer*.
# 
# If a *signed integer* is needed, one bit of the binary string is used to specifies the sign, 0 for $+$ and 1 for $-$, and remaining bits are used for the magnitude. An 8-bit binary string spans from $-128$ to $+127$.  {numref}`table-int-range` shows the range of other integer types.  The default size of signed integer is 32 bit in most computer languages.  However, 64-bit integer can be used for large scale calculation.  Common hardware cannot handle integers larger than 64 bit. If more than 64 bit is needed, you must use a special numerical library.  

# ```{table} The range of unsigned and signed integers
# :name: table-int-range
# 
# |bit size| min | max |
# |:---:|---:|---:|
# |8|-128|+127|
# |16|-32768|+32767|
# |32|-2147483648|+2147483647|
# |64|-9223372036854775808|+9223372036854775807|
# 
# ```
# 

# 
# > **Example** {numref}`%s <sec-integers>`.1  Huge intgers.  Python can handle even $2 \times 10^{100}$.
# 

# In[31]:


print(2 * 10**100)


# While such a huge integers are supported at the software level, hardware (cpu) can't handle large binary strings at each cycle of computation.  The limit is can be obtained by `sys.maxsize`.

# > **Example** {numref}`%s <sec-integers>`.2  Let's us try to find the max size of the hardware.

# In[33]:


import sys
print(sys.maxsize)


# which corresponds to 64 bits.

# 
# ---
# Last modified on 09/08/2022 by R. Kawai.
