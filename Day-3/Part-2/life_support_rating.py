import sys
sys.path.append('../Part-1')
from common_bit import get_bit_list, get_revised_list, get_common_bit

sample_filepath='../input/sample.txt'
input_filepath='../input/input.txt'

def get_oxygen_gen_rate(bit_list):
	pattern=''
	x=bit_list
	for i in range(len(bit_list[0])):
		temp_list=[]
		rev_list=get_revised_list(x)
		mcb, lcb=get_common_bit(rev_list)
		pattern+=mcb[i]
		if len(x)==2  and x[0][i]!=x[1][i]:
			for b in x:
				if b[i]=='1':
					return b
		elif len(x)==1:
			return x
		else:
			for b in x:
				if b[:i+1] == pattern:
					temp_list.append(b)
		x=temp_list.copy()

def get_co2_scrubber_rate(bit_list):
	pattern=''
	x=bit_list
	for i in range(len(bit_list[0])):
		temp_list=[]
		rev_list=get_revised_list(x)
		mcb, lcb=get_common_bit(rev_list)
		pattern+=lcb[i]
		if len(x)==2  and x[0][i]!=x[1][i]:
			for b in x:
				if b[i]=='0':
					return b
		elif len(x)==1:
			return x
		else:
			for b in x:
				if b[:i+1] == pattern:
					temp_list.append(b)
		x=temp_list.copy()

def main():
	bit_list=get_bit_list(input_filepath)
	ogr=get_oxygen_gen_rate(bit_list)
	csr=get_co2_scrubber_rate(bit_list)
	life_support_rate=int(ogr,2)*int(csr,2)
	print(f"Life support rate is {life_support_rate}.")

if __name__=='__main__':
	main()