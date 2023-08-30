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
    width_of_window=550
    height_of_window=600
    screen_width=q.winfo_screenwidth()
    screen_height=q.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width_of_window/2)
    y_coordinate=(screen_height/2)-(height_of_window/2)
    q.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))


    lab1 = customtkinter.CTkLabel(master=q,text='Welcome',fg_color='#153749',bg_color='white',font=customtkinter.CTkFont('Calibri (body)',30))
    lab1.pack()
    lab2 = customtkinter.CTkLabel(master=q,text='TO',fg_color='#153749',bg_color='white',font=customtkinter.CTkFont('Calibri (body)',20))
    lab2.pack()
    lab3 = customtkinter.CTkLabel(master=q,text='Modern VPN',fg_color='#153749',bg_color='white',font=customtkinter.CTkFont('Calibri (body)',20))
    lab3.pack()
    
    def vpn_call():
        def vpn_on():
            open_vpn_call.open_openvpn_connect()
            
            

        button1 = customtkinter.CTkButton(q,text="Connect to VPN",hover_color="green",command=vpn_on)
        button1.pack()


    def mail_masking():
        def call_spoofing():
            curent_switch_value = "on"
            if (curent_switch_value=='on'):
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

                def update():
                    spoofed_name.pack_forget()
                    reciver_input.pack_forget()
                    subjet_input.pack_forget()
                    lable_input.pack_forget()
                    content_input.pack_forget()
                    button.pack_forget()
                    switch1.configure(command=call_spoofing)
                    h.pack_forget()
                switch1.configure(command=update)
                

        switch1 = customtkinter.CTkSwitch(q,text=None,fg_color='red',progress_color='#90EE90',command=call_spoofing,onvalue="on",offvalue="off")
        switch1.pack()
        switch1.place(x=410,y=130)
        lab5 = customtkinter.CTkLabel(master=q,text='Switch on to enable email spoofing ',fg_color='#153749',bg_color='white',font=customtkinter.CTkFont('Calibri (body)',15))
        lab5.pack()
        lab5.place(x=180,y=130)
        

    vpn_call()
    mail_masking()
    q.mainloop()