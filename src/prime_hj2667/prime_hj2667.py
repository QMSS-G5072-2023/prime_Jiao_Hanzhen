import math

def is_prime(n):
    
    """
    Determine if a given number is prime.
    
    Purpose:
        This function checks if a number is prime or not. A prime number is a number 
        greater than 1 that is not divisible by any other number other than 1 and itself.
    
    Inputs:
        n (int): The number to be checked if it's prime or not.
        
    Outputs:
        bool: Returns True if the number is prime, otherwise returns False.
        
    Example:
        >>> is_prime(5)
        True
        >>> is_prime(4)
        False
        
    """
    
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True