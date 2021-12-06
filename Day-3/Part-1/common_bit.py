sample_filepath='../input/sample.txt'
input_filepath='../input/input.txt'

def get_bit_list(bit_filepath):
	bit_list=[]
	with open(bit_filepath, 'r') as f:
		for line in f.readlines():
			bit_list.append(line.strip())
	return bit_list

def get_revised_list(bit_list):
	rev_list=[]
	for i in range(len(bit_list[0])):
		temp=''
		for j in range(len(bit_list)):
			temp+=bit_list[j][i]
			# print(temp)
		rev_list.append(str(temp))
	return rev_list

def get_common_bit(rev_list):
	mcb=''
	lcb=''
	for binr in rev_list:
		if binr.count('0')>binr.count('1'):
			mcb+= '0'
			lcb+='1'
		else:
			lcb+='0'
			mcb+='1'
	return mcb, lcb


def main():
	bit_list=get_bit_list(input_filepath)
	rev_list=get_revised_list(bit_list)
	mcb, lcb=get_common_bit(rev_list)
	gamma=int(mcb, 2)
	epsilon=int(lcb, 2)
	power=gamma*epsilon
	print(f"The power consumption is {power}")

if __name__=='__main__':
	main()