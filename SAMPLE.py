import sqlite3
dbase=sqlite3.connect('GIS.db')
cursor = dbase.cursor()

#Creating table

cursor.execute('''
                CREATE TABLE IF NOT EXISTS GIS_Records(
                LOCATION_ID INT PRIMARY KEY NOT NULL ,
                LAKE TEXT NOT NULL,   
                RIVER TEXT NOT NULL,       
                OCEAN TEXT NOT NULL,   
                CITY TEXT NOT NULL,          
                COUNTRY TEXT NOT NULL)''')

#Insert function

def insert(LOCATION_ID,LAKE,RIVER,OCEAN,CITY,COUNTRY):
    
    cursor.execute('''INSERT INTO GIS_records(LOCATION_ID,LAKE,RIVER,OCEAN,CITY,COUNTRY)
      VALUES(?,?,?,?,?,?)''',(LOCATION_ID,LAKE,RIVER,OCEAN,CITY,COUNTRY))
    dbase.commit()
    print("\nRecords got updated\n")

    
'''
insert(1,'Vihar lake','Godavari river','Arabian Sea','Maharashtra','India')
insert(2,'Madhuri lake','Brahmaputra river','IndianOcean','Arunachal Pradesh','India')
insert(3,'Bellandur lake','Cauvery river','Bay of Bengal','Karnataka','India')
insert(4,'Lake Victoria','Nile river','Mediterranean Sea','Uganda','Africa')
'''
      


       

#Display functions
      
def displayall():
    data = cursor.execute(''' SELECT * FROM GIS_Records ORDER BY LOCATION_ID''' )
    for record in data:
        print('\n LOCATION_ID :'+str(record[0]))
        print(' LAKE : '+str(record[1]))
        print(' RIVER: '+str(record[2]))
        print(' OCEAN: '+str(record[3]))
        print(' CITY : '+str(record[4]))
        print(' COUNTRY: '+str(record[5])) 

def displayspecific(a):    
    data =cursor.execute(''' SELECT * FROM GIS_Records WHERE LOCATION_ID=?''',(a,))
    x = data.fetchall()
    if x == []:
        print('Doesnot exist')
    else:
        print (x)

#Update function      

def update():
    cursor.execute('''
    UPDATE GIS_Records set COUNTRY='China' WHERE LOCATION_ID=5
    ''')
    dbase.commit()
    print("\nRecords got updated\n")

#Delete function     

def delete(a):
    cursor.execute(''' DELETE from GIS_Records WHERE LOCATION_ID=?''',(a,))
    dbase.commit()
    print('\nDataDeleted')

#Start of program

print("Welocome To GIS Database 🌎 \n")

print("1.Display\n2.Insert\n3.Delete\n4.Update\n5.Exit\n")



for x in range(1, 12):

    if x==11:
        print("\nMaximum attempt finished...Exiting loop\n")
        break
    i = int(input("\nEnter your choice among above fields:\n"))   

    if i==1:
         print("1.Display entire content\n2.Display your preference")
         ch=int(input("\nEnter your choice:"))
         if ch==1:
             displayall()
         elif ch==2:
             a=int(input("\nEnter your location id to display the data:"))
             displayspecific(a)
             
    elif i==2:
          print("\nEnter the following details\n")
          a= int(input("LOCATION_ID:"))
          b = str(input("LAKE:"))
          c = str(input("RIVER:"))
          d= str(input("OCEAN:"))
          e = str(input("CITY:"))
          f= str(input("COUNTRY:"))
          insert(a,b,c,d,e,f)   
  
    elif i==3:
        a=int(input("\nEnter your location id to delete the data:"))
        delete(a)
    elif i==4:
        print("\nExample changing the country name of location id 5")
        update()
    elif i==5:
        break
    else:
        print("\nInvalid data input...Enter valid data\n")
        continue
    


print("\nThanks for visiting GIS Database 🙏")


dbase.close()


