from entidades.Table import Table
from entidades.Pawn import Pawn
from entidades.Horse import Horse

class Execute(object):
	def __init__(self):
		self.tab = Table()
		self.tab.initTable()
		self.pawn = Pawn()
		self.horse = Horse()

	def execMove(self, piece_name, positions):
		old_position = self.tab.getPiecePosition(piece_name)

		if self.pawn.validateMovePawn(piece_name, old_position, positions):
			self.tab.movePiece(piece_name, int(positions[0]), int(positions[1]))

		elif self.horse.validateHorsesMove(piece_name, old_position, [int(positions[0]), int(positions[1])]):
			self.tab.movePiece(piece_name, int(positions[0]), int(positions[1]))

		else:
			if self.pawn.isPawn(piece_name):
				input('Movimento invalido do peao!')
			elif self.horse.isHorse(piece_name):
				input('Movimento invalido do cavalo!')

		self.showTable()

	def showTable(self):
		self.tab.printTable()