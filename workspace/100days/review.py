#%%#
def hanoi(height, left='left', middle='middle', right='right'):
  if(height):
    hanoi(height - 1, left, right, middle)
    print(left, "=>", right)
    hanoi(height - 1, middle, left, right)

hanoi(3)