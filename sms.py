import pymysql

def dashboard():
    con = pymysql.connect(host="localhost", user="root", password="", database="student")
    print("Welcome Arpit,")
    print("1. Add Student")
    print("2. Read Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = int(input("Enter Your Choice :- "))
    if choice == 1:
        cur1 = con.cursor()
        print("------Add Student------")
        roll = input("Enter Roll.No :- ")
        name = input("Enter Name :- ")
        class_inp = input("Enter Class :- ")
        gender = input("Enter Gender :- ")
        email = input("Enter Email :- ")
        phone_number = input("Enter Phone Number :- ")
        address = input("Enter Address :- ")

        cur1.execute("INSERT INTO `student` (`roll`, `name`, `class`, `gender`, `email`, `phone_number`, `address`) VALUES (%s, %s, %s, %s, %s, %s, %s)", (roll, name, class_inp, gender, email, phone_number, address))
        con.commit()
        print("Student Added!!!")
        
        cur1.close()

    elif choice == 2:
        cur2 = con.cursor()

        print("------Read Student------")


        query = "SELECT * FROM STUDENT"
        cur2.execute(query)

        # read student
        results = cur2.fetchall()
        for result in results:
            print(result)
        
        con.commit()
        cur2.close()

    elif choice == 3:
        cur3 = con.cursor()
        print("------Update Student------")
        roll = input("Enter Search By Roll.No :- ")
        name = input("Enter Name :- ")
        class_inp = input("Enter Class :- ")
        gender = input("Enter Gender :- ")
        email = input("Enter Email :- ")
        phone_number = input("Enter Phone Number :- ")
        address = input("Enter Address :- ")

        cur3.execute("UPDATE STUDENT SET name=%s, class=%s, gender=%s, email=%s, phone_number=%s, address=%s WHERE roll =%s", (
            name, class_inp, gender, email, phone_number, address, roll
        ))
        con.commit()
        print("Student Updated!!!")
        
        cur3.close()

    elif choice == 4:
        cur4 = con.cursor()
        print("------Delete Student------")
        roll = input("Enter Search By Roll.No :- ")

        cur4.execute("DELETE FROM student WHERE roll = %s", (
            roll
        ))
        con.commit()
        print("Student Deleted!!!")
        
        cur4.close()

    elif choice == 5:
        quit()

    else:
        print("Invalid Choice")

    con.close()


def main():
    print("Login")
    log_inp = input("Enter Your Password :- ")
    if log_inp == "password":
        while True:
            dashboard()

if __name__ == '__main__':
    main()
