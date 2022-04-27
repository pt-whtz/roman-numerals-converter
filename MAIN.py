from tkinter import *
from tkinter import messagebox

roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

title_font = ("Courier", 35)
font = ("Courier", 15)


# --------------------------- Converter Functions ---------------------------


def decode_roman(roman):

    values = [roman_numerals[numeral] for numeral in roman]
    values.append(0)
    result = 0

    for value_id in range(0, len(values)-1):

        current_value = values[value_id]
        next_value = values[value_id + 1]

        if current_value >= next_value:
            result += current_value

        else:
            result -= current_value

    return result


def convert():

    user_entry = numeral_entry.get().upper()

    try:
        result = decode_roman(roman=user_entry)
    except KeyError:
        background.itemconfig(label_result, text="error")
        messagebox.showerror("Error", message="Please enter a valid roman numeral!")
    else:
        background.itemconfig(label_result, text=f"{result}")


# ---------------------------------- GUI ------------------------------------

# main window
window = Tk()
window.title("Roman Numerals Converter")
window.minsize(width=800, height=400)
window.resizable(width=False, height=False)

# canvas
background = Canvas(width=800, height=504)

image = PhotoImage(file="rome.png")
bg_image = background.create_image(400, 252, image=image)

bg_title = background.create_text(400, 50, text="Roman Numerals Converter", font=title_font, fill="black")
title_frame = background.create_rectangle(background.bbox(bg_title), fill="#F8ECD1")
background.tag_lower(title_frame, bg_title)

background.grid(column=0, row=0)

# text labels
label_input = background.create_text(400, 100, text="Enter a numeral", font=font, fill="black")
label_input_frame = background.create_rectangle(background.bbox(label_input), fill="#F8ECD1")
background.tag_lower(label_input_frame, label_input)

label_result = background.create_text(400, 170, text="Result", font=font, fill="black")
label_result_frame = background.create_rectangle(background.bbox(label_result), fill="#F8ECD1")
background.tag_lower(label_result_frame, label_result)

# user entries
numeral_entry = Entry(font=("Courier", 12), width=10, bg="white")
numeral_entry.focus()
numeral_entry_window = background.create_window(360, 135, window=numeral_entry)

# buttons
convert_button = Button(text="Convert", font=("Courier", 10), command=convert)
convert_button_window = background.create_window(460, 135, window=convert_button)


window.mainloop()
