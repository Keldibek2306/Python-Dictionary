permissions = {"read": True, "write": False, "delete": True}

for permission in permissions:
    if permissions[permission] == True:
        print(permission)    