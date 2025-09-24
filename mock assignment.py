num = int(input("Enter a number: "))      #asks user for number
def oddeven():  

    """odd or even"""

    if num%2 == 0:
        print("number you put is even")  #checks if odd or even by using mod
    else:
        print("the number you put is odd")

def positivenegative():

    """finds negative or positive"""

    if num<=0:                            #checks if number is less than 0
        print("number is negative")
    elif num>=0:                          #checks if number is greater than 0
        print("number is postive")

def squarecube():

    """squares and cubes the number"""

    square = num**2                      #squares the number
    cube = num**3                        #cubes the number
    print("the square of",num,"is", square)
    print("the cube of",num,"is", cube)

def main():                             #main function to combine everything
    oddeven()
    positivenegative()
    squarecube()
main()                                  #call main function
