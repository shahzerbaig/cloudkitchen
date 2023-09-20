import hashlib


class User:
    limbs = 4
    head = 1

    def __init__(self, name: str, password: str, email: str, phone_number):
        self.name = name
        self.__password = password
        self.email = email
        self.phone_number = phone_number
        self.set_password(password)

    def password(self):
        return self.__password

    def set_password(self, password: str):
        hash_object = hashlib.sha256()

        hash_object.update(password.encode('utf-8'))

        hashed_password = hash_object.hexdigest()
        self.__password = hashed_password



# Rectify this
class EndUser(User):

    def __int__(self,
                name,
                password,
                email,
                phone_number,
                address,
                office_address,
                limbs):
        super().__init__(name, password, email, phone_number)
        self.address = address
        self.office_address = office_address
        pass


eu1 = EndUser("shah",
              "sasa",
              "shaja@awds.com",
              "8978625622",
              )
