
def horizontal_movement(old_position, new_position):
	if new_position[0] == old_position[0]:
		return True
	return False

def vertical_movement(old_position, new_position):
	if new_position[1] == old_position[1]:
		return True
	return False
	
def diagonal_movements(old_position, new_position):
	diag = abs(new_position[1] - old_position[1])
	if new_position[0] == new_position[1]:
		return False
	if new_position[0] > old_position[0] and new_position[1] > old_position[1] and diag == old_position[0]:	
		return True 
	elif new_position[0] < old_position[0] and new_position[1] < old_position[1] and diago == old_position[0]:
		return True
	elif new_position[0] > old_position[0] and new_position[1] < old_position[1] and diag == old_position[0]:
		return True
	elif new_position[0] < old_position[0] and new_position[1] > old_position[1] and diag == new_position[0]:
		return True

	return False
