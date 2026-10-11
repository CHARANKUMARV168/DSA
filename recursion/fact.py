def count(N):
  if N == 1 or N == 0:
    return 1
  return N * count(N-1)

x = count(4)
print(x)