
def main():
	red_dress = dress("red")
	red_dress.wear_dress()
	print(red_dress.color)
	print(red_dress.state)



	black_dress = dress("black")
	black_dress.wear_dress()
	print(black_dress.color)
	print(black_dress.state)






class dress(object):
	"""docstring for ClassName"""
	def __init__(self, color):
		self.color = color
		self.state = "new"

	def wear_dress(self):
		self.state = "used"

		

if __name__ == '__main__':
	main()