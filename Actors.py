import hashlib

class User:
    def __init__(self,name: str,password:str,email:str,phone_number):
        self.name = name
        self._password = password
        self.email = email
        self.phone_number = phone_number
        self.set_password(password)

    def get_password(self):
            return self._password        
    
    def set_password(self,password : str):
        hash_object = hashlib.sha256()

        hash_object.update(password.encode('utf-8'))

        hashed_password = hash_object.hexdigest()
        self._password = hashed_password

    

    