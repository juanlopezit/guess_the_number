import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
from warnings import showwarning

window = tk.Tk()

correct_number = str(random.randint(1, 8))
print(f"Correct Number: {correct_number}")
attempts = 0

box = ttk.Entry()

########################################
# Dinamic Labels

e_first_try = tk.Label(text = "First Try", font = ("Arial", 15), fg = "red")
e_second_try = tk.Label(text = "Second Try", font = ("Arial", 15), fg = "red")
e_third_try = tk.Label(text = "Third Try", font = ("Arial", 15), fg = "red")
e_fourth_try = tk.Label(text = " One Last try", font = ("Arial", 15), fg = "red")
e_you_lose = tk.Label(text = "¡You lose!", font = ("Arial", 25), fg = "red")
e_you_win = tk.Label(text = "¡You win!", font = ("Arial", 25), fg = "green")
e_even_number = tk.Label(text = "¡Even Number!", font = ("Arial", 10), fg = "blue")
e_odd_number = tk.Label(text = "¡Odd Number!", font = ("Arial", 10), fg = "blue")


########################################
# Functions

def delete_odd_number():
    if e_odd_number:
        e_odd_number.place_forget()


def delete_even_number():
    if e_even_number:
        e_even_number.place_forget()

def give_a_hint():
    if correct_number == "1" or correct_number == "3" or correct_number == "5" or correct_number == "7":
        e_odd_number.place(x = 5, y = 30)
        window.after(1100, delete_odd_number)
        
    elif correct_number == "2" or correct_number == "4" or correct_number == "6" or correct_number == "8":
        e_even_number.place(x = 5, y = 30)
        window.after(00, delete_even_number())
        

def delete_labels():
    e_first_try.place_forget()
    e_second_try.place_forget()
    e_third_try.place_forget()
    e_fourth_try.place_forget()
    e_you_lose.place_forget()


def main():
    global box
    global correct_number
    global attempts

    print(correct_number)


    while attempts < 5:
        inside_box = box.get()

        if inside_box != correct_number:
            print(f"Inside box: {inside_box}")
            attempts += 1
            box.delete(0, tk.END)

            if attempts == 1:
                e_first_try.place (x = 250, y = 60)
            elif attempts == 2:
                e_second_try.place (x = 250, y = 100)
            elif attempts == 3:
                e_third_try.place (x = 250, y = 140)
            elif attempts == 4:
                e_fourth_try.place (x = 250, y = 180)

            print(f"Attempt N°: {attempts}")

            if attempts == 5:
                # Label
                e_you_lose.place(x= 130, y = 210)

                # Question
                wrong_answer = messagebox.askyesno(title = "¡Game Over!", message="¿Do you want to play again?")

                if wrong_answer:
                    delete_labels()
                    e_you_win.place_forget()
                    correct_number = str(random.randint(1, 8))
                    print(f"Correct number: {correct_number:}")
                    
                    box.delete(0, tk.END)
                    attempts = -1
                else:
                    messagebox.showinfo(message="Thanks for playing")
                    return quit()
            else:
                break

        elif inside_box == correct_number:
            print(f"Inside box: {inside_box}")

            # Label
            e_you_win.place(x= 125, y = 210)

            # Question
            correct_answer = messagebox.askyesno(title="¡You Win!", message="¿Do you want to play again?")

            if correct_answer:
                delete_labels()
                e_you_win.place_forget()
                correct_number = str(random.randint(1, 8))
                print(f"Correct Number: {correct_number:}")

                box.delete(0, tk.END)
                attempts = 0
                
            else:
                messagebox.showinfo(message="Thanks for playing")
                return quit()
            break 
    return

    


def one():
    global box
    global correct_number
    global attempts
    box.insert(tk.END, 1)
    
    
    main()
        


def two():
    global box
    global correct_number
    global attempts
    box.insert(tk.END, 2)

    main()

        

def three():
    global box
    global correct_number
    global attempts
    box.insert(tk.END, 3)

    main()
        

def four():
    global box
    global correct_number
    global attempts
    box.insert(tk.END, 4)

    main()
        

def five():
    global box
    global correct_number
    global attempts
    box.insert(tk.END, 5)

    main()
        

def six():
    global box
    global correct_number
    global attempts
    box.insert(tk.END, 6)

    main()
        

def seven():
    global box
    global correct_number
    global attempts
    box.insert(tk.END, 7)

    main()
        

def eight():
    global box
    global correct_number
    global attempts
    box.insert(tk.END, 8)

    main()
    


########################################
# Window
window.config (width = 410, height = 360)
window.title ("Guess the Number")



########################################
# Labels
e_title = tk.Label(text = "---------- Guess the Number ----------", font = ("Arial", 15 ))
e_title.place (x = 50, y = 5)

e_title2 = tk.Label(text = "(You have five attempts)", font = ("Arial", 10))
e_title2.place (x = 135, y = 30)

e_question_sign = tk.Label(text = "¿?", font = ("Arial", 80))
e_question_sign.place(x = 30, y = 70)

e_equal_sign = tk.Label(text = "=", font = ("Arial", 20))
e_equal_sign.place(x = 200, y = 115)

e_division = tk.Label(text = "-------------------------------------------------------------------------------")
e_division.place (x = 1, y = 250)


########################################
#  Buttons
b_one = ttk.Button(text = "1", command = one)
b_one.place(x = 30, y = 280)

b_two = ttk.Button(text = "2", command = two)
b_two.place(x = 120, y = 280)

b_three = ttk.Button(text = "3", command = three)
b_three.place(x = 210, y = 280)

b_four = ttk.Button(text = "4", command = four)
b_four.place(x = 300, y = 280)

b_five = ttk.Button(text = "5", command = five)
b_five.place(x = 30, y = 320)

b_six = ttk.Button(text = "6", command = six)
b_six.place(x = 120, y = 320)

b_seven = ttk.Button(text = "7", command = seven)
b_seven.place(x = 210, y = 320)

b_eight = ttk.Button(text = "8", command = eight)
b_eight.place(x = 300, y = 320)

b_hint = ttk.Button(text = "Hint", width = 4, command = give_a_hint)
b_hint.place(x = 2, y = 2)



window.mainloop()