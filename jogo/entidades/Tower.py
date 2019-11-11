from .Movements import *

class Tower(object):
	
	def __init__(self):
		self.black_tower = ['TP1', 'TP2']
		self.white_tower = ['TB1', 'TB2']

	def validateTowersMove(self, piece_name, old_position, new_position):
		if self.isTower(piece_name):	
			if horizontal_movement(old_position, new_position):
				return True
			
			elif vertical_movement(old_position, new_position):
				return True

		return False

	def isBlackTower(self, piece_name):
		return piece_name in self.black_tower

	def isWhiteTower(self, piece_name):
		return piece_name in self.white_tower

	def isTower(self, piece_name):
		return self.isBlackTower(piece_name) or self.isWhiteTower(piece_name)