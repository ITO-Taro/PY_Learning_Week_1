# Create a function named add that expects two arguments
# Return the sum of those two arguments.
# Repeat this process for Subtracting, Multiplying and Dividing


num = [123, 78902, 34567]

# ADDITION
def add():
    return sum(num)
print(add())

# SUBTRACTION
def subt():
    return min(num) - max(num)
print(subt())

# MULTIPICATION
def mult():
    return max(num) * min(num)
print(mult())

# DIVISION
import statistics
def div():
    return statistics.median(num)/max(num)
print(div())

def test():
    return statistics.stdev(num)
print(test())

def test1():
    return statistics.variance(num)
print(test1())

def makes10(a,b):
    return (a==10 or b==10 or a+b==10) 
print(makes10)