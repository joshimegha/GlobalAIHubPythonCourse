lower = 0
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")
def prime(lower,upper):
  for num in range(lower+1, upper):
    # all prime numbers are greater than 1
    if num > 1:
      for i in range(2, num):
        if (num % i) == 0:
          break
      else:
        print(num)
prime(lower,upper)
