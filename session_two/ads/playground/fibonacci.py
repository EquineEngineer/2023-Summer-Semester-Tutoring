def F(n):
  """
  Compute the Fibonacci sequence up to the given n
  """
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return F(n-1) + F(n-2)