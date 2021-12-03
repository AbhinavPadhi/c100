class Atm():
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def cashWithdrawl(self):
        print("money has been withdrawn")
    def balanceEnqiry(self):
        print("your account has ₹100,000")
    def enterPin(self):
        print("pin has been entered")

a = Atm(1234567890, 1234)
print(a.cashWithdrawl() , "from" , a.cardNumber)
print(a.enterPin(), a.pin)
print(a.balanceEnqiry())