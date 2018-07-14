from getpass import getpass
import time
bank = {
    'user' : ['python','java','c','c+'],
    'acc' : [1001,1002,1003,1004],
    'password' : ['redhat','hi','bye','hello'],
    'bal' : [50000,30000,10000,0]
}
admin = 'root'
admin_password = 'red'

while True:
    print('*'*50)
    print('\t\t',time.ctime())
    print("\t\tWelcome...")
    print('*'*50)
    print('\nSelect one option :\n1.Log in\n2.Sign in\n3.Admin\n4.Exit')
    res = int(input().strip())
    if res == 1 :
        acc_no = int(input("Enter your valid account number :").strip())
        if acc_no in bank['acc'] :
            indx = bank['acc'].index(acc_no)
            print("\n\tWelcome {} ".format(bank['user'][indx]))
            pas = getpass("Enter your valid password :").lower()
            
          
            while True:
                if pas == bank['password'][indx]:
                    print('\nSelect one option :\n1.Credit\n2.Debit\n3.Balance Enquiry\n4.Change password\n5.Log out')
                    res1 = int(input().strip())
                
                    if res1 == 1 :
                            crdt_amt = int(input("How much you have to credit :").strip())
                            bank['bal'][indx] = bank['bal'][indx] + crdt_amt
                            print('\nNew balance : ',bank['bal'][indx])
                        
                    elif res1 == 2 :
                        dbt_amt = int(input("How much you want to withdraw :").strip())
                        if dbt_amt > bank['bal'][indx] :
                            print("\nYou don't have sufficient balance..")
                        else :
                            bank['bal'][indx] = bank['bal'][indx] - dbt_amt
                            print('\nNew balance : ',bank['bal'][indx])
                    
                    elif res1 == 3 :
                        print('\nYour balance : ',bank['bal'][indx])
                        
                    elif res1 == 4 :
                        old_paswrd = getpass('\nEnter your old password : ').strip()
                        pas_index = bank['password'].index(old_paswrd)
                        print(pas_index)
                        if old_paswrd == pas :
                            new_paswrd = getpass('\nEnter your new password : ').strip()
                            verify_paswrd = getpass('\nEnter your new password : ').strip()
                            if new_paswrd == verify_paswrd:
                                bank['password'][pas_index] = new_paswrd
                                print('\nPassword successfully changed..')
                                print(bank)
                                break
                            else :
                                print("Password doesn't match..")
                        else :
                            print('You have entered wrong password..')
                    
                    elif res1 == 5 :
                        break
                    
                    else:
                        print('\nInvalid choice..')
                
                else:
                    print("\nYou have entered a invalid password...")
                    break
            
        else:
            print("\nYou have entered invalid account number..")
        
    elif res == 2 :
        leng = len(bank['acc'])
        hldr_name = input("Enter your name : ").strip().lower()
        hldr_passwrd = getpass("Enter your password : ").strip().lower()
        bank['user'].append(hldr_name)
        bank['password'].append(hldr_passwrd)
        bank['bal'].append(0)
        bank['acc'].append(bank['acc'][leng-1] + 1)
        print("\n\tYour details :\nYour name : {}\nYour password : {}\nYour account number :  {}\nYour balance : {}".format(hldr_name,hldr_passwrd,bank['acc'][leng],bank['bal'][leng]))
        while True:
                    print('\nSelect one option :\n1.Credit\n2.Debit\n3.Balance Enquiry\n4.Change password\n5.Log out')
                    res1 = int(input().strip())
                
                    if res1 == 1 :
                            crdt_amt = int(input("How much you have to credit :").strip())
                            bank['bal'][leng] = bank['bal'][leng] + crdt_amt
                            print('\nNew balance : ',bank['bal'][leng])
                        
                    elif res1 == 2 :
                        dbt_amt = int(input("How much you want to withdraw :").strip())
                        if dbt_amt > bank['bal'][leng] :
                            print("\nYou don't have sufficient balance..")
                        else :
                            bank['bal'][leng] = bank['bal'][leng] - dbt_amt
                            print('\nNew balance : ',bank['bal'][leng])
                    
                    elif res1 == 3 :
                        print('\nYour balance : ',bank['bal'][leng])
                    
                    elif res1 == 4 :
                        old_paswrd = getpass('\nEnter your old password : ').strip()
                        if old_paswrd == hldr_passwrd :
                            new_paswrd = getpass('\nEnter your new password : ').strip()
                            verify_paswrd = getpass('\nEnter your new password : ').strip()
                            if new_paswrd == verify_paswrd :
                                index = bank['user'].index(hldr_name)
                                bank['password'][index] = new_paswrd
                                print('\nPassword successfully changed..')
                                break
                            else :
                                print("password doesn't match..")
                        else :
                            print('You have entered wrong password..')
                            
                    elif res1 == 5:
                        break
                    else:
                        print('\nInvalid choice..')
                
    elif res == 3 :
        admin_name = input("Enter admin name : ").strip().lower()
        if admin_name == admin :
            print("Hello {}...".format(admin))
            admin_paswrd = getpass("Enter admin password : ").strip()
            if admin_paswrd == admin_password :
                for key in bank :
                    print("{} = {}".format(key,bank[key]))
                   # print(*bank.items())
            else :
                print('You have entered invalid password')
                        
        else :
             print("You have entered invalid admin name")
                          
    elif res == 4 :
        #exit(0)  it's  will not work in jupyter
        break
                          
    else :
        print("\nInvalid choice..")
