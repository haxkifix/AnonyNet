from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import * 
import customtkinter
import open_vpn_call
import emailspoof
from emailspoof import temp

def mainWindow():
    q=customtkinter.CTk(fg_color='#153749')
    # q.geometry('426x250')
    q.title("VPN")
    width_of_window=470
    height_of_window=500

    screen_width=q.winfo_screenwidth()
    screen_height=q.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width_of_window/2)
    y_coordinate=(screen_height/2)-(height_of_window/2)
    q.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))

    lab1 = customtkinter.CTkLabel(master=q,text='AnonyNet',fg_color='#153749',bg_color='white',font=customtkinter.CTkFont('Calibri (body)',30))
    lab1.place(x=180,y=10)
   


    def mail_masking():
        spoofed_name= customtkinter.CTkEntry(q, placeholder_text='Enter Spoofed email',width=200)
        spoofed_name.pack( padx=(20, 0), pady=(50, 0))
        reciver_input= customtkinter.CTkEntry(q, placeholder_text='Enter Reciver email',width=200)
        reciver_input.pack( padx=(20, 0), pady=(10, 0))
        subjet_input= customtkinter.CTkEntry(q, placeholder_text='Enter email subjet',width=400)
        subjet_input.pack( padx=(20, 0), pady=(10, 0))
        lable_input= customtkinter.CTkEntry(q, placeholder_text='Enter email content below',width=170)
        lable_input.pack( padx=(20, 0), pady=(10, 0))
        lable_input.configure(state="disabled")
        content_input= customtkinter.CTkTextbox(q,width=400,height=200,)
        content_input.pack( padx=(20, 0), pady=(10, 0))
            
            
        def butten():
            def butten_push():
                global h
                fake_name = str(spoofed_name.get())
                to_email = str(reciver_input.get())
                subject = str(subjet_input.get())
                content = str(content_input.get('0.0', customtkinter.END))
                emailspoof.spoof_mail(fake_name,to_email,subject,content)
                if(emailspoof.temp==1):
                    h=customtkinter.CTkLabel(master=q,text='Mail sent successfully',fg_color='#153749',bg_color='white')
                    h.pack()
                    emailspoof.temp=0
            global button
            button = customtkinter.CTkButton(q,text="SEND",command=butten_push)
            button.pack( padx=(20, 0), pady=(10, 0))
        butten()

       
                

        

    mail_masking()
    q.mainloop()