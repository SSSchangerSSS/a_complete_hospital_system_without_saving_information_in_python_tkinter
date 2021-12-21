

class main():
    def __init__(self):
      self.Patients = []
      self.doctors = []
    def add_doctor(self,new_doctor):
        boolean = False
        for p in self.doctors:
          if p.name == new_doctor.name and p.last_name == new_doctor.last_name:
              boolean = True
        if boolean == False:      
         self.doctors.append(doctor(new_doctor.name,new_doctor.last_name,new_doctor.home_phone_number,new_doctor.mobile_number,new_doctor.address,new_doctor.Expertise))
         return 1#msg : doctor information saved!
        else:
         return 2#msg : doctor information already exists!   
 
    def add_Patient(self,new_Patient):
        boolean = False
        for b in self.Patients:
          if b.name == new_Patient.name and b.last_name == new_Patient.last_name:
              boolean = True
        if boolean == False:     
           self.Patients.append(Patient(new_Patient.name,new_Patient.last_name,new_Patient.mobile_number))
           return 1
        else:
           return 2

    def get_doctor_index(self,name,last_name):
        for i in range(len(self.doctors)):
            if self.doctors[i].name == name and self.doctors[i].last_name == last_name:
                return i


                
    def doctor_exists(self,name,last_name):
        boolean = False
        for x in self.doctors:
            if x.name == name and x.last_name == last_name:
                boolean = True
        return boolean
            
                  
    def get_Patient_index(self,name,last_name):
        for i in range(len(self.Patients)):
            if self.Patients[i].name == name and self.Patients[i].last_name == last_name:
                return i

                
    def Patient_exists(self,name,last_name):
        boolean = False
        for x in self.Patients:
            if x.name == name and x.last_name == last_name:
                boolean = True
        return boolean
        
        
class Patient_msg():        
      def __init__(self,message):  
        self.message = message
        
class Patient_msg_number():        
      def __init__(self,number):  
        self.number = number
                

class doctor_visit():
    
    def __init__(self,day,hour):
     self.day = day
     self.hour = hour
     self.reserved = False

class Patient_visit():
    
    def __init__(self,day,hour,name,last_name):
     self.day = day
     self.hour = hour
     self.name = name
     self.last_name = last_name


class doctor():
    
    def __init__(self,name,last_name,home_phone_number,mobile_number,address,Expertise):
     self.name = name
     self.last_name = last_name
     self.home_phone_number = home_phone_number
     self.mobile_number = mobile_number
     self.address = address
     self.Expertise = Expertise
     self.messages = []
     self.number_of_Patients = 0
     self.all_visiting_times = []
     self.all_visiting_times_that_reserved = []
     
    def insert_visiting_time(self,visiting_time):
         self.all_visiting_times.append(doctor_visit(visiting_time.day,visiting_time.hour))
         
         
    def add_message(self,message):    
         self.messages.append(Patient_msg(message))     

class Patient():
   
    def __init__(self,name,last_name,mobile_number):
     self.name = name
     self.last_name = last_name
     self.mobile_number = mobile_number
     self.all_visiting_times = []
             
    def insert_visiting_time(self,day,hour,name,name_khanevade):
        self.all_visiting_times.append(Patient_visit(day,hour,name,name_khanevade)) 





















import tkinter as tt
from tkinter import messagebox as mb


root = tt.Tk()
root.geometry("400x400")
doctor_ = doctor(None,None,None,None,None,None)
Patient_ = Patient(None,None,None)
MAIN_CONTROLLER = main()
class counter: 
    
    def __init__(self,count):
        self.count = count
        self.b = False
        
    def get_(self):
        return self.count
    
    def up_count(self):
        self.count = self.count + 1
        
    def down_count(self):
        self.count = self.count - 1    
        
    def set_(self,count):
        self.count = count
        
    def can_count(self):
        return self.b    
    
    def set_can(self,b):
        self.b = b

#codes for taking inputs for doctor informations 
text_to_get = tt.StringVar()
canvas = tt.Canvas(root,width = 400 ,height = 300)
entry = tt.Entry(root,textvariable = text_to_get)
entry.focus_set()
canvas.create_window(200,140,window = entry)
counter_ = counter(0)
main_label = tt.Label( root,text = "hospital_management",fg = "pink" , bg = "green" )    



def a():  
    if not(len(entry.get()) == 0) and counter_.can_count() == False :
     save(text_to_get.get())
     if counter_.get_() == 0 :
        doctor_.name = get()
     if counter_.get_() == 1 :    
        doctor_.last_name = get()
     if counter_.get_() == 2 :
        doctor_.home_phone_number = get()
     if counter_.get_() == 3 :
        doctor_.mobile_number = get() 
     if counter_.get_() == 4 :
        doctor_.address = get() 
     if counter_.get_() == 5 :
        doctor_.Expertise = get()
        stop_geting_inputs_for_doctor() 
        return
     counter_.set_can(True)
     entry.delete(0,'end')
     print(get())
     
 
      
def b():
    
    if not(len(entry.get()) == 0) and counter_.can_count() == True :
     counter_.set_can(False)
     if counter_.get_() < 5 :
      counter_.up_count() 
  
        
    
def save(t):
    global s
    s = t
    
def get():
   return s


#codes for taking inputs for Patient informations
text_to_get2 = tt.StringVar()
canvas2 = tt.Canvas(root,width = 400 ,height = 300)
entry2 = tt.Entry(root,textvariable = text_to_get2)
entry2.focus_set()
canvas2.create_window(200,140,window = entry2)
counter2_ = counter(0)

def a2():  
    if not(len(entry2.get()) == 0) and counter2_.can_count() == False :
     save2(text_to_get2.get())
     if counter2_.get_() == 0 :
        Patient_.name = get2()
     if counter2_.get_() == 1 :    
        Patient_.last_name = get2()
     if counter2_.get_() == 2 :
        Patient_.mobile_number = get2() 
        stop_geting_inputs_for_Patient()
        return
     counter2_.set_can(True)
     entry2.delete(0,'end')
     print(get2())
     
def b2():
    
    if not(len(entry2.get()) == 0) and counter2_.can_count() == True :
     counter2_.set_can(False)
     if counter2_.get_() < 2 :
      counter2_.up_count()

         
      
    
def save2(t):
    global s2
    s2 = t
    
def get2():
   return s2



#codes for taking inputs for entring as doctor 
text_to_get3 = tt.StringVar()
canvas3 = tt.Canvas(root,width = 400 ,height = 300)
entry3 = tt.Entry(root,textvariable = text_to_get3)
entry3.focus_set()
canvas3.create_window(200,140,window = entry3)
counter3_ = counter(0)

def a3():  
    if not(len(entry3.get()) == 0) and counter3_.can_count() == False :
     save3(text_to_get3.get())
     if counter3_.get_() == 0 :
        doctor_.name = get3()
     if counter3_.get_() == 1 :    
        doctor_.last_name = get3()
        stop_taking_inputs_entering_as_doctor() 
        return
     counter3_.set_can(True)
     entry3.delete(0,'end')
     print(get3())

def b3():
    
    if not(len(entry3.get()) == 0) and counter3_.can_count() == True :
     counter3_.set_can(False)
     if counter3_.get_() < 1 :
      counter3_.up_count()

                  
      
    
def save3(t):
    global s3
    s3 = t
    
def get3():
   return s3


#codes for taking inputs for entering as Patient
text_to_get4 = tt.StringVar()
canvas4 = tt.Canvas(root,width = 400 ,height = 300)
entry4 = tt.Entry(root,textvariable = text_to_get4)
entry4.focus_set()
canvas4.create_window(200,140,window = entry4)
counter4_ = counter(0)

def a4():  
    if not(len(entry4.get()) == 0) and counter4_.can_count() == False :
     save4(text_to_get4.get())
     if counter4_.get_() == 0 :
        Patient_.name = get4()
     if counter4_.get_() == 1 :    
        Patient_.last_name = get4()
        stop_taking_inputs_entering_as_Patient() 
        return   
     counter4_.set_can(True)
     entry4.delete(0,'end')
     print(get4())


def b4():
    
    if not(len(entry4.get()) == 0) and counter4_.can_count() == True :
     counter4_.set_can(False)
     if counter4_.get_() < 1 :
      counter4_.up_count()

        
      
    
def save4(t):
    global s4
    s4 = t
    
def get4():
   return s4



#codes for inserting visiting time for doctor
text_to_get5 = tt.StringVar()
canvas5 = tt.Canvas(root,width = 400 ,height = 300)
entry5 = tt.Entry(root,textvariable = text_to_get5)
entry5.focus_set()
canvas5.create_window(200,140,window = entry5)
counter5_ = counter(0)
day = tt.Label(root , text = "day")
hour = tt.Label(root , text = "hour")

temp_visiting_time_doctor = []
for i in range(5):
    temp_visiting_time_doctor.append(doctor_visit(None,None))


def a5():  
    if not(len(entry5.get()) == 0) and counter5_.can_count() == False :
     save5(text_to_get5.get())
     
     if counter5_.get_() == 0 :
        temp_visiting_time_doctor[0].day = get5()
     if counter5_.get_() == 1 :    
        temp_visiting_time_doctor[0].hour = get5()
     if counter5_.get_() == 2 :
        temp_visiting_time_doctor[1].day = get5()
     if counter5_.get_() == 3 :
        temp_visiting_time_doctor[1].hour = get5()
     if counter5_.get_() == 4 :
        temp_visiting_time_doctor[2].day = get5()
     if counter5_.get_() == 5 :
        temp_visiting_time_doctor[2].hour = get5()
     if counter5_.get_() == 6 :
        temp_visiting_time_doctor[3].day = get5()
     if counter5_.get_() == 7 :    
        temp_visiting_time_doctor[3].hour = get5()
     if counter5_.get_() == 8 :
        temp_visiting_time_doctor[4].day = get5()
     if counter5_.get_() == 9 :
        temp_visiting_time_doctor[4].hour = get5()
        stop_taking_input_for_visiting_time_doctor()
        return
     counter5_.set_can(True)
     entry5.delete(0,'end')
     print(get5())

def b5():
    
    if not(len(entry5.get()) == 0) and counter5_.can_count() == True :
     counter5_.set_can(False)
     if counter5_.get_() < 9 :
      counter5_.up_count()
      if not(counter5_.get_() % 2 == 0) :
          hour.pack()
          day.forget()
      else:
          hour.forget()
          day.pack()

          
      
    
def save5(t):
    global s5
    s5 = t
    
def get5():
   return s5













#codes for enter a doctor page in Patient_mode 
text_to_get6 = tt.StringVar()
canvas6 = tt.Canvas(root,width = 400 ,height = 300)
entry6 = tt.Entry(root,textvariable = text_to_get6)
entry6.focus_set()
canvas6.create_window(200,140,window = entry6)
counter6_ = counter(0)

def a6():  
    if not(len(entry6.get()) == 0) and counter6_.can_count() == False :
     save6(text_to_get6.get())
     
     if counter6_.get_() == 0 :
        doctor_.name = get6()
     if counter6_.get_() == 1 :    
        doctor_.last_name = get6()
        stop_taking_input_for_enter_a_doctor_page_in_Patient_mode () 
        return
     counter6_.set_can(True)
     entry6.delete(0,'end')
     print(get6())

def b6():
    
    if not(len(entry6.get()) == 0) and counter6_.can_count() == True :
     counter6_.set_can(False)
     if counter6_.get_() < 1 :
      counter6_.up_count()

      
    
def save6(t):
    global s6
    s6 = t
    
def get6():
   return s6









#codes for send message to doctor in Patient_mode
text_to_get7 = tt.StringVar()
canvas7 = tt.Canvas(root,width = 400 ,height = 300)
entry7 = tt.Entry(root,textvariable = text_to_get7)
entry7.focus_set()
canvas7.create_window(200,140,window = entry7)
counter7_ = counter(0)

Patient_message_temp__ = Patient_msg(None)

def a7():  
    if not(len(entry7.get()) == 0) and counter7_.can_count() == False :
     save7(text_to_get7.get())
     
     if counter7_.get_() == 0 :
        Patient_message_temp__.message = get7()
        stop_taking_input_for_send_message_to_doctor_in_Patient_mode()
        return
     counter7_.set_can(True)
     entry7.delete(0,'end')
     print(get7())




def save7(t):
    global s7
    s7 = t
    
def get7():
   return s7






#codes for taking visit_time from a doctor in Patient_mode
text_to_get8 = tt.StringVar()
canvas8 = tt.Canvas(root,width = 400 ,height = 300)
entry8 = tt.Entry(root,textvariable = text_to_get8)
entry8.focus_set()
canvas8.create_window(200,140,window = entry8)
counter8_ = counter(0)
visit_time_from_doctor = doctor_visit(None,None)
def a8():  
    if not(len(entry8.get()) == 0) and counter8_.can_count() == False :
     save8(text_to_get8.get())
     
     if counter8_.get_() == 0 :
        visit_time_from_doctor.day = get8()
     if counter8_.get_() == 1 :    
        visit_time_from_doctor.hour = get8()
        stop_taking_input_for_taking_visit_time_from_a_doctor_in_Patient_mode() 
        return
     counter8_.set_can(True)
     entry8.delete(0,'end')
     print(get8())

def b8():
    
    if not(len(entry8.get()) == 0) and counter8_.can_count() == True :
     counter8_.set_can(False)
     if counter8_.get_() < 1 :
      counter8_.up_count()

      
    
def save8(t):
    global s8
    s8 = t
    
def get8():
   return s8






#codes for Cancel visit_time from a doctor in Patient_mode
text_to_get9 = tt.StringVar()
canvas9 = tt.Canvas(root,width = 400 ,height = 300)
entry9 = tt.Entry(root,textvariable = text_to_get9)
entry9.focus_set()
canvas9.create_window(200,140,window = entry9)
counter9_ = counter(0)
def a9():  
    if not(len(entry9.get()) == 0) and counter9_.can_count() == False :
     save9(text_to_get9.get())
     
     if counter9_.get_() == 0 :
        doctor_.name = get9()
     if counter9_.get_() == 1 :    
        doctor_.last_name = get9()
        stop_taking_input_for_Cancel_visit_time_from_a_doctor_in_Patient_mode() 
        return
     counter9_.set_can(True)
     entry9.delete(0,'end')
     print(get9())

def b9():
    
    if not(len(entry9.get()) == 0) and counter9_.can_count() == True :
     counter9_.set_can(False)
     if counter9_.get_() < 1 :
      counter9_.up_count()

      
    
def save9(t):
    global s9
    s9 = t
    
def get9():
   return s9









#codes to remove msg of Patient in doctor_mode
text_to_get10 = tt.StringVar()
canvas10 = tt.Canvas(root,width = 400 ,height = 300)
entry10 = tt.Entry(root,textvariable = text_to_get10)
entry10.focus_set()
canvas10.create_window(200,140,window = entry10)
counter10_ = counter(0)

Patient_msg_number_to_remove = Patient_msg_number(None)

def a10():  
    if not(len(entry10.get()) == 0) and counter10_.can_count() == False :
     save10(text_to_get10.get())
     
     if counter10_.get_() == 0 :
        Patient_msg_number_to_remove.number = get10()
        stop_taking_input_for_remove_msg_of_Patient_in_doctor_mode()
        return
     counter10_.set_can(True)
     entry10.delete(0,'end')
     print(get10())




def save10(t):
    global s10
    s10 = t
    
def get10():
   return s10











#sign up doctor
next_doctor = tt.Button(text="save",command = a,fg = "blue" , bg = "gray")
save_doctor = tt.Button(text="next",command = b,fg = "blue" , bg = "gray")

#sign up Patient
next_Patient = tt.Button(text="save",command = a2,fg = "blue" , bg = "gray")
save_Patient = tt.Button(text="next",command = b2,fg = "blue" , bg = "gray")

#sign in doctor
next_doctor_exist = tt.Button(text="save",command = a3,fg = "blue" , bg = "gray")
save_doctor_exist = tt.Button(text="next",command = b3,fg = "blue" , bg = "gray")

#sign in Patient
next_Patient_exist = tt.Button(text="save",command = a4,fg = "blue" , bg = "gray")
save_Patient_exist = tt.Button(text="next",command = b4,fg = "blue" , bg = "gray")

#save visiting time for doctor
next_visiting_time = tt.Button(text="save",command = a5,fg = "blue" , bg = "gray")
save_visiting_time = tt.Button(text="next",command = b5,fg = "blue" , bg = "gray")

#search for a doctor in Patient_mode
next_doctor_page = tt.Button(text="save",command = a6,fg = "blue" , bg = "gray")
save_doctor_page = tt.Button(text="next",command = b6,fg = "blue" , bg = "gray")

#send message to a doctor in Patient_mode
save_msg_Patient = tt.Button(text="save",command = a7,fg = "blue" , bg = "gray")


#taking visiting time from a doctor in Patient_mode
next_take_visiting_time = tt.Button(text="save",command = a8,fg = "blue" , bg = "gray")
save_take_visiting_time = tt.Button(text="next",command = b8,fg = "blue" , bg = "gray")


#cancel visiting_time in Patient_mode
next_cancel_visiting_time = tt.Button(text="save",command = a9,fg = "blue" , bg = "gray")
save_cancel_visiting_time = tt.Button(text="next",command = b9,fg = "blue" , bg = "gray")


#delete msg of Patient in doctor_mode
save_deleting_msg_doctor_mode = tt.Button(text="save",command = a10,fg = "blue" , bg = "gray")


def enter_as_doctor():
     forget_main_menu()
     doctor_menu() 
     
     
def enter_as_Patient():
     forget_main_menu()
     Patient_menu()
      
def sign_up_doctor():
     taking_input_for_enter_as_doctor()
     forget_doctor_menu()

def sign_up_Patient():
     taking_input_for_enter_as_Patient()
     forget_Patient_menu()
    
def enter_as_existing_doctor():
     taking_input_for_existing_doctor()
     forget_doctor_menu()

def enter_as_existing_Patient():
     taking_input_for_existing_Patient()
     forget_Patient_menu()
     
def Record_visiting_times():
   forget_doctor_options_menu()
   day.pack()
   taking_inputs_for_Record_visiting_times()
       
   
def show_doctor_visiting_times():
    string = "day\tsaat\twas taken?\n"
    index = MAIN_CONTROLLER.get_doctor_index(doctor_.name,doctor_.last_name)
    for i in MAIN_CONTROLLER.doctors[index].all_visiting_times:
        string += i.day
        string += "\t"
        string += i.hour
        string += "\t"
        if i.reserved == False:
           string += "not reserved"    
        else:
           string += "reserved"   
        string += "\n"  
    mb.showinfo("hospital system message",string) 
    
   
    
def back_from_Patient_to_main_menu():    
    forget_Patient_menu()
    main_menu()
    
def back_from_doctor_to_main_menu():    
    forget_doctor_menu()
    main_menu()    
    
    
    
def back_from_doctor_page_menu_to_Patient_options_menu():
    forget_doctor_page_menu()
    Patient_options_menu()
    
    
def back_from_Patient_options_menu_to_Patient_menu():
   forget_Patient_options_menu()
   Patient_menu()    
    
def  show_how_many_Patient_visited():
    number_of_bimaran = 0
    for p in MAIN_CONTROLLER.doctors:
       for n in p.all_visiting_times:
           if n.reserved == True:
              number_of_bimaran += 1
    string = "number of visited Patients = "
    string += str(number_of_bimaran)
    mb.showinfo("hospital system message",string)
    
    
#main_menu:    
doctor_enter = tt.Button(text = "enter as doctor",command = enter_as_doctor,fg = "blue" , bg = "gray")
Patient_enter = tt.Button(text = "enter as Patient",command = enter_as_Patient,fg = "blue" , bg = "gray")  
number_of_visited_Patients = tt.Button(text = "number of visited Patients",command = show_how_many_Patient_visited,fg = "blue" , bg = "gray") 

#enter doctor menu 
sign_up_doctor = tt.Button(text = "sign up",command = sign_up_doctor,fg = "blue" , bg = "gray")
doctor_enter_exist = tt.Button(text = "sign in",command = enter_as_existing_doctor,fg = "blue" , bg = "gray")
back_from_Patient_menu = tt.Button(text = "back" , command = back_from_Patient_to_main_menu ,fg = "blue" , bg = "gray")

#enter Patient menu
sign_up_Patient = tt.Button(text = "sign up",command = sign_up_Patient,fg = "blue" , bg = "gray") 
Patient_sign_in = tt.Button(text = "sign in",command = enter_as_existing_Patient,fg = "blue" , bg = "gray")  
back_from_doctor_menu = tt.Button(text = "back" , command = back_from_doctor_to_main_menu ,fg = "blue" , bg = "gray")


def enter_doctor_page_in_Patient_mode():
    forget_Patient_options_menu()
    taking_inputs_for_enter_doctor_page_in_Patient_mode()

def send_msg_to_doctor_in_Patient_mode():
    forget_doctor_page_menu()
    taking_inputs_for_send_msg_to_doctor_in_Patient_mode()

def gereftane_nobat():
    _boolean = False
    index2 = MAIN_CONTROLLER.get_Patient_index(Patient_.name,Patient_.last_name)
    for t in MAIN_CONTROLLER.Patients[index2].all_visiting_times:
        if t.name == doctor_.name and t.last_name == doctor_.last_name:   
            _boolean = True
       
    if _boolean == False:
       show_doctor_visiting_times()
       forget_doctor_page_menu()
       taking_inputs_for_taking_visit_time_from_doctor()
    else:
        mb.showinfo("hospital system message","you can not take 2 visiting time from one doctor")


def list_of_Patient_reserved_visit_times():
    string = "day\tsaat\tn_p\tln_p\n"
    index = MAIN_CONTROLLER.get_Patient_index(Patient_.name,Patient_.last_name)
    for i in MAIN_CONTROLLER.Patients[index].all_visiting_times:
        string += i.day
        string += "\t"
        string += i.hour
        string += "\t"
        string += i.name
        string += "\t" 
        string += i.last_name
        string += "\n"  
    mb.showinfo("hospital system message",string) 
    
    
def cancel_visit_time_by_Patient():
    index2 = MAIN_CONTROLLER.get_Patient_index(Patient_.name,Patient_.last_name)
    if len( MAIN_CONTROLLER.Patients[index2].all_visiting_times ) <= 0:
        mb.showinfo("hospital system message","you can not cancel the visit time tha you did not take")
    else:    
       forget_Patient_options_menu()
       taking_inout_for_cancel_visit_time_by_Patient()


     
    
    
    
    
#Patient options menu    
search_for_doctor_page = tt.Button(text = "search for doctor page" , command = enter_doctor_page_in_Patient_mode ,fg = "blue" , bg = "gray")     
list_of_reserved_visit_time_Patient = tt.Button(text = "list of reserved visit time Patient",command = list_of_Patient_reserved_visit_times,fg = "blue" , bg = "gray")
cancel_the_reserved_visit_time = tt.Button(text = "cancel the reserved visit time",command = cancel_visit_time_by_Patient,fg = "blue" , bg = "gray")
back_from_patient_options_to_patient = tt.Button(text = "back" , command = back_from_Patient_options_menu_to_Patient_menu ,fg = "blue" , bg = "gray")



#doctor page
taking_visit_time_from_doctor = tt.Button(text = "taking visit time from doctor",command = gereftane_nobat,fg = "blue" , bg = "gray") 
sending_message_to_doctor = tt.Button(text = "send message to doctor" ,command = send_msg_to_doctor_in_Patient_mode,fg = "blue" , bg = "gray")
back_from_doctor_page_to_patient_options = tt.Button(text = "back" , command = back_from_doctor_page_menu_to_Patient_options_menu ,fg = "blue" , bg = "gray")



def show_doctor_messages_list():
    string = ""
    index = MAIN_CONTROLLER.get_doctor_index(doctor_.name,doctor_.last_name)
    for i in range(len(MAIN_CONTROLLER.doctors[index].messages)):
     string += str(i+1)
     string += ":\t"
     string += MAIN_CONTROLLER.doctors[index].messages[i].message
     string += "\n"
    mb.showinfo("hospital system message",string) 
    
def back_from_doctor_options_menu_to_doctor_menu():
    forget_doctor_options_menu()    
    doctor_menu()
    
    
def pak_kardan_payam_bimar():    
    index = MAIN_CONTROLLER.get_doctor_index(doctor_.name,doctor_.last_name)
    if len(MAIN_CONTROLLER.doctors[index].messages) <= 0 :
        mb.showinfo("hospital system message","you do not have any message")
    else:
        forget_doctor_options_menu() 
        taking_input_for_deleting_message()
    
Record_visiting_times = tt.Button(text = "add visit time", command = Record_visiting_times,fg = "blue" , bg = "gray") 
show_all_available_visiting_times = tt.Button(text = "show all available visit times",command = show_doctor_visiting_times,fg = "blue" , bg = "gray")
doctor_show_messages_list = tt.Button(text = "show messages list" , command = show_doctor_messages_list,fg = "blue" , bg = "gray")
select_and_delete_messages = tt.Button(text = "select and delete messages",command = pak_kardan_payam_bimar,fg = "blue" , bg = "gray")
back_from_doctor_options_to_doctor = tt.Button(text = "back" , command = back_from_doctor_options_menu_to_doctor_menu,fg = "blue" , bg = "gray")

def taking_input_for_enter_as_doctor():
    next_doctor.pack()
    save_doctor.pack()
    canvas.pack()
    entry.pack()

def stop_geting_inputs_for_doctor():
    next_doctor.forget()
    save_doctor.forget()
    canvas.forget()
    entry.forget()
    counter_.set_(0)    
    entry.delete(0,'end')
    message_to_user = MAIN_CONTROLLER.add_doctor(doctor_)
    if (message_to_user == 1):
        mb.showinfo("hospital system message","doctor informations successfully Registered")
    else:
        mb.showinfo("hospital system message","doctor information already exists")
    
    rt = " "
    for p in MAIN_CONTROLLER.doctors:
          rt = " "
          rt += p.name
          rt += p.last_name
          rt += p.home_phone_number
          rt += p.mobile_number
          rt += p.address
          rt += p.Expertise
          print (rt)
    doctor_menu()
    
def taking_input_for_enter_as_Patient():
    next_Patient.pack()
    save_Patient.pack()
    canvas2.pack()
    entry2.pack()
    

def stop_geting_inputs_for_Patient():
    next_Patient.forget()
    save_Patient.forget()
    canvas2.forget()
    entry2.forget()
    counter2_.set_(0)
    entry2.delete(0,'end')
    message_to_user = MAIN_CONTROLLER.add_Patient(Patient_)
    if (message_to_user == 1):
        mb.showinfo("hospital system message","Patient information successfully Registered")
    else:
        mb.showinfo("hospital system message","Patient information already exists")
    
    rt = " "
    for b in MAIN_CONTROLLER.Patients:
          rt = " "
          rt += b.name
          rt += b.last_name
          rt += b.mobile_number
          print (rt)
    Patient_menu()
   



def taking_input_for_existing_doctor():
    next_doctor_exist.pack()
    save_doctor_exist.pack()
    canvas3.pack()
    entry3.pack()

def stop_taking_inputs_entering_as_doctor():
    next_doctor_exist.forget()
    save_doctor_exist.forget()
    canvas3.forget()
    entry3.forget()
    counter3_.set_(0)
    entry3.delete(0,'end')
 
    if MAIN_CONTROLLER.doctor_exists(doctor_.name,doctor_.last_name) == False:
        mb.showinfo("hospital system message","the doctor you are looking for does not exists!")
        doctor_menu()
    else:
        doctor_options_menu()
    
def taking_input_for_existing_Patient():
    next_Patient_exist.pack()
    save_Patient_exist.pack()
    canvas4.pack()
    entry4.pack()
    

def stop_taking_inputs_entering_as_Patient():
    next_Patient_exist.forget()
    save_Patient_exist.forget()
    canvas4.forget()
    entry4.forget()
    counter4_.set_(0)
    entry4.delete(0,'end')

    if MAIN_CONTROLLER.Patient_exists(Patient_.name,Patient_.last_name) == False:
        mb.showinfo("hospital system message","the Patient you are looking for does not exists!")
        Patient_menu()
    else:
        Patient_options_menu()
    


def taking_inputs_for_Record_visiting_times():
    next_visiting_time.pack()
    save_visiting_time.pack()
    canvas5.pack()
    entry5.pack()
    

def stop_taking_input_for_visiting_time_doctor():
    next_visiting_time.forget()
    save_visiting_time.forget()
    canvas5.forget()
    entry5.forget()
    counter5_.set_(0)
    entry5.delete(0,'end')
    day.forget()
    hour.forget()

    index = MAIN_CONTROLLER.get_doctor_index(doctor_.name,doctor_.last_name)
    for t in temp_visiting_time_doctor: 
        MAIN_CONTROLLER.doctors[index].insert_visiting_time(t)
      
    temp_str = " "    
    for h in MAIN_CONTROLLER.doctors[index].all_visiting_times:   
      temp_str += h.day
      temp_str += h.hour
      temp_str += "\n"
      
    print(temp_str)  
        
    doctor_options_menu()
    
    
    
    
    
def taking_inputs_for_enter_doctor_page_in_Patient_mode():
      next_doctor_page.pack()
      save_doctor_page.pack()
      canvas6.pack()
      entry6.pack()
    
    
def stop_taking_input_for_enter_a_doctor_page_in_Patient_mode ():
      next_doctor_page.forget()
      save_doctor_page.forget()
      canvas6.forget()
      entry6.forget()
      counter6_.set_(0)
      entry6.delete(0,'end')
 
      if MAIN_CONTROLLER.doctor_exists(doctor_.name,doctor_.last_name) == False:
          mb.showinfo("text","the doctor you are looking for does not exist!")
          Patient_options_menu()
      else:
          doctor_page_menu()
        
        
        
def taking_inputs_for_send_msg_to_doctor_in_Patient_mode():
      save_msg_Patient.pack()
      canvas7.pack()
      entry7.pack()
    
    
def stop_taking_input_for_send_message_to_doctor_in_Patient_mode():
      save_msg_Patient.forget()
      canvas7.forget()
      entry7.forget()
      counter7_.set_(0)
      entry7.delete(0,'end')
      
      index = MAIN_CONTROLLER.get_doctor_index(doctor_.name,doctor_.last_name)
      MAIN_CONTROLLER.doctors[index].add_message(Patient_message_temp__.message)
      
      doctor_page_menu()
      
        
      
        
def taking_inputs_for_taking_visit_time_from_doctor():
      save_take_visiting_time.pack()
      next_take_visiting_time.pack()
      canvas8.pack()
      entry8.pack()
    
    
def stop_taking_input_for_taking_visit_time_from_a_doctor_in_Patient_mode():
      save_take_visiting_time.forget()
      next_take_visiting_time.forget()
      canvas8.forget()
      entry8.forget()
      counter8_.set_(0)
      entry8.delete(0,'end')
      
      index = MAIN_CONTROLLER.get_doctor_index(doctor_.name,doctor_.last_name)
      
      boolean__ = False
      
      for t in MAIN_CONTROLLER.doctors[index].all_visiting_times:
       if visit_time_from_doctor.day == t.day and visit_time_from_doctor.hour == t.hour and t.reserved == False:
           t.reserved = True
           boolean__ = True
       
      if boolean__ == True:
          mb.showinfo("hospital system message","visiting time reserved")
      else:
          mb.showinfo("hospital system message","you can not reserve this visit time (is reserved)")
          doctor_page_menu()
          return
      
      index2 = MAIN_CONTROLLER.get_Patient_index(Patient_.name,Patient_.last_name)
      MAIN_CONTROLLER.Patients[index2].insert_visiting_time(visit_time_from_doctor.day,visit_time_from_doctor.hour,doctor_.name,doctor_.last_name)
          
      doctor_page_menu()
      
        
        


def taking_inout_for_cancel_visit_time_by_Patient():
      save_cancel_visiting_time.pack()
      next_cancel_visiting_time.pack()
      canvas9.pack()
      entry9.pack()
    
    
def stop_taking_input_for_Cancel_visit_time_from_a_doctor_in_Patient_mode():
      save_cancel_visiting_time.forget()
      next_cancel_visiting_time.forget()
      canvas9.forget()
      entry9.forget()
      counter9_.set_(0)
      entry9.delete(0,'end')    
   
      
      index = MAIN_CONTROLLER.get_doctor_index(doctor_.name,doctor_.last_name)
      index2 = MAIN_CONTROLLER.get_Patient_index(Patient_.name,Patient_.last_name)
      
      _boolean_ = False
      
      
      for s in range(len(MAIN_CONTROLLER.Patients[index2].all_visiting_times)):
          if MAIN_CONTROLLER.Patients[index2].all_visiting_times[s].name == doctor_.name and MAIN_CONTROLLER.Patients[index2].all_visiting_times[s].last_name == doctor_.last_name :
               index3 = s
               rooz___ = MAIN_CONTROLLER.Patients[index2].all_visiting_times[s].day
               saat___ = MAIN_CONTROLLER.Patients[index2].all_visiting_times[s].hour
               _boolean_ = True
               break
      
      if _boolean_ == True:  
        
       for s2 in range(len(MAIN_CONTROLLER.doctors[index].all_visiting_times)):
           if MAIN_CONTROLLER.doctors[index].all_visiting_times[s2].day == rooz___ and MAIN_CONTROLLER.doctors[index].all_visiting_times[s2].hour == saat___ :
                index4 = s2
                break
                   
       MAIN_CONTROLLER.doctors[index].all_visiting_times[index4].reserved = False
       del MAIN_CONTROLLER.Patients[index].all_visiting_times[index3]
       mb.showinfo("hospital system message","visiting time canceled")
      else:
          mb.showinfo("hospital system message","you did not reserved this visiting time")          
          
      Patient_options_menu()
          
    
    
    
    
def taking_input_for_deleting_message():
      save_deleting_msg_doctor_mode.pack()
      canvas10.pack()
      entry10.pack()
    
    
def stop_taking_input_for_remove_msg_of_Patient_in_doctor_mode():
      save_deleting_msg_doctor_mode.forget()
      canvas10.forget()
      entry10.forget()
      counter10_.set_(0)
      entry10.delete(0,'end')
      
      number_of_msg__ = int(Patient_msg_number_to_remove.number)
      number_of_msg__ = number_of_msg__ -1
      index = MAIN_CONTROLLER.get_doctor_index(doctor_.name,doctor_.last_name)
      
      if number_of_msg__ >=0 and number_of_msg__ < len(MAIN_CONTROLLER.doctors[index].messages):
         del MAIN_CONTROLLER.doctors[index].messages[number_of_msg__]
         mb.showinfo("hospital system message","message removed")
      else:   
          mb.showinfo("hospital system message","this number does not point any message")
         
      doctor_options_menu()
      
    
    
    
    
    
    
    
    
    
    

def doctor_options_menu():
    
   Record_visiting_times.pack()
   show_all_available_visiting_times.pack()
   doctor_show_messages_list.pack()
   select_and_delete_messages.pack()
   back_from_doctor_options_to_doctor.pack()

def forget_doctor_options_menu():
    
   Record_visiting_times.forget()
   show_all_available_visiting_times.forget()
   doctor_show_messages_list.forget()
   select_and_delete_messages.forget()
   back_from_doctor_options_to_doctor.forget()

def Patient_options_menu():
    search_for_doctor_page.pack()
    list_of_reserved_visit_time_Patient.pack()
    cancel_the_reserved_visit_time.pack()
    back_from_patient_options_to_patient.pack()
    

def forget_Patient_options_menu():
    search_for_doctor_page.forget()
    list_of_reserved_visit_time_Patient.forget()
    back_from_patient_options_to_patient.forget()
    cancel_the_reserved_visit_time.forget()

def doctor_page_menu():
     taking_visit_time_from_doctor.pack()
     sending_message_to_doctor.pack()
     back_from_doctor_page_to_patient_options.pack()
     
def forget_doctor_page_menu():    
     taking_visit_time_from_doctor.forget()
     sending_message_to_doctor.forget()
     back_from_doctor_page_to_patient_options.forget()
    
    




def main_menu():
    main_label.pack()
    doctor_enter.pack()
    Patient_enter.pack()
    number_of_visited_Patients.pack()

def forget_main_menu():
    doctor_enter.forget()
    Patient_enter.forget()
    main_label.forget()    
    number_of_visited_Patients.forget()


def Patient_menu():
     Patient_sign_in.pack() 
     sign_up_Patient.pack()
     back_from_Patient_menu.pack()

def forget_Patient_menu():
     Patient_sign_in.forget() 
     sign_up_Patient.forget()
     back_from_Patient_menu.forget()

def doctor_menu():
     doctor_enter_exist.pack() 
     sign_up_doctor.pack()
     back_from_doctor_menu.pack()
     

def forget_doctor_menu():
     doctor_enter_exist.forget() 
     sign_up_doctor.forget()
     back_from_doctor_menu.forget()







    
    
main_menu()

root.mainloop()









