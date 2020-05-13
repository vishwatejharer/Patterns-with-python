#This program prints stars in X shape. 

def x_pattern(n):		#name of the function and parameter n
    for i in range(n):
        for j in range(n):
            if (j == i) or (j == n-1-i):
                print('*', end='')
            else:
                print(' ', end='')
        print()


#Example 
'''
input: x_pattern(5)

Output:
*   *
 * * 
  *  
 * * 
*   *

'''
