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
per_total = grand_total = 0.0
count = 0

########################################
# BM_driver_log class for data entrance
########################################
class BM_driver_log(object):
    def __init__(self, start, loc, fee, date, payper):
        self.start_time = start
        self.location = loc
        self.delivery_fee = fee
        self.date_of_delivery = date
        self.end_time = "<Waiting for entry>"
        self.pay_period = payper
    
    def disp_current_info(self):
        print("\t\t\t\t\tCurrent info\n\n\n")
        print("Start time: ", self.start_time)
        print("End time: ", self.end_time)
        print("Location: ", self.location)
        print("Delivery fee: ", self.delivery_fee)
        print("Date: ", self.date_of_delivery)
        print("Pay Period: ", self.pay_period)
            
    def write_txt(self):
        file = open("BM_data.txt.txt", "a")
        
        # Push line of data into file in this format (append)
        file.write(self.start_time)
        file.write('\t')
        file.write(self.end_time)
        file.write('\t')
        file.write(self.location)
        file.write('\t')
        file.write(self.delivery_fee)
        file.write('\t')
        file.write(self.date_of_delivery)
        file.write('\t')
        file.write(self.pay_period)
        file.write('\n')
        
        print("File written successfully!")
        file.close()
    
#############################################
# Read and print all data from the txt file
#############################################
def read_txt():
    print("Start \tEnd \tAddress \tDelivery fee \tDate \tPay Period\n") # Added a legend for the user. Displays what each data piece is in file.
    
    with open('BM_data.txt.txt') as driver:
        for line in driver:
            print(line, end='')
   
##########################################
# Finds and updates any missing end times
##########################################             
def update_end():
    global count, updates_to_file
    end_time_update = ""
    Flagger = True
    have_update = False


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
        
                    # Initialize/Reset values for next file line
                    new_j = ""
                    count = 5
                    
                    # Push new data into file and seperate each piece by placing a tab as before
                    for counter in range(len(j)):
                        new_j += j[counter]
        
                        if(count > 0):
                            new_j += '\t'
                            count -= 1
                        
                    # Add data line to list
                    updates_to_file.append(new_j)
                    
                    # Reset string to empty
                    Flagger = False
                    have_update = True
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
        
    # Check to see if there are any records that need end times
    if(have_update == False):
        CLS()
        print("All data points have end times!!!")
        time.sleep(3)
        CLS()
        
##################################
# Calculate pay periods from file
##################################
def calc_pay_periods():
    # Variables used in function
    global per_total, count, grand_total
    minutes = hrs = ind_total = del_fee_price = 0.0
    ready = exists = False
    
    # Clear screen and open file
    CLS()
    which_period = input("Which pay period would you like to calculate? ")
    calculate = open("BM_data.txt.txt", "r")
    
    # Read all lines
    lines = calculate.readlines()
    
    #Search line-by-line for missing end times
    for i in lines:
        CLS()
        ind_data = i.split('\t') # Split data into seperate points by tabs to grab what I need for calculations
        if("<Waiting for entry>" not in i):            
            # Get start and end times
            end = ind_data[1]
            start = ind_data[0]
            
            # Find range
            ind_range = (int(end) - int(start))
            
            # Convert data points to int, then determine if entered value matches stored value in file. Yes = calculate; No = Skip
            if(int(ind_data[5]) == int(which_period)):
                count += 1
                while(ready == False):
                    if(ind_range >= 100):
                        ind_range -= 100
                        hrs += 1
                    else:
                        minutes = (ind_range / 60)
                        ready = True
                
                
                # Add data together for a sub-total
                ind_total = (hrs + minutes)
                del_fee_price += float(ind_data[3])
                exists = True
                
            # Reset all values
            hrs = 0
            minutes = 0.0
            ready = False
        
        elif(("<Waiting for entry>" in i) and (int(ind_data[5]) == int(which_period))):
            print("Data entry skipped due to no end time!")
            print(i)
            time.sleep(2)
            exists = True
                        
        # Add pay period totals
        per_total += ind_total
        
        # Reset individual total for no summed values
        ind_total = 0.0

    # Display period total
    CLS()
    if(exists == True):    
        per_total = round(per_total, 2)
        if(per_total > 0):
            # Calculate final pay
            base_pay = float(input("Enter your hourly rate: "))
            grand_total = ((base_pay * per_total) + del_fee_price)
            
            # Check if grand total ends in $x.00. If so, append a 0 to a string
            check_gt = (grand_total - int(grand_total))
            
            if(check_gt != 0):
                CLS()
                if(count == 1):
                    print("Pay Period (", which_period, ") total with", count, "entry: $", grand_total)
                else:
                    print("Pay Period (", which_period, ") total with", count, "entries: $", grand_total)
            else:
                CLS()
                concate_grand_total = str(grand_total) + "0"
                if(count == 1):
                    print("Pay Period (", which_period, ") total with", count, "entry: $", concate_grand_total)
                else:
                    print("Pay Period (", which_period, ") total with", count, "entries: $", concate_grand_total)                

            time.sleep(3)
        else:
            print("Pay Period total: $0.00")
            time.sleep(3)
    else:
        print("Pay period (", which_period, ") does not contain any data!")
        time.sleep(3)
        
    # Reset the period tatal to avoid summed values
    per_total = 0.0
    grand_total = 0.0
    count = 0
    
######################################
# Calculate total earnings from file
######################################
def calc_total():
    # Variables used in function
    global per_total, count, grand_total
    minutes = hrs = ind_total = del_fee_price = 0.0
    ready = exists = False
    
    # Clear screen and open file
    CLS()
    calculate = open("BM_data.txt.txt", "r")
    
    # Read all lines
    lines = calculate.readlines()
    
    #Search line-by-line for missing end times
    for i in lines:
        CLS()
        ind_data = i.split('\t') # Split data into seperate points by tabs to grab what I need for calculations
        if("<Waiting for entry>" not in i):            
            # Get start and end times
            end = ind_data[1]
            start = ind_data[0]
            
            # Find range
            ind_range = (int(end) - int(start))
            
            # Convert data points to int, then determine if entered value matches stored value in file. Yes = calculate; No = Skip
            if("<Waiting for entry>" not in i):
                count += 1
                while(ready == False):
                    if(ind_range >= 100):
                        ind_range -= 100
                        hrs += 1
                    else:
                        minutes = (ind_range / 60)
                        ready = True
                
                
                # Add data together for a sub-total
                ind_total = (hrs + minutes)
                del_fee_price += float(ind_data[3])
                exists = True
                
            # Reset all values
            hrs = 0
            minutes = 0.0
            ready = False
        else:
            print("Data entry skipped due to no end time!")
            print(i)
            time.sleep(2)
            exists = True
                        
        # Add pay period totals
        per_total += ind_total
        
        # Reset individual total for no summed values
        ind_total = 0.0

    # Display period total
    CLS()
    if(exists == True):    
        per_total = round(per_total, 2)
        if(per_total > 0):
            # Calculate final pay
            base_pay = float(input("Enter your hourly rate: "))
            grand_total = ((base_pay * per_total) + del_fee_price)
            
            # Check if grand total ends in $x.00. If so, append a 0 to a string
            check_gt = (grand_total - int(grand_total))
            
            if(check_gt != 0):
                CLS()
                if(count == 1):
                    print("Your grand total with", count, "entry: $", grand_total)
                else:
                    print("Your grand total with", count, "entries: $", grand_total)
            else:
                CLS()
                concate_grand_total = str(grand_total) + "0"
                if(count == 1):
                    print("Your grand total with", count, "entry: $", concate_grand_total)
                else:
                    print("Your grand total with", count, "entries: $", concate_grand_total)

            time.sleep(3)
    else:
        print("Grand total: $0.00")
        time.sleep(3)
        
    # Reset the period tatal to avoid summed values
    per_total = 0.0
    grand_total = 0.0
    count = 0
            
#################################
# Create a clear screen illusion
#################################
def CLS():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
#################################
# Main entry point into program
#################################
if(__name__ == '__main__'):
    count = 0
    while(menu_bool == False):
        # Display menu for current data
        CLS()
        print("*********************")
        print("        Menu")
        print("*********************")
        print("\n1) Add data")
        print("2) Look at current info")
        print("3) Push data to txt file")
        print("4) View data in file")
        print("5) Update end time")
        print("6) Calculate pay period")
        print("7) Calculate total")
        print("8) Exit Program")
    
        choice = int(input("Choice? "))
        
        # if-else through menu options
        if(choice == 1):
            CLS()
            test = False
            while(test == False):

                get_start = input("Enter start time [null to terminate]: ")
                
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
                    
                    # Add pay period for calculations of seperate deliveries
                    get_pay_period = input("Enter pay period number: ")
                
                if(get_start == "null" or get_start == "Null" or get_start == "NULL"):
                    test = True
                elif(get_start != "" and get_location != "" and get_del_fee != "" and get_date != "" and get_pay_period != ""):
                    test = True       
                    # Send data to class for start
                    push_data = BM_driver_log(get_start, get_location, get_del_fee, get_date, get_pay_period)
                    
                    # Clear variable memory
                    get_start = get_location = get_del_fee = get_date = get_pay_period = ""
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
            calc_pay_periods()
            time.sleep(2)
            CLS()
        elif(choice == 7):
            CLS()
            calc_total()
            time.sleep(2)
            CLS()
        elif(choice == 8):
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