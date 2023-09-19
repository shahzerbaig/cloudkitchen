# __author__ = "BaiG"

from CKLogger import CKLogger

def main():
    user_input = {"Name": "",
                  "Password": "",
                  "email": "",
                  "phone_number": ""}
    
    for key in user_input:
        new_value = input(f"Enter {key}: ")
        user_input[key] = new_value
    
    logger = CKLogger("Logger")
    
    # Log user input
    logger.log_info("User Input:")
    for key, value in user_input.items():
        logger.log_info(f"{key}: {value}")
    
    logger.log_warn("This is a warning msg")
    logger.log_info("This is just an Info")

if __name__ == '__main__':
    main()
