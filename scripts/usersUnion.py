def find_union(file1, file2):
	
	user_list = []

	with open(file1) as f1, open(file2) as f2:
		
		for line in f1:
			user = line.strip()
			if user not in user_list:
				user_list.append(user)

		for line in f2:
			user = line.strip()
			if user not in user_list:
				user_list.append(user)

	return user_list
	
if __name__ == "__main__":

	users = find_union("users_list_1.txt", "users_list_1.txt")

	print len(users)
