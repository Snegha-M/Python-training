class InsufficientBalanceError(Exception):

 def __init__(self, bal, message="insufficient amount to withdraw"):
  self.bal = balance
  self.message = message
 def __str__(self):
  return  "only" + str (self.bal)+" => "+self.message;

balance = 10000
withDrawlAmount = int(input("Enter the amount to withdraw: "))
try:
  if withDrawlAmount > balance:
   raise InsufficientBalanceError(withDrawlAmount)
  else:
   print("Remaining balance is: ",balance - withDrawlAmount)
except InsufficientBalanceError as e:
 print(e)
else:
 print("Successfully withdrawn!")

