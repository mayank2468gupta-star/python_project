print("============================================================")
print("       SMARTCAMPUS UTILITY & ACCES PASS GENERATOR")
print("============================================================")

User = int(input("Enter Select Category(1:Student , 2:Faculty/Staff): "))

if User==1:
    Student = str(input("enter sub category of student(UG/PG): "))                
    if Student=="UG":                                                               #UG student
        Student_CGPA = float(input("enter UG student CGPA(0.0 - 10.0): ")) 
        Base_Fee = 500         
        if Student_CGPA>=8.5:
            Discount = "20%"
            Merit_Discount = (500*20)/100
        elif Student_CGPA>=7.5:
            Discount = "10%"
            Merit_Discount = (500*10)/100    
        else :
            Discount = "0%"
            Merit_Discount = 0                                                         

        Vehicle = int(input("Select Parking Permits (0:None, 2:Two Wheeler,4:Four Wheeler): "))
        if Vehicle == 2:
            Parking_Fee= 200  
            if User==1:
                peak_surchage = 0   
            else :
                Parking_Fee = 200   
           
        elif Vehicle == 4:
                    Parking_Fee = 600
                    if User==1:
                        peak_surchage = 150     
                    else :
                        peak_surchage = 0
                        
        elif Vehicle == 0:
                Parking_Fee = 0
                if User==1:
                    peak_surchage = 0   
                else :
                    Vehicle == 0
                    Parking_Fee = 0
  
        else :
            print("[ERROR]: ENTER VALID VECHICAL TYPE(0: None, 2: Two-Wheeler, 4: Four-Wheeler )")  
        
                
        unit = float(input("Enter Monthly Electricity Consumption(in kWh) : "))
        print()


        if 100 > unit >= 0:
            bill = (3.00*unit)+50


        elif 300>  unit >= 101:
            bill_1 = (3.00*100)+50
            unit_2=unit-100
            bill = bill_1+(unit_2*5.00)+100

        elif 301< unit <=500 :
            bill_1= (3.00*100)+50
            bill_2 = bill_1+(200*5.00)+100
            unit_3=unit-300
            bill = bill_2+(unit_3*7.50)+150

        elif unit>500 :
            bill_1 = (3.00*100)+50
            bill_2= bill_1+(200*5.00)+100
            bill_3 = bill_2+(200*7.50)+150
            unit_4=unit-500
            bill = bill_3*(unit_4*10.00)+250
             

        else :
            print("[ERROR] Enter invalid units (Positive Integer)")           

                 
    else :
        Student_CGPA = float(input("enter PG student CGPA(0.0 - 10.0): "))            #PG student
        Base_Fee = 350         
        if Student_CGPA>=8.5:
            Discount = "20%"
            Merit_Discount = (350*20)/100
        elif Student_CGPA>=7.5:
            Discount = "10%"
            Merit_Discount = (350*10)/100    
        else :
            print("Less CGPA") 
            Discount = "0%"
            Merit_Discount = 0

        
        Vehicle = int(input("Select Parking Permits (0:None, 2:Two Wheeler,4:Four Wheeler): "))
        if Vehicle == 2:
            Parking_Fee= 200  
            if User==1:
                peak_surchage = 150     
            elif Vehicle == 0:
                Parking_Fee = 0
            else :
                print("[ERROR]: ENTER VALID VECHICAL TYPE(0: None, 2: Two-Wheeler, 4: Four-Wheeler )")      
        elif Vehicle == 4:
            Parking_Fee = 600
            if User==1:
                peak_surchage = 150     
            elif Vehicle == 0:
                Parking_Fee = 0
            else :
                print("[ERROR]: ENTER VALID VECHICAL TYPE(0: None, 2: Two-Wheeler, 4: Four-Wheeler )")    
        elif Vehicle == 0:
            Parking_Fee = 0
            if User==1:
               peak_surchage = 0   
            else :
                Vehicle == 0
                Parking_Fee = 0
          
        else :
            print("[ERROR]: ENTER VALID VECHICAL TYPE(0: None, 2: Two-Wheeler, 4: Four-Wheeler )")  
                
                        
        unit = float(input("Enter Monthly Electricity Consumption(in kWh) : "))
        print()
        
        
        if 100 > unit >= 0:
            bill = (3.00*unit)+50
        
        
        elif 300>  unit >= 101:
            bill_1 = (3.00*100)+50
            unit_2=unit-100
            bill = bill_1+(unit_2*5.00)+100
        
        elif 301< unit <=500 :
            bill_1= (3.00*100)+50
            bill_2 = bill_1+(200*5.00)+100
            unit_3=unit-300
            bill = bill_2+(unit_3*7.50)+150
        
        elif unit>500 :
            bill_1 = (3.00*100)+50
            bill_2= bill_1+(200*5.00)+100
            bill_3 = bill_2+(200*7.50)+150
            unit_4=unit-500
            bill = bill_3*(unit_4*10.00)+250
            
                
        
        else :
            print("[ERROR] Enter invalid units (Positive Integer)")       

else :
    Faculty = str(input("enter sub category of faculty (Resident Faculty, Visiting Faculty): "))                             # Faculty
    if Faculty=="Resident Faculty":                                                                                     #Resident Faculty
        
        Years_of_service = int(input("enter Faculty years of service: "))
        Base_Fee = 800
        if Years_of_service>10:
            Discount="15%"
            Merit_Discount = (800*15)/100
        else:
            Discount = "0%"
            Merit_Discount = 0   
        Vehicle = int(input("Select Parking Permits (0:None, 2:Two Wheeler,4:Four Wheeler): "))
        if Vehicle == 2:
            Parking_Fee= 200  
            peak_surcharge = 0      
        elif Vehicle == 4:
            Parking_Fee = 600
            peak_surchage = 0   
        elif Vehicle == 0:
            Parking_Fee = 0
            peak_surchage = 0   

                  
        else :
            print("[ERROR]: ENTER VALID VECHICAL TYPE(0: None, 2: Two-Wheeler, 4: Four-Wheeler )")  
                        
                                
        unit = float(input("Enter Monthly Electricity Consumption(in kWh) : "))
        print()
                
                
        if 100 > unit >= 0:
            bill = (3.00*unit)+50
                
                
        elif 300>  unit >= 101:
            bill_1 = (3.00*100)+50
            unit_2=unit-100
            bill = bill_1+(unit_2*5.00)+100
                
        elif 301< unit <=500 :
            bill_1= (3.00*100)+50
            bill_2 = bill_1+(200*5.00)+100
            unit_3=unit-300
            bill = bill_2+(unit_3*7.50)+150
                
        elif unit>500 :
            bill_1 = (3.00*100)+50
            bill_2= bill_1+(200*5.00)+100
            bill_3 = bill_2+(200*7.50)+150
            unit_4=unit-500
            bill = bill_3*(unit_4*10.00)+250
                
        else :
            print("[ERROR] Enter invalid units (Positive Integer)")       
        
    else :                                                               #Visiting Faculty
        Years_of_service = int(input("enter Faculty years of service: "))
        Base_Fee = 1200
        if Years_of_service>10:
            Discount="15%"
            Merit_Discount = (1200*15)/100
        else :
            print("No Discount")   
            Discount = 0 
            Merit_Discount = 0        
        Vehicle = int(input("Select Parking Permits (0:None, 2:Two Wheeler,4:Four Wheeler): "))
        if Vehicle == 2:
            Parking_Fee= 200  
            peak_surchage = 0
                     
        elif Vehicle == 4:
                    Parking_Fee = 600
                    peak_surchage = 0  
        elif Vehicle == 0:
                    Parking_Fee = 0
                    peak_surchage = 0
        else :
                    print("[ERROR]: ENTER VALID VECHICAL TYPE(0: None, 2: Two-Wheeler, 4: Four-Wheeler )")  
                                
                                        
        unit = float(input("Enter Monthly Electricity Consumption(in kWh) : "))
        print()
                        
                        
        if 100 > unit >= 0:
            bill = (3.00*unit)+50
                        
                        
        elif 300>  unit >= 101:
            bill_1 = (3.00*100)+50
            unit_2=unit-100
            bill = bill_1+(unit_2*5.00)+100
                        
        elif 301< unit <=500 :
            bill_1= (3.00*100)+50
            bill_2 = bill_1+(200*5.00)+100
            unit_3=unit-300
            bill = bill_2+(unit_3*7.50)+150
                        
        elif unit>500 :
            bill_1 = (3.00*100)+50
            bill_2= bill_1+(200*5.00)+100
            bill_3 = bill_2+(200*7.50)+150
            unit_4=unit-500
            bill = bill_3*(unit_4*10.00)+250
                        
        else :
            print("[ERROR] Enter invalid units (Positive Integer)")           

        
        
print("---------------------------------------------------")
print("          CALCULATED INVOICE BREAKDOWN")
print("---------------------------------------------------") 
print()
print("Base Access Pass Fee  : {}".format(Base_Fee))
print("Merit Discount({}): {}".format(Discount,Merit_Discount))

if  Vehicle == 0:
    print("Parking Fee (none)      :₹",Parking_Fee)
elif Vehicle == 2:
    print("Parking Fee (2-wheeler) :₹",Parking_Fee)
elif Vehicle == 4:
    print("Parking Fee (4-wheeler) :₹",Parking_Fee)
else :
    print("[ERROR]")


if User == 1:
    print("Student Peak Surcharge  :₹",peak_surchage)
else:
    print("Faculty Peak Surcharge  :₹ 00.00")

net_pass = Base_Fee - Merit_Discount + Parking_Fee + peak_surchage

 
print("Net Pass & Parking Total            :₹", net_pass)   

print("-------------------------------------------------")
print()
print(f"Electricity Bill {unit} kwh:₹ {bill}")
print()
print("--------------------------------------------------")
print()
Total =  net_pass + bill
print("TOTAL MONTHLY PAYABLE    :₹",Total)

print("========================================================")

exit()


        



