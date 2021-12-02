sample_filepath='../input/sample.txt'
input_filepath='../input/input.txt'

def get_position(position_input):
	coord_dict = {'hor': 0, 'depth': 0}
	with open(position_input) as f:
		for line in f.readlines():
			coords=line.split(' ')
			if coords[0]=='up':
				coord_dict['depth']-=int(coords[1])
			elif coords[0]=='down':
				coord_dict['depth']+=int(coords[1])
			elif coords[0]=='forward':
				coord_dict['hor']+=int(coords[1])
		# print(coord_dict)
		return coord_dict['hor']*coord_dict['depth']


def main():
	pos=get_position(input_filepath)
	print(pos)

if __name__=='__main__':
	main()