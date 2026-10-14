nums = [5,3,7,1]
res = []

if len(nums) == 1 :
  print([[],nums[0]])
def back(ind , cur=[]) :
  if ind >= len(nums):
    res.append(cur.copy())
    return
  cur.append(nums[ind])
  back(ind+1,cur)
  cur.pop()
  back(ind+1,cur)

back(0,cur=[])
print(res)