#!/usr/bin/env python
# coding: utf-8

# In[4]:


import dataset_module as DS
import distance_module as Distance


# In[5]:


# A function that returns the average transactions of any user and of all users.

#The Default value for id is None
def Mean(id=None): 
    user = DS.dataset()
    try:
        # if we don't pass any arguments it will return the Mean for all transactions 
        if id is None: 
            count = 0
            amount = 0
            #iterating user dictionary, i as user id
            for i in user:
              #iterating transaction dictionary, j as transaction id
                for j in user[i]:
                    amount += user[i][j]['amount']
                    count += 1
            if count == 0:
                raise ZeroDivisionError("No transactions found for all users")
            # Calculation of mean
            avg = amount/count
        
        #Else case for checking mean of transactions for a specific user
        else:
            #checking for the user id in user dictionary, if it's not found raise an error
            if id not in user:
                raise KeyError(f"User id {id} not found")
            count = 0
            amount = 0
            # iterateing user dictionary of id given, i is the transaction id
            for i in user[id]:
                amount += user[id][i]['amount']
                count += 1
            #if there are no transactions for the user, raise a ZeroDivisionError with a message
            if count == 0:
                raise ZeroDivisionError(f"No transactions found for user id {id}")
            avg = amount/count
        return round(avg, 2)
    #for any other exception, print a general error message
    except Exception as e:
        print(f"Error: {e}")


# In[7]:


# A function that returns the mode of transactions of any user and that of all users.
def Mode(id=None):
    user = DS.dataset()
    # For all users
    if id is None: 
        mode_dic = []
        for i in user:
            for j in user[i]:
                mode_dic.append(user[i][j]['amount'])
        try:
            # the key parameter of max() compares the count of each mode_dic value and return the value with highest count
            mode = max(mode_dic, key = mode_dic.count)
        except ValueError as e:
            return f"No unique mode found for all users. Error: {e}"

    # For a specific user
    else:
        #if the user is not found in the dataset, raise a KeyError with a message
        if id not in user:
            raise KeyError(f"User id {id} not found")
        mode_dic = []
        for i in user[id]:
            mode_dic.append(user[id][i]['amount'])
        try:
            mode = max(mode_dic, key = mode_dic.count)
        #If there is no unique mode found in the dataset, raise a ValueError with a message
        except ValueError as e:
            return f"No unique mode found for user {id}. Error: {e}"
      
    return mode


# In[9]:


# A function that returns the median of all transactions of a user and that of all users.
def Median(id=None):
  try:
    user = DS.dataset()
    # for all users
    if id == None:
      median_dic =[]
      for i in user:
        for j in user[i]:
          median_dic.append(user[i][j]['amount'])
      median_dic.sort()
      n = len(median_dic)
      # if the list has an even number of elements, take the average of the middle two
      if n % 2 == 0:
        median = (median_dic[n//2-1] + median_dic[n//2])/2
      # if the list has an odd number of elements, take the middle element
      else:
        median = median_dic[n//2]

    # for a specific user id
    else:
      if id not in user:
        raise KeyError(f"User id {id} not found")
      median_dic =[]
      for i in user[id]:
        median_dic.append(user[id][i]['amount'])
      median_dic.sort()
      n = len(median_dic)
      # if the list has an even number of elements, take the average of the middle two
      if n == 0:
        median = 0
      elif n % 2 == 0:
        median = (median_dic[n//2-1] + median_dic[n//2])/2
      # if the list has an odd number of elements, take the middle element
      else:
        median = (median_dic[n//2])
    return round(median,2)
  #if the user is not found in the dataset, raise a KeyError with a message
  except KeyError:
    print("Error: User ID not found in dataset")
  #if there is a division with zero, raise a ZeroDivisionError with a message
  except ZeroDivisionError:
    print("Error: The list is empty and cannot be divided by zero")
  #for any other exception, print a general error message
  except:
    print("Error: An unexpected error occurred") 


# In[11]:


# A function that returns the interquartile range of any user’s transactions and of all users.
def IQR(id=None):
    try:
        user = DS.dataset()
        # setting the transation amount in a list
        amounts = []
        #for all
        if id is None:
            for i in user:
                for j in user[i]:
                    amounts.append(user[i][j]['amount'])
        # for given id
        else:
            for i in user[id]:
                amounts.append(user[id][i]['amount'])

        # sorting the list
        amounts.sort()
        # n is the number of items in the list
        n = len(amounts)
        # Q1 is the 1/4 postionn of the list, hence we are doing n/4
        q1 = amounts[int(n/4)]
        # q3 is the 3/4 postion of the list , we can calculte by 3* n/4
        q3 = amounts[int(3*n/4)]
        # Inter Quartile Range or IQR is calculated as q3 - q1
        iqr = q3 - q1
        return iqr
    #for any exception, print a general error message
    except Exception as e:
        print(f"Error: {e}")
        return None


# In[13]:


# A function that returns the location centroid of any user, based on their transaction locations.

def LocCentroid(id):
    try:
        #load the dataset
        user = DS.dataset()
        # create empty lists to store the x and y coordinates
        loc_x = []
        loc_y = []
        #iterate through the transactions of the user and append the x and y coordinates to the lists
        for i in user[id]:
            loc_x.append(user[id][i]['x_coordinate'])
            loc_y.append(user[id][i]['y_coordinate'])
        #calculating the centoid
        x_center = (sum(loc_x)) / (len(loc_x))
        y_center = (sum(loc_y)) / (len(loc_y))
      
        return round(x_center, 2), round(y_center, 2)
    # if the user is not found in the dataset, raise a KeyError with a message
    except KeyError:
        print(f"User {id} not found in the dataset.")
    # if there are no transactions for the user, raise a ZeroDivisionError with a message
    except ZeroDivisionError:
        print(f"No transactions found for user {id}.")
    # for any other exception, print a general error message
    except:
        print("An error occurred while processing the data.")


# In[18]:


# A function that computes the standard deviation of any specific user’s transactions.
def SD(id):
    try:
        user = DS.dataset()
        # if user id not found in dataset, raise ValueError with a message
        if id not in user:
            raise ValueError(f"User {id} does not exist.")
        # create empty list to store transactions amounts 
        amount = []
        for i in user[id]:
            amount.append(user[id][i]['amount'])
        n = len(amount)
        # amount1 contain the mean of transactions of the user
        amount1 = Mean(id)

        # creating a list to store the (x-x1)**2 value, where x is the value and x1 is the mean
        sd1 = []
        for i in user[id]:
          sd1.append(((user[id][i]['amount']) - amount1 ) ** 2)

        # calculating Standard deviation
        amt_SD = (sum(sd1) / (n-1)) **.5
        
        return round(amt_SD, 2)
    #for any exception, print a general error message
    except Exception as e:
        print(f"Error: {str(e)}")


# In[37]:


# A function that determines whether a transaction is fraudulent or not. It should provide details of such transactions.
def fraudOrNot(tid):
  try:
    user = DS.dataset()
    # initializing a string to store fruad transactions 
    fruad_str =""
    # iterate through the users in the dataset
    for i in user:
        # check if the transaction id exists in the user's transactions
        if tid in user[i]:
            # check if the transaction is fraudulent
            if user[i][tid]['fraud'] == 'true':
#                 print("Fraudulent")
                print(f"Transaction ID: {tid}")
                print(f"User ID: {i}")
                print("Details: ")
                print(user[i][tid])
                return "Fraudulent"
                # return print("Fraudulent" + "\n" + str(i) + ":\t"+ str(tid) + ":\t" + str(user[i][tid]))
            # check if the transaction is not fraudulent
            elif user[i][tid]['fraud'] == 'false':
                return "Not Fraudulent"
            else:
                return "Invalid input"
  # if there is any other error while processing the data, return an error message.
  except:
        return "An error occurred while processing the data."


# In[22]:


# A function that returns an abnormal transaction for any given user
def abnormal(id):
  try:
    user = DS.dataset()
    # initializing a string to store abnormal transactions 
    abnormal_transition = ""
    # computing the abnormal transaction threshold as median + 3SD
    abnormal_threshold = Median(id)+ 3*SD(id)
    # iterates through each transaction of the user
    for tid in user[id]:
      # if the transaction amount is greater than the threshold, mark it as abnormal
      if user[id][tid]['amount'] > abnormal_threshold:
        abnormal_transition += str(tid) + ":\t" + str(user[id][tid]) + "\n"
    
    return abnormal_threshold,print(abnormal_transition)
  # if the user is not found in the dataset, raise a KeyError with a message
  except KeyError:
    print(f"User {id} not found in the dataset.")
  # if there are no transactions for the user, raise a ZeroDivisionError with a message
  except ZeroDivisionError:
    print(f"No transactions found for user {id}.")
  #for any other exception, print a general error message
  except:
    print("An error occurred while processing the data.")


# In[26]:


# A function that computes the Z score of any user’s transactions and for all users’ transactions.
def ZScore(id=None):
  try:
    user = DS.dataset()
    # initializing the string for store z-score
    Z = ""
    sd_lst =[]

    # If id is not provided, calculate Z-score for all users
    if id is None:
      for i in user:
        for j in user[i]:
          # creating a list to store the (x-x1)**2 value, where x is the value and x1 is the mean
          # here i have used the Mean function from above to calulate the mean
          sd_lst.append(( (user[i][j]['amount']) - Mean() ) **2 )
      # Calculating the standard deviation
      n = len(sd_lst)
      stdv = (sum(sd_lst) / n-1)**.5
      
      # Calculating the Z-score for each transaction and store it in the Z string
      for i in user:
        for j in user[i]:
          z_score = round((((user[i][j]['amount']) - Mean()) / stdv),3)
          Z += str(j) +  ":\t" + str(z_score) + "\n"
    # z-score for specific user
    else:
      # if the user is not found in the dataset, raise a KeyError with a message
      if id not in user:
        raise KeyError(f"User {id} not found in the dataset.")
      sd = SD(id)
      # if sd is 0 for the user, raise a ZeroDivisionError with a message
      if sd == 0:
        raise ZeroDivisionError(f"No transactions found for user {id}.")
      # Calculate the Z-score for each transaction of the user and store in Z string
      for tid in user[id]:
        z_score = round((((user[id][tid]['amount']) - Mean(id)) / sd),3)
        Z += str(tid) +  ":\t" + str(z_score) + "\n"
    return print(Z)

  #for any other exception, print a general error message
  except:
    print("An error occurred while processing the data.")


# In[31]:


# A function that computes those frequencies of transactions at any given location
def Locfreq(x, y):
    try:
        user = DS.dataset()
        count = 0
        # iterating through each user as i
        for i in user:
            # iterate through each transaction of the user as j
            for j in user[i]:
                # check if the transaction's coordinates match the input coordinates
                if user[i][j]['x_coordinate'] == x and user[i][j]['y_coordinate'] == y:
                    count += 1
        # return the count of transactions at the given location
        return count
    # if there is any other exception, print a general error message
    except Exception as e:
        print(f"Error: {str(e)}")


# In[29]:


# A function that returns the outlier of any location and of any user
def Outlier(id):
  try:
      user = DS.dataset()
      # get the centroid of the user's location and assigning it into variables
      x1,y1 =  LocCentroid(id)
      distance = []
      for i in user[id]:
        x2 = user[id][i]['x_coordinate']
        y2 = user[id][i]['y_coordinate']
        # calculating the distance between each transaction and the centroid
        distance.append((((x2-x1)**2)+((y2-y1)**2))**.5)

      n = len(distance)
      # calculating the mean distance
      mean_distance = sum(distance)/n
      # calculating the standard deviation for the distances from the centroid
      sd1 = []
      for i in distance:
        sd1.append((i - mean_distance) ** 2)
      SD = (sum(sd1) / (n-1)) **.5

      # calculating the median of distance
      # sorting the distances
      distance.sort()
      if n % 2 == 0:
        median = (distance[n//2-1] + distance[n//2])/2
      else:
        median = distance[n//2]

      # calculate the outlier threshold using the equation median + 3 SD
      outlier_threshold = median + 3 * SD

      # initializing a list to store the outlier locations
      outlier_location = ""
      # check = []

      for i in user[id]:
        x2_check = user[id][i]['x_coordinate']
        y2_check = user[id][i]['y_coordinate']
        # checking if the distance between the transaction and the centroid is greater than the outlier threshold
        if ((((x2_check-x1)**2)+((y2_check-y1)**2))**.5) > outlier_threshold:
          # Adding the transaction to the outlier locations
          outlier_location += str(x2_check)+ "," + str(y2_check) +  "\n"
          # check.append(user[id][i])
      
      return print(outlier_location)
  
  # if the user is not found in the dataset, raise a KeyError with a message
  except KeyError:
        print(f"Error: User ID '{id}' not found in dataset.")
  # if user id not found in dataset, raise ValueError with a message
  except ValueError:
        print("Error: Invalid value in dataset.")
  # if there is any other exception, print a general error message
  except Exception as e:
        print(f"Error: {str(e)}")


# In[35]:


# A function that returns the nth percentiles of transactions of any user and of all users.

def nthPercentile(p, id=None):
  try:
    user = DS.dataset()
    # percentile for specific user
    if id and id in user:
      amount = []
      for i in user[id]:
        amount.append(user[id][i]['amount'])
    # percentile for all users
    else:
      amount = []
      for i in user:
        for j in user[i]:
          amount.append(user[i][j]['amount'])
    # sort transactions in amount
    amount.sort()
    # calculating the index for nth percentile
    n = len(amount)
    n_idx = ((p/100) * n)

    # check the input value for any error and exceptions
    if n == 0:
      raise ValueError("Error: Empty dataset.")
    elif n_idx <= 0 or n_idx >= n:
      raise ValueError(f"Error: Invalid percentile '{p}'.")
    elif not isinstance(p, (int, float)):
      raise TypeError("Error: Invalid data type for percentile.")
    
    # if index is an integer, we take the index and index-1th values and calculate the avarege
    if n_idx.is_integer():
      n_idx_low = int(n_idx) - 1
      n_idx_high = int(n_idx)
      nth = ((amount[n_idx_low]) + (amount[n_idx_high])) / 2

    # if index is not an integer, round up to the nearest integer
    else:
      nth = amount[int(n_idx)]
    # round nth percentile and return nth percentile value and index
    #return round(nth, 2), int(n_idx)
    return round(nth, 2)

  #If the file is not found in the location, it will raise an error message
  except FileNotFoundError:
    print("Error: The file was not found.")
  #if user id or transaction id were not found in the dataset, raise a KeyError
  except KeyError:
    print(f"Error: User ID '{id}' not found in dataset.")
  # if user id not found in dataset, raise ValueError with a message
  except ValueError as e:
    print(str(e))
   #for any other exception, print a general error message
  except Exception as e:
    print(f"Error: {str(e)}")


