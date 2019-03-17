#HAJDAROVIC
import mysql.connector
import datetime
db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root"
)

dbcursor = db.cursor()

try:
    dbcursor.execute("CREATE DATABASE library")
except:
    dbcursor.execute("drop database library")
    dbcursor.execute("CREATE DATABASE library")

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root",
  database="library"
)

dbcursor = db.cursor()

dbcursor.execute("CREATE TABLE lib_user (user_ID int(10), first_name varchar(20), last_name varchar(20), street varchar(20), street_num varchar(20), zip_code int(10), city varchar(20), state varchar(20), date_of_birth  varchar(20),library_ID int(20),primary key (user_ID))")

#adding user information into database
add_user = ("INSERT INTO lib_user (user_ID, first_name, last_name, street, street_num, zip_code, city, state, date_of_birth,library_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

user_data1 = (1001, 'Emelia', 'Hajdarovic', 'Esplanade Ave.', 2321, 10469, 'Bronx','NY', '2-16-1999',1234)
user_data2 = (1002, 'Ariana', 'Hajdarovic', 'Esplanade Ave.', 2321, 10469, 'Bronx','NY', '5-5-1994',1234)
user_data3 = (1003, 'Ariella', 'Hajdarovic', '55th St.', 43,10021, 'Manhattan','NY', '10-3-1997',1444)
user_data4 = (1004, 'Albion', 'Velic', 'Ace Ave.', 2738,10469, 'Bronx','NY', '11-21-1998',1122)
user_data5 = ( 1005, 'Rachal', 'Asante', 'Burke Ave,.', 9938,10464, 'City Island','NY', '5-9-1990',1268)
user_data6 = (1010, 'Mike', 'Ike', 'Church St.', 7463,10464, 'City Island','NY', '5-9-1974',1144)
user_data7 = (1006, 'Chris', 'Smith', '242nd St.', 2343,10471, 'Riverdale','NY', '5-9-1990',1121)
user_data8 = ( 1007, 'Emily', 'Pallinger', 'Linda Ave..', 1837,10471, 'Riverdale','NY', '5-9-1985',1233)
user_data9 = (1008, 'Joe', 'Jonas', 'Blaire St.', 2974,10501, 'Westchester','NY', '5-9-1990',1244)
user_data10 = (1009, 'Jessica', 'Jones', 'North Ave.',1293,10502, 'Westchester','NY', '5-9-1990',1222)
user_data11 = (1099, 'Claire', 'Boucher', 'Loor Ave.',3343,10503, 'Westchester','NY', '5-9-1990',1233)

dbcursor.execute(add_user,user_data1)
dbcursor.execute(add_user,user_data2)
dbcursor.execute(add_user,user_data3)
dbcursor.execute(add_user,user_data4)
dbcursor.execute(add_user,user_data5)
dbcursor.execute(add_user,user_data6)
dbcursor.execute(add_user,user_data7)
dbcursor.execute(add_user,user_data8)
dbcursor.execute(add_user,user_data9)
dbcursor.execute(add_user,user_data10)
dbcursor.execute(add_user, user_data11)


dbcursor.execute("CREATE TABLE user_phone_number (user_ID  int(10), phone_number numeric(50), primary key (user_ID,phone_number), foreign key (user_ID) references lib_user(user_ID)on delete cascade)")

#adding user phone numbers into database
add_phone = ("INSERT INTO user_phone_number (user_ID, phone_number) VALUES (%s,%s)")

phone_data1 = (1001, 9175473484)
phone_data2 = (1001, 9175473423)
phone_data3 = (1002, 7187982472)
phone_data4 = (1002, 917237334)
phone_data5 = (1002, 9175473484)
phone_data6 = (1003, 9174759384)
phone_data7 = (1003, 6465347489)
phone_data8 = (1004, 6465348384)
phone_data9 = (1004, 6463782938)
phone_data10 = (1005, 9173938490)
phone_data11 = (1006, 9172039489)
phone_data12 = (1007, 9173984893)
phone_data13 = (1008, 9143849300)
phone_data14 = (1010, 9148984930)
phone_data15 = (1099, 9145473849)
phone_data16 = (1099, 9143743849)


dbcursor.execute(add_phone,phone_data1)
dbcursor.execute(add_phone,phone_data2)
dbcursor.execute(add_phone,phone_data3)
dbcursor.execute(add_phone,phone_data4)
dbcursor.execute(add_phone,phone_data5)
dbcursor.execute(add_phone,phone_data6)
dbcursor.execute(add_phone,phone_data7)
dbcursor.execute(add_phone,phone_data8)
dbcursor.execute(add_phone,phone_data9)
dbcursor.execute(add_phone,phone_data10)
dbcursor.execute(add_phone,phone_data11)
dbcursor.execute(add_phone,phone_data12)
dbcursor.execute(add_phone,phone_data13)
dbcursor.execute(add_phone,phone_data14)
dbcursor.execute(add_phone,phone_data15)
dbcursor.execute(add_phone,phone_data16)


dbcursor.execute("CREATE TABLE message (message_id int(10), user_ID  int(10), content varchar(100), date_sent varchar(20), primary key (message_id), foreign key (user_ID) references lib_user(user_ID)on delete cascade)")
#adding user messages into database
add_message = ("INSERT INTO message (message_id, user_ID, content, date_sent) VALUES (%s,%s,%s,%s)")

message_data1 = (662,1001,'Please return your book', '2018-11-06')
message_data2 = (223, 1002,'Thank you for returning your book!', '2018-09-16')
message_data3 = (983,1003,'Please return your book', '2018-10-03')
message_data4 = (393,1004,'Please return your book', '2018-09-16')
message_data5 = (834,1005,'Thank you for returning your book!', '2018-04-04')
message_data6 = (694,1006,'Please return your book', '2018-02-14')
message_data7 = (539, 1007,'Please return your book', '2018-05-07')
message_data8 = (434,1007,'Thank you for returning your book!', '2018-06-03')
message_data9 = (178, 1007,'Please return your book', '2018-11-23')
message_data10 = ( 112,1008,'Please return your book', '2018-08-30')

dbcursor.execute(add_message,message_data1)
dbcursor.execute(add_message,message_data2)
dbcursor.execute(add_message,message_data3)
dbcursor.execute(add_message,message_data4)
dbcursor.execute(add_message,message_data5)
dbcursor.execute(add_message,message_data6)
dbcursor.execute(add_message,message_data7)
dbcursor.execute(add_message,message_data8)
dbcursor.execute(add_message,message_data9)
dbcursor.execute(add_message,message_data10)

dbcursor.execute("CREATE TABLE library (library_ID int(10), library_name varchar(20), street varchar(20),  street_num int(10), zip_code int(10), city varchar(20), state varchar(20), primary key(library_ID))")
#adding library information into database
add_lib = ("INSERT INTO library (library_ID, library_name, street, street_num, zip_code, city, state) VALUES (%s,%s,%s,%s,%s,%s,%s)")

lib_data1 = (1234,'Morris Park Library', 'Morris Park Ave.', 2343,10469,'Bronx','NY')
lib_data2 = (1122, 'Pelham Library', 'Pelham Parkway', 8767, 10469, 'Bronx', 'NY')
lib_data3 = (1233, 'NewRo Library', 'North Ave.', 8374, 10501, 'Westchester', 'NY')
lib_data4 = (1444, 'East Side Library', '54th St.', 2343, 10021, 'Manhattan', 'NY')
lib_data5 = ( 1268, 'Lincoln Library', 'Douglas Ave.', 2834, 10464, 'City Island', 'NY')
lib_data6 = (1144, 'City Island Library', 'Burke Ave.', 984, 10464, 'City Island', 'NY')
lib_data7 = (1112, 'Riverdale Library', '243rd St.', 2983, 10471, 'Riverdale', 'NY')
lib_data8 = ( 1223, 'Heart Library', '238th St.', 328, 10471, 'Riverdale', 'NY')
lib_data9 = (1244, 'Westchester Library', 'Angela Ave.', 2838, 10501, 'Westchester', 'NY')
lib_data10 = (1222, 'Jefferson Library', 'Lumen Ave.', 384, 10503, 'Westchester', 'NY')


dbcursor.execute(add_lib,lib_data1)
dbcursor.execute(add_lib,lib_data2)
dbcursor.execute(add_lib,lib_data3)
dbcursor.execute(add_lib,lib_data4)
dbcursor.execute(add_lib,lib_data5)
dbcursor.execute(add_lib,lib_data6)
dbcursor.execute(add_lib,lib_data7)
dbcursor.execute(add_lib,lib_data8)
dbcursor.execute(add_lib,lib_data9)
dbcursor.execute(add_lib,lib_data10)



dbcursor.execute("CREATE TABLE book (book_id int(20), title varchar(100), author varchar(100), genre varchar(20),primary key (book_id))")
#adding book information into database
add_book = ("INSERT INTO book (book_id, title,author,genre) VALUES (%s,%s,%s,%s)")

book_data1 = (9876,'Bad Blood: Secrets and Lies in a Silicon Valley Startup', 'John Carreyrou', 'Nonfiction')
book_data2 = (8445,'Army of None: Autonomous Weapons and the Future of War', 'Paul Scharre', 'Nonfiction')
book_data3 = (8335,'21 Lessons for the 21st Century', 'Yuval Noah Harari', 'Nonfiction')
book_data4 = (8225,'The Corrections', 'Jonathan Franzen', 'Fiction')
book_data5 = ( 8995,'Outlander', 'Diana Gabaldon', 'Romance')
book_data6 = (8122,'Hunger Games', 'Suzanne Collins', 'Fiction')
book_data7 = (8398,'Harry Potter and the Chamber of Secrets', 'J. K. Rowling', 'Fiction')
book_data8 = ( 7733,'The Girl with the Dragon Tattoo', 'Stieg Larsson', 'Thriller')
book_data9 = (8844,'The Girl on the Train', 'Paula Hawkins', 'Thriller')
book_data10 = (9483,'The Brothers Karamazov', 'Fyodor Dostoevsky', 'Fiction')
book_data11 = (9999,'Alice Wonderland', 'Charles Dodgson', 'Kids')


dbcursor.execute(add_book,book_data1)
dbcursor.execute(add_book,book_data2)
dbcursor.execute(add_book,book_data3)
dbcursor.execute(add_book,book_data4)
dbcursor.execute(add_book,book_data5)
dbcursor.execute(add_book,book_data6)
dbcursor.execute(add_book,book_data7)
dbcursor.execute(add_book,book_data8)
dbcursor.execute(add_book,book_data9)
dbcursor.execute(add_book,book_data10)
dbcursor.execute(add_book,book_data11)




dbcursor.execute("CREATE TABLE lib_issue (issue_id int(10), user_ID int(10), book_id int(20),date_issued varchar(20), primary key (issue_id), foreign key (user_ID) references lib_user(user_ID) on delete cascade, foreign key (book_id) references book(book_id)on delete cascade)")
#adding issue information into database
add_issue = ("INSERT INTO  lib_issue (issue_id,user_ID,book_id,date_issued) VALUES (%s,%s,%s,%s)")

issue_data1 = (374,1001, 9876, '2018-08-04')
issue_data2 = (375,1002, 8445, '2018-09-06')
issue_data3 = (376,1003, 8335, '2018-02-08')
issue_data4 = (377,1004, 8225, '2018-8-24')
issue_data5 = ( 378,1005, 8995, '2018-10-04')
issue_data6 = (379,1006, 8122, '2018-11-20')
issue_data7 = (380,1007, 8398, '2018-10-19')
issue_data8 = ( 381,1008, 7733, '2018-11-17')
issue_data9 = (382,1009, 8844, '2018-11-16')
issue_data10 = (383,1099, 9999, '2018-09-04')
issue_data11 = ( 384,1010, 9483, '2018-09-10')


dbcursor.execute(add_issue,issue_data1)
dbcursor.execute(add_issue,issue_data2)
dbcursor.execute(add_issue,issue_data3)
dbcursor.execute(add_issue,issue_data4)
dbcursor.execute(add_issue,issue_data5)
dbcursor.execute(add_issue,issue_data6)
dbcursor.execute(add_issue,issue_data7)
dbcursor.execute(add_issue,issue_data8)
dbcursor.execute(add_issue,issue_data9)
dbcursor.execute(add_issue,issue_data10)
dbcursor.execute(add_issue,issue_data11)

dbcursor.execute("CREATE TABLE lib_return (return_id int(10), user_ID int(10), issue_id int(10), return_date varchar(10), primary key (return_id,issue_id),foreign key (user_ID) references lib_user(user_ID)on delete cascade, foreign key (issue_id) references lib_issue(issue_id)on delete cascade)")
#adding return information into database
add_return = ("INSERT INTO  lib_return (return_id,user_ID, issue_id,return_date ) VALUES (%s,%s,%s,%s)")

return_data1 = (474,1001, 374, '2018-09-04')
return_data2 = (475,1002, 375, '2018-10-06')
return_data3 = (476,1003, 376, '2018-03-08')
return_data4 = (477,1004, 377, '2018-11-24')
return_data5 = ( 478,1005, 378, '2018-11-04')
return_data6 = (479,1006, 379, '2018-12-20')
return_data7 = (480,1007, 380, '2018-11-19')
return_data8 = (481,1008, 381, '2018-12-17')
return_data9 = (482,1009, 382, '2018-12-16')
return_data10 = (483,1099, 383, '2018-10-04')



dbcursor.execute(add_return,return_data1)
dbcursor.execute(add_return,return_data2)
dbcursor.execute(add_return,return_data3)
dbcursor.execute(add_return,return_data4)
dbcursor.execute(add_return,return_data5)
dbcursor.execute(add_return,return_data6)
dbcursor.execute(add_return,return_data7)
dbcursor.execute(add_return,return_data8)
dbcursor.execute(add_return,return_data9)
dbcursor.execute(add_return,return_data10)


dbcursor.execute("CREATE TABLE fine (fine_id int(20), user_ID int(20),amount varchar(20), date_due varchar(20),date_paid varchar(20),primary key (user_id,fine_id), foreign key (user_ID) references lib_user(user_ID) on delete cascade)")
#adding fine information into database
add_fine = ("INSERT INTO  fine  (fine_id,user_ID, amount,date_due,date_paid) VALUES (%s,%s,%s,%s,%s)")


fine_data1 = (574,1001, 3, '2018-08-09','2018-09-21')
fine_data2 = (575,1002, 3, '2018-10-12','2018-09-27')
fine_data3 = (576,1003, 4, '2018-09-15', '2018-10-09')
fine_data4 = (577,1004, 5, '2018-09-05', '2018-09-24')
fine_data5 = ( 578,1005, 6, '2018-10-18', '2018-11-16')
fine_data6 = (579,1006, 10, '2018-08-06', '2018-09-10')
fine_data7 = (580,1007, 23, '2018-02-18','2018-10-15')
fine_data8 = (581,1008, 10, '2018-08-12', '2018-09-12')
fine_data9 = (582,1009, 4, '2018-04-14', '2018-05-13')
fine_data10 = (583,1099, 5, '2018-09-21', '2018-10-10')
fine_data11 = (584,1010, 5, '2018-08-29', '2018-09-09')



dbcursor.execute(add_fine,fine_data1)
dbcursor.execute(add_fine,fine_data2)
dbcursor.execute(add_fine,fine_data3)
dbcursor.execute(add_fine,fine_data4)
dbcursor.execute(add_fine,fine_data5)
dbcursor.execute(add_fine,fine_data6)
dbcursor.execute(add_fine,fine_data7)
dbcursor.execute(add_fine,fine_data8)
dbcursor.execute(add_fine,fine_data9)
dbcursor.execute(add_fine,fine_data10)
dbcursor.execute(add_fine,fine_data11)

dbcursor.execute("CREATE TABLE book_locations (book_id int(20), library_ID int(10),primary key (book_id,library_ID),foreign key (library_ID) references library(library_ID),  foreign key (book_id) references book(book_id)on delete cascade)")
#adding book locations information into database
add_loc = ("INSERT INTO  book_locations(book_id,library_ID) VALUES (%s,%s)")

loc_data1 = (9876, 1234)
loc_data2 = (9876, 1122)
loc_data3 = (9876, 1233)
loc_data4 = (9876, 1444)
loc_data5 = (9876, 1112)
loc_data6 = (9876, 1268)
loc_data7 = (9876, 1144)
loc_data8 = (9876,1223)
loc_data9 = (9876, 1244)
loc_data10 = (9876, 1222)
loc_data11 = (8445, 1234)
loc_data12 = (8445, 1122)
loc_data13 = (8335,1233)
loc_data14 = (8335,1444)
loc_data15 = (8225,1122)
loc_data16 = (8225,1268)
loc_data17 = (8995,1268)
loc_data18 = (8995,1144)
loc_data19 = (8122,1234)
loc_data20 = (8122,1223)
loc_data21 = (8398,1223)
loc_data22 = (8398,1244)
loc_data23 = (8398,1234)
loc_data24 = (7733,1244)
loc_data25 = (7733,1234)
loc_data26 = (8844,1222)
loc_data27 = (8844,1234)
loc_data28 = (9483,1144)
loc_data29 = (9483,1122)
loc_data30 = (9999,1233)
loc_data31 = (9999,1144)



dbcursor.execute(add_loc,loc_data1)
dbcursor.execute(add_loc,loc_data2)
dbcursor.execute(add_loc,loc_data3)
dbcursor.execute(add_loc,loc_data4)
dbcursor.execute(add_loc,loc_data5)
dbcursor.execute(add_loc,loc_data6)
dbcursor.execute(add_loc,loc_data7)
dbcursor.execute(add_loc,loc_data8)
dbcursor.execute(add_loc,loc_data9)
dbcursor.execute(add_loc,loc_data10)
dbcursor.execute(add_loc,loc_data11)
dbcursor.execute(add_loc,loc_data12)
dbcursor.execute(add_loc,loc_data13)
dbcursor.execute(add_loc,loc_data14)
dbcursor.execute(add_loc,loc_data15)
dbcursor.execute(add_loc,loc_data16)
dbcursor.execute(add_loc,loc_data17)
dbcursor.execute(add_loc,loc_data18)
dbcursor.execute(add_loc,loc_data19)
dbcursor.execute(add_loc,loc_data20)
dbcursor.execute(add_loc,loc_data21)
dbcursor.execute(add_loc,loc_data22)
dbcursor.execute(add_loc,loc_data23)
dbcursor.execute(add_loc,loc_data24)
dbcursor.execute(add_loc,loc_data25)
dbcursor.execute(add_loc,loc_data26)
dbcursor.execute(add_loc,loc_data27)
dbcursor.execute(add_loc,loc_data28)
dbcursor.execute(add_loc,loc_data29)
dbcursor.execute(add_loc,loc_data30)
dbcursor.execute(add_loc,loc_data31)

dbcursor.execute("CREATE TABLE employee (employee_id int(20),first_name varchar(30),last_name varchar(30),library_ID int(10),  primary key (employee_id),foreign key (library_ID) references library(library_ID))")
#adding employee information into database
add_emp = ("INSERT INTO  employee(employee_id ,first_name,last_name,library_ID) VALUES (%s,%s,%s,%s)")

emp_data1 = (2001, 'Imari', 'Bloom', 1234)
emp_data2 = (2011, 'Ken', 'Marin', 1234)
emp_data3 = (2002, 'Christal', 'Murphy', 1122)
emp_data4 = (2012, 'Karin', 'Jenns', 1233)
emp_data5 = (2003, 'Blane', 'Jon', 1233)
emp_data6 = (2004, 'Ashley', 'Thurston',1444 )
emp_data7 = (2005, 'Amanda', 'Garrin',1268 )
emp_data8 = (2006, 'Kery', 'Killim', 1144)
emp_data9 = (2007, 'Barry', 'Kinsha', 1112)
emp_data10 = (2008, 'Nina', 'Garret', 1223)
emp_data11 = (2009, 'John', 'Green', 1244)
emp_data12 = (2010, 'Kelly', 'Harrin', 1244)
emp_data13 = (2013, 'Kim', 'Loori', 1222)



dbcursor.execute(add_emp,emp_data1)
dbcursor.execute(add_emp,emp_data2)
dbcursor.execute(add_emp,emp_data3)
dbcursor.execute(add_emp,emp_data4)
dbcursor.execute(add_emp,emp_data5)
dbcursor.execute(add_emp,emp_data6)
dbcursor.execute(add_emp,emp_data7)
dbcursor.execute(add_emp,emp_data8)
dbcursor.execute(add_emp,emp_data9)
dbcursor.execute(add_emp,emp_data10)
dbcursor.execute(add_emp,emp_data11)
dbcursor.execute(add_emp,emp_data12)
dbcursor.execute(add_emp,emp_data13)



db.commit()
#menu of options 
print("Users:")
print("1. Enter the user ID and all issues(with dates) correlated with user will display.")
print("2. Add a new issue")
print("3. Return an issue")
print("Employees:")
print("4. Add a book.")
print("5. Delete a book.")
print("6. Change location of work.")
print("Both:")
print("7. Display all locations of a book")
print("8. Exit")


#display the issues a user has or had and the date it was issued 
def menu1():
    id =eval(input('Enter id: '))

#checks if user exists 
    dbcursor.execute("SELECT user_ID FROM lib_user")
    result = dbcursor.fetchall()
    id_flag = 0
    for x in result:
        if id == x[0]:
            id_flag = 1
            break

#if user id exists than issues will be displayed  
    if id_flag == 1:
        print("All issues: ")
        dbcursor.execute("SELECT title,date_issued FROM book natural join  lib_issue WHERE user_id = %s", (id,))
        result = dbcursor.fetchall()
        for x in result:
            print(x[0],x[1])
    else:
        print("The user id was not found in the database.")
   
def menu2():

    
    while True:
        #new issue id must be three numbers 
        try:
            issueID = eval(input('Enter new issue id: '))
            if len(str(issueID))!=3:
                raise ValueError
        except ValueError:
            print("Enter an acceptable issue ID.")
        else:
            break
        
#checks if issue id already exists       
    dbcursor.execute("SELECT issue_id FROM lib_issue")
    result = dbcursor.fetchall()
    issue_flag = 0
    for x in result:
        if issueID == x[0]:
            issue_flag = 1
            break
        
    if issue_flag == 1:
        print("issue ID already appears in database.")
        print("Try again please.")
        return
    
#checks if user exists 
    uid = eval(input('Enter user id: '))
    dbcursor.execute("SELECT user_ID FROM lib_user")
    result = dbcursor.fetchall()
    id_flag = 0
    for x in result:
        if uid == x[0]:
            id_flag = 1
            break
        
    if id_flag == 0:
        print("The user ID does not appear in the database.")
        print("Try again please.")
        return
    
#checks if book already exists         
    book_id = eval(input('Enter book id: '))
    dbcursor.execute("SELECT book_id FROM book")
    result = dbcursor.fetchall()
    book_flag = 0
    for x in result:
        if book_id == x[0]:
            book_flag = 1
            break

    if  book_flag == 0:
        print("The book does not appear in the database.")
        print("Try again please.")
        return

#date for issue is today's date 
    now = datetime.datetime.now()
    date = now.date()

#new issue will be inserted into database  
    issue_data = (issueID,uid,book_id,str(date))
    dbcursor.execute(add_issue,issue_data)
    db.commit();
    print("The issue has been added to the database.")
    

def menu3():
    
    while True:
        #new return id must be three numbers 
        try:
            returnID = eval(input('Enter new return id: '))
            if len(str(returnID))!=3:
                raise ValueError
            elif type(returnID)==str:
                raise ValueError
        except ValueError:
            print("Enter an acceptable return ID.")
        else:
            break

#checks if issue return id already exists         
    dbcursor.execute("SELECT return_id FROM lib_return")
    result = dbcursor.fetchall()
    r_flag = 0
    for x in result:
        if returnID == x[0]:
            r_flag = 1
            break
        
    if r_flag == 1:
        print("return ID already appears in database.")
        print("Try again please.")
        return
    
#checks if user exists 
    uid = eval(input('Enter user id: '))
    dbcursor.execute("SELECT user_ID FROM lib_user")
    result = dbcursor.fetchall()
    id_flag = 0
    for x in result:
        if uid == x[0]:
            id_flag = 1
            break
        
    if id_flag == 0:
        print("The user ID does not appear in the database.")
        print("Try again please.")
        return

#checks if issue belongs to user       
    issue_id = eval(input('Enter issue id: '))
    dbcursor.execute("SELECT issue_id FROM lib_issue where user_id=%s", (uid,))
    result = dbcursor.fetchall()
    i_flag = 0
    for x in result:
        if issue_id == x[0]:
            i_flag = 1
            break

    if  i_flag == 0:
        print("The issue does not appear in the database.")
        print("Try again please.")
        return
    
#checks if the return already exists  
    dbcursor.execute("SELECT issue_id FROM lib_return where issue_id=%s", (issue_id,))
    result = dbcursor.fetchall()
    return_flag = 0
    for x in result:
        if issue_id == x[0]:
            return_flag = 1
            break

    if return_flag == 1:
        print("The return already appears in the database.")
        print("Try again please.")
        return
    
#date for return is today's date     
    now = datetime.datetime.now()
    date = now.date()
    
#new return will be inserted into database     
    return_data = (returnID,uid,issue_id,str(date))
    dbcursor.execute(add_return,return_data)
    db.commit();
    print("The return has been added to the database.")
    

def menu4():
    while True:
#book id must be 4 numbers
        try:
            bid = eval(input('Enter new book id: '))
            if len(str(bid))!=4:
                raise ValueError
        except ValueError:
            print("Enter an acceptable book id.")
        else:
            break
        
#checks if book already exists      
    dbcursor.execute("SELECT book_id FROM book")
    result = dbcursor.fetchall()
    bid_flag = 0
    for x in result:
        if bid == x[0]:
            bid_flag = 1
            break
        if bid_flag == 1:
            print("The book is already in database.")
            print("Try again.")
            return

#book title and author must be below 100 characters
#book genre must be below 20 characters 
    while True:
        try:
            title = input('Enter the title: ')
            if len(str(title))>100:
                    raise ValueError
        except ValueError:
                print("Enter an acceptable book title.")
        else:
            break
        
    while True:
        try:
            author = input('Enter the author: ')
            if len(str(author))>100:
                raise ValueError
        except ValueError:
            print("Enter an acceptable book author.")
        else:
            break
        
    while True:
        try:
            genre = input('Enter genre: ')
            if len(str(genre))>20:
                raise ValueError
        except ValueError:
            print("Enter an acceptable book author.")
        else:
            break
        
#new book will be added to database 
    book_data = (bid,title,author,genre)
    dbcursor.execute(add_book,book_data)
    db.commit();
    print("The book has been added to the database.")

   


def menu5():
    #checks if book exists 
    bid = eval(input('Enter book id: '))

    dbcursor.execute("SELECT book_id FROM book")
    result = dbcursor.fetchall()
    bid_flag = 0
    for x in result:
        if bid == x[0]:
            bid_flag = 1
            break

   
    if bid_flag == 0:
        print("book is not in database.")
    else:
        #deletes book from database 
        dbcursor.execute("DELETE FROM book where book_id=%s", (bid,))
        db.commit();
        print("The book has been deleted from the database.") 

def menu6():

    eid = eval(input('Enter employee ID: '))
    #checks if employee exists 
    dbcursor.execute("SELECT employee_id FROM employee")
    result = dbcursor.fetchall()
    eid_flag = 0
    for x in result:
        if eid == x[0]:
            eid_flag = 1
            break

    if eid_flag == 0:
        print("employee id is not in the database.")
        print("try again.")
        return

    
    lid = eval(input('Enter library ID of where you want to work: '))
    #checks if library exists 
    dbcursor.execute("SELECT library_id FROM library")
    result = dbcursor.fetchall()
    lid_flag = 0
    for x in result:
        if lid == x[0]:
            lid_flag = 1
            break

    if lid_flag == 0:
        print("library is not in database.")
        print("try again.")
        return

    #location of work is updated 
    dbcursor.execute("UPDATE employee SET library_id =%s WHERE employee_id =%s", (lid,eid))
    db.commit();
    print("location of work has changed.") 

def menu7():
    #check if book exists 
    bid =eval(input('Enter book id: '))
    dbcursor.execute("SELECT book_id FROM book")
    result = dbcursor.fetchall()
    book_flag = 0
    for x in result:
        if bid == x[0]:
            book_flag = 1
            break

    if book_flag == 1:
        print("All locations of the book: ")
        #get locations of book 
        dbcursor.execute("SELECT library_name from library natural join book_locations WHERE book_id = %s", (bid,))
        result = dbcursor.fetchall()
        for x in result:
            print(x[0])
    else:
        print("The book is not found in the database.")
 
user_input = eval(input('Enter choice: '))
#user must put #1-8 
while user_input != 8:
    if user_input == 1:
        menu1()
    elif user_input == 2:
        menu2()
    elif user_input == 3:
        menu3()
    elif user_input == 4:
        menu4()
    elif user_input == 5:
        menu5()  
    elif user_input == 6:
        menu6()
    elif user_input == 7:
        menu7()
    else:
        print("You have entered an invalid choice.")
        user_input = eval(input('Enter choice: '))

    user_input = eval(input('Enter choice: '))

print("Thank you for using this program!")
dbcursor.close()
