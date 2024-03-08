import tkinter as tk
import tkinter.messagebox
import csv
from OrderClass import Order


class confirmOrderGUI:
    """This class creates a GUI for the final project. (name, product, brand, price).
       Program Created By: Daniel O'Malley"""

    def __init__(self, orderList):
        self.__orderList = orderList
        # main window
        self.main_window = tk.Tk()
        # title
        self.main_window.title('Confirm Order')
        # window size
        self.main_window.geometry('300x500')
        # frame
        self.confirmFrame = tk.Frame(self.main_window)
        self.confirmFrame.grid(row=0, column=0, rowspan=2, columnspan=3)
        self.finalOrderFrame = tk.Frame(self.main_window)
        self.finalOrderFrame.grid(row=0, column=0, rowspan=1, columnspan=3)
        # keep shopping? label
        self.keepShoppingLabel = tk.Label(self.confirmFrame, text='Would you like to keep shopping')
        # yes/no buttons
        self.yesButton = tk.Button(self.confirmFrame, text='Yes', command=self.yesButton)
        self.noButton = tk.Button(self.confirmFrame, text='No', command=self.noButton)
        # final order
        orderText = []
        for order in orderList:
            orderText.append(str(order))
        self.finalOrderLabel = tk.Label(self.finalOrderFrame, text='\n'.join(orderText))
        # positioning
        self.keepShoppingLabel.grid(row=0, column=1)
        self.yesButton.grid(row=1, column=0, pady=.2)
        self.noButton.grid(row=1, column=3, pady=.2)
        self.finalOrderLabel.pack(side='bottom')

        # place frame
        self.confirmFrame.place(relx=.5, rely=.1, anchor='center')
        self.finalOrderFrame.place(relx=.5, rely=.5, anchor='center')
        # window loop
        self.main_window.mainloop()

    def noButton(self):
        yesOrNo = tk.messagebox.askyesno('CONFIRMATION', 'Are you sure you are done shopping?')
        if yesOrNo == True:
            confirmation = tk.messagebox.showinfo('CONFIRMATION',
                                                  'Your order has been confirmed and reserved. Please come into the '
                                                  'store for payment and pickup.')
            with open('orders.csv', 'w', newline='') as csvFile:
                writer = csv.writer(csvFile)
                for order in self.__orderList:
                    writer.writerow([order.orderName, order.orderItem, order.orderBrand, order.orderQuantity])
            self.main_window.destroy()

    def yesButton(self):
        self.main_window.destroy()
