class Horse(object):
	
	def __init__(self):
		self.black_horses = ['CP1', 'CP2']
		self.white_horses = ['CB1', 'CB2']

	#old_position[0] - linha

	def validateHorsesMove(self, piece_name, old_position, new_position):
		if self.isBlackHorse(piece_name) or self.isWhiteHorse(piece_name):
			if new_position[0] == old_position[0] - 2:
				if (new_position[1] == old_position[1] - 1) or (new_position[1] == old_position[1] + 1): 
					return True
			
			elif new_position[0] == old_position[0] - 1:
				if (new_position[1] == old_position[1] - 2) or (new_position[1] == old_position[1] + 2):
					return True
			
			elif new_position[0] == old_position[0] + 2:
				if (new_position[1] == old_position[1] - 1) or (new_position[1] == old_position[1] + 1):
					return True

			elif new_position[0] == old_position[0] - 1:
				if (new_position[1] == old_position[1] - 2) or (new_position[1] == old_position[1] + 2):
					return True

		return False


	def isBlackHorse(self, piece_name):
		return piece_name in self.black_horses

	def isWhiteHorse(self, piece_name):
		return piece_name in self.white_horses

	def isHorse(self, piece_name):
		return self.isBlackHorse(piece_name) or self.isWhiteHorse(piece_name)