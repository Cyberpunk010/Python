#Recursion

def recursive_function(n):
    '''Recursive function'''             #doc strings
    if(n==0 or n==1):
        return n
    else:
        return(n*recursive_function(n-1))
    
print(recursive_function(5))
print(recursive_function.__doc__)