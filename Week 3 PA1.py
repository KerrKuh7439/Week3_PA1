print("KerKuh7439")

def functionOne():
    print("My Student ID is KerKuh7439")


def functionTwo():
    numberOne = int(input("Please enter a number: "))
    numberTwo = int(input("Please enter a number: "))
    sumOfNumbers = numberOne + numberTwo
    print(f"The sum of {numberOne} and {numberTwo} is {sumOfNumbers}.")
    return sumOfNumbers


def functionThree(sumOfNumbers):
    if sumOfNumbers > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")
    return 7439


def main():
    functionOne()  # Calls functionOne to display my Student ID.
    sumOfNumbers = functionTwo()  # Calls functionTwo and stores the returned sum.
    studentIdNumber = functionThree(sumOfNumbers)  # Passes the sum to functionThree and stores its returned value.
    print(f"functionThree returned the value of {studentIdNumber}.")  # Displays the value returned by functionThree.


main()
