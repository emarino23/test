class UserDto():
    def __init__(self, data):
        self.user_id = data.get("user_id") or None
        self.description = data.get("description") or None
        self.created = data.get("created") or None
        self.updated = data.get("updated") or None
        self.firstname = data.get("firstname") or None
        self.lastname = data.get("lastname") or None
        self.username = data.get("username") or None
        self.password = data.get("password") or None
        self.identification = data.get("identification") or None
        self.state = data.get("state") or None
        self.email = data.get("email") or None
        self.phone = data.get("phone") or None
        self.confirmation = data.get("confirmation") or None
        self.user_type_id = data.get("user_type_id") or None
        self.is_active = data.get("is_active") or None

    def set(self, attr):
        setattr(self, attr, attr)

    def __dict__(self):
        return {
            "user_id": self.user_id,
            "description": self.description,
            "created": self.created,
            "updated": self.updated,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "password": self.password,
            "identification": self.identification,
            "state": self.state,
            "email": self.email,
            "phone": self.phone,
            "confirmation": self.confirmation,
            "user_type_id": self.user_type_id,
            "is_active": self.is_active,
        }


class UserListDto():
    def __init__(self, data):
        self.user_list = []
        for d in data:
            userDto = UserDto(d)
            self.user_list.append(userDto)

    def __dict__(self):
        return {
            "user_list": self.user_list
        }

    def __list__(self):
        return self.user_list
