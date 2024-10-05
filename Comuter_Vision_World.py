from tkinter import *
from PIL import ImageTk, Image

from Virtual_Whiteboard import *
from Virtual_Volume_Controller import *
from Virtual_Keyboard import *
from Virtual_Finger_Counter import *
from Virtual_Mouse import *
import Virtual_Calculator as Vc

root=Tk()
# root.geometry("1500x780")



#To open geometry in centre
root.title("Computer Vision World")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 1500
window_height = 780
x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

root.state("zoomed")

# To apply background image in geometry
img = Image.open('D:\\BCA\\Semesters\\BCA_Sem_6\\Major project\\Computer-Vision-World\\Images\\bgImg.jpg')
photo = ImageTk.PhotoImage(img)
label = Label(root, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
l1=Label(text="Welcome To The Computer Vision World",font=('Berlin Sans FB Demi', 26),fg="black",bg="cyan")
l1.pack(side=TOP)



# To apply image in mouse button
button1 = Button(root, command=virtualmouse)
img1 = Image.open("D:\\BCA\\Semesters\\BCA_Sem_6\\Major project\\Computer-Vision-World\\Images\\mouse.jpg")
img1 = img1.resize((300, 200), Image.LANCZOS)
img1 = ImageTk.PhotoImage(img1)
button1.config(image=img1)
button1.pack()
button1.place(x=115, y=170)

# To apply image in painter button
button2 = Button(root, command=virtualWhiteboard)
img2 = Image.open("D:\\BCA\\Semesters\\BCA_Sem_6\\Major project\\Computer-Vision-World\\Images\\painter.jpg")
img2 = img2.resize((300, 200), Image.LANCZOS)
img2 = ImageTk.PhotoImage(img2)
button2.config(image=img2)
button2.pack()
button2.place(x=615, y=170)

# To apply image in volume button
button3 = Button(root, command=virtualVolumeController)
img3 = Image.open("D:\\BCA\\Semesters\\BCA_Sem_6\\Major project\\Computer-Vision-World\\Images\\volume.jpg")
img3 = img3.resize((300, 200), Image.LANCZOS)
img3 = ImageTk.PhotoImage(img3)
button3.config(image=img3)
button3.pack()
button3.place(x=1115, y=170)

# To apply image in keyboard button
button4 = Button(root, command=Vc.virtualCalculator)
img4 = Image.open("D:\\BCA\\Semesters\\BCA_Sem_6\\Major project\\Computer-Vision-World\\Images\\calci.jpg")
img4 = img4.resize((300, 200), Image.LANCZOS)
img4 = ImageTk.PhotoImage(img4)
button4.config(image=img4)
button4.pack()
button4.place(x=115, y=470)

# To apply image in finger counter button
button5 = Button(root, command=fingerCounter)
img5 = Image.open("D:\\BCA\\Semesters\\BCA_Sem_6\\Major project\\Computer-Vision-World\\Images\\finger.jpg")
img5 = img5.resize((300, 200), Image.LANCZOS)
img5 = ImageTk.PhotoImage(img5)
button5.config(image=img5)
button5.pack()
button5.place(x=615, y=470)

# To apply image in virtual calculator button
button6 = Button(root, command=virtualKeyboard)
img6 = Image.open("D:\\BCA\\Semesters\\BCA_Sem_6\\Major project\\Computer-Vision-World\\Images\\key.jpg")
img6 = img6.resize((300, 200), Image.LANCZOS)
img6 = ImageTk.PhotoImage(img6)
button6.config(image=img6)
button6.pack()
button6.place(x=1115, y=470)

root.mainloop()