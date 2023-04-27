#Elyza Jane G. Relucio
#The program reads a file with 20 students' names and GWAs, then outputs the name of the student with the highest GWA.

import tkinter as tk

# create a tkinter window
root = tk.Tk()
root.geometry("800x400")
root.title("GWA Checker")

# def function to display the result
def show_result():
    # open the file containing the student data
    file = open("Names_gwa.txt", "r")

    # read the contents of the file into a str variable
    file_contents = file.read()

    # split the str variable into a list of lines
    lines = file_contents.split("\n")

    # initialize variables to store the highest GWA and the name of the student who got it
    highest_gwa = 0
    highest_gwa_student = ""

    # loop through each line in the file
    for line in lines: 
    # split the line into two parts: the student's name and their GWA
        name, gwa_str = line.split(",")
    # convert the GWA from a string to a float
        gwa = float(gwa_str)
    # if this student has a higher GWA than the current highest GWA, update the variables
        if gwa > highest_gwa:
            highest_gwa = gwa
            highest_gwa_student = name
    # close the file
    file.close()

# create a label to display the result
    result_label = tk.Label(root, text=f"The student with the highest GWA is {highest_gwa_student} with a GWA of {highest_gwa:.2f}.",bg="violet", font=("Helvetica", 16))
    result_label.pack()

# define function to show the second page
def show_second_page():
    # remove the first page widgets
    introduction_label.pack_forget()
    next_button.pack_forget()

    # create a label for the second page
    second_page_label = tk.Label(root, text="Who has the highest GWA?", bg="light yellow", font=("Helvetica", 18,))
    second_page_label.pack()

    # create a button to display the result
    result_button = tk.Button(root, text="Check Result", command=show_result, bg="green", fg="white", font=("Helvetica", 14))
    result_button.pack()

# create a label for the introduction page
introduction_label = tk.Label(root, text="Welcome to GWA Checker", bg="light pink", font=("Helvetica", 18))
introduction_label.pack()

# create a button to go to the second page
next_button = tk.Button(root, text="Next", command=show_second_page, bg="blue", fg="white", font=("Helvetica", 14))
next_button.pack()

# run the tkinter event loop
root.mainloop()