#!/usr/bin/env python
# coding: utf-8

# # Bits

# The current digital computers are mostly binary machines\footnote{We don't consider q-bit used in quantum computers.} and use a bit $b$ as the smallest unit of information where $b=0$ or $1$ (or we write it equivalently as $b=\{0,1\}$). Inside a computer,  information is generally encoded in a string of bits such as $01100101000101100\cdots$.  The number of unique expressions depends on the length of the string, which is measured as the number of bits. An $N$-bit string
# 
# $$
# N\text{-bit string} = b_{N-1} b_{N-2} \cdots b_2 b_1 b_0
# $$
# 
# can express $2^N$ different values.  For instance, there are only four possible realizations of a 2-bit string: $00$, $01$, $10$, $11$.  $N$ can be very large but always finite and limited by the size of hardware.[^note-brain]
# The common lengths of the binary string in the present computers are $8$, $16$, $32$, and $64$.   The string of 8 bit is called a byte.  The number of different expressions these strings can have is shown in {numref}`table-binary-sizes`.
# 
# ```{table} Common binary strings and their capacity
# :name: table-binary-sizes
# 
# | size in bits | size in bytes | # of expressions |
# | ---: | ---: | ---: |
# | 8    | 1    | $2^8=256$ |
# | 16   | 2    | $2^{16}=65536$ |
# | 32   | 4    | $2^{32}=4,294,967,296$ |
# | 64   | 8    | $2^{64}=18,446,744,073,709,551,616$|
# ```
# 
# 
# We *encode* numbers and characters in binary strings and *decode* binary strings to get human-readable information.  Encoding/decoding is not a one-to-one map.  
# The same one byte of string may correspond to multiple different things, integer, character, and others as shown in the following sections. For example, $01000001$ can be character 'A' or integer $65$.  Some computer languages (dynamical language) such as python choose an appropriate encoding scheme based on the context but in compiler-based languages, programmers must declare the type of each variable before using it or otherwise the computer issues an error message.
# 
# [^note-brain]: Our brain also consists of a finite number of neurons but it is huge (about $10^{11}$). Despite of that, humans are able to develop the concept of infinity and continuous numbers!

# 
# ---
# Last modified on 09/08/2022 by R. Kawai.

# In[ ]:




