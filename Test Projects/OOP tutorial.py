import pandas as pd
import xlsxwriter

barstaff = pd.ExcelFile("C:/Users/Mushroom/python/python/barstaff.xlsx")
security = pd.ExcelFile("C:/Users/Mushroom/python/python/security.xlsx")
guest = pd.ExcelFile("C:/Users/Mushroom/python/python/guestlist.xlsx")
events = pd.ExcelFile("C:/Users/Mushroom/python/python/events.xlsx")


events_data = pd.read_excel(events)
barstaff_data = pd.read_excel(barstaff)
security_data = pd.read_excel(security)
guest_data = pd.read_excel(guest)

all_barstaff = []
all_security = []
all_guests = []

new_events = []

class Event:
    def __init__(self, name, max_guests):
        self.name = name
        self.max_guests = max_guests
        
        self.req_security = max_guests / 2
        self.req_barstaff = max_guests / 3
        
        self.guest_list = []
        self.barstaff_list = []
        self.security_list = []

        self.req_drinks_budget = max_guests * 20
        

    
        
    def add_guest(self, guest):
        
        if len(self.guest_list) < self.max_guests:
            if guest.age > 17:
                self.guest_list.append(guest)
                return True
        else:
            return False
        
    def add_bar(self, staff):
            if len(self.barstaff_list) < self.req_barstaff:
                self.barstaff_list.append(staff)

    def add_secs(self, staff):
        if len(self.security_list) < self.req_security:
            self.security_list.append(staff)
            
    def get_guest_age(self):
        av_age = 0
        for guest in self.guest_list:
            av_age += float(guest.age)
        print(av_age)
        no_guests = len(self.guest_list)
        av_age /= no_guests
        return av_age
        
            
class Guest:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Staff:
    def __init__(self, name, title, wage):
        self.name = name
        self.title = title
        self.wage = wage


    def get_wage(self):
        return self.wage
    
class Barstaff(Staff):
    def __init__(self, name, title, wage, experience):
        super().__init__(name, title, wage)
        self.experience = experience

class Security(Staff):
    def __init__(self, name, title, wage, qualification):
        super().__init__(name, title, wage)
        self.qualification = qualification
        
def get_all_guests():
    for i in guest_data.index:
        name = guest_data.iat[i, 0]
        age = guest_data.iat[i, 1]
        new_guest = Guest(name, age)
        all_guests.append(new_guest)

def get_all_bars():
    for i in barstaff_data.index:
        name = barstaff_data.iat[i, 0]
        title = barstaff_data.iat[i, 1]
        wage = barstaff_data.iat[i, 2]
        experience = barstaff_data.iat[i, 3]

        new_barstaff = Barstaff(name, title, wage, experience)
        all_barstaff.append(new_barstaff)

def get_all_secs():
    for i in security_data.index:
        name = security_data.iat[i, 0]
        title = security_data.iat[i, 1]
        wage = security_data.iat[i, 2]
        qualification = security_data.iat[i, 3]

        new_security = Security(name, title, wage, qualification)
        all_security.append(new_security)


def get_events():
    global no_events
    no_events = 0
    for i in events_data.index:
        no_events += 1
        print(no_events)

def save_events():
    writer = pd.ExcelWriter("Events.xlsx", engine = "xlsxwriter")
    x = 0
    for event in new_events:
        
        event_name = new_events[x].name
        event_guests = new_events[x].max_guests
        event_req_bar = new_events[x].req_barstaff
        event_req_sec = new_events[x].req_security
        event_drinks_budg = new_events[x].req_drinks_budget
        x += 1
        event = pd.DataFrame({event_name: [event_guests, event_req_bar, event_req_sec, event_drinks_budg]})
        event.to_excel("Events.xlsx", sheet_name = "Sheet1", startrow = no_events + 1)
        get_events()
    

get_all_bars()           
        
get_all_guests()

get_all_secs()


def create_event(name, max_guests):
    event = Event(name, max_guests)
    new_events.append(event)
    print("The minimum number of barstaff is %s and the minimum number of security staff is %s" %(event.req_barstaff, event.req_security))
    response = input("Auto fill staff and guests?")
    if response == "Yes":
        for guest in all_guests:
            event.add_guest(guest)
        for bars in all_barstaff:
            event.add_bar(bars)
        for secs in all_security:
            event.add_secs(secs)
    print(len(event.barstaff_list))
    print(len(event.security_list))
    print(len(event.guest_list))
    
    if response == "No":
        print("Please select guests (0-n)")
        print(guest_data)
        while len(event.guest_list) < event.max_guests:
            response = int(input("Please select guests"))
            if all_guests[response] in event.guest_list:
                print("That guest is already attending")
                continue
            else:
                event.guest_list.append(all_guests[response])
                print("%s Has been added to the guestlist"%(all_guests[response].name))
        print("Please select Barstaff")
        print(barstaff_data)
        while len(event.barstaff_list) < event.req_barstaff:
            response = int(input("Please select bartenders (1-n)"))
            if all_barstaff[response] in event.barstaff_list:
                print("That staff member is already recruited")
                continue
            else:
                event.barstaff_list.append(all_barstaff[response])
                print("%s has been added to the barstaff list" % (all_barstaff[response].name))
    exitt = input("Do you want to add another event?")
    if exitt == "Yes":
        pass
    elif exitt == "No":
        get_events()
        save_events()
        print("Events have been saved")
        running = False
    else:
        print("Invalid answer, please reply yes or no")
        pass
"""    
def event_config(event):
    response = input("Auto fill staff and guests?")
    if response == "Yes":
        for guest in all_guests:
            event.add_guest(guest)
            print(len(event.guest_list))
        for bars in all_barstaff:
            event.add_bar(bars)
            print(len(event.staff_list))
        for secs in all_security:
            event.add_secs(secs)
            print(len(event.staff_list))
    print(len(event.staff_list))"""
    
            
running = True
while running:
    create_event(input("What is the name of the event?"), int(input("What's the max guestage?")))
    
                 
    


