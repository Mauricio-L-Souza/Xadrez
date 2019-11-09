import os

class Table(object):

	def __init__(self):
		self.__table = []


	def initTable(self):
		self.__table = [
						['TP1', 'CP1', 'BP1', 'REP', 'RAP', 'BP2', 'CP2', 'TP2'],
						['PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'PP6', 'PP7', 'PP8'],
						['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
						['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
						['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
						['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
						['PB1', 'PB2', 'PB3', 'PB4', 'PB5', 'PB6', 'PB7', 'PB8'],
						['TB1', 'CB1', 'BB1', 'REB', 'RAB', 'BB2', 'CB2', 'TB2']
						]

	def printTable(self):
		os.system('cls || reset || clear')
		for line in self.__table:
			print('\n', end = '')
			for slot in line:
				print(slot + '| ', end = '')
		print('')

	def getPiecePosition(self, piece_name):
		for pos_line, line in enumerate(self.__table):
			for pos_slot, piece in enumerate(line):
				if piece_name == piece:
					return [pos_line, pos_slot]

	def movePiece(self, piece_name, end_pos_line, end_pos_slot):
		(old_pos_line, old_pos_slot) = self.getPiecePosition(piece_name)
		empty = '   '

		self.__table[end_pos_line][end_pos_slot] = piece_name
		self.__table[old_pos_line][old_pos_slot] = empty
