import sys
from tkinter import *
from PIL import ImageTk, Image 
from Arena import *
from TkinterDnD2 import *

root = Tk(className="GUI")
root.title("GUI")
root.geometry('1200x805')
root.resizable(False, False)
root.configure(bg='#ffffff')

Obstacle_left_img  = Image.open("GUI_Images/Obstacle_Left.png")
Obstacle_left_img  = Obstacle_left_img.convert('RGBA')
Obstacle_left_img  = Obstacle_left_img.resize((40,40), Image.ANTIALIAS)
Obstacle_left_img  = ImageTk.PhotoImage(Obstacle_left_img)

Obstacle_right_img = Image.open("GUI_Images/Obstacle_Right.png")
Obstacle_right_img = Obstacle_right_img.convert('RGBA')
Obstacle_right_img = Obstacle_right_img.resize((40,40), Image.ANTIALIAS)
Obstacle_right_img = ImageTk.PhotoImage(Obstacle_right_img)

Obstacle_up_img    = Image.open("GUI_Images/Obstacle_Up.png")
Obstacle_up_img    = Obstacle_up_img.convert('RGBA')
Obstacle_up_img    = Obstacle_up_img.resize((40,40), Image.ANTIALIAS)
Obstacle_up_img    = ImageTk.PhotoImage(Obstacle_up_img)

Obstacle_down_img  = Image.open("GUI_Images/Obstacle_Down.png")
Obstacle_down_img  = Obstacle_down_img.convert('RGBA')
Obstacle_down_img  = Obstacle_down_img.resize((40,40), Image.ANTIALIAS)
Obstacle_down_img  = ImageTk.PhotoImage(Obstacle_down_img)

class Obstacle():
    x_coordinate = None
    y_coordinate = None
    def __init__(self):
        pass

    def change_orientation(self):
        pass
        # self.img = Image.ROTATE_90
    
    def get_Obstacle_Type(self):
        return self.Obstacle_Type

    def set_Obstacle_Type(self, direction):
        self.Obstacle_Type = direction

    # def Obstacle_type(self, direction):
    #     self.direction = direction
    #     if self.direction == 'Left':
    #         img = Image.open("GUI_Images/Obstacle_Left.png")
    #         img = img.convert('RGBA')
    #         img = img.resize((40,40), Image.ANTIALIAS)
    #         return ImageTk.PhotoImage(img)
    #     elif self.direction == 'Right':
    #         img = Image.open("GUI_Images/Obstacle_Right.png")
    #         img = img.convert('RGBA')
    #         img = img.resize((40,40), Image.ANTIALIAS)
    #         return ImageTk.PhotoImage(img)
    #     elif self.direction == 'Up':
    #         img = Image.open("GUI_Images/Obstacle_Up.png")
    #         img = img.convert('RGBA')
    #         img = img.resize((40,40), Image.ANTIALIAS)
    #         return ImageTk.PhotoImage(img)
    #     elif self.direction == 'Down':
    #         img = Image.open("GUI_Images/Obstacle_Down.png")
    #         img = img.convert('RGBA')
    #         img = img.resize((40,40), Image.ANTIALIAS)
    #         return ImageTk.PhotoImage(img)
    #     else:
    #         pass


class Car():
    img = Image.open("GUI_Images/Car.png")
    img = img.convert('RGBA')
    img = img.resize((120,120), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

class Arena():
    pass





if __name__ == '__main__':
    Arena_img = get_img()
    Arena_img = ImageTk.PhotoImage(Arena_img)

    canvas = Canvas(width = 800, height = 800, borderwidth = 0, bg = 'white')
    canvas.grid(row=0)
    canvas.create_image(0,0, image=Arena_img, anchor=NW)

    # button_Obstacle = Button(root, height = 3, width = 30, bg = '#F0F8FF', text="Insert Obstacle")
    # button_Obstacle.place(x=810, y=5)

    # box1 = Obstacle()
    # box1.set_Obstacle_Type('Left')
    # print(box1.get_Obstacle_Type())
    # box1.img = box1.Obstacle_type(box1.get_Obstacle_Type())
    # box1 = Button(root, borderwidth=0, image = box1.img)
    # box1.place(x=500,y=500)

    point_of_reference = Button(root, borderwidth=0, height=0, width=0)
    point_of_reference.place(x=0,y=800)

    car = Car()
    car1 = Button(root, borderwidth=0, image = car.img)
    car1.place(x=20, y=660)

    box1 = Obstacle()
    box1_img = Obstacle_left_img
    box1 = Button(root, borderwidth=0, image = box1_img)
    box1.place(x=660, y=660)

    box2 = Obstacle()
    box2_img = Obstacle_right_img
    box2 = Button(root, borderwidth=0, image = box2_img)
    box2.place(x=500, y=500)

    box3 = Obstacle()
    box3_img = Obstacle_left_img
    box3 = Button(root, borderwidth=0, image = box3_img)
    box3.place(x=520, y=160)

    box4 = Obstacle()
    box4_img = Obstacle_down_img
    box4 = Button(root, borderwidth=0, image = box4_img)
    box4.place(x=40, y=400)

    box5 = Obstacle()
    box5_img = Obstacle_down_img
    box5 = Button(root, borderwidth=0, image = box5_img)
    box5.place(x=220, y=220)


    root.update()


    print(box1.winfo_rootx()-point_of_reference.winfo_rootx(), point_of_reference.winfo_rooty()-box1.winfo_rooty())

    
    root.mainloop()






