# Author: Daniel O'Malley
# Class:  CIS-2531-NET01
# Prog:   Final Project
# Descr:
# Order Class

class Order:
    """This class creates an order class (name, product, brand, price).
       Program Created By: Daniel O'Malley"""

    def __init__(self, orderName='', orderItem='', orderBrand='', orderQuantity=0):
        self.__orderName = orderName
        self.__orderItem = orderItem
        self.__orderBrand = orderBrand
        self.__orderQuantity = orderQuantity

    @property
    def orderName(self):
        return self.__orderName

    @orderName.setter
    def orderName(self, orderName):
        self.__orderName = orderName

    @property
    def orderItem(self):
        return self.__orderItem

    @orderItem.setter
    def orderItem(self, orderItem):
        self.__orderItem = orderItem

    @property
    def orderBrand(self):
        return self.__orderBrand

    @orderBrand.setter
    def orderBrand(self, orderBrand):
        self.__orderBrand = orderBrand

    @property
    def orderQuantity(self):
        return self.__orderQuantity

    @orderQuantity.setter
    def orderQuantity(self, orderQuantity):
        self.__orderQuantity = orderQuantity

    def __str__(self):
        displayOrder = str('Name: {}\nItem: {}\nBrand: {}\nQuantity: {}\n'.format(self.__orderName,
                                                                                  self.__orderItem,
                                                                                  self.__orderBrand,
                                                                                  self.__orderQuantity))
        return displayOrder

