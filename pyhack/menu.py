#!/usr/bin/env python3


class menu:
    def __init__(self,menu_name):
        print("init menu")
        self.menu_name = menu_name
        self.menu = []
        self.menu_text=[]
        self.selector = []
        self.functions=[]
        self.value=[]

    def print_menu(self,loop):
        counter = 0
        print (30 * "-",self.menu_name,30 * "-")
        for option in self.menu_text:
            print(self.selector[counter],"\t-\t", option)
            counter = counter+1
        print ('quit \t-\t exits the program')
        print (67 * "-")
        self.choice = input("Enter your choice: ")
        loop=self.process_menu()
        if loop == False:
            return loop
        else:
            return True
        
    
    def new_option(self, selector, menu_text ,funciton, value):
        self.menu_text.append(menu_text)
        self.selector.append(selector)
        self.functions.append(funciton)
        self.value.append(value) 

    def process_menu(self):
        counter = 0 
        print(self.choice)
        if self.choice=='quit': 
            return False
        for option in self.functions:
            if self.choice==self.selector[counter]:   
                option(self.value[counter])
                return True
        