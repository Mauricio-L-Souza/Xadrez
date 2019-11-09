from Throw import Throw

class Game(Throw):
	
	def play(self):
		_input = self.getInput()
		piece_name = _input[0]
		positions = _input[1]
		self.execMove(piece_name, positions)
		

	def getInput(self):
		_input = input("Digite seu movimento ex.: PP2-4x1: ")
		_input = _input.split('-')

		piece_name = _input[0]

		positions = _input[1].split('x')

		return [piece_name, positions]

	def gameLoop(self):
		while 1:
			self.play()