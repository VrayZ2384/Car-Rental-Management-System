import mysql.connector
from tabulate import tabulate
import datetime
import time
import getpass
import sys

login_count = 0

for i in range(0, 3):
    try:
        print("\n")
        passwd = getpass.getpass("Enter the MySQL Client Password: ")
        conobj = mysql.connector.connect(host = 'localhost', user = 'root', password = passwd)

        if conobj.is_connected:
            print("Connected Successfully")
            break

        else:
            print("Password Entered is Incorrect\n")
            login_count = login_count + 1
        
            if login_count > 3:
                print("\nPassword Entered Incorrectly 3 times")
                time.sleep(5)
                print('\nExiting Program')            
                sys.exit(1)
                break

        print(login_count)

    except mysql.connector.errors.ProgrammingError:
        print("\nConnection failed, incorrect password entered\n")
        if login_count > 3:
            sys.exit(1)
            break

try:
    cur = conobj.cursor()

except NameError:
    print("This program requires Authorisation / DataBase Admin Password")

#CHECKING FOR THE EXISTENCE FOR THE DATABASE IN THE MYSQL COMMAND LINE CLIENT
 
def checkdatab():
 
    #To check the existence of the database "car_rental"
    cur.execute('show databases')
    databases_in_system = cur.fetchall()
    if ('car_rental',) in databases_in_system:
        print('The database already exists in the system')
    else:
        print('The database specified does not exist in the file')
        print()
        print('creating database "car_rental"')
        
        cur.execute('create database car_rental')
        cur.execute('commit')
        print()
        print('Database created Successfully')
 
checkdatab()
 
cur.execute("use car_rental") 
 
#CARS TABLE
 
def checktable():
 
    #To check the existance of the tables "cars" in the database "car_rental"
    cur.execute("show tables")
    lst1=cur.fetchall()
    if ('cars',) and ('drivers',) in lst1:
        print("the tables are present in the database")
    else:
 
        #CARS TABLE
 
        print('The required table does not exist in the database')
        print('Creating table')
        car="create table Cars(SNo INT,Model varchar(50),Type varchar(30),Brand varchar(30),Engine varchar(50),Displacement varchar(10),Quantity INT,PriceHour varchar(30))"
        cur.execute(car)
        cur.execute('commit')
 
        #ADDING RECORDS TO TABLE CARS
 
        cur.execute("insert into cars values(1,'Fiesta','Hatchback','Ford','4-Cyl TDI','1.6L',25,'25 Dhs')")
        cur.execute("insert into cars values(2,'Fiesta ST','Hatchback','Ford','3-Cyl Turbo','1.5L',15,'30 Dhs')")
        cur.execute("insert into cars values(3,'Focus','Hatchback','Ford','4-Cyl TDI','1.6L',25,'30 Dhs')")
        cur.execute("insert into cars values(4,'Focus RS','Hatchback','Ford','4-Cyl Turbo','2.3L',10,'35 Dhs')")
        cur.execute("insert into cars values(5,'Mustang','Coupe','Ford','V6','3.2L',10,'40 Dhs')")
        cur.execute("insert into cars values(6,'Mustang GT','Coupe','Ford','Coyote V8','5.0L',10,'45 Dhs')")
        cur.execute("insert into cars values(7,'Mustang GT','Cabriolet','Ford','V6','3.2L',8,'40 Dhs')")
        cur.execute("insert into cars values(8,'Mustang GT (CAB)','Cabriolet','Ford','Coyote V8','5.0L',8,'45 Dhs')")
        cur.execute("insert into cars values(9,'F-150','Pick up','Ford','V6','3.5L',12,'50 Dhs')")
        cur.execute("insert into cars values(10,'F-150 Raptor','Pick up','V6 Turbo','4-Cyl TDI','3.5L',12,'55 Dhs')")
        cur.execute("insert into cars values(11,'Camry','Sedan','Toyota','4-Cyl','1.4L',30,'20 Dhs')")
        cur.execute("insert into cars values(12,'Corolla','Sedan','Toyota','4-Cyl','1.4L',40,'20 Dhs')")
        cur.execute("insert into cars values(13,'Rav-4','CUV','Toyota','6-Cyl','2.5L',35,'25 Dhs')")
        cur.execute("insert into cars values(14,'Civic','Sedan','Honda','4-Cyl','2.0L',50,'20 Dhs')")
        cur.execute("insert into cars values(15,'Accord','Sedan','Honda','4-Cyl','2.0L',50,'20 Dhs')")
        cur.execute("insert into cars values(16,'Sunny','Sedan','Nissan','4-Cyl','1.4L',25,'20 Dhs')")
        cur.execute("insert into cars values(17,'Altima','Sedan','Nissan','4-Cyl','1.4L',20,'20 Dhs')")
        cur.execute("insert into cars values(18,'Patrol','SUV','Nissan','V8','4.5L',30,'40 Dhs')")
        cur.execute("insert into cars values(19,'GT-R','Coupe','Nissan','V6-Twin Turbo','5.2L',5,'100 Dhs')")
        cur.execute("insert into cars values(20,'Juke','CUV','Nissan','4-Cyl','3.0L',35,'30 Dhs')")
        cur.execute("insert into cars values(21,'Malibu','Sedan','Chevrolet','6-Cyl Turbo','2.7L',25,'25 Dhs')")
        cur.execute("insert into cars values(22,'Camaro','Coupe','Chevrolet','6-Cyl','3.8L',10,'40 Dhs')")
        cur.execute("insert into cars values(23,'Camaro SS','Coupe','Chevrolet','V8','4.5L',10,'45 Dhs')")
        cur.execute("insert into cars values(24,'Charger','Saloon','Dodge','V6','4.2L',10,'35 Dhs')")
        cur.execute("insert into cars values(25,'Charger SRT-8','Saloon','Dodge','V8','4.8L',15,'40 Dhs')")
        cur.execute("insert into cars values(26,'Challenger SRT-8','Coupe','Dodge','V8','4.8L',15,'40 Dhs')")
        cur.execute("insert into cars values(27,'ChallengerHellcat','Coupe','Dodge','V8 Supercharged','7.0L',10,'70 Dhs')")
        cur.execute("insert into cars values(28,'Durango','SUV','Dodge','V6','6.5L',20,'40 Dhs')")
        cur.execute("insert into cars values(29,'Grand Cheroke','SUV','Jeep','V8','6.5L',20,'45 Dhs')")
        cur.execute("insert into cars values(30,'CX-3','CUV','Mazda','4-Cyl','3.2L',45,'25 Dhs')")
        cur.execute("insert into cars values(31,'CX-5','SUV','Mazda','4-Cyl','3.2L',45,'25 Dhs')")
        cur.execute("insert into cars values(32,'CX-8','SUV','Mazda','6-Cyl','3.2L',45,'25 Dhs')")
        cur.execute("insert into cars values(33,'Rio','Hatchback','Kia','3-Cyl','1.5L',20,'20 Dhs')")
        cur.execute("insert into cars values(34,'Seoul','Hatchback','Kia','4-Cyl','1.6L',20,'25 Dhs')")
        cur.execute("insert into cars values(35,'Stinger GT','Saloon','Kia','6-Cyl Turbo','3.5L',20,'40 Dhs')")
        cur.execute("insert into cars values(36,'Cayenne','SUV','Porsche','6-Cyl','5.0L',15,'50 Dhs')")
        cur.execute("insert into cars values(37,'Macan','CUV','Porsche','6-Cyl Diesel','2.8L',15,'35 Dhs')")
        cur.execute("insert into cars values(38,'488 GTB','Coupe','Ferrari','V8 Twin Turbo','5.2L',5,'120 Dhs')")
        cur.execute("insert into cars values(39,'Q5','SUV','Audi','V6','4.5L',25,'60 Dhs')")
        cur.execute("insert into cars values(40,'Q7','Coupe','Audi','V8','4.5L',25,'60 Dhs')")
        cur.execute("insert into cars values(41,'RS-4','Hatchback','Audi','V6-Twin Turbo','5.0L',20,'50 Dhs')")
        cur.execute("insert into carsvalues(42,'S6','Saloon','Audi','V6','5.0L',30,'50 Dhs')")
        cur.execute("insert into cars values(43,'S8','Saloon','Audi','W16','6.7L',10,'70 Dhs')")
        cur.execute("insert into cars values(44,'R8-Spyder','Cabriolet','Audi','V8-Turbo','6.0L',5,'100 Dhs')")
        cur.execute("insert into cars values(45,'R8-Sport','Coupe','Audi','V8-Turbo','6.0L',5,'100 Dhs')")
        cur.execute("insert into cars values(46,'520S','Coupe','McLaren','V8-Turbo','5.2L',6,'120 Dhs')")
        cur.execute("insert into cars values(47,'650-LT','Coupe','McLaren','V8-Turbo','6.5L',4,'150 Dhs')")
        cur.execute("insert into cars values(48,'720S','Coupe','McLaren','V8-Turbo','6.5L',5,'175 Dhs')")
        cur.execute("insert into cars values(49,'Urus','SUV','Lamborghini','V8-Supercharged','5.5L',8,'90 Dhs')")
        cur.execute("insert into cars values(50,'Aventador','Coupe','Lamborghini','V12-Twin Turbo','6.4L',2,'200 Dhs')") 
        conobj.commit()
 
        # DRIVER'S TABLE
 
        driver="create table Drivers(SNo INT,Name varchar(30),Age INT,Gender char(1),Car varchar(50),DepartTime time,ArriveTime time,Rent varchar(30))"
        cur.execute(driver)
 
        cur.execute("insert into drivers values(1,'Lewis',36,'M','R8 Spyder','8:30','22:30','1500 Dhs')")
        cur.execute("insert into drivers values(2,'Max',23,'M','GT-R','9:30','19:30','1000 Dhs')")
        cur.execute("insert into drivers values(3,'Daniel',32,'M','650 LT','10:00','23:00','1950 Dhs')")
        cur.execute("insert into drivers values(4,'Esteban',22,'M','Challenger hellcat','9:30','20:30','770 Dhs')")
        conobj.commit()
 
checktable()
 



#Pretty printing the Cars table using the tabulate module

def cars():
    cur.execute("select * from cars")
    cars_data=cur.fetchall()
    print (tabulate(cars_data, headers=["SNo", "Model", "Type", "Brand", "Engine", "Displacement", "Quantity", "PriceHour"]))

#Raw data from the cars table to be used as reference and in functions
def cars_raw():
    cur.execute("select * from cars")
    cars_data=cur.fetchall()
    return cars_data

#Raw data from the drivers table to be used as reference and in functions
def drivers_raw():
    cur.execute("select * from drivers")
    drivers_data=cur.fetchall()
    return drivers_data

#Pretty printing the Drivers table using the tabulate module
def drivers():
    cur.execute("select * from drivers")
    drivers_data=cur.fetchall()
    print (tabulate(drivers_data, headers=["SNo", "Name", "Age", "Gender", "Car", "DepartTime", "ArriveTime", "Rent"]))

#Conversion of 12h time to 24h.
def convert(string):

      if string[-2:] == "AM" and string[:2] == "12":
         return "00" + string[2:-2]

      elif string[-2:] == "AM":
         return string[:-2]

      elif string[-2:] == "PM" and string[:2] == "12":
         return string[:-2]
        
      else:
          return str(int(string[:2]) + 12) + string[2:5]


#month and days dictionary

months={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}

        
#VALIDATIONS

def validation_date():
    n=1
    while n>0:
        
        year=int(input("Enter a year: "))
        month=int(input("Enter a month: "))
        day=int(input("Enter a day: "))
        
        correctDate=None
        try:
            date1=datetime.datetime(year, month, day)
            correctDate=True
        except ValueError:
            correctDate=False
        if correctDate==True:
            n-=1
            return date1
        else:
            print("date not valid, enter year, month, day in the yyyy mm dd format") 
            

                         
def validation_age():
    age=int(input("Enter your age: "))
    
    if age>=18:
        print("You are eligible to rent a car")
        return age
    
    else:
        print("You are NOT eligible to rent a car")


#Q1) Rent

def rentperhour():
    cur.execute("select distinct Model, PriceHour from cars")
    rent_data=cur.fetchall()
    print(tabulate(rent_data, headers=["Model", "PriceHour"]))

#Q2) Query for Name, Age, Gender, Car, Depart-Time, Arrive-Time, Rent

def driverswosno():
    cur.execute("select Name, Gender, Age, Car, DepartTime, ArriveTime, Rent from drivers")
    drivers_data=cur.fetchall()
    print(tabulate(drivers_data, headers=["Name", "Age", "Gender", "Car", "DepartTime", "ArriveTime", "Rent"]))



# Q3) Check for availability of the car for the customers’ choice is available for not
# a)If available write all the details of the car and the driver to the drivers table, then check if the data is added in the database and print the information 

# Date of rent: 16-Jan-2007 
# -------------------------------------------------------------------------------------------------
# Sno   |   Name |    Age   |   Gender |     Car         | DepartTime   | ArriveTime   |  Rent
# -------------------------------------------------------------------------------------------------
# 11    | Adit   |    23    |    M     |  Ford Fiesta    |  (8:30)      |  22:30       |  350dhs
# 12    | Tania  |    25    |    F     | Ford Mustang    |  (10:30)     | 17:30        |  280dhs
# -------------------------------------------------------------------------------------------------


def car_new_rent(brand,model):
    raw1=cars_raw()
    raw2=drivers_raw()
    

    for record in cars_raw():
        if (record[1]!=model and record[3]!=brand):
            print("Not available, try again later\n")
            break
            
        else:
            
            print("Checking for availability.... \n")
            
            if record[6]>0:
                print("The car is available and the details of the car are as follows: \n")

                print(tabulate([record], headers=["SNo", "Model", "Type", "Brand", "Engine", "Displacement", "Quantity", "PriceHour"]))
                print("\n")
          
            
            print("Please fill up the following information: ")
            print("\n")
            
            #date of renting
            print("------------Date of Rent-------------")
            
            date2=validation_date()
            dsplit=str(date2).split('-')
            if dsplit[1] in months:
                fdate=dsplit[2][0:2] + "-" + months[dsplit[1]] + "-" + dsplit[0]
                         
            
            #personal details
            print("------------Personal Details-------------")
            
            name=input("Enter your name: ")
            gender=input("Enter your gender: ")
            fage=validation_age()
            if fage==None:
                break
            
            
            #duration to rent
            print("------------Departure and Arrival time-------------")
            
            depart_time=input("enter time to depart (hh:mm am/pm 12h format): ")
            arrival_time=input("enter time of arrival (hh:mm am/pm 12h format): ")
            dtime=convert(depart_time.upper())
            atime=convert(arrival_time.upper())
            TF="%H:%M"
            duration = datetime.datetime.strptime(atime, TF) - datetime.datetime.strptime(dtime, TF)
            tsplit=str(duration).split(':')
            fduration=tsplit[0] + ":" + tsplit[1]
            
           
            #rental price
            print("------------Daily rental price-------------")
            
            split3=record[-1].split()
            rent_per_hour=int(split3[0])
            print("Rent/hour: ",rent_per_hour)
            duration_of_rent_hours=int(tsplit[0])
            duration_of_rent_minutes=int(tsplit[1])
            print("Duration of rent: ",fduration)
            print("\n")
            total_rental=str(int((rent_per_hour * duration_of_rent_hours) + (rent_per_hour * duration_of_rent_minutes/60))) + " Dhs"
            
            
            #inserting into table 
            prev_record=raw2[-1][0]
            insert_query = "insert into drivers (Sno, Name, Age, Gender, Car, DepartTime, ArriveTime, Rent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            param = (prev_record+1, name, fage, gender, model, dtime, atime, total_rental)
            
            cur.execute(insert_query,param)
            conobj.commit()
            
            #Final output
        
            print("Date of rent: ",fdate)
            print("\n")
            drivers()
            print("\n")
            print("Car rented successfully, thank you for using our services.")
        
          
    else:
        print("Not available, try again later\n")
             

# 5. Display of reservation list for any car in a day in the following format 

# Name of car: Audi R8-Spyder                                                  

# --------------------------------------------------------------------------------------------------------
# Sno |  Name  |   Age  | Gender | DepartTime   | ArriveTime |  Rent 
# --------------------------------------------------------------------------------------------------------
# 2   | Lalit  |    55  |   M    | 8:30         |  13:30     |  500 
# 3   | Priya  |    25  |   F    | 10:30        |  16:30     |  500 
# 4   | Harsh  |    18  |   M    | 14:30        |  18:30     |  500 
# --------------------------------------------------------------------------------------------------------
# Total Reservation : 3
# Total rent : 1700 


def rent_details_specific_car(brand,model):
    raw1=cars_raw()
    raw2=drivers_raw()
    
    for record in cars_raw():
        
        found=0
        if (record[1]==model and record[3]==brand):
            found+=1
            print("Car has been rented previously, following is the information: ")
            
            print("\n Name of car: {} {}".format(brand,model))
            cur.execute("select Sno, Name, Age, Gender, DepartTime, ArriveTime, Rent from drivers where car like 'R8-Spyder'")
            specific_car=cur.fetchall()
            print(tabulate(specific_car, headers=["SNo", "Name", "Age", "Gender", "DepartTime", "ArriveTime", "Rent"]))
            
            total_rent=0
            no_of_reservation=0
            for record_new in specific_car:
                no_of_reservation+=1
                split4=record_new[-1].split()
                rent_each=int(split4[0])
                total_rent+=rent_each
                
            print("Total reservation: ",no_of_reservation)
            print("Total rent: ",total_rent)
            break
            
    if found==0:
        print("Car has not been rented yet, no data available")
            

            
ans="y"
while ans=="y" or ans=="Y":
    
    print("----------------------- MENU -----------------------------")
    print("\n")
    print("Option1: Displaying data of the cars")
    print("Option2: Displaying data of the drivers")
    print("Option3: Displaying the rent price/hour of all the cars")
    print("Option4: Displaying the drivers data except the serial number")
    print("Option5: Accepting customers car choice to rent and displaying the specified data")
    print("Option6: Accepting name of a car and displaying its rent details")
    print("\n")
    option=int(input("enter option to continue with(1,2,3,4,5 or 6): "))
    
    if option==1:
        cars()
    
        
    elif option==2:
        drivers()
        
    elif option==3:
        rentperhour()
    
    elif option==4:
        driverswosno()
    
    elif option==5:
        
        brand=input("enter brand of the car to rent: ")
        model=input("enter model of the car to rent: ")
        
        confirm=input("\n Is this the car you wish to rent: {} {}? (Yes/No)".format(brand,model))
        print("\n")
        
        if confirm.upper()=="YES":
            car_new_rent(brand,model)
        else:
            print("Made a mistake? No problem")
    
    elif option==6:
        
        brand=input("enter brand of the car to check details of: ")
        model=input("enter model of the car to check details of: ")
        
        confirm=input("\nDisplay driver details and rent for this car: {} {}? (Yes/No)".format(brand,model))
        print("\n")
        
        if confirm.upper()=="YES":
            rent_details_specific_car(brand,model)
        else:
            print("Made a mistake? No problem")
        
        
    
    ans=input("Do u wish to continue(y/n)?")
    print("\nThank you for using our services :) ")
    print("\n") 
    


