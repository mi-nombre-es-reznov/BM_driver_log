# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 08:49:35 2019
Description: This will serve as the input method for Boston Market deliveries
                on the phone; true until GUI is made and accessible.
@author: xXSexybeastXx
"""
import time
test = menu_bool = False
get_start = get_location = get_del_fee = get_date = ""
updates_to_file = []


class BM_driver_log(object):
    def __init__(self, start, loc, fee, date):
        self.start_time = start
        self.location = loc
        self.delivery_fee = fee
        self.date_of_delivery = date
        self.end_time = "<Waiting for entry>"
    
    def disp_current_info(self):
        print("\t\t\t\t\tCurrent info\n\n\n")
        print("Start time: ", self.start_time)
        print("End time: ", self.end_time)
        print("Location: ", self.location)
        print("Delivery fee: ", self.delivery_fee)
        print("Date: ", self.date_of_delivery)
            
    def write_txt(self):
        file = open("BM_data.txt.txt", "a")
        
        file.write(self.start_time)
        file.write('\t')
        file.write(self.end_time)
        file.write('\t')
        file.write(self.location)
        file.write('\t')
        file.write(self.delivery_fee)
        file.write('\t')
        file.write(self.date_of_delivery)
        file.write('\n')
        
        print("File written successfully!")
        file.close()
        
def read_txt():
    with open('BM_data.txt.txt') as driver:
        for line in driver:
            print(line, end='')
                
def update_end():
    global count, updates_to_file
    end_time_update = ""
    Flagger = True


    update = open("BM_data.txt.txt", "r")
    
    # Read all lines
    lines = update.readlines()
    
    #Search line-by-line for missing end times
    for i in lines:
        CLS()
        if("<Waiting for entry>" in i):       
            # Go into the second tabbed entry and replace with end time
            Flagger = True
            while Flagger == True:
                print("\t\t\tCurrent Data\n\n", i)            
                j = i.split('\t')   
                end_time_update = input("\n\nPlease enter your end time: ")
                
                if(end_time_update != ""):
                    j[1] = end_time_update
        
                    new_j = ""
                    count = 4
                    
                    for counter in range(len(j)):
                        new_j += j[counter]
        
                        if(count > 0):
                            new_j += '\t'
                            count -= 1
                        
                    # Add data line to list
                    updates_to_file.append(new_j)
                    
                    # Reset string to empty
                    Flagger = False
                else:
                    print("Invalid entry. Please input an end time.")
                    time.sleep(2.5)
                    CLS()
                    Flagger = True
        else:
            updates_to_file.append(i)
        
    # Empty all data from the file
    open('BM_data.txt.txt', 'w').close()
    
    # Push all data to the file as a updated replacement
    with open("BM_data.txt.txt", "w") as replace:
        for i in range(len(updates_to_file)):
            replace.write(updates_to_file[i])
        
        # Clear the list for new data
        updates_to_file.clear()
            
def CLS():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        

if(__name__ == '__main__'):
    count = 0
    while(menu_bool == False):
        # Display menu for current data
        print("\n\n\n\n\n\n\n\nMenu")
        print("1) Add data")
        print("2) Look at current info")
        print("3) Push data to txt file")
        print("4) View data in file")
        print("5) Update end time")
        print("6) Exit Program")
    
        choice = int(input("Choice? "))
        
        if(choice == 1):
            CLS()
            test = False
            while(test == False):

                get_start = input("Enter start time: ")
                
                if(get_start == "null" or get_start == "Null" or get_start == "NULL"):
                    CLS()
                    print("Skipping data entry", end='')
                    time.sleep(1)
                    print(".", end='')
                    time.sleep(1)
                    print(".", end='')
                    time.sleep(1)
                    print(".", end='')
                    time.sleep(1)
                    CLS()
                    
                    # Exit to menu
                    test = True
                else:
                    get_location = input("Enter location: ")
                    get_del_fee = input("Enter delivery fee: ")
                    get_date = input("Enter date: ")
                
                if(get_start == "null" or get_start == "Null" or get_start == "NULL"):
                    test = True
                elif(get_start != "" and get_location != "" and get_del_fee != "" and get_date != ""):
                    test = True       
                    # Send data to class for start
                    push_data = BM_driver_log(get_start, get_location, get_del_fee, get_date)
                    
                    # Clear variable memory
                    get_start = get_location = get_del_fee = get_date = ""
                else:
                    # Re-enter data. Something is missing
                    print("Need more info!")
                    test = False
                    
            # Rerun menu
            menu_bool == False
        elif(choice == 2):
            CLS()
            push_data.disp_current_info()
            time.sleep(5)
            CLS()
            menu_bool = False
        elif(choice == 3):
            CLS()
            push_data.write_txt()
            time.sleep(3)
            CLS()
            menu_bool = False
        elif(choice == 4):
            CLS()
            read_txt()
            time.sleep(10)
            CLS()
            menu_bool = False
        elif(choice == 5):
            update_end()
            menu_bool = False
            CLS()
        elif(choice == 6):
            CLS()
            print("Exiting", end = '')
            time.sleep(1)
            print(".", end = '')
            time.sleep(1)
            print(".", end = '')
            time.sleep(1)
            print(".", end = '')
            time.sleep(1)
            CLS()
            print("Exiting", end = '')
            time.sleep(1)
            print(".", end = '')
            time.sleep(1)
            print(".", end = '')
            time.sleep(1)
            print(".", end = '')
            time.sleep(1)
            CLS()
            menu_bool = True
        else:
            print("Choice is invalid")
            menu_bool = False