print("\n************************")
print("Welcome to ATM machine")
print("************************")
class Atm(object):
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    def cashWithdrawl(self):
        amount=int(input("\nHow much amount you want to withdraw:"))
        print("\n******************************")
        print("Rupees",amount,"is withdrawn")
        balance=10000-amount
        print("Current Balance=",balance)
        print("******************************")
    def balanceEnquiry(self):
        print("\nYour balance is 10000")
def main():
    card_number=input("\nEnter your card number:")
    _pin=input("\nEnter your pin number:")
    user1=Atm(card_number,_pin)
    print("\nPress (1) for Cash Withdrawl and (2) for Balance Enquiry")
    activity=int(input("Select the transaction type:"))
    if(activity==1):
        user1.cashWithdrawl()
    elif(activity==2):
        user1.balanceEnquiry()
if __name__ == "__main__":
    main()