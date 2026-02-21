import csv
budgetentry=False
monthlybudget=0

#------------------------function 1 : creating a file ------------------------

def create():
    global budgetentry
    if budgetentry==False:
        yn=input("do you wish to enter your data into an existing file? (y/n)")
        if yn=="n":
            file1=input("enter the file name, kindly use the format [name.csv]")
            F=open(file1,"a")
            wobj = csv.writer(F)
            wobj.writerow(['Date','Month', 'Description', 'Amount', 'Type'])
        else:
            file1=input("enter the file name, kindly use the format [name.csv]")
            F=open(file1,"a")
            wobj = csv.writer(F)
        while True:
            date = input("Enter date (YY-DD): ")
            month = input("Enter month [ JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC| ]: ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            transaction_type = input("Enter type (Income/Expense): ")
            rec=[date,month,description, amount, transaction_type]
            wobj.writerow(rec)
            print("date entered succesfully !")
            cont = input("Do you want to add another record? (y/n): ")
            if cont.lower() == 'n':
                break
        print()
    #-----budgeting initiated--------
    else:
        monthlybudget=int(input("kindly enter the monthly budget for your expenditure"))
        print("enter your data only into an existing file")
        file1=input("enter the file name, kindly use the format [name.csv]")
        F=open(file1,"a")
        wobj = csv.writer(F)
        wobj.writerow(['Date','Month', 'Description', 'Amount', 'Type'])
        while True:
            date = input("Enter date (YY-DD): ")
            month = input("Enter month [ JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC| ]: ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            transaction_type = input("Enter type (Income/Expense): ")
            rec=[date,month,description, amount, transaction_type]
            wobj.writerow(rec)
            print("date entered succesfully !")
            budgetchecker(file1,monthlybudget,month,amount)    
            cont = input("Do you want to add another record? (y/n): ")
            if cont.lower() == 'n':
                break
        print()
#------------------------function 2 : display total expense ------------------------



def viewexp():
    file2 = input("Enter the file name, kindly use the format [name.csv]: ")
    F=open(file2, "r")  
    robj = csv.reader(F)
    data = list(robj)
    texp = 0
    C=input("would you like to view total expense of all months (y)? if you do not wish to, please enter n.").lower()
    if C=="y":
        header=False
        for i in data:
            if header==False:
                header=True
            else:
                if i[4].lower()=="expense":
                    texp+=int(i[3])
        if texp>0:
            print("the total expenditure is for is =", texp)
            print()
        else:
            print("no enpenditure this month !")
        
    else:
        m=input("For which month would you like to find the total income ?[JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|]")
        header=False
        for i in data:
            if header==False:
                header=True
            else:
                if i[1]==m and i[4].lower()=="expense":
                    texp+=int(i[3])
            print(texp)
#------------------------function 3 : display total income----------------------

def viewinc():
    file2 = input("Enter the file name, kindly use the format [name.csv]: ")
    F=open(file2, "r")  
    robj = csv.reader(F)
    data = list(robj)
    texp = 0
    C=input("would you like to view total income of all months (y)? if you do not wish to, please enter n.").lower()
    if C=="y":
        header=False
        for i in data:
            if header==False:
                header=True
            else:
                if i[4].lower()=="income":
                    texp+=int(i[3])
        if texp>0:
            print("the total income is for is =", texp)
            print()
        else:
            print("no income this month !")
        
    else:
        m=input("For which month would you like to find the total income ?[JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|]")
        header=False
        for i in data:
            if header==False:
                header=True
            else:
                if i[1]==m and i[4].lower()=="expense":
                    texp+=int(i[3])
                    
        if texp>0:
            print("the total expenditure is for",m,"is =", texp)
            print()
        else:
            print("no enpenditure this month !")
            print()


        
#------------------------function 4 : data analysis----------------------

def analysis():
    file3=input("enter your budget file's name. kindly follow the format [name.csv]")
    F=open(file3,"r")
    robj=csv.reader(F)
    data=list(robj)
    m=input("enter the earliest month [JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|]")
    m2=input("enter the recent month [JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|]")
    m3=input("enter the most recent month [JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEPT|OCT|NOV|DEC|]")
    mexp=mexp2=mexp3=sumexp=0
    L=[]
    header=False
    for i in data:

        if header==False:
            header=True

        else: #-----1st task in fn-------
            
            if i[1]==m and i[4].lower()=="expense":
                mexp+=int(i[3])
              
            elif i[1]==m2 and i[4].lower()=="expense":
                mexp2+=int(i[3])

            elif i[1]==m3 and i[4].lower()=="expense":
                mexp3+=int(i[3])
            

            #-----2nd task in fn-------
                
            if i[1] not in L:
                L.append(i[1])
                
            if i[4].lower()=="expense":
                sumexp+=int(i[3])

    print()        
    print("SELECT OPTION FOR TREND ANALYSIS")
    print("1---between",m,"&",m2)
    print("2---between",m2,"&",m3)
    print()
    TA=input(" 1/2 ?")
    
    if TA=="1":
        CIR=(mexp2-mexp)/mexp
    else:
        CIR=(mexp3-mexp2)/mexp

    avgexp=sumexp/len(L)
    MAC=(mexp+mexp2+mexp3)//3


    #-----DISPLAY-------
    
    print()
    print("----------------------------------------")
    print()
    
    print("TREND ANALYSIS")
    if CIR<0:
        if TA=="y":
            print("there was a decline, decline rate of expenditure:",abs(CIR),"for the months",m2,"and",m)
        else:
            print("there was a decline, decline rate of expenditure:",abs(CIR),"for the months",m3,"and",m2)
            
    else:
        if TA=="y":
            print("there was an increase, increase rate of expenditure:",CIR,"for the months",m2,"and",m)
        else:
            print("there was an increase, increase rate of expenditure:",CIR,"for the months",m3,"and",m2)

    print()
    print("----------------------------------------")
    print()

    print("AVERAGE EXPENDITURE")
    print("The average expenditure for",len(L),"months in given file is",avgexp)

    print()
    print("----------------------------------------")
    print()

    print("MOVING AVERAGE CALCULATION")
    print("The moving average expenditure for 3 months is",MAC)
    print("this shows that your total expenditure for the following months will most likely be of an amount similiar to the this value")
    print()

    
#------------------------function 5 : budgetting----------------------
def budgetting():
    global budgetentry
    budgetentry=True
    print("budget is intiated, kindly type 1 and enter data now")
  #----------------------- **function to check budget** ------------------------
def budgetchecker(file1,monthlybudget,month,amount):
    F=open(file1, "r")  
    robj = csv.reader(F)
    data = list(robj)
    sumexp = 0
    header=False
    for i in data:
        if header==False:
            header=True
        else:
            if i[1]==month and i[4]=="expense":
                sumexp+=int(i[3])
        if sumexp>monthlybudget:
            print()
            print("But expense exceeded budget, this months expenditure exceeds your budget by", sumexp-monthlybudget,"!!!")
            print()
            break

#------------------------function 6 : view data----------------------
def viewdata():
    file6 = input("Enter the file name, kindly use the format [name.csv]: ")
    F=open(file6, "r")  
    robj = csv.reader(F)
    data = list(robj)
    for i in data:
        print(i)
        print()
#---------------------main program ----------------------
print()
print("Welcome to your PyBudget Tracker. Track Smart, Save Big today ! ")
while True:
    print()
    print("----------Tr@ck----$@ve----------Tr@ck----$@ve----------Tr@ck----$@ve----------")
    print()
    print("What would you like to do today ?")
    print()
    print("---1--- to enter expenses/income")
    print("---2--- to view expense details")
    print("---3--- to view income details")
    print("---4--- to retrieve predictive analysis")      
    print("---5--- to enable Budgeting")
    print("---6--- to view data, before chosing to budget")
    print()
    ch=int(input("kindly enter the number of your choice"))
    print()
    if ch==1:
        print()
        create()
    elif ch==2:
        print()
        viewexp()
    elif ch==3:
        print()
        viewinc()
    elif ch==4:
        analysis()
    elif ch==5:
        budgetting()
    elif ch==6:
        viewdata()
        
