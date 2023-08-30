from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import * 
import customtkinter
import open_vpn_call
import emailspoof
from emailspoof import temp
import emailimpersonaitonwindow




def mainWindow():
    q=customtkinter.CTk(fg_color='#153749')
    # q.geometry('426x250')
    q.title("VPN")
    width_of_window=427
    height_of_window=250
    screen_width=q.winfo_screenwidth()
    screen_height=q.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width_of_window/2)
    y_coordinate=(screen_height/2)-(height_of_window/2)
    q.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))
    


    lab1 = customtkinter.CTkLabel(master=q,text='AnonyNet',fg_color='#153749',bg_color='white',font=customtkinter.CTkFont('Calibri (body)',30))
    lab1.pack()
    lab1.place(x=140,y=30)

    def vpn_on():
        open_vpn_call.open_openvpn_connect()
            

    button1 = customtkinter.CTkButton(q,text="Enable VPN",hover_color="green",command=vpn_on)
    button1.pack()
    button1.place(x=60,y=120)

    def emailscreen():
        emailimpersonaitonwindow.mainWindow()

    button2 = customtkinter.CTkButton(q,text="Email impersonation",hover_color="green",command=emailscreen)
    button2.pack()
    button2.place(x=230,y=120)

    

    q.mainloop()