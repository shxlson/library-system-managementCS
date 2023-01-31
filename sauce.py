#   project name    : Library management system

import mysql.connector
from datetime import date

fine_per_day =5.0  #global variable

def clear():
  for _ in range(1):
     print


def add_book():
  conn = mysql.connector.connect(
       host='localhost', database='library', user='root', password='1234')
  cursor = conn.cursor()
  ID=input('enter the book id')
  title = input('Enter Book Title :')
  author = input('Enter Book Author : ')
  publisher = input('Enter Book Publisher : ')
  pages = input('Enter Book Pages : ')
  price = input('Enter Book Price : ')
  edition = input('Enter Book Edition : ')
  copies  = int(input('Enter copies : '))
  sql = 'insert into books(ID,title,author,price,pages,publisher,edition,status)  values ("'+ID+'", "' +title + '","' +author+'","'+price+'","'+pages+'","'+publisher+'","'+edition+'","available");'
  #sql2 = 'insert into transaction(dot,qty,type) values ("'+str(today)+'",'+qty+',"purchase");'
  #print(sql)
  for _ in range(0,copies):
    cursor.execute(sql)
    conn.commit()
  conn.close()
  print('\n\nNew Book added successfully')
  wait = input('\n\n\n Press any key to continue....')


def add_member():
  conn = mysql.connector.connect(
      host='localhost', database='library', user='root', password='1234')
  cursor = conn.cursor()
  ID=input('Enter Member ID : ')
  name = input('Enter Member Name :')
  clas = input('Enter Member Class & Section : ')
  address = input('Enter Member Address : ')
  phone = input('Enter Member Phone  : ')
  email = input('Enter Member Email  : ')
  
 
  sql = 'insert into members(ID,name,class,address,phone,email) values ("'+ID+'", "' + \
      name + '","' + clas+'","'+address+'","'+phone + \
        '","'+email+'");'
  #sql2 = 'insert into transaction(dot,qty,type) values ("'+str(today)+'",'+qty+',"purchase");'
  #print(sql)
  
  cursor.execute(sql)
  conn.commit()
  conn.close()
  print('\n\nNew Member added successfully')
  wait =input('\n\n\n Press any key to continue....')


def modify_book():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='1234')
    cursor = conn.cursor()
    clear()
    print('Modify BOOK Details Screen ')
    print('-'*120)
    print('\n1. Book Title')
    print('\n2. Book Author')
    print('\n3. Book Publisher')
    print('\n4. Book Pages')
    print('\n5. Book Price')
    print('\n6. Book Edition')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'title'
    if choice == 2:
        field = 'author'
    if choice == 3:
        field = 'publisher'
    if choice == 4:
        field = 'pages'
    if choice == 5:
        field = 'price'
    book_id = input('Enter Book ID :')
    value = input('Enter new value :')
    if field =='pages' or field == 'price':
        sql = 'update books set ' + field + ' = '+value+' where id = '+book_id+';'
    else:
        sql = 'update books set ' + field + ' = "'+value+'" where id = '+book_id+';'
    #print(sql)
    cursor.execute(sql)
    conn.commit()
    print('\n\n\nBook details Updated.....')
    conn.close()
    wait =input('\n\n\n Press any key to continue....')


def modify_member():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='1234')
    cursor = conn.cursor()
    clear()
    print('Modify Memeber Information Screen ')
    print('-'*120)
    print('\n1. Name')
    print('\n2. Class')
    print('\n3. address')
    print('\n4. Phone')
    print('\n5. Emaile')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field =''
    if choice == 1:
        field ='name'
    if choice == 2:
        field = 'class'
    if choice ==3:
        field ='address'
    if choice == 4:
        field = 'phone'
    if choice == 5:
        field = 'email'
    mem_id =input('Enter member ID :')
    value = input('Enter new value :')
    sql = 'update members set '+ field +' = "'+value+'" where id = '+mem_id+';'
    #print(sql)
    cursor.execute(sql)
    conn.commit()
    print('Member details Updated.....')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def mem_issue_status(mem_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='1234')
    cursor = conn.cursor()
    sql ='select * from transactions where m_id ='+mem_id +' and dor is NULL;'
    #print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def book_status(book_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='1234')
    cursor = conn.cursor()
    sql = 'select * from books where id ='+book_id + ';'
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def book_issue_status(book_id,mem_id):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='1234')
    cursor = conn.cursor()
    sql = 'select * from transactions where b_id ='+book_id + ' and m_id ='+ mem_id +' and dor is NULL;'
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

#ISSUE BOOK
#========================
def issue_book():
    conn = mysql.connector.connect(
      host='localhost', database='library', user='root', password='1234')
    cursor = conn.cursor()

    clear()
    print('\n BOOK ISSUE SCREEN ')
    print('-'*120)
    book_id = input('Enter Book  ID : ')
    mem_id  = input('Enter Member ID :')
    St="select * from books where id={}".format(book_id)
    cursor.execute(St)
    m = cursor.fetchall()
    
    tid=1
    print(m)
    today=date.today()
    if m[0][5] == 'available':
      sql3 = 'insert into transactions(tid,b_id, m_id, doi) values('+str(tid)+','+str(book_id)+','+str(mem_id)+',"'+str(today)+'");'
      sql_book = 'update books set status="issue" where id ='+book_id + ';'
      cursor.execute(sql3)
      cursor.execute(sql_book)
      conn.commit()
      print('\n\n\n Book issued successfully')
      tid+=1
    else:
      print('\n\nBook is not available for ISSUE... Current status :')
    conn.close()
    wait =input('\n\n\n Press any key to continue....')
#RETURN BOOK
#=====================================================
def return_book():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='1234')
    cursor = conn.cursor()
    
    clear()
    print('\n BOOK RETURN SCREEN ')
    print('-'*120)
    book_id = input('Enter Book  ID : ')
    mem_id = input('Enter Member ID :')
    today =date.today()
    result = book_issue_status(book_id,mem_id)
    m='issued'
    if m==None:
       print('Book was not issued...Check Book Id and Member ID again..')
    else:
       sql='update books set status ="available" where id ='+book_id +';'
       sql1 = 'update transactions set dor ="'+str(today)+'"' 
       
       cursor.execute(sql)
       cursor.execute(sql1)
       conn.commit()
       print('\n\nBook returned successfully')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def search_book(field):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='1234')
    cursor = conn.cursor()

    clear()
    print('\n BOOK SEARCH SCREEN ')
    print('-'*120)
    msg ='Enter '+ field +' Value :'
    title = input(msg)
    sql ='select * from books where '+ field + ' like "%'+ title+'%"'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result for :',field,' :' ,title)
    print('-'*120)
    for record in records:
      print(record)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def search_menu():
    while True:
      clear()
      print(' S E A R C H   M E N U ')
      print("\n1.  Book Title")
      print('\n2.  Book Author')
      print('\n3.  Publisher')
      print('\n4.  Exit to main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      field =''
      if choice == 1:
        field='title'
      if choice == 2:
        field = 'author'
      if choice == 3:
        field = 'publisher'
      if choice == 4:
        break
      search_book(field)


def main_menu():
    while True:
      clear()
      print(' L I B R A R Y    M E N U')
      print("\n1.  Add Books")
      print('\n2.  Add Member')
      print('\n3.  Modify Book Information')
      print('\n4.  Modify Student Information')
      print('\n5.  Issue Book')
      print('\n6.  Return Book')
      print('\n7.  Search Menu')
      print('\n0.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))

      if choice == 1:
        add_book()
      if choice == 2:
        add_member()
      if choice == 3:
        modify_book()
      if choice == 4:
        modify_member()
      if choice == 5:
        issue_book()
      if choice == 6:
        return_book()
      if choice == 7:
        search_menu()    
      if choice == 0:
        break


if __name__ == "__main__":
    main_menu()
