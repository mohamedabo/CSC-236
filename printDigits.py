# Abdirahman Mohamed CSC236 A12
def printDigits (num,base):
   """Recursive function:
    precondition: num and base are both greater than 0.
            Function will check for base > 1.
    postcondition: the digits of num will be output to
            the screen, stopping when most significant
            digit is output."""
   assert (base>1) # if base equals zero or one, a seg-fault or FPE will occur.
   if num<base:
    print(num)
   else:
    printDigits(num//base,base) # The recursion does an integer division
    print(num%base) # prints num modulo base
def main():
    """Takes num and base to do the mathematical operation at the recrusive function"""
    print("What is the number to convert?")
    num = int(input("Enter num:"))
    print("What is the new number base for that number?")
    base = int(input("Enter base:"))
    printDigits(num,base)
main()
