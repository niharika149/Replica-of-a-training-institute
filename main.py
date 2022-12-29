import re

if __name__=='__main__':
    while True:
        try:
            choice=int(input("Enter \n1.Register \n2.login \n3.Exit\n"))
        except ValueError:
            print("Please enter valid choice(Between 1-3)")
            continue

        if choice==1:
            try:
                register_choice=int(input("Enter \n1.Regester as Admin \n2.Register as student\n"))
            except ValueError:
                print("Please enter a valid choice")
            if register_choice==1:
                name=input("Enter your name ")
                phone=input("Enter your phone number")
                mail_id=input("Enter your mail ID")
                #password=input("Enter your password")

                name_re=re.findall(r"^[A-Za-z]+$",name)
                phone_re=re.findall(r"^[1-9]{1}+[1-9]{9}$",phone)
                mail_id_re=re.findall(r"^\w+[@][a-z]+[.]com$",mail_id)
                #password_re=re.findall(r"^")

            if name_re and phone_re and mail_id_re and password_re:
                print("All looks good!")
            else:
                if not name_re:
                    print("Entered name format is incorrect")
                if not phone_re:
                    print("Entered phone number format is incorrect")
                if not mail_id_re:
                    print("Entered mail ID format is incorrect")
                #if not password_re:
                    #print("Entered password format is incorrect")