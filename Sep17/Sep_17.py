from functools import reduce

product_price = [37,85,90,41,49,59,21,82,99]

# 1) Addition
# def add(pri, val):
#     return pri + val
# total = reduce(add, product_price, 0)
# print(f"sum of list is = {total}")

# sum of list is = 563


# 2) Multiplication
# def multiply(pri, val):
#     return pri * val
# product = reduce(multiply, product_price, 1)
# print(f"product of all list is = {product}")

# product of all list is = 5719570918884900


# 3) Maximum
# def max_num(pri, val):
#     if val > pri:
#         return val
#     return pri
# maximum = reduce(max_num, product_price)
# print(f"maximum numbers of given list is : {maximum}")

# maximum numbers of given list is : 99


# 4) Minimum
# def min_num(pri, val):
#     if pri > val :
#         return val
#     return pri
# minimum = reduce(min_num, product_price)
# print(f"minimum price of given list is : {minimum}" )

# minimum price of given list is : 21


# 5) Average
# def avg(pri, val):
#     return pri + val
# total_price = reduce(avg, product_price, 0)
# avgerage = total_price/len(product_price)
# print(f"average of given product price list is : {avgerage}")

# average of given product price list is : 62.55555555555556


# 6) Divide 
# def divide(pri, val):
#     return pri / val
# divide = reduce(divide, product_price)
# print(f" after divide list element we get the final answer is: {divide}")

#  after divide list element we get the final answer is: 2.393536192513727e-13


# 7) Count occourances
# words = ["a", "b", "a", "c", "b", "a"]

# def count_alphabet(acc, val):
#     if val in acc:
#         acc[val] += 1
#     else:
#         acc[val] = 1
#     return acc

# counts = reduce(count_alphabet, words, {})

# print(f" counts of alphabet in given list is : {counts}")

# counts of alphabet in given list is : {'a': 3, 'b': 2, 'c': 1}

