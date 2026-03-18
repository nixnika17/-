sh = int(input())
v = list(map(int,input().split()))

total = sum(v)
for m in range(sh,0, -1):
   if total % m == 0:
      target = total // m
      cursum = 0
      ok = True
      for x in v:
        cursum += x
        if cursum == target:
          cursum = 0
        elif cursum > target:
          ok = False
          break
        

      if ok and cursum == 0:
        print(m - 1)
        break

