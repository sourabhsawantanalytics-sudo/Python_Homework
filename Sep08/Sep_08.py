# 1) Right Traingle / Left align traingle
# def star_pattern(rows):
#     for i in range(1, rows + 1):
#         print("*" * i)
# star_pattern(5)

# *
# **
# ***
# ****
# *****

# 2) Inverted Right Traingle
# def inverted_traingle(rows):
#     for i in range(rows, 0, -1):
#         print("*" * i )
# inverted_traingle(5)

# *****
# ****
# ***
# **
# *

# 3) Pyramid (Equilateral Traingle)
# def pyramid(rows):
#     for i in range(1, rows + 1):
#         spaces = " " * (rows - i)
#         stars = "*" * (2*i -1)
#         print(spaces+stars)
# pyramid(5)

#     *
#    ***
#   *****
#  *******
# *********

# 4) Inverted Traingle Pyramid
# def inverted_pyramid(rows):
#     for i in range(rows,0,-1):
#         print(" " * (rows-i)+ '*' * (2 * i - 1))
# inverted_pyramid(5)

#  *********
#   *******
#    *****
#     ***
#     *


# 5) Diamond
# def diamond(n):
#     # Upper part
#     for i in range(1, n + 1):
#         print(" " * (n - i) + "* " * i)

#     # Lower part
#     for i in range(n - 1, 0, -1):
#         print(" " * (n - i) + "* " * i)

# diamond(5)

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

# 6) Star Rectangle/Grid pattern
# def star_rectangle(rows, cols):
#     for i in range(rows):
#         print('*' * cols)
# star_rectangle(4 , 4)

# ****
# ****
# ****
# ****

# 7) Number Traingle Pattern
# def number_traingle(rows):
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()
# number_traingle(5) 

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

# 8) Alphabet Traingle Pattern
# def alphabet_traingle(n):
#     for i in range (n, 0, -1):
#         letters = ''
#         for j in range(i):
#             letters += chr(65+j) #65 = 'A'
#         print(letters)
# alphabet_traingle(4)

# ABCD
# ABC
# AB
# A