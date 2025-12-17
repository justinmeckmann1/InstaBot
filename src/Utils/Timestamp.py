from datetime import datetime

def print_timestamp(): 
    """_summary_
    
    Prints the current date and time to console. 
    Used for logging
    
    """
    print(datetime.now().strftime("%b %d, %Y %H:%M:%S"))