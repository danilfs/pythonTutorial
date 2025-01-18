# user_roles = ("admin", "editor", "viewer")
# print(user_roles)  # Outputs: ("admin", "editor", "viewer")
#
# user_roles = ("admin", "editor", "viewer")
# print(len(user_roles))  # Outputs: 3
#
# for role in user_roles:
#     print(role)
#
# print("admin" in user_roles)  # Outputs: True
# print("writer" in user_roles)


user_roles = ('adm', 'user', 'writer')

# for role in user_roles:
# 	print(role)

# print(len(user_roles))

# role_1, role_2, role_3 = user_roles
# print(role_1, role_2, role_3)

# user_roles[1] = 'author'
# print(user_roles)

# not_tuple = ('admin')
# print(type(not_tuple))
#
# real_tuple = ('admin',)
# print(type(real_tuple))

role_1, role_2, _ = user_roles
print(role_1)
print(role_2)