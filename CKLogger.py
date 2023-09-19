"""This is a Module for Logging Events in the system,
    It'll provide support for system specific events and 
    help the Engineer to debug and miss happenings.
    
    *** Inner Working ***
    The Module consist of a Class and Its Method,
    on inititalization the class stores the name 
    of the logger, it also checks for the 
"""
from pathlib import Path
import logging # Built-In Logging Module


class CKLogger:
    """
    This is a Logging class for Cloud Kitchen,
    It have four Methods and an attribute

    1. [Attribute] Name 
    1. log_info()
    2. log_error()
    3. log_warn()
    4. log_critical()

    """
    def __init__(self,name) -> None:
        self.name = name
        root_path = Path.cwd() # Get the current Directory
        dir_path = root_path / "Logs" # Make a new Directory Path

        # Check if directory Exist or not
        if  dir_path.exists():
                log_file_path = Path.cwd() / "Logs" / "system.log"
                logging.basicConfig(filename=log_file_path,level=logging.INFO) 
            
        else :
            try :
                dir_path.mkdir()
                log_file_path = Path.cwd() / "Logs" / "system.log"
                logging.basicConfig(filename=log_file_path,level=logging.INFO) 
                # Configuration for Error logging
                print("Directory Made")
            except:
                print("Error")

    # Function to check if Directory Exists or not 
    def dir_exist(self):
        current = Path.cwd() / "Logs" / "system.log"
        if current.exists():
            return True
        else :
            return False
        
    # Logging Methods for Logging Events into log file
    def log_info(self,msg): 
        logging.info(msg)

    def log_error(self,msg):
        logging.error(msg)

    def log_warn(self,msg):
        logging.warning(msg)

    def log_critical(self,msg):
        logging.critical(msg)

    


new_logger = CKLogger("new_logger")

print(new_logger.dir_exist())





    





