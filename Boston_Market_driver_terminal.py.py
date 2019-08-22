# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 08:49:35 2019
Description: This will serve as the input method for Boston Market deliveries
                on the phone; true until GUI is made and accessible.
@author: xXSexybeastXx
"""
test = False

class BM_driver_log(object):
    def __init__(self, start, loc, fee, date):
        self.start_time = start
        self.location = loc
        self.delivery_fee = fee
        self.date_of_delivery = date
        self.end_time = None
    
    def disp_current_info(self):
        print("\t\t\t\t\tCurrent info\n\n\n")
        print("Start time: ", self.start_time)
        print("End time: ", self.end_time)
        print("Location: ", self.location)
        print("Delivery fee: ", self.delivery_fee)
        print("Date: ", self.date_of_delivery)
        
    def read_txt(self):
        with open('BM_data.txt.txt') as driver:
            for line in driver:
                if("None" in line):
                    print(line, end='')
            
#    def write_txt(self):
                    
if(__name__ == '__main__'):
    while(test == False):
        get_start = get_location = get_del_fee = get_date = ""
        
        get_start = input("Enter start time: ")
        get_location = input("Enter location: ")
        get_del_fee = input("Enter delivery fee: ")
        get_date = input("Enter date: ")
        
        if(get_start != "" and get_location != "" and get_del_fee != "" and get_date != ""):
            print("Success!")
            test = True
            
            # Send data to class for start
        else:
            # Re-enter data. Something is missing
            print("Need more info!")
            test = False
    
    
        
# Test data
test = BM_driver_log("11:05", "972 Holt Ave", "$25", "21 Aug 2019")