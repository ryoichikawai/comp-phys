#!/usr/bin/env python
# coding: utf-8

# (sec-characters)=
# # Characters
# 

# In English or most of western languages, the number of alphanumeric characters is less than $256$.  Hence, all characters can be encoded in one byte ($8$-bit) binary string.  In US, the encoding map is known as American Standard Code for Information Interchange or [ASCII](https://en.wikipedia.org/wiki/ASCII) and lower and upper cases of all letters and various symbols are encoded in 7-bit strings.  For example, 'A'=1000001B and 'a'=1100001B. (B at the end indicates that it is a binary string.)  Note that integer 1=00000001B and character '1'=00110001B in ASCII are two different things.  Sending 00000001B to a printer does not print 1.  You need to convert a number to a character string. When you type  '1' on a keyboard, you are sending character '1' to computer.  You need to convert it to integer. I/O functions do that automatically.  If you want to convert manually using  funtions `str()` and `int()`.  See Example below
# 
# Some languages use a lot more characters than $256$.  For example, Chinese uses several thousand characters.  Therefore, $8$-bit string is not large enough. Two-byte ($16$-bit) strings can encode $65536$ characters, which seems long enough for all languages.
# 
# In python, character strings are enclosed in "..." or '...', for example 'Hello world!'.

# >**Example** {numref}`%s <sec-characters>`.1  Converstion from a character string to the corresponding integer.
# 
# Let us convert character string '365' to integer $365$ using `int()`.

# In[3]:


int('365')


# >**Example** {numref}`%s <sec-characters>`.2  Converstion from an integer to the corresponding character string.
# 
# Try to convert integer $365$  to character string '365' using `str()`.

# In[4]:


str(365)


# >**Example** {numref}`%s <sec-characters>`.3 print` function automatically converts numbers to characters nd send it to display.

# In[13]:


x=365
a=print(x)


# **Example** {numref}`%s <sec-characters>`.3   Conversion using variables.
# 
# We store an integer 365 in a variable x, then convert it to character and store it in another variable c. Using an enquirer function `type()`, we check the type of the variables.  Notice that printout of x and c are identical but their type is different.

# In[8]:


x = 365
print("x=",x," and  its type is ",type(x))
c = str(x)
print("c=",c," and  its type is ",type(c))


# 
# ---
# Last modified on 09/08/2022 by R. Kawai.
