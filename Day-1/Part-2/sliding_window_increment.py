input_filepath='../input/input.txt'
sample_filepath='../input/sample.txt'

def get_depth_list(depth, window_size=3):
  depth_list=[]
  with open(depth, 'r') as f:
    for line in f:
      depth_list.append(int(line.split()[0]))
  
  return depth_list

def get_sliding_window(depth_list):
  depth_sliding_win=[]
  pointer=0
  while pointer<len(depth_list)-2:
    depth_sliding_win.append(depth_list[pointer]+depth_list[pointer+1]+depth_list[pointer+2])
    pointer+=1
  
  return depth_sliding_win

def get_increment_count(depth_sliding_win):
  prev=None
  count=0
  for depth in depth_sliding_win:
    if prev==None:
      pass
    elif depth>prev:
      count+=1
    prev=depth

  return count

def main():
  depth_list=get_depth_list(input_filepath)
  depth_sliding_win=get_sliding_window(depth_list)
  count=get_increment_count(depth_sliding_win)
  print(f"Number of times depth measurement increased is {count}")

if __name__=='__main__':
  main()
  






