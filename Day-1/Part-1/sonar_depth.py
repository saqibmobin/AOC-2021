input_filepath='../input/input.txt'
sample_filepath='../input/sample.txt'

def get_incremental_depth(depth):
	count=0
	prev=None
	with open(depth, 'r') as f:
		for line in f:
			number=int(line.split()[0])
			if prev==None:
				prev=number
			elif number>prev:
				count+=1
				prev=number
			else:
				prev=number

	return count	
	

def main():
	count=get_incremental_depth(input_filepath)
	print(f"Number of times depth measurement increased is {count}")


if __name__=='__main__':
	main()