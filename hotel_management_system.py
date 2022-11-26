import mysql.connector 

#Clears screen for creating blank spaces
def clear():
  for i in range(65):  
     print()

class Hotel:
    #checking for duplicate rooms
    def room_exist(self,room_no):
        self.conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='')
        self.cursor = self.conn.cursor()
        sql ="select * from rooms where room_no ="+room_no+";"
        self.cursor.execute(sql)
        self.record = self.cursor.fetchone()
        return self.record

    #checking for duplicate customers
    def customer_exist(self,cust_no):
        self.conn = mysql.connector.connect(
            host='localhost', database='hotel', user='root', password='')
        self.cursor = self.conn.cursor()
        sql = "select * from customer where id ="+cust_no+";"
        self.cursor.execute(sql)
        self.record = self.cursor.fetchone()
        return self.record

    #Adding rooms to the database
    def add_room(self):
        conn = mysql.connector.connect(
            host='localhost', database='hotel', user='root', password='')
        cursor = conn.cursor()
        clear()
        print('Add New Room - Screen')
        print('-'*120)
        self.room_no = input('\n Enter Room No :')
        self.room_type = input('\n Enter Room Type( AC/DELUX/Super Delux/ /Presedential suite) :')
        self.room_rent = input('\n Enter Room Rent (RS.) :')
        self.room_bed = input('\n Enter Room Bed Type(Single/Double/Triple) :')
        sql = 'insert into rooms(room_no,room_type,room_rent,room_bed,status) values \
                ('+self.room_no+',"'+ self.room_type.upper()+'",'+self.room_rent+',"'+self.room_bed.upper()+'","free");'
        
        result = self.room_exist(self.room_no)
        if result is None:
            cursor.execute(sql)
            print("Room added sucessfully.....")
        else:
            print('\n\n\nRoom No ',self.room_no, ' already exists in our database')
        conn.close()
        wait = input('\n\n\n Press any key to continue....')

    #modifing rooms 
    def modify_room(self):
        conn = mysql.connector.connect(
            host='localhost', database='hotel', user='root', password='')
        cursor = conn.cursor()
        clear()
        print(' Change Room Information ')
        print('*'*60)
        print('1.   Room Type')
        print('2.   Room Rent')
        print('3.   Room Bed')
        choice = int(input('Enter your choice :'))
        self.field_name = ''
        if choice == 1:
            self.field_name = 'room_type'
        if choice == 2:
            self.field_name = 'room_rent'
        if choice == 3:
            self.field_name = 'room_bed'
        self.room_no  = input('Enter room No :')   
        self.value = input('Enter new value :')
        sql = 'update rooms set ' +self.field_name +' = '+ self.value +' where  room_no =' + self.room_no +';'
        cursor.execute(sql)
        wait = input('\n\n\n Record Updated .............Press any key to continue......')


    #Adding customer to the database
    def add_customer(self):
        conn = mysql.connector.connect(
            host='localhost', database='hotel', user='root', password='')
        cursor = conn.cursor()
        clear()
        print('Add New Customer - Screen')
        print('-'*120)
        name = input('\n Enter Customer Name :')
        address = input('\n Enter Customer Address:')
        phone = input('\n Enter Customer Phone NO :')
        email = input('\n Enter Customer Email ID :')
        id_proof = input('\n Enter Customer ID(Passport/Driving License/Citizenchip)  :')
        id_proof_no = input('\n Enter Customer ID proof NO :')
        males = input('\n Enter Total Males :')
        females = input('\n Enter Total Females :')

        sql = 'insert into customer(name,address,phone,email,id_proof,id_proof_no,males,females) values \
                ("'+name+'","' + address.upper()+'","'+phone+'","'+email.upper()+'","'+id_proof.upper()+'","'+id_proof_no.upper()+'",'+males+','+females+');'

        cursor.execute(sql)
        print('\n\n\nCustomer Added successfully ...........')
        conn.close()
        wait = input('\n\n\n Press any key to continue....')

    #Modifying customer in the database
    def modify_customer(self):
        self.conn = mysql.connector.connect(
            host='localhost', database='hotel', user='root', password='')
        self.cursor = self.conn.cursor()
        clear()
        print(' Change Customer Information ')
        print('*'*60)
        print('1.   Name')
        print('2.   Address')
        print('3.   Phone No')
        print('4.   Email ID')
        print('5.   ID Proof')
        print('6.   ID Proof No')
        print('7.   Males')
        print('8.   Females')
        choice = int(input('Enter your choice :'))
        self.field_name = ''
        if choice == 1:
            self.field_name = 'name'
        if choice == 2:
            self.field_name = 'address'
        if choice == 3:
            self.field_name = 'phone'
        if choice == 4:
            self.field_name = 'email'
        if choice == 5:
            self.field_name = 'id_proof'
        if choice == 6:
            self.field_name = 'id_proof_no'
        if choice == 7:
            self.field_name = 'males'
        if choice == 8:
            self.field_name = 'females'
        cust_no = input('Enter Customer No :')
        value = input('Enter new value :')
        sql = 'update customer set ' + self.field_name + ' = ' + \
            value + ' where  id =' + cust_no + ';'
        self.cursor.execute(sql)
        wait = input(
            '\n\n\n Record Updated .............Press any key to continue......')

#booing room and adding its key values to database
def room_booking():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='')
    cursor = conn.cursor()
    room_id =input('Enter room no to book :')
    cust_id = input('Enter customer ID :')
    date_of_occ = input('Enter date of occupancy (yyyy-mm-dd) :')
    advance = input('Enter advance amount :')
    sql1 = 'update rooms set status = "occupied" where id ='+room_id +';'
    sql2 = 'insert into booking(room_id,cust_id,doo,advance) values ('+room_id+','+cust_id+',"'+date_of_occ+'",'+advance+');'
    #print(sql2)
    #print(sql1)
    result = customer.room_exist(room_id)
    result1 = customer.customer_exist(cust_id)

    if result[5]=='free' and result1 is not None: 
      cursor.execute(sql1)
      cursor.execute(sql2)
      print('\n\n\nRoom no ', room_id, 'booked for', cust_id)
    

    if result[5] !='free':
       print('\n Room is not available for booking. Right now it is :',result[5])
    if result1 is None:
       print('Customer does not exist....Please add customer first in our database')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def search_menu():
    while True:
      clear()
      print(' Search Menu')
      print('*'*60)
      print("\n1.  Room Status")
      print('\n2.  Booking Status')
      print('\n3.  customer Details')
      print('\n4.  Back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      try:
        if choice==1:
            search_rooms()
        if choice==2:
            search_booking()
        if choice==3:
            search_customer()
        if choice==4:
            break
      except Exception as e:
        continue      


def report_room_status():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='')
    cursor = conn.cursor()
    sql = 'select * from rooms'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print(' Rooms Status - Report')
    print('-'*120)
    print('{:10s} {:10s} {:20s} {:20s} {:>40s} {:>30s}'.format('Room ID','Room No', 'Room Type', 'Rent','Bedding', 'Status'))
    for idr,no,rtype,rent,bed,status in records:
        print('{:<10d} {:<10d} {:20s} {:<7.2f} {:>40s} {:>30s}'.format(idr, no, rtype, rent, bed, status))
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def report_booking_status():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='')
    cursor = conn.cursor()
    sql = 'select b.book_id,room_no,doo,dol,advance, name,address,phone \
           from booking b, customer c ,rooms r \
           where b.room_id = r.id and b.cust_id = c.id and dol is NULL;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print(' Booking Status - Report')
    print('-'*120)
    print('{:10s} {:10s} {:20s} {:20s} {:>30s} {:20s} {:30s} {:15s}'.format(
        'Booking ID', 'Room No', 'DOO', 'DOL', 'Advance', 'Name','Address','Phone'))
    for idr, no, doo,dol,advance,name,addr,phone in records:
        print('{:10d} {:10d} {:20s} {:20s} {:10.2f} {:20s} {:30s} {:15s}'.format(
            idr, no, str(doo), str(dol), advance, name, addr, phone))
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def search_rooms():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='')
    cursor = conn.cursor()
    room_no = input('Enter Room No :')
    sql ='select * from rooms where room_no ='+room_no +';'
    cursor.execute(sql)
    record = cursor.fetchone()
    clear()
    print('Room Status')
    print('*'*60)
    print('Room NO :',record[1])
    print('Room Rent :',record[2])
    print('Room Bed :',record[3])
    print('Room Status :',record[4])
    conn.close()
    wait = input('\n\n\nPress any key to continue......')


def search_customer():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='')
    cursor = conn.cursor()
    
    clear()
    print('Search Customer DataBase')
    print('*'*60)
    print('1.   Customer Name')
    print('2.   Customer Address')
    print('3.   Customer Phone')
    print('4.   Customer Email')
    print('5.   Address Proof')
    print('6.   Address Proof ID')
    choice = int(input('Enter your choice : '))
    field_name =''
    if choice ==1:
      field_name = 'name'
    if choice ==2:
      field_name = 'address'
    if choice ==3:
      field_name = 'phone'
    if choice ==4:
      field_name = 'email'
    if choice ==5:
      field_name = 'id_proof'
    if choice ==6:
      field_name = 'id_proof_no'
    
    value = input('Enter value that you want to search :')
    if field_name =='id':
      sql = 'select * from customer where '+ field_name +' = '+ value + ';'
    else:
      sql = 'select * from customer where ' + field_name + ' like "%' + value + '%";'
    print(sql)
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result for {} = {}'.format(field_name,value))
    print('*'*80)
    print('{} {:20s} {:30s} {:15s} {:30s} {:20s} {:15s}'.format('ID','Name','Address','Phone','Email','ID Used','ID No'))
    for record in records:
      print('{} {:20s} {:30s} {:15s} {:30s} {:20s} {:15s}'.format(
          record[0], record[1], record[2], record[3], record[4], record[5], record[6]))

    conn.close()
    wait = input('\n\n\nPress any key to continue......')


def search_booking():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='')
    cursor = conn.cursor()
    cust_no = input('Enter Customer No :')
    sql = 'select book_id,r.room_no,c.name,doo,advance from booking b, customer c,rooms r where b.room_id = r.id AND b.cust_id = '+cust_no+' and dol is NULL;'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Booking information for customer ID :{}'.format(cust_no))
    print('{} {} {} {} {}'.format('ID','RoomID', 'Customer Name','Date of Occupancy','Advance'))
    print('*'*140)
    for record in records:
      print('{} {} {} {} {}'.format(
          record[0], record[1], record[2], record[3], record[4]))
    conn.close()
    wait = input('\n\n\nPress any key to continue......')

def report_menu():


    while True:
      clear()
      print('Report Menu')
      print("\n1.  Room Status")
      print('\n2.  Booking Status')
      print('\n3.  Back to Main Menu')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      try:
        if choice == 1:
            report_room_status()
        if choice == 2:
            report_booking_status()
        if choice == 3:
            break
      except Exception as e:
        print(e);
        continue      


def change_room_status():
    conn = mysql.connector.connect(
        host='localhost', database='hotel', user='root', password='')
    cursor = conn.cursor()
    clear()
    room_no = input('Enter Room No :')
    status = input('Enter current status(Renovation/modification ) :')
    sql = 'update rooms set status="'+status+'" where room_no ='+room_no+';'
    cursor.execute(sql)
    print('\n\nRoom Status Updated')
    wait = input('\n\n\n Press any key to continue....')



if __name__ == "__main__":
       while True:
        clear()
        print(' H O T E L   M A N A G E M E N T   S Y S T E M ')
        print('*'*30)
        print("\n1.   Add New Room")
        print('\n2.   Add Customer')
        print('\n3.   Modify Room Information')
        print('\n4.   Modify Customer Information')
        print('\n5.   Room Booking')
        print('\n6.   Search Database')
        print('\n7.   Report Menu')
        print('\n8.  Close application')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))
        customer=Hotel()
        if choice == 1:
            customer.add_room()
        if choice == 2:
            customer.add_customer()
        if choice == 3:
            customer.modify_room()
        if choice == 4:
            customer.modify_customer()
        if choice ==5 :
            room_booking()
        if choice ==6 :
            search_menu()
        if choice == 7:
            report_menu()
        if choice ==8:
            break