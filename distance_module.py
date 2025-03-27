#!/usr/bin/env python
# coding: utf-8

# In[17]:


# You will implement distance_module containing two functions. 
# a. A function that computes the distance between any two given transactions of a user. 
import dataset_module as DS
def SameUserDistance(id,tran1,tran2):
  user = DS.dataset()
  try:
    x1 = user[id][tran1]['x_coordinate']
    y1 = user[id][tran1]['y_coordinate']
    x2 = user[id][tran2]['x_coordinate']
    y2 = user[id][tran2]['y_coordinate']
    # calculating the distance
    distance =(((x2-x1)**2)+((y2-y1)**2))**.5 
    return round(distance,2)
  except KeyError as e:
    print(f"Error: {e}. Please check the input values.")

# b. And another function should be implemented for computing the distance of transactions of any two users.
def TwoUserDistance(id1,id2,tran1,tran2):
  user = DS.dataset()
  try:
    x1 = user[id1][tran1]['x_coordinate']
    y1 = user[id1][tran1]['y_coordinate']
    x2 = user[id2][tran2]['x_coordinate']
    y2 = user[id2][tran2]['y_coordinate']
    dis_Bw_2 = (((x2-x1)**2)+((y2-y1)**2))**.5
    return round(dis_Bw_2,2)
  #if user id or transaction id were not found in the dataset, raise a KeyError
  except KeyError as e:
    print(f"Error: {e}. Please check the input values.") 

