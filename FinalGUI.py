# Author: Daniel O'Malley
# Class:  CIS-2531-NET01
# Prog:   Final Project GUI
# Descr:
# GUI Classes

import tkinter as tk
from OrderClass import Order
from FinalGUIpart2 import confirmOrderGUI
import tkinter.messagebox


class OrderGUI:
    """This class creates a GUI for the final project. (name, product, brand, price).
       Program Created By: Daniel O'Malley"""

    def __init__(self):
        # create order
        self.__orderList = []
        # main window
        self.main_window = tk.Tk()
        # title
        self.main_window.title("Dan's Golf Store")

        # window size
        self.main_window.geometry('300x375')
        # frame
        self.orderFrame = tk.Frame(self.main_window)
        self.orderFrame.grid(row=0, column=0, rowspan=9, columnspan=3)
        # name entry
        self.name_label = tk.Label(self.orderFrame, text='Name')
        self.name_entry = tk.Entry(self.orderFrame, width=25)
        # product radio buttons
        self.radio_label = tk.Label(self.orderFrame, text='Select an item')
        self.radio_var = tk.IntVar()
        self.driverRad = tk.Radiobutton(self.orderFrame,
                                        text='Driver', variable=self.radio_var,
                                        value=1)
        self.woodsRad = tk.Radiobutton(self.orderFrame,
                                       text='Set of Woods/Hybrids', variable=self.radio_var,
                                       value=2)
        self.ironsRad = tk.Radiobutton(self.orderFrame,
                                       text='Set of Irons', variable=self.radio_var,
                                       value=3)
        self.wedgesRad = tk.Radiobutton(self.orderFrame,
                                        text='Set of Wedges', variable=self.radio_var,
                                        value=4)
        self.putterRad = tk.Radiobutton(self.orderFrame,
                                        text='Putter', variable=self.radio_var,
                                        value=5)
        self.driverRad.select()
        # brand list box
        self.brand_label = tk.Label(self.orderFrame, text='Select a brand')
        self.brandLBX = tk.Listbox(self.orderFrame, height=3)
        self.brandLBX.insert(1, 'Titleist')
        self.brandLBX.insert(2, 'Callaway')
        self.brandLBX.insert(3, 'Taylor Made')
        self.brandLBX.select_set(0)
        # quantity entry
        self.quantity_label = tk.Label(self.orderFrame, text='Quantity')
        self.quantity_entry = tk.Entry(self.orderFrame, width=5)
        # price per item display
        self.LBLitemPrice_label = tk.Label(self.orderFrame, text='Price per Item')
        self.itemPrice_label = tk.Label(self.orderFrame, text='')
        # button frame
        self.buttonFrame = tk.Frame(self.main_window)
        # bottom buttons
        self.exit_button = tk.Button(self.buttonFrame, text='Exit', command=self.exit_app)
        self.clear_button = tk.Button(self.buttonFrame, text='Clear', command=self.clear_order)
        self.add_button = tk.Button(self.buttonFrame, text='Add', command=self.add_order)
        # positioning
        self.name_label.grid(row=0, column=0, pady=5)
        self.name_entry.grid(row=0, column=1, pady=5)
        self.radio_label.grid(row=1, column=0)
        self.driverRad.grid(row=1, column=1)
        self.woodsRad.grid(row=2, column=1)
        self.ironsRad.grid(row=3, column=1)
        self.wedgesRad.grid(row=4, column=1)
        self.putterRad.grid(row=5, column=1)
        self.brand_label.grid(row=6, column=0)
        self.brandLBX.grid(row=6, column=1)
        self.quantity_label.grid(row=8, column=0, pady=5)
        self.quantity_entry.grid(row=8, column=1, pady=5)
        self.exit_button.pack(side='left', padx=5)
        self.clear_button.pack(side='left', padx=5)
        self.add_button.pack(side='left', padx=5)
        # place frame
        self.orderFrame.place(relx=.5, rely=.4, anchor='center')
        self.buttonFrame.place(relx=.5, rely=.85, anchor='s')
        # window loop
        self.main_window.mainloop()

    def exit_app(self):
        yesOrNo = tk.messagebox.askyesno('EXIT?', 'Are you sure you want to exit?')
        if yesOrNo == True:
            self.main_window.destroy()

    def clear_order(self):
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def add_order(self):
        orderName = self.name_entry.get()
        # name error handling
        if orderName.isalpha() == False:
            tk.messagebox.showerror('ERROR', 'Cannot leave name empty. Letters only in the name entry box.')
            return
        orderItem = self.radio_var.get()
        if orderItem == 1:
            orderItem = 'Driver'
        elif orderItem == 2:
            orderItem = 'Set of Woods/Hybrids'
        elif orderItem == 3:
            orderItem = 'Set of Irons'
        elif orderItem == 4:
            orderItem = 'Set of Wedges'
        elif orderItem == 5:
            orderItem = 'Putter'
        else:
            tk.messagebox.showerror('ERROR', 'Please select an item.')
            return
        orderBrand = self.brandLBX.get(self.brandLBX.curselection())

        orderQuantity = self.quantity_entry.get()
        # exception handling (quantity)
        try:
            orderQuantity = int(orderQuantity)
        except ValueError:
            tk.messagebox.showerror('ERROR', 'Quantity must be a positive number')
            self.quantity_entry.focus()
        else:
            try:
                assert orderQuantity > 0
            except AssertionError:
                tk.messagebox.showerror('ERROR', 'Quantity must be a positive number')
                self.quantity_entry.focus()
            else:
                self.__orderList.append(Order(orderName, orderItem, orderBrand, orderQuantity))
                orderConfirmation = confirmOrderGUI(self.__orderList)


if __name__ == '__main__':
    my_gui = OrderGUI()
