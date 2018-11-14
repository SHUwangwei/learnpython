import argparse
from PIL import Image
#coding=utf-8
'''
Python 图片转字符画 

'''

if __name__ == '__main__':
	def printchar(path):
		image = Image.open(path)
		width,height = image.size
		width = 80
		height = 80
		# if width>80:
		# 	height = int((height/width)*80)
		# elif height>80:
		# 	width = int((width/height)*80)
		image = image.resize((width,height))
		image = image.convert('L')
		print(image.size)
		txt = ''
		for i in range(height):
			for j in range(width):
				gray = image.getpixel((j,i))
				txt += ascii_char[int(gray*length/256)]
			txt+='\n'
		return txt
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	imgpath = args.path
	ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
	length = len(ascii_char)
	txt = printchar(imgpath)
	print(txt)





