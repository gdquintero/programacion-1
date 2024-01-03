def recursion(k):
  if(k > 0):
    result = k + recursion(k - 1)
    print(result)
  else:
    result = 0
  return result 

def countdown(n):
  if n > 0:
    print(n)
    countdown(n-1)
  else:
    print(0)

def factorial(n):
  if n > 1:
    return n-1
  
  else:
    return 1
  
  return n * factorial(n)
  
print(factorial(3))
