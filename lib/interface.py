from functions import *
import customtkinter as ctk

def updatepassword():
    try:
        length = int(password_length.get())  # Convert input to integer
        if length <= 0:
            raise ValueError("Length must be positive")  # Prevent negative/zero length
        elif length > 35:
            length = 35
    except ValueError:
        password_var.set("Invalid length")  # Show error in entry
        return

    password_var.set(generatepassword(length))


def update_characters():
    set_characters(
        use_upper=upper_var.get(),
        use_lower=lower_var.get(),
        use_numbers=numbers_var.get(),
        use_special=special_var.get(),
    )


app = ctk.CTk()

    # Define window parameters
app.title('PassGen')
app.iconbitmap('img\\notpassgen (512x512).ico')
app.geometry("800x640")
app.resizable(width=False, height=False)

    # Define initial parameters
password_var = ctk.StringVar(value=generatepassword())
user_url = str()

upper_var = ctk.IntVar(value=0)
lower_var = ctk.IntVar(value=0)
numbers_var = ctk.IntVar(value=0)
special_var = ctk.IntVar(value=0)

    # Generate password button
button = ctk.CTkButton(
    app,
    command=updatepassword,
    text="Generate Password",
    width=340,
    height=50,
    corner_radius=5,
    hover_color='#1E90FF',
    text_color='White',
    font=("Helvetica", 30)
)
button.place(x=60, y=50)

    # URL entry
entry_url = ctk.CTkEntry(
    app,
    #text_variable=user_url,
    placeholder_text="URL",
    width=680,
    height=50,
    corner_radius=5,
    font=("Helvetica", 30),
    text_color='white'
)
entry_url.place(x=60, y=150)

    # Password Display
entry_password = ctk.CTkEntry(
    app,
    textvariable=password_var,
    width=580,
    height=50,
    corner_radius=5,
    font=("Helvetica", 30),
    text_color='yellow'
)
entry_password.place(x=60, y=350)

    # Refresh button
btn_refresh = ctk.CTkButton(
    app,
    command=updatepassword,
    text="⟳",
    width=50,
    height=50,
    corner_radius=5,
    border_width=0,
    fg_color='transparent',
    hover_color='#1E90FF',
    text_color='white',
    font=("Helvetica", 30)
)
btn_refresh.place(x=640, y=350)

    # Copy button
btn_copy = ctk.CTkButton(
    app,
    text="📋",
    width=50,
    height=50,
    command=password_copy,
    corner_radius=5,
    border_width=0,
    fg_color='transparent',
    hover_color='#1E90FF',
    text_color='white',
    font=("Helvetica", 30)
)
btn_copy.place(x=690, y=350)

    # Password Length Input
password_length = ctk.CTkEntry(
    app,
    placeholder_text="Password Length",
    width=680, height=50,
    corner_radius=5,
    font=("Helvetica", 30)
)
password_length.place(x=60, y=250)

    # Character Selection Checkboxes
check_upper = ctk.CTkCheckBox(
    app,
    command=update_characters,
    variable=upper_var,
    onvalue=1,
    offvalue=0,
    text=" A - Z",
    checkbox_height=50,
    checkbox_width=50,
    font=("Helvetica", 30),
    border_width=4,
    hover_color='#1E90FF'
)
check_upper.place(x=60, y=450)
#check_upper.select()

check_lower = ctk.CTkCheckBox(
    app,
    command=update_characters,
    variable=lower_var,
    onvalue=1,
    offvalue=0,
    text=" a - z",
    checkbox_height=50,
    checkbox_width=50,
    font=("Helvetica", 30),
    border_width=4,
    hover_color='#1E90FF'
)
check_lower.place(x=231, y=450)
#check_lower.select()

check_numbers = ctk.CTkCheckBox(
    app,
    command=update_characters,
    variable=numbers_var,
    onvalue=1,
    offvalue=0,
    text=" 0 - 9",
    checkbox_height=50,
    checkbox_width=50,
    font=("Helvetica", 30),
    border_width=4,
    hover_color='#1E90FF'
)
check_numbers.place(x=403, y=450)
#check_numbers.select()

check_special = ctk.CTkCheckBox(
    app,
    command=update_characters,
    variable=special_var,
    onvalue=1,
    offvalue=0,
    text=" !@#^&*",
    checkbox_height=50,
    checkbox_width=50,
    font=("Helvetica", 30),
    border_width=4,
    hover_color='#1E90FF'
)
check_special.place(x=575, y=450)
#check_special.select()

app.mainloop()
