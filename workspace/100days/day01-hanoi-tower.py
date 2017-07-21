#%%#
"""
To move N disks from left to right:
#1 [recurisively] move N-1 disks from left to right
#2 move largest disk from left to right
#3 [recurisively] move N-1 disks from middle to right
"""
def hanoi(height, left='left', middle='middle', right='right'):
  if height:
    hanoi(height - 1, left, right, middle)
    print(left, '=>', right)
    hanoi(height - 1, middle, left, right)

hanoi(2)