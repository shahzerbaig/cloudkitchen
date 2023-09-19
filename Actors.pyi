class User:

    """This is An interface class""" 
    def __init__(self,name: str,password:str,email:str,phone_number):
        ...
    
    def get_password(self):
        ...
    
    def set_password(self,password : str):
        ...
        