"""
Name:
UCINetID:
"""

class IntegerOutOfRangeException(Exception):
    pass
class NoStaircaseSizeException(Exception):
    pass
''' This functions asks the user for the number of steps
they want to climb, gets the value provided by the user
and returns it to the calling function. This function will
raise any exceptions related to none integer user inputs.'''
def getUserInput():
    #your code belongs here
    num = input("Please input your staircase size: ")
    if num == 'DONE':
        return 'z'
    else:
        num = int(num)

        return num

''' This function takes the number of steps as an input parameter,
creates a string that contains the entire steps based on the user input
and returns the steps string to the calling function. This function will raise
any exceptions resulting from invalid integer values.
'''

def printSteps(stepCount):
    if stepCount == 0:
        raise NoStaircaseSizeException()

    #your code belongs here

        
    if 1 <= stepCount < 1000:
        n = stepCount
    else:
        raise IntegerOutOfRangeException()
    num = n

    while num > 0:
        if (num == n):
            w = (2 * (num - 1 )) * ' '
            s = (w + '+-+\n')
            s += (w + '| |\n')
            num -= 1
            continue
        w = (2 * (num - 1)) * ' '
        s += (w + "+-+-+\n")
        s += (w + "| |\n")
        num -= 1
       
    s += ('+-+')
    return s

'''This function kicks off the running of your program. Once it starts
it will continuously run your program until the user explicitly chooses to
end the running of the program based on the requirements. This function returns
the string "Done Executing" when it ends. Additionally, all exceptions will be
handled (caught) within this function.'''
def runProgram():
    prin = True
    while prin:
        try:
            a = getUserInput()
            if a == 'z' :#it was DONE
                prin = False
            else:#if not DONE and valid
                print(printSteps(a))
        except ValueError:
            print("Invalid staircase value entered.")
        except IntegerOutOfRangeException:
            print("That staircase size is out of range.")
        except NoStaircaseSizeException:
            print("I cannot draw a staircase with no steps.")
    #your code belongs here
    return "Done Executing"
    
    
'''Within this condition statement you are to write the code that kicks off
your program. When testing your code the code below this
should be the only code not in a function and must be within the if
statement. I will explain this if statement later in the course.'''
if __name__ == "__main__":
    runProgram()
