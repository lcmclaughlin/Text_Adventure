import rooms, parser

def generate_response(action,arguments):
	response = error_no_action
	if action == "quit":
		response = quit_message
	elif action == "look":
		response = rooms.current_room.long_desc
	elif action == "look direction closed":
		response = arguments.desc
	elif action == "look direction open":
		response = arguments.short_desc
	elif action == "look direction error":
		response = look_direction_error
	elif action == "look error":
		response = look_error(arguments)
	elif action == "move":
		response = arguments.show_full_desc()
	elif action == "move direction error":
		response = move_direction_error
	elif action == "move closed":
		response = move_closed_error(arguments.name)
	return response

error_no_action = "I have no idea what you're talking about."
quit_message = "Thanks for playing!\nGoodbye!"
look_direction_error = "There's nothing to look at in that direction."
move_direction_error = "You can't go that way."
welcome = "Welcome!"
prompt = "Enter a command: "

def move_closed_error(s):
	response = "The %s is closed." % s
	return response

def look_error(s):
	response = "I don't see a %s around here." % s
	return response
