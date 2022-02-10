'''
    UserDefined Exception:
        User defined exceptions in python are created by programmers to enforce constraints on the
        values which the variables in the program can take.
        Python has many built in exceptions which are raised when there is some error in the program.
'''
class Error(Exception):
    pass
class TooSmallError(Error):
    pass
class TooLargeError(Error):
    pass
num=10
while True:
    try:
        choice=int(input("Enter a number:"))
        if choice < 10:
            raise TooSmallError
        elif choice > 10:
            raise TooLargeError
        break
    except TooSmallError:
        print("you entered too small number.please enter again")
    except TooLargeError:
        print("you entered too large number.please enter again")
print("you entered correct number")

# class Error(Exception):
#     pass
# class TooSmallError(Error):
#     pass
# class TooLargeError(Error):
#     pass
# num=10
# while True:
#     try:
#         choice=int(input("Enter a number:"))
#         if choice < 10:
#             raise TooSmallError
#         elif choice > 10:
#             raise TooLargeError
#
#
#
#     except TooSmallError:
#         print("you entered too small number.please enter again")
#     except TooLargeError:
#         print("you entered too large number.please enter again")
#     else:
#         print("you entered correct number ")
#
#     finally:
#         print("im finally block")




