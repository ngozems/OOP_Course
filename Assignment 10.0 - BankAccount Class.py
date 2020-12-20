class BankAccount:

    def readAccountDetails(self):
        self.__Acc_no = int(input("Enter account number: "))
        self.__HolderName = input("Enter name of account holder: ")
        self.__Type = input("Enter account type")
        self.__Balance = float(input("Enter balance"))

    def displayAccountDetails(self):
        print("Account number is: " + str(self.__Acc_no))
        print("Acount holder is: " + self.__HolderName)
        print("Bank account type is: " + self.__Type)
        print("Balance is: " + str(self.__Balance))

#         er is nu wat veranderd

