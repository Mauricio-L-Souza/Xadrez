from entidades.Table import Table

class Throw(object):
	def __init__(self):
		self.tab = Table()
		self.tab.initTable()
		self.tab.printTable()

	def execMove(self, name_piece, positions):
		self.tab.movePiece(name_piece, int(positions[0]), int(positions[1]))
		self.tab.printTable()
