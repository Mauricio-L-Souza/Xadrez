from entidades.Table  import Table
from entidades.Pawn   import Pawn
from entidades.Horse  import Horse
from entidades.Tower  import Tower
from entidades.King   import King
from entidades.Bishop import Bishop
from entidades.Queen  import Queen

class Execute(object):
	def __init__(self):
		self.tab = Table()
		self.tab.initTable()

		self.pawn = Pawn()
		self.horse = Horse()
		self.tower = Tower()
		self.bishop = Bishop()
		self.king = King()
		self.queen = Queen()


	def execMove(self, piece_name, positions):
		old_position = self.tab.getPiecePosition(piece_name)

		if self.pawn.validatePawnsMove(piece_name, old_position, positions):
			self.tab.movePiece(piece_name, int(positions[0]), int(positions[1]))

		elif self.horse.validateHorsesMove(piece_name, old_position, [int(positions[0]), int(positions[1])]):
			self.tab.movePiece(piece_name, int(positions[0]), int(positions[1]))

		elif self.tower.validateTowersMove(piece_name, old_position, [int(positions[0]), int(positions[1])]):
			self.tab.movePiece(piece_name, int(positions[0]), int(positions[1]))

		elif self.bishop.validateBishopMove(piece_name, old_position, [int(positions[0]), int(positions[1])]):
			 self.tab.movePiece(piece_name, int(positions[0]), int(positions[1]))

		else:
			if self.pawn.isPawn(piece_name):
				input('Movimento invalido do peao!')
			elif self.horse.isHorse(piece_name):
				input('Movimento invalido do cavalo!')
			elif self.tower.isTower(piece_name):
				input('Movimento invalido da torre!')
			elif self.bishop.isBishop(piece_name):
				input('Movimento invalido do bispo!')
 
		self.showTable()

	def showTable(self):
		self.tab.printTable()