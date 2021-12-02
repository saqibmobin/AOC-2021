sample_filepath='../input/sample.txt'
input_filepath='../input/input.txt'

def get_position(position_input):
	hor=0
	depth=0
	aim=0
	with open(position_input) as f:
		for line in f.readlines():
			coords=line.split(' ')
			if coords[0]=='up':
				aim-=int(coords[1])
			elif coords[0]=='down':
				aim+=int(coords[1])
			elif coords[0]=='forward':
				hor+=int(coords[1])
				depth+=aim*int(coords[1])
		return hor*depth


def main():
	pos=get_position(input_filepath)
	print(pos)

if __name__=='__main__':
	main()