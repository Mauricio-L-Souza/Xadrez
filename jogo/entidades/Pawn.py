
class Pawn(object):
	
	def __init__(self):
		self.black_pawns = ['PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'PP6', 'PP7', 'PP8']
		self.white_pawns = ['PB1', 'PB2', 'PB3', 'PB4', 'PB5', 'PB6', 'PB7', 'PB8']
		self.first_bpawn_pos = 1
		self.first_wpawn_pos = 6

	def validatePawnsMove(self, piece_name, old_position, new_position):
		if self.isBlackPawn(piece_name):
			if old_position[0] == self.first_bpawn_pos and int(new_position[0]) == 3:
				return True
			elif int(new_position[0]) == old_position[0] + 1:
				return True
			return False

		if self.isWhitePawn(piece_name):
			if old_position[0] == self.first_wpawn_pos and int(new_position[0]) == 4:
				return True
			elif int(new_position[0]) == old_position[0] - 1:
				return True
			return False

		return False


	def isBlackPawn(self, piece_name):
		return piece_name in self.black_pawns

	def isWhitePawn(self, piece_name):
		return piece_name in self.white_pawns

	def isPawn(self, piece_name):
		return self.isWhitePawn(piece_name) or self.isBlackPawn(piece_name)
		#return (piece_name in self.white_pawn) or (piece_name in self.black_pawn)