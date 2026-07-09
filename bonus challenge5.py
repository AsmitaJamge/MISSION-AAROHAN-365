#smart  ATM PIN

correct_pin = 1234
attempt = 1
while attempt <=3:
    pin = int(input("enter ATM PIN : "))
    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("wrong PIN")
        attempt = attempt+1
if attempt>3:
    print("Account Locked")