import socket
import pickle
from tkinter import *

def send(list_of_absentees):
    # Sending the attendance data to the server
    data = pickle.dumps(list_of_absentees)
    client_socket.send(data)

    # Receiving the server's response
    response = client_socket.recv(1024)

    print(response.decode()) # Printing the response

    client_socket.close()    # Closing the socket

def submit():
    list_of_absentees = ["p", "p", "p","p","p"]
    for i in range(5):
        if checkbox_variables[i].get() == 1:
            list_of_absentees[i] = "a"
    send(list_of_absentees)
    root.destroy()

# Creating the socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Getting local machine name and port number
host = "127.0.0.1"
port = 9999

# Connecting to the server
client_socket.connect((host, port))

# Receiving the srn's and unpickling it
data = client_socket.recv(1024)
data = pickle.loads(data)
#gui part
root = Tk()
root.title("Attendance")
root.geometry("300x500")

l1 = Label(root, text="SRN")
l2 = Label(root, text="Absentees")
l1.grid(row=0, column=0)
l2.grid(row=0, column=1)

a = IntVar()
b = IntVar()
c = IntVar()
d = IntVar()
e = IntVar()

checkbox_variables = [a,b,c,d,e]

cb1 = Checkbutton(root, variable=checkbox_variables[0], onvalue=1, offvalue=0)
cb2 = Checkbutton(root, variable=checkbox_variables[1], onvalue=1, offvalue=0)
cb3 = Checkbutton(root, variable=checkbox_variables[2], onvalue=1, offvalue=0)
cb4 = Checkbutton(root, variable=checkbox_variables[3], onvalue=1, offvalue=0)
cb5 = Checkbutton(root, variable=checkbox_variables[4], onvalue=1, offvalue=0)
cb1.grid(row=1, column=1)
cb2.grid(row=2, column=1)
cb3.grid(row=3, column=1)
cb4.grid(row=4, column=1)
cb5.grid(row=5, column=1)

srn1 = Label(root, text=data[0])
srn2 = Label(root, text=data[1])
srn3 = Label(root, text=data[2])
srn4 = Label(root, text=data[3])
srn5 = Label(root, text=data[4])

srn1.grid(row=1, column=0)
srn2.grid(row=2, column=0)
srn3.grid(row=3, column=0)
srn4.grid(row=4, column=0)
srn5.grid(row=5, column=0)

but = Button(root, text="Submit", command=submit, font=("Helvetica", 12))
but.grid(row=6, rowspan=3, column=0, columnspan=2,pady=20)

mainloop()
