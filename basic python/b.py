from getpass import getpass
bank = {
    'user' : ['python','java','c','c+'],
    'acc' : [1001,1002,1003,1004],
    'password' : ['redhat','hi','bye','hello'],
    'bal' : [50000,30000,10000,0]
}
while True:
    print("\n\tWelcome...")
    print('\nSelect one option :\n1.Log in\n2.Sign in\n3.Exit')
    res = int(input().strip())
    if res == 1 :
        acc_no = int(input("Enter your valid account number :").strip())
        if acc_no in bank['acc'] :
            indx = bank['acc'].index(acc_no)
            print("\n\tWelcome {} ".format(bank['user'][indx]))
            pas = getpass("Enter your valid password :").lower()
            
          
            while True:
                if pas == bank['password'][indx]:
                    print('\nSelect one option :\n1.Credit\n2.Debit\n3.Balance Enquiry\n4.Log out')
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
                        break
                    
                    else:
                        print('\nInvalid choice..')
                
                else:
                    print("\nYou have entered a invalid password...")
                    break
            
        else:
            print("\nYou have entered invalid name..")
        
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
             #   for pas in bank['password']:
                    print('\nSelect one option :\n1.Credit\n2.Debit\n3.Balance Enquiry\n4.Log out')
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
                        break 
                    
                    else:
                        print('\nInvalid choice..')
                
    elif res == 3 :
        exit(0)  
       # break
        
    else :
        print("\nInvalid choice..")
    
