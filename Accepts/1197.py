while True:
  try:
      num = list(map(int,input().split()))
      print((num[0]*num[1])*2)
  except EOFError:
    break
