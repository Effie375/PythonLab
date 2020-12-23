#!/usr/bin/env python3


from tkinter import Tk, BOTH, messagebox
from tkinter.ttk import Frame, Button


class Example(Frame):
  
   def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
        
   def initUI(self):
      
        self.parent.title("Buttons")

        self.pack(fill=BOTH, expand=1)

        btn1 = Button(self, text="Button 1",
            command=lambda: self.onClick("Button 1"))
        btn1.pack(padx=5, pady=5)
        
        btn2 = Button(self, text="Button 2",
            command=lambda: self.onClick("Button 2"))
        btn2.pack(padx=5, pady=5)
        
        btn2 = Button(self, text="Button 3",
            command=lambda: self.onClick("Button 3"))
        btn2.pack(padx=5, pady=5)   
        
        
   def onClick(self, text):
        
        messagebox.showinfo("Button label", text);


def main():
  
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main() 