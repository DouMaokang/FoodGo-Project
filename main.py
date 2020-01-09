
# ----------------------------------- Project : NTU food court search engine ----------------------------------------- #
# Contributors:
# _____________________________________________________________________________
# Name:         Dou Maokang     |   Heng Cheng Kiat   |  Hasan Mohammad Yusuf |
# -----------------------------------------------------------------------------
# Matric no.    U1822704B       |   U1822588L         |  U1822478E            |
# -----------------------------------------------------------------------------
#
# There are mainly 3 parts of this program
#
#   1. Functions for sorting/ searching/ updating/ displaying/ data processing
#   2. Functions for Graphical User Interface
#   3. GUI basic settings
# Each team member contributed to these three parts above
#



import tkinter as tk
import math
import pickle
from tkinter import messagebox


canteen_information = {
    'Canteen 1': {'rank': 1, 'price': 7, 'distance': 0, 'food': ['Chicken Rice', 'Fried Rice', 'Noodles', 'Indian Cuisine'], 'pos': (0, 50), 'comments': ['very good','cheap food' , 'tasty' ],
                  'rate': [3 , 3.5 , 4.1 , 5], 'average rate':0, 'time':(7,21), 'tel':63343033},
    'Canteen 2': {'rank': 3, 'price': 6, 'distance': 0, 'food': ['Pasta','Ayam penyet' , 'Carrot cake' , ' Hokkien mee' ], 'pos': (100, 200), 'comments': ['nice','food given in plenty amounts' , ' Store owners are polite'],
                  'rate': [4,5 , 4.7 , 3 , 4.2],'average rate':0,'time':(7,21), 'tel':63343033},
    'Canteen 9': {'rank': 2, 'price': 6, 'distance': 0, 'food': ['Chinese', 'Western', 'Vegetarian','Mixed Rice' ], 'pos': (100, 255), 'comments': ['delicious', 'too little seats available', 'affordable food', 'mixed rice is tasty'],
                  'rate': [3 , 3.5 , 4 , 4.3],'average rate':0,'time':(7,21), 'tel':96923456},
    'Canteen 11': {'rank': 5, 'price': 8, 'distance': 0, 'food': ['Indian', 'Chicken Rice' , 'Mala' , 'Fish soup' ], 'pos': (300, 75), 'comments': ['Tasty', 'Affordable' , 'Plenty of seats available'],
                   'rate': [3 , 3.2 , 5 , 5],'average rate':0,'time':(7,21), 'tel':97866726},
    'Canteen 13': {'rank': 4, 'price': 12, 'distance': 0, 'food': ['Western', ' Roasted Delights' , 'Nasi Lemak', ' Waffles' ], 'pos': (60, 300), 'comments': ['Tasty' , 'Delicious' , 'Would recommend', 'Opens till late'],
                   'rate': [4 ,4 , 2 , 4.3],'average rate':0,'time':(7,21), 'tel':98510908},
    'Canteen 14': {'rank': 4, 'price': 12, 'distance': 0, 'food': ['Japanese', 'Chinese' , ' Handmade Noodles' , 'Chicken Rice' ], 'pos': (0, 300), 'comments': ['Ramen is good', 'A healthy choice', ' Delicious', 'No seats during peak hours'],
                   'rate': [5 , 5 , 4.9 ,3],'average rate':0,'time':(7,21), 'tel':81127239},
    'Canteen 16': {'rank': 4, 'price': 12, 'distance': 0, 'food': ['Japanese', 'Chicken Rice' , 'Muslim Cuisine' , 'Chinese'], 'pos': (150, 600), 'comments': ['Awesome' , 'Would come again' , 'Love the Japanese food' , 'Place is well maintaned'],
                   'rate': [4 , 5 , 3.5 , 3.9 , 4.2],'average rate':0,'time':(7,21), 'tel':94505893},
    'North Hill': {'rank': 4, 'price': 12, 'distance': 0, 'food': ['Western',' Chinese' , 'Mixed Rice' , 'Noodles' ], 'pos': (650, 500), 'comments': ['Most stores usually not opened' , 'food is bad' , 'has plenty of seats'],
                   'rate': [2 , 3 , 2.9 , 3.5 , 2.2 ],'average rate':0,'time':(7,21), 'tel':85080232},
    'Canteen Pioneer': {'rank': 4, 'price': 12, 'distance': 0, 'food': ['Western','Indian' , 'Wanton noodles', 'Congee' ], 'pos': (160, 450), 'comments': ['Very nice Western food', 'Clean' , 'Plenty of seats', 'Delicious'],
                        'rate': [3 , 4 , 4.2 , 2.1 , 4],'average rate':0,'time':(7,21), 'tel': 'nil'},
    'Canteen Foodgle': {'rank': 4, 'price': 12, 'distance': 0, 'food': ['Western', ' Chinese' , 'Hokkien Mee' , 'Minced Meat Noodles' ], 'pos': (360, 700), 'comments': ['Portion given is abundant', 'Would come again' , 'Cheap and tasty food'],
                        'rate': [4 , 3 , 5 , 4.6 , 4.9],'average rate':0, 'time':(7,21), 'tel':82963633}
}

aFile = open('data_base.txt', 'wb')
pickle.dump(canteen_information, aFile)
aFile.close()
data_base = open('data_base.txt', 'rb')
canteen_information = pickle.load(data_base)


# -------------------------------------------------------------------------------------------------------------------- #

#  Functions for sorting / searching / updating / displaying / data processing  #

# 1. Sorting functions
def merge_sort(alist):
    alist_len = len(alist)

    if alist_len < 2:
        return alist
    left = alist[:(alist_len // 2)]  # divide the list into the left part and the right part
    right = alist[(alist_len // 2):]

    left = merge_sort(left)  # sort the left part of the list
    right = merge_sort(right)  # sort the right part of the list

    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    else:
        result.extend(right)
    return result


def canteen_sublist(data_base, target):
    """retrieve the targeted information of each canteen,
     and store them in a list for easy processing
    """

    sublist = []
    for key, value in data_base.items():
        sub_information = {value[target]: key}
        sublist.append(sub_information)
    return sublist


def sort_canteen(alist):
    """sort canteen in the sublist defined by function canteen_sublist"""

    lst = []
    for i in alist:
        for key in i.keys():
            lst.append(key)  # store the value of price/distance/rank, etc. in a list for sorting

    sorted_lst = merge_sort(lst)

    new_list = []
    for i in sorted_lst:
        for canteen in alist:
            for key in canteen.keys():
                if i == key:                            # find the corresponding canteen
                    sub_information = {i: canteen[i]}   # associate the each canteen with the sorted value
                    if sub_information not in new_list:
                        new_list.append(sub_information)
    return new_list


def sort_by_price(data_base):
    """sort canteens in an ascending order of price"""

    sorted_list = canteen_sublist(data_base, 'price')
    return sort_canteen(sorted_list)


def sort_by_rank(data_base):
    """sort canteens in an ascending order of rank"""

    sorted_list = canteen_sublist(data_base, 'rank')
    return sort_canteen(sorted_list)


def sort_by_distance(data_base):
    """sort canteens in an ascending order of distance"""

    sorted_list = canteen_sublist(data_base, 'distance')
    return sort_canteen(sorted_list)


def sort_by_average_rate(data_base):
    """sort canteens in an asceding order of average rate"""

    sorted_list = canteen_sublist(data_base, 'average rate')
    return sort_canteen(sorted_list)


# 2. Searching functions
def search_by_food(data_base, food):
    canteen_with_wantedfood = []
    for key, value in data_base.items():
        for i in value['food']:
            if i.lower() == food.lower():
                canteen_with_wantedfood.append({food: key})

    return canteen_with_wantedfood


def search_by_price(data_base, high=50, low=0):
    canteen_with_wantedprice = []
    for key, value in data_base.items():
        if low <= value['price'] <= high:
            canteen_with_wantedprice.append(key)
    return canteen_with_wantedprice


# 3. Calculating functions
# Done by : Cheng Kiat
def cal_distance(data_base, pos_user):
    """calculate the distance between the user and each canteen"""

    coordinates_of_canteen = canteen_sublist(data_base, 'pos')
    for canteens in coordinates_of_canteen:
        for pos_can, can in canteens.items():
            square_distance = ((pos_can[0]-pos_user[0])**2 + (pos_can[1]-pos_user[1])**2)
            distance = int(math.sqrt(square_distance))
            data_base[can]['distance'] = distance

    update(data_base)  # update the new data into the database


def cal_walking_time(data_base, target):
    distance = data_base[target]['distance']
    time = distance//60
    return time


def cal_average_rate(data_base):
    """update the average rate of each canteen"""
    for key, value in data_base.items():
        av_rate = sum(value['rate']) / len(value['rate'])
        value['average rate'] = av_rate

    update(data_base)  # update the new data into the database


def cal_rank(data_base):
    """update the rank of each canteen according to the average rate"""
    sorted_list = sort_by_average_rate(data_base)
    j = 0
    for i in range(10, 0, -1):
        for value in sorted_list[j].values():
            canteen_information[value]['rank'] = i
        j += 1

    update(data_base)  # update the new data into the database


# 4. Updating functions
def update(new_database):
    """update new database into the external database file"""
    data_base = open('data_base.txt', 'wb')
    pickle.dump(new_database, data_base)
    data_base.close()

    data_base = open('data_base.txt', 'rb')
    canteen_information = pickle.load(data_base)


def update_food(data_base, canteen_name, entry):
    """allow users to update new rank to the database"""

    user_input = entry.get()
    if user_input in data_base[canteen_name]['food']:
        messagebox.showwarning("Update Failed", "We already had this food in the canteen")
        entry.delete(0, 'end')
    else:
        data_base[canteen_name]['food'].append(user_input)
        messagebox.showinfo("Succeeded", "Information updated successfully!\nThanks for your support!")
        entry.delete(0, 'end')


def update_price(data_base, canteen_name, entry):
    """allow users to update new mean value of price to the database"""

    new_info = entry.get()
    try:
        data_base[canteen_name]['price'] = float(new_info)
        messagebox.showinfo("Succeeded", "Information updated successfully!\nThanks for your support!")
        entry.delete(0, 'end')
    except:
        messagebox.showwarning("Invalid Input", "Please enter a positive number.")
        entry.delete(0, 'end')


def update_location(data_base, canteen_name, entry):
    """allow users to update new location of canteen to the database"""

    new_info = entry.get()
    new_info_list = new_info.split(',')
    try:
        new_info_tuple = (int(new_info_list[0]), int(new_info_list[1]))
        data_base[canteen_name]['pos'] = new_info_tuple

        update(data_base)  # update the new data into the database

        messagebox.showinfo("Succeeded", "Information updated successfully!\nThanks for your support!")
        entry.delete(0, 'end')
    except:
        messagebox.showwarning("Invalid Input", "Please enter two positive numbers separated by a comma.")
        entry.delete(0, 'end')


def update_tel(data_base, canteen_name, entry):
    """allow users to update new telephone number of canteens to the database"""

    new_info = entry.get()

    if new_info.isdigit() and len(new_info) == 8:
        new_tel = int(new_info)
        if new_tel > 9999999:
            data_base[canteen_name]['tel'] = new_tel

            update(data_base)  # update the new data into the database

            messagebox.showinfo("Succeeded", "Information updated successfully!\nThanks for your support!")
            entry.delete(0, 'end')
        else:
            messagebox.showwarning("Invalid Input", "Telephone number should not begin with 0s.")
            entry.delete(0, 'end')

    else:
        messagebox.showwarning("Invalid Input", "Please enter an 8-digit telephone number.")
        entry.delete(0, 'end')


# 5. Getting user feedback functions
def add_comments(data_base, canteen_name, entry):
    """allow users to leave comments of each canteen and store it in the database"""

    new_comments = entry.get()
    if new_comments:
        data_base[canteen_name]['comments'].append(new_comments)

        update(data_base)  # update the new data into the database

        messagebox.showinfo("Succeeded", "Comment is successfully updated.\nThanks for your support!")
        entry.delete(0, 'end')
    else:
        messagebox.showwarning("Empty box", "No comments entered")


def add_rate(data_base, canteen_name, entry):
    """allow users to rate each canteen and store the rating in the database"""

    rate_str = entry.get()
    if rate_str:
        try:
            rate_float = float(rate_str)
            if 0 <= rate_float <= 5:
                data_base[canteen_name]['rate'].append(rate_float)

                cal_average_rate(data_base)  # calculate the new average rate
                cal_rank(data_base)  # calculate the new rank

                update(data_base)  # update the new data into the database

                messagebox.showinfo("Succeeded", "Rate is successfully updated.\nThanks for your support!")
                entry.delete(0, 'end')

            else:
                messagebox.showwarning("Invalid Input", "Please enter a positive number(0~5)")
                entry.delete(0, 'end')
        except:
            messagebox.showwarning("Invalid Input", "Please enter a positive number(0~5)")
    else:
        messagebox.showwarning("Empty box", "No rate entered")


# 6.1 Displaying functions
def display_information(data_base, target):
    info = data_base[target]
    rank = 'rank:\t\t' + str(info['rank'])
    rate = 'average rate:\t' + str(info['average rate'])
    price = 'average price:\t' + str(info['price'])
    distance = 'distance:\t\t' + str(info['distance'])
    food = 'food:\t' + ', '.join(info['food'])
    pos = 'position:\t\t' + str(info['pos'])
    time = 'open hours:\t' + 'from ' + str(info['time'][0]) + ' to ' + str(info['time'][1])
    tel = 'tel no.\t\t' + str(info['tel'])
    comments = "\nComments about " + target + ' :\n\t\t' + '\n\t\t'.join(info['comments'])

    info_list = [rank, rate, price, distance, food, pos, time, tel, comments]
    info_msg = '\n'.join(info_list)

    return info_msg


def display_recommendation(ranklist, criteria):
    for value in ranklist[0].values():
        canteen = value
    print(canteen)
    for key, value in canteen_information.items():
        if key == canteen:
            recommended_canteen = {canteen: value}
            print(recommended_canteen)
            break
    msg = 'If  ' + criteria.upper() + '  is your main concern,\nwe recommend you to go to \n\t' + canteen.upper() + '\n\n' + \
            'Distance:\t\t' + str(recommended_canteen[canteen]['distance']) + '\n' +\
            'It will take you about ' + str(cal_walking_time(canteen_information, canteen)) + ' minute(s) to arrive there.\n' +\
            'Rank:\t\t' + str(recommended_canteen[canteen]['rank']) + '\n' +\
            'Average price:\t' + str(recommended_canteen[canteen]['price']) + '\n' +\
            "Food:\t\t" + get_food(canteen)
    return msg


def get_comments(canteen):
    """display the first 3 comments of a canteen in our database"""

    comment_list = canteen_information[canteen]['comments'][0:3]
    comments_str = "People's Comments about " + canteen + '\n' + '\n'.join(comment_list)
    return comments_str


def get_food(canteen):
    """display the first 3 food of a canteen in our database"""

    food_list = canteen_information[canteen]['food'][0:2]
    food_str = ', '.join(food_list)
    print(food_str)
    return food_str


# 6.2 Displaying functions
def display_image(ranklist):
    for value in ranklist[0].values():
        canteen = value
    image_dic = {'Canteen 1': can1_img_file, 'Canteen 2': can2_img_file, 'Canteen 9': can9_img_file,
                 'Canteen 11': can11_img_file, 'Canteen 13': can13_img_file,
                 'Canteen 14': can14_img_file, 'Canteen 16': can16_img_file,
                 'North Hill': cannh_img_file, 'Canteen Pioneer': canp_img_file,
                 'Canteen Foodgle': canf_img_file}
    image_file = image_dic[canteen]
    print(image_file)
    return image_file


def display_ranking(sorted_list, target):
    """display ranked canteens to users"""

    message_list = []
    for i in sorted_list:
        for key, value in i.items():
            sub_message = value + " :\t\t " + str(key)
            message_list.append(sub_message)
    message_str = "The " + target + " of each Canteen is:\n" + "\n".join(message_list)
    return message_str


# 7. Getting user location functions
def enter_location(entry):
    """get user location by user inputs"""

    location = entry.get()
    location_list = location.split(',')
    try:
        location_tuple = (int(location_list[0]), int(location_list[1]))
        cal_distance(canteen_information, location_tuple)
        messagebox.showinfo("Succeeded", "We've updated your location! \nEnjoy our canteens~")
        goto_main_frame()
        entry.delete(0, 'end')
    except:
        messagebox.showwarning("Invalid Input", "Please enter two positive numbers separated by a comma.")
        entry.delete(0, 'end')


def get_position(event):
    """get user location by clicking and update it to the database"""

    x = event.x
    y = event.y
    position = (x, y)
    messagebox.showinfo("Succeeded", "We've updated your location! \nEnjoy our canteens~")
    cal_distance(canteen_information, position)
    goto_main_frame()


# -------------------------------------------------------------------------------------------------------------------- #

#  Functions for Graphical User Interface (GUI)  #

# The following functions are used to switch between different frames
def goto_map_frame():
    """display the map and get user location"""

    main_frame.grid_forget()  # erasing other frames
    map_frame.grid()          # displaying map_frame

    window.bind("<Double 1>", get_position)  # detecting user clicks

    # frame labels
    canvas_1.grid(row=2, column=0, columnspan=5)
    map_label.grid(row=0, column=0)
    LocationEntry.grid(row=0, column=1)
    LocationButton.grid(row=0, column=2)
    tk.Button(map_frame, text='Back to Main', command=goto_main_frame,
              font=('Big Caslon', 20)).grid(row=0, column=4, padx=60)


def goto_sort_frame():
    """show the result of sorted canteens"""

    # erasing other frames and displaying sort_frame
    map_frame.grid_forget()
    sub_frame.grid_forget()
    main_frame.grid_forget()
    canteen_frame.grid_forget()
    food_price_frame.grid_forget()
    sort_frame.grid()

    # frame labels
    sort_label = tk.Label(sort_frame, text='Please select one sorting criteria.',
                            font=('Big Caslon', 25))
    sort_label.grid(row=0, column=0, columnspan=3, sticky='w', pady=10)
    Distance.grid(row=1, column=0, padx=2)
    Price.grid(row=1, column=1, padx=2)
    Rank.grid(row=1, column=2, padx=2)
    tk.Button(sort_frame, text='Back to Main', command=goto_main_frame, width=10,
              font=('Big Caslon', 15)).grid(row=1, column=3)


def goto_distance():
    """pop up canteens sorted by distance"""

    # erasing other windows
    for widget in sub_frame.winfo_children():
        widget.destroy()
    sub_frame.grid(row=2, column=0, columnspan=5, sticky='nw')

    ranklist = sort_by_distance(canteen_information)  # getting the sorted list

    # displaying the sorted canteens
    var = tk.StringVar()
    message = display_ranking(ranklist, 'distance')
    var.set(message)
    tk.Message(sub_frame, textvariable=var, width=300,
               font=('Big Caslon', 20)).grid(row=0, column=0, columnspan=4, sticky='nw')

    # displaying the message of recommendation
    recommendation = tk.StringVar()
    msg = display_recommendation(ranklist, 'distance')
    recommendation.set(msg)
    tk.Message(sub_frame, textvariable=recommendation, width=450,
               font=('Big Caslon', 20)).grid(row=0, column=4, columnspan=4, sticky='nw', padx=100)

    # load image of the most recommended canteen
    # go to the corresponding canteen window when clicking the image
    imageLabel_d = tk.Label(sub_frame, text='Click the image to find more info', font=('Big Caslon', 20))
    imageLabel_d.grid(row=1, column=5, columnspan=3)
    imageButton_d = tk.Button(sub_frame, image=display_image(ranklist),
                              command=lambda: (goto_canteen_frame(), decide_canteen(ranklist)))
    imageButton_d.grid(row=2, column=6)


def goto_price():
    """pop up canteens sorted by price"""

    # erasing other windows
    for widget in sub_frame.winfo_children():
        widget.destroy()
    sub_frame.grid(row=2, columnspan=3, sticky='nw', pady=10)

    ranklist = sort_by_price(canteen_information)  # getting the sorted list

    # displaying the sorted canteens
    var = tk.StringVar()
    message = display_ranking(ranklist, 'price')
    var.set(message)
    tk.Message(sub_frame, textvariable=var, width=300,
               font=('Big Caslon', 20)).grid(row=0, column=0, columnspan=4, sticky='nw')

    # displaying the message of recommendation
    recommendation = tk.StringVar()
    msg = display_recommendation(ranklist, 'price')
    recommendation.set(msg)
    tk.Message(sub_frame, textvariable=recommendation, width=350,
               font=('Big Caslon', 20)).grid(row=0, column=4, columnspan=4, sticky='nw', padx=100)

    # load image of the most recommended canteen
    # go to the corresponding canteen window when clicking the image
    imageLabel_p = tk.Label(sub_frame, text='Click the image to find more info', font=('Big Caslon', 20))
    imageLabel_p.grid(row=1, column=5, columnspan=3)
    imageButton_p = tk.Button(sub_frame, image=display_image(ranklist),
                              command=lambda: (goto_canteen_frame(), decide_canteen(ranklist)))
    imageButton_p.grid(row=2, column=6)


def goto_rank():
    """pop up canteens sorted by rank"""

    # erasing other windows
    for widget in sub_frame.winfo_children():
        widget.destroy()
    sub_frame.grid(row=2, columnspan=3, sticky='nw', pady=10)

    ranklist = sort_by_rank(canteen_information)

    # displaying the sorted canteens
    var = tk.StringVar()
    message = display_ranking(ranklist, 'rank')
    var.set(message)
    tk.Message(sub_frame, textvariable=var, width=300,
               font=('Big Caslon', 20)).grid(row=0, column=0, columnspan=4, sticky='nw')

    # displaying the message of recommendation
    recommendation = tk.StringVar()
    msg = display_recommendation(ranklist, 'rank')
    recommendation.set(msg)
    tk.Message(sub_frame, textvariable=recommendation, width=300,
               font=('Big Caslon', 20)).grid(row=0, column=4, columnspan=4, sticky='nw', padx=100)

    # load image of the most recommended canteen
    # go to the corresponding canteen window when clicking the image
    imageLabel_r = tk.Label(sub_frame, text='Click the image to find more info', font=('Big Caslon', 20))
    imageLabel_r.grid(row=1, column=5, columnspan=3)
    imageButton_r = tk.Button(sub_frame, image=display_image(ranklist),
                              command=lambda: (goto_canteen_frame(), decide_canteen(ranklist)))
    imageButton_r.grid(row=2, column=6)


def decide_canteen(ranklist):
    """go to different canteens according to sorting results"""

    for value in ranklist[0].values():  # get the most recommended canteen
        canteen = value

    if canteen == 'Canteen 1':
        goto_can1()
    elif canteen == 'Canteen 2':
        goto_can2()
    elif canteen == 'Canteen 9':
        goto_can9()
    elif canteen == 'Canteen 11':
        goto_can11()
    elif canteen == 'Canteen 13':
        goto_can13()
    elif canteen == 'Canteen 14':
        goto_can14()
    elif canteen == 'Canteen 16':
        goto_can16()
    elif canteen == 'North Hill':
        goto_cannh()
    elif canteen == 'Canteen Pioneer':
        goto_canp()
    else:
        goto_canf()


def goto_food_price_frame():
    """show the frame for searching canteen by food / price"""

    # erasing other frames and displaying the food_price_frame
    main_frame.grid_forget()
    update_frame.grid_forget()
    canteen_frame.grid_forget()
    sort_frame.grid_forget()
    rate_frame.grid_forget()
    food_price_frame.grid()

    # frame labels
    tk.Button(food_price_frame, text='back to main', font=('Big Caslon', 20),
              command=lambda: goto_main_frame()).grid(row=1, column=7)


def show_food(entry):
    """display canteens with wanted food"""

    # erasing other windows
    for widget in show_frame.winfo_children():
        widget.destroy()

    show_frame.grid(row=2, rowspan=10, column=4, columnspan=4)

    wanted_food = entry.get()
    canteens = search_by_food(canteen_information, wanted_food)
    print(canteens)
    canteen_list = []
    if canteens:
        for i in canteens:
            for value in i.values():
                if value == 'Canteen 1' or value == 'Canteen 2' or value == 'Canteen 9' \
                        or value == 'Canteen 11':
                    value_1 = str(value + '\t')  # to change the display format
                else:
                    value_1 = value
                info = value_1 + '\t' + str(canteen_information[value]['distance']) + \
                    '\t' + str(canteen_information[value]['price'])
                canteen_list.append(info)

    # check whether such canteen exists
    if canteen_list:
        msg = 'Name\t\tDistance\tPrice\n' + '\n'.join(canteen_list)

        var = tk.StringVar()
        var.set(msg)
        FoodMessage = tk.Message(show_frame, textvariable=var, font=('Big Caslon', 20), width=1000)
        FoodMessage.grid(column=0, columnspan=4, sticky='nw')
    else:
        messagebox.showwarning("Sorry", "No canteens are found.")


def goto_search_food():
    """pop up window for getting user inputs of wanted food"""

    # erasing other windows
    show_frame.grid_forget()
    price_frame.grid_forget()
    for widget in food_frame.winfo_children():
        widget.destroy()

    # window settings
    food_frame.grid(row=2, rowspan=3, column=0, columnspan=4)
    FoodType = tk.Label(food_frame, text='Suggested food:'
                                         '\nchicken rice, fried rice, mixed rice, western, chinese, '
                                         '\nvegiterian, mala, indian, japanese, fish soup, '
                                         '\ncarrot cake, hokkien mee, ayam penyet, \nwaffles, noodles, pasta',
                        font=('Big Caslon', 15), width=40)
    FoodType.grid(row=0, pady=10)
    FoodLabel = tk.Label(food_frame, text='Enter the food you want', font=('Big Caslon', 25))
    sample_food = tk.StringVar()
    sample_food.set("chicken rice")
    FoodEntry = tk.Entry(food_frame, textvariable=sample_food, font=('Big Caslon', 15), width=15)
    ConfirmFood = tk.Button(food_frame, text='Search', command=lambda: show_food(FoodEntry),
                            font=('Big Caslon', 20))

    FoodLabel.grid(row=1, pady=10)
    FoodEntry.grid(row=2)
    ConfirmFood.grid(row=4)


def show_price(upper_entry, lower_entry):
    """display cannteens with wanted price"""

    # erasing other windows
    for widget in show_frame.winfo_children():
        widget.destroy()

    show_frame.grid(row=2, rowspan=10, column=4, columnspan=4)

    # getting valid user input
    upper_str = upper_entry.get()
    lower_str = lower_entry.get()
    try:
        upper_int = int(upper_str)
        lower_int = int(lower_str)
        canteen = search_by_price(canteen_information, upper_int, lower_int)
        canteen_list = []

        for i in canteen:
            if i == 'Canteen 1' or i == 'Canteen 2' or i == 'Canteen 9' or i == 'Canteen 11':
                i_1 = i + '\t'  # to change the display format
            else:
                i_1 = i
            info = i_1 + '\t' + str(canteen_information[i]['distance']) + \
                   '\t' + str(canteen_information[i]['rank'])
            canteen_list.append(info)

        # check whether such canteen exists
        if canteen_list:
            msg = 'Name\t\tDistance\tRank\n' + '\n'.join(canteen_list)
            var = tk.StringVar()
            var.set(msg)
            PriceMessage = tk.Message(show_frame, textvariable=var, font=('Big Caslon', 20), width=1000)
            PriceMessage.grid(column=0, columnspan=4, sticky='nw')
        else:
            messagebox.showwarning("Sorry", "No canteens are found.")
    except:
        messagebox.showwarning("Invalid Input", "Please enter a positive number.")


def goto_search_price():
    """pop up window for getting user inputs of wanted prices"""

    # erasing other windows
    show_frame.grid_forget()
    food_frame.grid_forget()
    for widget in price_frame.winfo_children():
        widget.destroy()

    # window settings
    price_frame.grid(row=2, rowspan=4, column=0, columnspan=4)
    PriceLabel = tk.Label(price_frame, text='Enter the lower & upper limit of price', font=('Big Caslon', 25))
    UpperLabel = tk.Label(price_frame, text='Upper limit', font=('Big Caslon', 20))
    LowerLabel = tk.Label(price_frame, text='Lower limit', font=('Big Caslon', 20))
    UpperEntry = tk.Entry(price_frame, width=5)
    LowerEntry = tk.Entry(price_frame, width=5)
    ConfirmPrice = tk.Button(price_frame, text='Search', command=lambda: show_price(UpperEntry, LowerEntry),
                             font=('Big Caslon', 20))
    PriceLabel.grid(row=0, column=0, columnspan=2)
    UpperLabel.grid(row=1, column=0)
    LowerLabel.grid(row=2, column=0)
    UpperEntry.grid(row=1, column=1)
    LowerEntry.grid(row=2, column=1)
    ConfirmPrice.grid(row=3)


def goto_rate_frame():
    """show the frame for getting user feedback"""

    # erasing other frames and displaying the rate_frame
    main_frame.grid_forget()
    rate_frame.grid()

    # frame labels
    rateTitle.grid(row=0, column=0, columnspan=7)
    sub_rate_frame.grid(row=1, rowspan=12, column=1, columnspan=6)
    Can1_rate.grid(row=1, column=0, pady=10)
    Can2_rate.grid(row=2, column=0, pady=10)
    Can9_rate.grid(row=3, column=0, pady=10)
    Can11_rate.grid(row=4, column=0, pady=10)
    Can13_rate.grid(row=5, column=0, pady=10)
    Can14_rate.grid(row=6, column=0, pady=10)
    Can16_rate.grid(row=7, column=0, pady=10)
    Cannh_rate.grid(row=8, column=0, pady=10)
    Canp_rate.grid(row=9, column=0, pady=10)
    Canf_rate.grid(row=10, column=0, pady=10)
    tk.Button(rate_frame, text='Back to Main', command=goto_main_frame,
              font=('Big Caslon', 20)).grid(row=11, column=0, pady=60)


def rate(canteen):
    """pop up the feedback window"""

    for widget in sub_rate_frame.winfo_children():
        widget.destroy()  # erasing other windows

    # window settings
    text = tk.StringVar()
    text.set('How do you like ' + canteen)
    Can = tk.Label(sub_rate_frame, textvariable=text, font=('Apple Chancery', 30))
    Can.grid(column=0, columnspan=6, row=0, pady=50, sticky='w')

    rate = tk.Label(sub_rate_frame, text='Give a score 0~5', font=('Big Caslon', 20))
    rate.grid(row=1, column=0, columnspan=3, pady=10, sticky='w')
    comment = tk.Label(sub_rate_frame, text='Leave your comments below', font=('Big Caslon', 20))
    comment.grid(row=1, column=3, columnspan=3, pady=10)

    Can_ratebox = tk.Entry(sub_rate_frame, width=10)
    Can_ratebox.grid(row=2, column=0, columnspan=2, pady=10)
    Can_commentbox = tk.Entry(sub_rate_frame, width=45)
    Can_commentbox.grid(row=2, column=3, columnspan=3, pady=10, sticky='we')

    Confirm_rate = tk.Button(sub_rate_frame, text='OK', font=('Big Caslon', 20),
                              command=lambda: (add_comments(canteen_information, canteen, Can_commentbox),
                                               add_rate(canteen_information, canteen, Can_ratebox)))
    Confirm_rate.grid(row=3, column=5, pady=10, sticky='e')

    imgLabel = tk.Label(sub_rate_frame, image=img)
    imgLabel.grid(row=4, column=0, columnspan=6, sticky='nw')


def goto_update_frame():
    """show the frame for updating canteen information"""

    # erasing other frames and displaying the update_frame
    main_frame.grid_forget()
    update_frame.grid()
    canteen_frame.grid_forget()
    food_price_frame.grid_forget()

    # frame labels
    label.grid(row=0, column=0, columnspan=3, pady=20, padx=30)
    Can1_info.grid(row=1, column=1, pady=10)
    Can2_info.grid(row=2, column=1, pady=10)
    Can9_info.grid(row=3, column=1, pady=10)
    Can11_info.grid(row=4, column=1, pady=10)
    Can13_info.grid(row=5, column=1, pady=10)
    Can14_info.grid(row=6, column=1, pady=10)
    Can16_info.grid(row=7, column=1, pady=10)
    Cannh_info.grid(row=8, column=1, pady=10)
    Canp_info.grid(row=9, column=1, pady=10)
    Canf_info.grid(row=10, column=1, pady=10)
    tk.Button(update_frame, text='Back to Main', command=goto_main_frame,
              font=('Big Caslon', 20)).grid(row=11, column=1, pady=60)


def update_info(canteen):
    """pop up the window to get user input of new information of canteens"""

    # window settings
    text = 'Update information of ' + canteen
    var = tk.StringVar()
    var.set(text)
    UpdateLabel = tk.Label(update_frame, textvariable=var, font=('Big Caslon', 20))
    UpdateLabel.grid(column=3, columnspan=3, row=3, padx=30)

    tk.Label(update_frame, text='New Location', font=('Big Caslon', 20)).grid(column=3, row=4)
    location_entry = tk.Entry(update_frame)
    location_entry.grid(column=4, row=4)

    tk.Label(update_frame, text='New Price', font=('Big Caslon', 20)).grid(column=3, row=5)
    price_entry = tk.Entry(update_frame)
    price_entry.grid(column=4, row=5)

    tk.Label(update_frame, text='New Food', font=('Big Caslon', 20)).grid(column=3, row=6)
    food_entry = tk.Entry(update_frame)
    food_entry.grid(column=4, row=6)

    tk.Label(update_frame, text='New Tel', font=('Big Caslon', 20)).grid(column=3, row=7)
    tel_entry = tk.Entry(update_frame)
    tel_entry.grid(column=4, row=7)

    confirm_location = tk.Button(update_frame, text='Confirm Location', font=('Big Caslon', 20), width=15,
                                command=lambda: update_location(canteen_information, canteen, location_entry))
    confirm_location.grid(column=5, row=4, padx=10)

    confirm_price = tk.Button(update_frame, text='Confirm Price', font=('Big Caslon', 20),width=15,
                             command=lambda: update_price(canteen_information, canteen, price_entry))
    confirm_price.grid(column=5, row=5)

    confirm_food = tk.Button(update_frame, text='Confirm Food', font=('Big Caslon', 20), width=15,
                            command=lambda: update_food(canteen_information, canteen, food_entry))
    confirm_food.grid(column=5, row=6)

    confirm_tel = tk.Button(update_frame, text='Confirm Tel', font=('Big Caslon', 20), width=15,
                            command=lambda: update_tel(canteen_information, canteen, tel_entry))
    confirm_tel.grid(column=5, row=7)


def goto_main_frame():
    """show the main frame"""

    # erasing other frames and displaying the main_frame
    sort_frame.grid_forget()
    rate_frame.grid_forget()
    update_frame.grid_forget()
    map_frame.grid_forget()
    canteen_frame.grid_forget()
    food_price_frame.grid_forget()

    # frame labels
    main_frame.grid()
    Welcome_label.grid(row=1, column=0, columnspan=6, sticky='news')
    Function_label.grid(row=2, column=0, sticky='w')

    List_label.grid(row=4, column=0, sticky='w')
    SetLocation.grid(row=3, column=0, columnspan=2, sticky='news')
    SearchButton.grid(row=3, column=2, columnspan=1, sticky='news')
    SortButton.grid(column=3, columnspan=1, row=3, sticky='news')
    RateButton.grid(column=4, row=3, columnspan=1, sticky='news')
    UpdateButton.grid(column=5, row=3, columnspan=1, sticky='news')

    Can1_Button.grid(row=5, column=0)
    Can2_Button.grid(row=5, column=1)
    Can9_Button.grid(row=5, column=2)
    Can11_Button.grid(row=5, column=3)
    Can13_Button.grid(row=5, column=4)
    Can14_Button.grid(row=5, column=5)
    Can16_Button.grid(row=6, column=1)
    CanNH_Button.grid(row=6, column=2)
    CanP_Button.grid(row=6, column=3)
    CanF_Button.grid(row=6, column=4)

    canvas.grid(columnspan=2, row=0, column=2)


def goto_canteen_frame():
    """pop up the window for showing detailed information of each canteen"""

    # frame labels
    main_frame.grid_forget()
    map_frame.grid_forget()
    sub_frame.grid_forget()
    sort_frame.grid_forget()
    food_price_frame.grid_forget()

    canteen_frame.grid()


def goto_can1():
    for widget in canteen_frame.winfo_children():
        widget.destroy()

    canteen_frame.grid()
    can_label = tk.Label(canteen_frame, text='Welcome to NTU canteen ---- Canteen 1!', font=('Zapfino', 35))
    can_label.grid(row=0, column=0, columnspan=7, sticky='news')

    can_canvas = tk.Canvas(canteen_frame, height=200, width=250)
    can_img = can_canvas.create_image(0, 0, anchor='nw', image=can1_img_file)
    can_canvas.grid(row=2, rowspan=15, column=0, columnspan=2, sticky='news', pady=80, padx=25)


    tk.Button(canteen_frame, text='Back to Main', font=('Big Caslon', 20),
              command=goto_main_frame).grid(row=1, column=6, sticky='ne')


    information = display_information(canteen_information, 'Canteen 1')
    info = tk.StringVar()
    info.set(information)
    info_msg = tk.Message(canteen_frame, textvariable=info, font=('Big Caslon', 20))
    info_msg.grid(row=2, rowspan=15, column=2, columnspan=5, pady=40)


def goto_can2():
    for widget in canteen_frame.winfo_children():
        widget.destroy()

    canteen_frame.grid()
    can_label = tk.Label(canteen_frame, text='Welcome to NTU canteen ---- Canteen 2!', font=('Zapfino', 35))
    can_label.grid(row=0, column=0, columnspan=7, sticky='news')

    can_canvas = tk.Canvas(canteen_frame, height=200, width=250)
    can_img = can_canvas.create_image(0, 0, anchor='nw', image=can2_img_file)
    can_canvas.grid(row=2, rowspan=15, column=0, columnspan=2, sticky='news', pady=80, padx=25)

    tk.Button(canteen_frame, text='Back to Main', font=('Big Caslon', 20),
              command=goto_main_frame).grid(row=1, column=6, sticky='ne')


    information = display_information(canteen_information, 'Canteen 2')
    info = tk.StringVar()
    info.set(information)
    info_msg = tk.Message(canteen_frame, textvariable=info, font=('Big Caslon', 20))
    info_msg.grid(row=2, rowspan=15, column=2, columnspan=5, pady=40)


def goto_can9():
    for widget in canteen_frame.winfo_children():
        widget.destroy()
    canteen_frame.grid()
    can_label = tk.Label(canteen_frame, text='Welcome to NTU canteen ---- Canteen 9!', font=('Zapfino', 35))
    can_label.grid(row=0, column=0, columnspan=7, sticky='news')

    can_canvas = tk.Canvas(canteen_frame, height=200, width=250)
    can_img = can_canvas.create_image(0, 0, anchor='nw', image=can9_img_file)
    can_canvas.grid(row=2, rowspan=15, column=0, columnspan=2, sticky='news', pady=80, padx=25)

    tk.Button(canteen_frame, text='Back to Main', font=('Big Caslon', 20),
              command=goto_main_frame).grid(row=1, column=6, sticky='ne')


    information = display_information(canteen_information, 'Canteen 9')
    info = tk.StringVar()
    info.set(information)
    info_msg = tk.Message(canteen_frame, textvariable=info, font=('Big Caslon', 20))
    info_msg.grid(row=2, rowspan=15, column=2, columnspan=5, pady=40)


def goto_can11():
    for widget in canteen_frame.winfo_children():
        widget.destroy()
    canteen_frame.grid()
    can_label = tk.Label(canteen_frame, text='Welcome to NTU canteen ----- Canteen 11!', font=('Zapfino', 34))
    can_label.grid(row=0, column=0, columnspan=7, sticky='news')

    can_canvas = tk.Canvas(canteen_frame, height=200, width=250)
    can_img = can_canvas.create_image(0, 0, anchor='nw', image=can11_img_file)
    can_canvas.grid(row=2, rowspan=15, column=0, columnspan=2, sticky='news', pady=80, padx=25)

    tk.Button(canteen_frame, text='Back to Main', font=('Big Caslon', 20),
              command=goto_main_frame).grid(row=1, column=6, sticky='ne')


    information = display_information(canteen_information, 'Canteen 11')
    info = tk.StringVar()
    info.set(information)
    info_msg = tk.Message(canteen_frame, textvariable=info, font=('Big Caslon', 20))
    info_msg.grid(row=2, rowspan=15, column=2, columnspan=5, pady=40)


def goto_can13():
    for widget in canteen_frame.winfo_children():
        widget.destroy()
    canteen_frame.grid()
    can_label = tk.Label(canteen_frame, text='Welcome to NTU canteen ----- Canteen 13!', font=('Zapfino', 34))
    can_label.grid(row=0, column=0, columnspan=7, sticky='news')

    can_canvas = tk.Canvas(canteen_frame, height=200, width=250)
    can_img = can_canvas.create_image(0, 0, anchor='nw', image=can13_img_file)
    can_canvas.grid(row=2, rowspan=15, column=0, columnspan=2, sticky='news', pady=80, padx=25)

    tk.Button(canteen_frame, text='Back to Main', font=('Big Caslon', 20),
              command=goto_main_frame).grid(row=1, column=6, sticky='ne')


    information = display_information(canteen_information, 'Canteen 13')
    info = tk.StringVar()
    info.set(information)
    info_msg = tk.Message(canteen_frame, textvariable=info, font=('Big Caslon', 20))
    info_msg.grid(row=2, rowspan=15, column=2, columnspan=5, pady=40)


def goto_can14():
    for widget in canteen_frame.winfo_children():
        widget.destroy()
    canteen_frame.grid()
    can_label = tk.Label(canteen_frame, text='Welcome to NTU canteen ---- Canteen 14!', font=('Zapfino', 34))
    can_label.grid(row=0, column=0, columnspan=7, sticky='news')

    can_canvas = tk.Canvas(canteen_frame, height=200, width=250)
    can_img = can_canvas.create_image(0, 0, anchor='nw', image=can14_img_file)
    can_canvas.grid(row=2, rowspan=15, column=0, columnspan=2, sticky='news', pady=80, padx=25)

    tk.Button(canteen_frame, text='Back to Main', font=('Big Caslon', 20),
              command=goto_main_frame).grid(row=1, column=6, sticky='ne')


    information = display_information(canteen_information, 'Canteen 14')
    info = tk.StringVar()
    info.set(information)
    info_msg = tk.Message(canteen_frame, textvariable=info, font=('Big Caslon', 20))
    info_msg.grid(row=2, rowspan=15, column=2, columnspan=5, pady=40)


def goto_can16():
    for widget in canteen_frame.winfo_children():
        widget.destroy()
    canteen_frame.grid()
    can_label = tk.Label(canteen_frame, text='Welcome to NTU canteen ---- Canteen 16!', font=('Zapfino', 34))
    can_label.grid(row=0, column=0, columnspan=7, sticky='news')

    can_canvas = tk.Canvas(canteen_frame, height=200, width=250)
    can_img = can_canvas.create_image(0, 0, anchor='nw', image=can16_img_file)
    can_canvas.grid(row=2, rowspan=15, column=0, columnspan=2, sticky='news', pady=80, padx=25)

    tk.Button(canteen_frame, text='Back to Main', font=('Big Caslon', 20),
              command=goto_main_frame).grid(row=1, column=6, sticky='ne')


    information = display_information(canteen_information, 'Canteen 16')
    info = tk.StringVar()
    info.set(information)
    info_msg = tk.Message(canteen_frame, textvariable=info, font=('Big Caslon', 20))
    info_msg.grid(row=2, rowspan=15, column=2, columnspan=5, pady=40)


def goto_cannh():
    for widget in canteen_frame.winfo_children():
        widget.destroy()
    canteen_frame.grid()
    can_label = tk.Label(canteen_frame, text='Welcome to NTU canteen ---- North Hill!', font=('Zapfino', 34))
    can_label.grid(row=0, column=0, columnspan=7, sticky='news')

    can_canvas = tk.Canvas(canteen_frame, height=200, width=250)
    can_img = can_canvas.create_image(0, 0, anchor='nw', image=cannh_img_file)
    can_canvas.grid(row=2, rowspan=15, column=0, columnspan=2, sticky='news', pady=80, padx=25)

    tk.Button(canteen_frame, text='Back to Main', font=('Big Caslon', 20),
              command=goto_main_frame).grid(row=1, column=6, sticky='ne')


    information = display_information(canteen_information, 'North Hill')
    info = tk.StringVar()
    info.set(information)
    info_msg = tk.Message(canteen_frame, textvariable=info, font=('Big Caslon', 20))
    info_msg.grid(row=2, rowspan=15, column=2, columnspan=5, pady=40)


def goto_canp():
    for widget in canteen_frame.winfo_children():
        widget.destroy()
    canteen_frame.grid()
    can_label = tk.Label(canteen_frame, text='Welcome to NTU canteen ----- Canteen Pioneer!', font=('Zapfino', 31))
    can_label.grid(row=0, column=0, columnspan=7, sticky='news')

    can_canvas = tk.Canvas(canteen_frame, height=200, width=250)
    can_img = can_canvas.create_image(0, 0, anchor='nw', image=canp_img_file)
    can_canvas.grid(row=2, rowspan=15, column=0, columnspan=2, sticky='news', pady=80, padx=25)

    tk.Button(canteen_frame, text='Back to Main', font=('Big Caslon', 20),
              command=goto_main_frame).grid(row=1, column=6, sticky='ne')


    information = display_information(canteen_information, 'Canteen Pioneer')
    info = tk.StringVar()
    info.set(information)
    info_msg = tk.Message(canteen_frame, textvariable=info, font=('Big Caslon', 20))
    info_msg.grid(row=2, rowspan=15, column=2, columnspan=5, pady=40)


def goto_canf():
    for widget in canteen_frame.winfo_children():
        widget.destroy()
    canteen_frame.grid()
    can_label = tk.Label(canteen_frame, text='Welcome to NTU canteen ---- Canteen Foodgle!', font=('Zapfino', 31))
    can_label.grid(row=0, column=0, columnspan=7, sticky='news')

    can_canvas = tk.Canvas(canteen_frame, height=200, width=250)
    can_img = can_canvas.create_image(0, 0, anchor='nw', image=canf_img_file)
    can_canvas.grid(row=2, rowspan=15, column=0, columnspan=2, sticky='news', pady=80, padx=25)

    tk.Button(canteen_frame, text='Back to Main', font=('Big Caslon', 20),
              command=goto_main_frame).grid(row=1, column=6, sticky='ne')


    information = display_information(canteen_information, 'Canteen Foodgle')
    info = tk.StringVar()
    info.set(information)
    info_msg = tk.Message(canteen_frame, textvariable=info, font=('Big Caslon', 20))
    info_msg.grid(row=2, rowspan=15, column=2, columnspan=5, pady=40)



# -------------------------------------------------------------------------------------------------------------------- #

# * Settings for Graphical User Interface (GUI)  #

# The following codes are used to set the GUI display
window = tk.Tk()
window.geometry('970x720')
window.resizable(width=False, height=False)
window.title('NTU Canteen')
main_frame = tk.Frame(window, width=810, height=640)
main_frame.grid()


# main_frame settings * Done By: Yusuf * #

Welcome_label = tk.Label(main_frame, text="Welcome to NTU food court search engine!", font=('Zapfino', 25))
Welcome_label.grid(row=1, column=0, columnspan=6, sticky='news')
Function_label = tk.Label(main_frame, text="Functions:", font=('Zapfino', 20))
Function_label.grid(row=2, column=0, sticky='w')
List_label = tk.Label(main_frame, text='Canteen List:', font=('Zapfino', 20))
List_label.grid(row=4, column=0, sticky='w')
SetLocation = tk.Button(main_frame, text='Set location', font=('Apple Chancery', 20), width=24,
                        command=goto_map_frame)
SetLocation.grid(row=3, column=0, columnspan=2, sticky='news')
SearchButton = tk.Button(main_frame, text='Search canteen', width=12, font=('Apple Chancery', 20),
                       command=lambda: goto_food_price_frame())
SearchButton.grid(row=3, column=2, columnspan=1, sticky='news')
SortButton = tk.Button(main_frame, text='Sort Canteen', command=goto_sort_frame,
                       width=12, font=('Apple Chancery', 20))
SortButton.grid(column=3, columnspan=1, row=3, sticky='news')
RateButton = tk.Button(main_frame, text='Rate Canteen', command=goto_rate_frame,
                       width=12, font=('Apple Chancery', 20))
RateButton.grid(column=4, row=3, columnspan=1, sticky='news')
UpdateButton = tk.Button(main_frame, text='Update Info', command=goto_update_frame,
                         width=12, font=('Apple Chancery', 20))
UpdateButton.grid(column=5, row=3, columnspan=1, sticky='news')

# load image to main_frame
canvas = tk.Canvas(main_frame, height=200, width=200)
image_file = tk.PhotoImage(file='logo.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.grid(columnspan=2, row=0, column=2)


# map frames settings * Done By: Yusuf * #
map_frame = tk.Frame(window, width=970, height=700)
position = tk.StringVar()
position.set("0 , 0")
map_label = tk.Label(map_frame, text='Enter your location here or\ndouble click your position on the map',
                     font=('Big Caslon', 20))
LocationEntry = tk.Entry(map_frame,textvariable=position, width=10)
LocationButton = tk.Button(map_frame, text="Confirm location", font=('Big Caslon', 20),
                           command=lambda: enter_location(LocationEntry))
canvas_1 = tk.Canvas(map_frame, height=650, width=965)
image_file_1 = tk.PhotoImage(file='NTU map.gif')
image_1 = canvas_1.create_image(0, 0, anchor='nw', image=image_file_1)


# sort frame settings  Done By: Dou Maokang ** #
sort_frame = tk.Frame(window, height=640, width=810)
sub_frame = tk.Frame(sort_frame, width=750)

Distance = tk.Button(sort_frame, text='Distance', command=goto_distance, width=23, font=('Big Caslon', 20))
Price = tk.Button(sort_frame, text='Price', command=goto_price, width=23, font=('Big Caslon', 20))
Rank = tk.Button(sort_frame, text='Rank', command=goto_rank, width=23, font=('Big Caslon', 20))
back_to_main = tk.Button(sort_frame, text='Back to Main', command=goto_main_frame, width=10, font=('Big Caslon', 20))


# food and price frame settings ** Done By: Dou Maokang ** #
food_price_frame = tk.Frame(window)
food_frame = tk.Frame(food_price_frame)
price_frame = tk.Frame(food_price_frame)
show_frame = tk.Frame(food_price_frame)
FoodButton = tk.Button(food_price_frame, text='Search by Food', font=('Big Caslon', 20),
                       command=goto_search_food)
FoodButton.grid(row=1, column=1, columnspan=2, pady=30)
PriceButton = tk.Button(food_price_frame, text='Search by Price', font=('Big Caslon', 20),
                        command=goto_search_price)
PriceButton.grid(row=1, column=5, columnspan=2, pady=30)

# load image to food price frame
canvas_2 = tk.Canvas(food_price_frame, height=220, width=970)
image_file_2 = tk.PhotoImage(file='NTUfood.gif')
image_2 = canvas_2.create_image(10, 0, anchor='nw', image=image_file_2)
canvas_2.grid(columnspan=8, row=0, column=0, sticky='we')


# rating frame settings *  * #
rate_frame = tk.Frame(window, width=970, height=720)
sub_rate_frame = tk.Frame(rate_frame)
img = tk.PhotoImage(file='comments.gif')
rateTitle = tk.Label(rate_frame, text='  --- Welcome to the Food Court Rating System --- ',
                     font=('Apple Chancery', 45))
label = tk.Label(rate_frame, text='Please choose a canteen', font=('Big Caslon', 25))
Can1_rate = tk.Button(rate_frame, text='Canteen 1', command=lambda: rate('Canteen 1'), font=('Big Caslon', 20))
Can2_rate = tk.Button(rate_frame, text='Canteen 2', command=lambda: rate('Canteen 2'), font=('Big Caslon', 20))
Can9_rate = tk.Button(rate_frame, text='Canteen 9', command=lambda: rate('Canteen 9'), font=('Big Caslon', 20))
Can11_rate = tk.Button(rate_frame, text='Canteen 11', command=lambda: rate('Canteen 11'), font=('Big Caslon', 20))
Can13_rate = tk.Button(rate_frame, text='Canteen 13', command=lambda: rate('Canteen 13'), font=('Big Caslon', 20))
Can14_rate = tk.Button(rate_frame, text='Canteen 14', command=lambda: rate('Canteen 14'), font=('Big Caslon', 20))
Can16_rate = tk.Button(rate_frame, text='Canteen 16', command=lambda: rate('Canteen 16'), font=('Big Caslon', 20))
Cannh_rate = tk.Button(rate_frame, text='North Hill', command=lambda: rate('North Hill'), font=('Big Caslon', 20))
Canp_rate = tk.Button(rate_frame, text='Canteen Pioneer', command=lambda: rate('Canteen Pioneer'), font=('Big Caslon', 20))
Canf_rate = tk.Button(rate_frame, text='Canteen Foodgle', command=lambda: rate('Canteen Foodgle'), font=('Big Caslon', 20))


# update frame settings  Done By: Yusuf  #
update_frame = tk.Frame(window)
label = tk.Label(update_frame, text='Please choose a canteen to \nupdate its information.',
                 font=('Big Caslon', 25))
Can1_info = tk.Button(update_frame, text='Canteen 1', command=lambda: update_info('Canteen 1'),
                      font=('Big Caslon', 20))
Can2_info = tk.Button(update_frame, text='Canteen 2', command=lambda: update_info('Canteen 2'),
                      font=('Big Caslon', 20))
Can9_info = tk.Button(update_frame, text='Canteen 9', command=lambda: update_info('Canteen 9'),
                      font=('Big Caslon', 20))
Can11_info = tk.Button(update_frame, text='Canteen 11', command=lambda: update_info('Canteen 11'),
                       font=('Big Caslon', 20))
Can13_info = tk.Button(update_frame, text='Canteen 13', command=lambda: update_info('Canteen 13'),
                       font=('Big Caslon', 20))
Can14_info = tk.Button(update_frame, text='Canteen 14', command=lambda: update_info('Canteen 14'),
                       font=('Big Caslon', 20))
Can16_info = tk.Button(update_frame, text='Canteen 16', command=lambda: update_info('Canteen 16'),
                       font=('Big Caslon', 20))
Cannh_info = tk.Button(update_frame, text='North Hill', command=lambda: update_info('North Hill'),
                       font=('Big Caslon', 20))
Canp_info = tk.Button(update_frame, text='Canteen Pioneer', command=lambda: update_info('Canteen Pioneer'),
                      font=('Big Caslon', 20))
Canf_info = tk.Button(update_frame, text='Canteen Foodgle', command=lambda: update_info('Canteen Foodgle'),
                      font=('Big Caslon', 20))


# canteen frame
canteen_frame = tk.Frame(window, width=970, height=720)
can1_img_file = tk.PhotoImage(file='1.gif')
can2_img_file = tk.PhotoImage(file='2.gif')
can9_img_file = tk.PhotoImage(file='9.gif')
can11_img_file = tk.PhotoImage(file='11.gif')
can13_img_file = tk.PhotoImage(file='13.gif')
can14_img_file = tk.PhotoImage(file='14.gif')
can16_img_file = tk.PhotoImage(file='16.gif')
cannh_img_file = tk.PhotoImage(file='nh.gif')
canp_img_file = tk.PhotoImage(file='p.gif')
canf_img_file = tk.PhotoImage(file='f.gif')

# canteen list
Can1_Button = tk.Button(main_frame, text='Canteen 1', command=lambda: (goto_canteen_frame(), goto_can1()),
                        width=13, font=('Apple Chancery', 20))
Can2_Button = tk.Button(main_frame, text='Canteen 2', command=lambda: (goto_canteen_frame(), goto_can2()),
                        width=13, font=('Apple Chancery', 20))
Can9_Button = tk.Button(main_frame, text='Canteen 9', command=lambda: (goto_canteen_frame(), goto_can9()),
                        width=13, font=('Apple Chancery', 20))
Can11_Button = tk.Button(main_frame, text='Canteen 11', command=lambda: (goto_canteen_frame(), goto_can11()),
                         width=13, font=('Apple Chancery', 20))
Can13_Button = tk.Button(main_frame, text='Canteen 13', command=lambda: (goto_canteen_frame(), goto_can13()),
                         width=13, font=('Apple Chancery', 20))
Can14_Button = tk.Button(main_frame, text='Canteen 14', command=lambda: (goto_canteen_frame(), goto_can14()),
                         width=13, font=('Apple Chancery', 20))
Can16_Button = tk.Button(main_frame, text='Canteen 16', command=lambda: (goto_canteen_frame(), goto_can16()),
                         width=13, font=('Apple Chancery', 20))
CanNH_Button = tk.Button(main_frame, text='North Hill', command=lambda: (goto_canteen_frame(), goto_cannh()),
                         width=13, font=('Apple Chancery', 20))
CanP_Button = tk.Button(main_frame, text='Canteen Pioneer', command=lambda: (goto_canteen_frame(), goto_canp()),
                        width=13, font=('Apple Chancery', 20))
CanF_Button = tk.Button(main_frame, text='Canteen Foodgle', command=lambda: (goto_canteen_frame(), goto_canf()),
                        width=13, font=('Apple Chancery', 20))

Can1_Button.grid(row=5, column=0)
Can2_Button.grid(row=5, column=1)
Can9_Button.grid(row=5, column=2)
Can11_Button.grid(row=5, column=3)
Can13_Button.grid(row=5, column=4)
Can14_Button.grid(row=5, column=5)
Can16_Button.grid(row=6, column=1)
CanNH_Button.grid(row=6, column=2)
CanP_Button.grid(row=6, column=3)
CanF_Button.grid(row=6, column=4)

# -------------------------------------------------------------------------------------------------------------------- #

cal_average_rate(canteen_information)
cal_rank(canteen_information)

window.mainloop()

# --------------------------------------------------END Of Program---------------------------------------------------- #
# ---------------------------------------------------- Thank you ----------------------------------------------------- #
