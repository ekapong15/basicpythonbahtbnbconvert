from tkinter import * 
from tkinter import ttk, messagebox

GUI = Tk() 
GUI.title('โปรแกรมคำนวนเงินBaht/BNB')
GUI.geometry('700x700')

bg = PhotoImage(file='bnbpng.png')
BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI, text='จำนวนเงินบาทที่ต้องการซื้อ',font=(None,20))
L.pack()

L2 = Label(GUI, text='ราคาเหรียญ BNB ปัจจุบัน 400 USD',font=(None,20))
L2.pack()

L3 = Label(GUI, text='ราคาเงินบาท 32 บาท/USD',font=(None,20))
L3.pack()

v_quantity = StringVar() #ตัวแปรเก็บข้อความเมื่อพิมพ์
E1 = ttk.Entry(GUI, textvariable=v_quantity , font=(None,20))
E1.pack() #pack แปะเข้าโปรแกรม

def Cal():
    try:
        quan = int(v_quantity.get())
        calusd = quan/32
        calbnb = calusd/400
        messagebox.showinfo('ราคาเหรียญ','จำนวนเหรียญ BNB ที่ได้ {} เหรียญ'.format(calbnb))
        v_quantity.set('0')
    except:
        messagebox.showinfo('กรอกผิด','กรอกเฉพาะตัวเลข')
        v_quantity.set('0')

submit = ttk.Button(GUI, text='คำนวน', command=Cal)
submit.pack(ipadx=30, ipady=20) #ipadx ขยายความกว้าง x/y

GUI.mainloop()