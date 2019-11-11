from .Movements import *

class Bishop(object):
	
	def __init__(self):
		self.black_bishop = ['BP1', 'BP2']
		self.white_bishop = ['BB1', 'BB2'] 		

	def validateBishopMove(self, piece_name, old_position, new_position):
		if self.isBishop(piece_name):
			if diagonal_movements(old_position, new_position):
				return True
		return False	

	def isBlackBishop(self,piece_name):
		return piece_name in self.black_bishop

	def isWhiteBishop(self, piece_name):
	    return piece_name in self.white_bishop

	def isBishop(self, piece_name):
		return self.isBlackBishop(piece_name) or self.isWhiteBishop(piece_name)
		