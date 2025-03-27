#!/usr/bin/env python
# coding: utf-8

# In[2]:


# You will implement a dataset_module with a function that retrieves the above attributes/features and returns a dictionary. You must use python file 
# objects. Please do not use any other libraries for this task. If you do, you will lose the marks for this task
def dataset(data_path="Transaction.txt"):
    user = {}  # Dictionary to store user transactions 
    try:
        with open(data_path,'r') as f: #opening the dataset as f
            for line in f:
                columns = line.strip().split(':')  # spliting datas into columns 
                user_id = columns[0]
                transaction_id = columns[1]
                description = columns[2]
                amount = columns[3]
                x_coordinate = columns[4]
                y_coordinate = columns[5]
                fraud = columns[6]

                #creating transaction dictionary 
                transaction = {'description':description , 'x_coordinate' : float(x_coordinate), 'y_coordinate' : float(y_coordinate) ,'amount': float(amount) , 'fraud': fraud}

                # user dictionary 
                if user_id in user:   #if user_id exists then add transactions 
                    user[user_id][transaction_id] = transaction
                else:    #if user_id not exists then creat new dictionary for the new user_id
                    user[user_id] = {transaction_id:transaction}
        return user
    #If the file is not found in the location, it will raise an error message
    except FileNotFoundError:
        print(f"Error: File {data_path} not found.")
        return {}
    #for any other exception, print a general error message
    except Exception as e:
        print(f"Error: {str(e)}")
        return {}

