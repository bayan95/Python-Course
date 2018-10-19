#!/usr/bin/env python
# coding: utf-8

# In[1]:


a= float(input("Enter the temprature value :"))
b= input( "Enter the temprature's type; f or c : ")
if b== "f"  :
    print("The temp. in Celsuis is :",(a-32)*5/9)
else :
    print("The temp. in Fahrenheit is :",9/5*a+32)

