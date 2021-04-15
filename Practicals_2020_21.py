import mysql.connector as m
import pandas as p
mysql1=m.connect(host='localhost', user='root', password='244Saket', database='Practicals_2020_21')
mysqlex=m.connect(host='localhost', user='root', password='244Saket', database='Practicals_2020_21')
cursor=mysql1.cursor()
cursorex=mysqlex.cursor()
p.set_option('display.max_columns', 30)

def start():
    choice=int(input('''

        >Menu<            

    1 | Login           
    2 | Register|SignUp 
    3 | Exit            

Make your choice:- '''))
    if choice==1:
        Login()
    elif choice==2:
        SignUp()
    elif choice==3:
        exit()
    else:
        print()
        print("Enter a Valid Choice")
        print()
        start()

def LoginDetails():
    LoginDetails.UserName=input('Enter Your UserName: ')
    LoginDetails.Password=input('Enter Your Password: ')

def Login():
    LoginDetails()
    cursor.execute("select * from Members where UserName='%s'"%LoginDetails.UserName)
    fetch=cursor.fetchone()
    
    tupex=(LoginDetails.UserName,LoginDetails.Password)
    commandex="select * from Members where UserName='%s' and Password='%s'"
    cursorex.execute(commandex % tupex)
    fetchex=cursorex.fetchone()

    if fetch==None:
        print('''No Record Found
              Please Register/Sign Up''')
        start()

    elif (fetch!=None) and (fetchex==None):
        print()
        print('''UserName or Password wrong. Please try again.''')
        print()
        Login()

    elif fetch!=None and fetchex!=None:
        print()
        print('''Login Successfull''')
        print()
        LoginMenu()

def RegNameCheck():
    RegName=input('Please Enter Your Full Name (Required): ')
    if len(RegName)==0:
        print()
        print('Name Is Required')
        print()
        RegNameCheck()
    elif RegName.isdigit()==True:
        print()
        print('Digits Not Allowed in Name')
        print()
        RegNameCheck()
    else:
         RegNameCheck.RegName=RegName  

def RegAddressCheck():
    RegAddress=input('Please Enter Your Address (Optional): ')
    RegAddressCheck.RegAddress=RegAddress

def RegNumberCheck():
    RegNumber=input('Please Enter Your Number (Required): (+91)')
    if RegNumber.isdigit()==True:
        if len(RegNumber)<10 or len(RegNumber)>12:
            print()
            print('Number Must be between 10 to 12 Digits')
            print()
            RegNumberCheck()
        else:
            RegNumberCheck.RegNumber=RegNumber
    else:
        print()
        print('Number Should be Digits')
        print()
        RegNumberCheck()

def RegSexCheck():
    Genders=['m','f','o']
    RegSex=input('Please Enter Your Gender (M/F/O) (Required): ')
    if len(RegSex)==1:
        if RegSex.lower() in Genders:
            RegSexCheck.RegSex=RegSex.upper()
        else:
            print()
            print('Please Input Only One of Given Letters ')
            print()
            RegSexCheck()
    else:
        print()
        print('Please Choose One of The Given Gender(s)!')
        print()
        RegSexCheck()

def RegEmailCheck():
    RegEmail=input('Please Enter Your Email (Required): ')
    if '.com' in RegEmail and '@' in RegEmail:
            if len(RegEmail)>10:
                RegEmailCheck.RegEmail=RegEmail
            else:
                print()
                print('Email too Short')
                print()
                RegEmailCheck()
    else:
        print()
        print('Enter a Proper Email')
        print()
        RegEmailCheck()


def RegAltNumberCheck():
    RegAltNumber=input('Please Enter Your AltNumber (Optional): (+91)')
    if len(RegAltNumber)==0:
        RegAltNumberCheck.RegAltNumber='None'
    else:
        if RegAltNumber.isdigit()==True:
            if len(RegAltNumber)<10 or len(RegAltNumber)>12:
                print()
                print('Number Must be between 10 to 12 Digits')
                print()
                RegAltNumberCheck()
            else:
                RegAltNumberCheck.RegAltNumber=RegAltNumber
        else:
            print()
            print('AltNumber Should be Digits')
            print()
            RegAltNumberCheck()
    
def RegUserNameCheck():
    RegUserName=input('Please Enter a UserName (Required): ')
    if len(RegUserName)<8 or len(RegUserName)>20:
        print()
        print('UserName Must be Between 8 to 20 Characters')
        print()
        RegUserNameCheck()
    elif len(RegUserName)==0:
        print()
        print('UserName Cannot be Empty')
        print()
        RegUserNameCheck()
    else:
        command="select * from members where UserName='%s'"
        tup=(RegUserName)
        cursor.execute(command % tup)
        fetch=cursor.fetchone()
        if fetch==None:
            RegUserNameCheck.RegUserName=RegUserName
        else:
            print()
            print('UserName Taken! Please Choose Another Username.')
            print()
            RegUserNameCheck()

def RegPasswordCheck():
    RegPassword=input('Please Enter a Password (Required): ')
    if len(RegPassword)<8:
        print()
        print('Password too Short')
        print()
        RegPasswordCheck()
    else:
        RegPasswordCheck.RegPassword=RegPassword
def SignUp():
    RegNameCheck()
    RegAddressCheck()
    RegNumberCheck()
    RegSexCheck()
    RegEmailCheck()
    RegAltNumberCheck()
    RegUserNameCheck()
    RegPasswordCheck()

    RegName=RegNameCheck.RegName
    RegAddress=RegAddressCheck.RegAddress
    RegNumber=RegNumberCheck.RegNumber
    RegSex=RegSexCheck.RegSex
    RegEmail=RegEmailCheck.RegEmail
    RegAltNumber=RegAltNumberCheck.RegAltNumber
    RegUserName=RegUserNameCheck.RegUserName
    RegPassword=RegPasswordCheck.RegPassword
    
    Input=(RegName,RegAddress,RegNumber,RegSex,RegEmail,RegAltNumber,RegUserName,RegPassword)
    command="insert into members values('%s','%s','%s','%s','%s','%s','%s','%s') "
    cursor.execute(command % Input)
    mysql1.commit()
    command="select * from Members where UserName='%s'"
    Input=(RegUserName)
    cursor.execute(command % Input)
    fetch=cursor.fetchone()
    if fetch!=None:
        print()
        print('Successfully Registered! Please Log In.')
        print()
        start()
    else:
        print()
        print('Error During Registration. Please Re-Register.')
        print()
        start()
        
def LoginMenu():
    LoginMenu=int(input('''

        >Login Menu<            

    1 | Change Personal Details           
    2 | View Phone Directory
    3 | Log Out
    4 | Delete Account

Make your choice:- '''))
    if LoginMenu==1:
        ChangePersonalDetails()
    if LoginMenu==2:
        ViewPhoneDirectory()
    if LoginMenu==3:
        start()
    if LoginMenu==4:
        DeleteAccount()

def ChangePersonalDetails():
    command="select * from members where username='%s'"
    tup=(LoginDetails.UserName)
    cursor.execute(command%tup)
    fetch=cursor.fetchone()
    Values=list(fetch)
    Values.__delitem__(-1)
    Keys=['Name','Address','Number','Sex','Email','AltNumber','UserName']
    ReviewDict={}
    for i in range(0,len(Keys)):
        ReviewDict[Keys[i]]=Values[i]
    ReviewDetails=p.DataFrame(ReviewDict,index=['I'])
    print('Please Review Your Details')
    print(ReviewDetails)
    print()
    Change=input('Choose Which Details You Want The Change: ')
    Choices=['Name','Address','Number','Sex','Email','AltNumber']
    if Change in Choices:
        ChangeInp=input("Input New %s: "%Change)
        tup=(Change,ChangeInp,LoginDetails.UserName)
        cursor.execute("update members set %s='%s' where UserName='%s'"%tup)
        mysql1.commit()
        print()
        print('Successful!')
        LoginMenu()
    elif Change=='UserName':
        NewUserName=RegUserNameCheck()
        tup=(NewUserName,LoginDetails.UserName)
        cursor.execute("update members set UserName='%s' where UserName='%s'"%tup)
        mysql1.commit()
        LoginDetails.UserName=NewUserName
        print()
        print('Successful!')
        LoginMenu()
    else:
        print('Please Choose a Correct Detail!')
        print()
        LoginMenu()
        
def Find():
    print('''
Rules For Using Find.
>Input the parameter you want to find and the value you want to find seperated by space for example:
Name amya (if I wish to search for someone with 'amya' in their Name)
>Parameters are Name, Address, Number, Sex, Email, AltNumber, UserName
>Any value to search can be incomplete or complete for result.
''')
    ToFind=input('Input Search Terms: ').split(' ')
    perc = "%"
    cursor.execute("select * from members where %s like '%s%s%s'"%(ToFind[0],perc,ToFind[1],perc))
    fetch=cursor.fetchall()
    print('Name|Address|Number|Sex|Email|AltNumber')
    for i in fetch:
        print(i)
    LoginMenu()
def ViewPhoneDirectory():
    cursor.execute("select Name,Address,Number,Sex,Email,AltNumber from members")
    fetch=cursor.fetchall()
    FetchList=list(fetch)
    ReviewDetails=p.DataFrame(FetchList,columns=['Name','Address','Number','Sex','Email','AltNumber'])
    p.options.display.width=0
    print(ReviewDetails)
    ViewPhoneChoice=int(input('''          

    1 | Go Back to Login Menu       
    2 | Find in Phone Directory

Make your choice:- '''))
    if ViewPhoneChoice==1:
        print()
        LoginMenu()
    elif ViewPhoneChoice==2:
        Find()
        
def DeleteAccount():
    print()
    Delete=input('Are You Sure? Y/N')
    if Delete.lower()=='y':
        cursor.execute("delete from members where username='%s'"%LoginDetails.UserName)
        print('Done!')
        mysql1.commit()
        start()
    elif Delete.lower()=='n':
        print()
        LoginMenu()
    else:
        print('Please give a proper input!')
        print()
        DeleteAccount()
start()
