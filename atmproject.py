import mysql.connector
from mysql.connector import Error

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abitha@12",
    database="atm3"
    
    
)

print("Welcome to xyz Bank ATM")
n=int(input("press 1 for login & 0 for register:"))
password=""
myname=""
depo=""
id=""

if n == 0:
    name = input("Enter name:")
    accn = int(input("Enter account no:"))
    t = int(input("Enter starting amount you want to deposit :"))
    pw = int(input("set your password:"))

    myname = name
    password = pw
    depo = t
    id = accn

    val = (myname, password, depo, id)

    sql = "INSERT INTO data (my_name, pass_word, de_po, i_d) VALUES (%s, %s, %s, %s)"

    mycursor=mydb.cursor()
    mycursor.execute(sql,val)
    mydb.commit()

if n == 1:
    info = int(input("Enter your id :"))
    passw = int(input("Enter your password :"))
    mycursor=mydb.cursor()
    mycursor.execute("""SELECT * FROM atm3.data where i_d='%s' """ % (info))
    row=mycursor.fetchone()

    if mycursor.rowcount == 1:
        mycursor.execute("""SELECT * FROM atm3.data where pass_word='%s' """ % (passw))
        row=mycursor.fetchone()

        if mycursor.rowcount == 1:
            print("login successful")
            print("please enter the number for 1 and 0 and 3, withdral and deposit and exist")
            d = int(input("Enter 1 for withdrawl and 0 for deposit and 3 for exist:"))
            if d == 1:
                a = int(input("how much you want to withdrawl:"))
                mycursor.execute("""SELECT de_po FROM atm3.data where pass_word='%s' """ % (passw))
                col=mycursor.fetchone()
                x=list(col)
                for i in x:
                    z = (int(i))
                    c = z - a
                mycursor.execute("UPDATE data SET de_po='%s' where pass_word='%s' " % (c,passw))
                mydb.commit()
            
            if d == 0:
                a = int(input("how much you want to deposit:"))
                mycursor.execute("""SELECT de_po FROM atm3.data where pass_word='%s' """ % (passw))
                col=mycursor.fetchone()
                x=list(col)
                for i in x:
                    z = (int(i))
                    c = z + a
                mycursor.execute("UPDATE data SET de_po='%s' where pass_word='%s' " % (c,passw))
                mydb.commit()

            if d == 3:
                exit(0)

        else:
            print("Invalid password")

    else:
        print("Account doesn't exist")

    mydb.commit()

        