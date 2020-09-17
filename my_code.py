# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# I got help over zoom from Megan

def find_gcf(x,y):   # Do not change function name!
    # User code goes here

    for fac1 in range(x,0,-1):
        if x % fac1 == 0:
            if y % fac1 == 0:

                return fac1
            
if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))

    print(find_gcf(x,y))

    # After you are satisfied with your results, use input() to prompt the user for two values:
    #x = int(input("Enter a number: "))
    #y = int(input("Enter another number: "))

