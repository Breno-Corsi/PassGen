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
app.iconbitmap("img\\notpassgen (512x512).ico")
app.geometry("800x640")
app.resizable(width=False, height=False)

    # Define initial parameters
password_var = ctk.StringVar(value=generatepassword())
user_url = str()

upper_var = ctk.IntVar(value=0)
lower_var = ctk.IntVar(value=0)
numbers_var = ctk.IntVar(value=0)
special_var = ctk.IntVar(value=0)

    # Define widget parameters
h_color='#1E90FF'
c_radius=5
p_height=50
p_font=("Helvetica", 30)

    # Generate password button
button = ctk.CTkButton(
    app,
    command=updatepassword,
    text="Generate Password",
    width=300,
    height=p_height,
    corner_radius=c_radius,
    hover_color=h_color,
    text_color='White',
    font=p_font
)
button.place(x=60, y=50)

    # Store credential button
button = ctk.CTkButton(
    app,
    text="Store Credential",
    width=240,
    height=p_height,
    corner_radius=c_radius,
    hover_color=h_color,
    text_color='White',
    font=p_font
)
button.place(x=500, y=50)

    # URL entry
entry_url = ctk.CTkEntry(
    app,
    placeholder_text="url.com",
    width=680,
    height=p_height,
    corner_radius=c_radius,
    font=p_font,
    text_color='white'
)
entry_url.place(x=60, y=150)

    # Username entry
entry_url = ctk.CTkEntry(
    app,
    #text_variable=user_url,
    placeholder_text="Username",
    width=680,
    height=p_height,
    corner_radius=c_radius,
    font=p_font,
    text_color='white'
)
entry_url.place(x=60, y=250)

    # Password Display
entry_password = ctk.CTkEntry(
    app,
    textvariable=password_var,
    width=580,
    height=p_height,
    corner_radius=c_radius,
    font=p_font,
    text_color='yellow'
)
entry_password.place(x=60, y=350)

    # Refresh button
btn_refresh = ctk.CTkButton(
    app,
    command=updatepassword,
    text="⟳",
    width=50,
    height=p_height,
    corner_radius=c_radius,
    fg_color='transparent',
    hover_color=h_color,
    text_color='white',
    font=p_font
)
btn_refresh.place(x=640, y=350)

    # Copy button
btn_copy = ctk.CTkButton(
    app,
    text="📋",
    width=50,
    height=p_height,
    command=password_copy,
    corner_radius=c_radius,
    fg_color='transparent',
    hover_color=h_color,
    text_color='white',
    font=p_font
)
btn_copy.place(x=690, y=350)

    # Password Length Input
password_length = ctk.CTkEntry(
    app,
    placeholder_text="Password Length",
    width=680,
    height=p_height,
    corner_radius=c_radius,
    font=p_font
)
password_length.place(x=60, y=450)

    # Character Selection Checkboxes
check_upper = ctk.CTkCheckBox(
    app,
    command=update_characters,
    variable=upper_var,
    onvalue=1,
    offvalue=0,
    text=" A - Z",
    checkbox_height=p_height,
    checkbox_width=50,
    font=p_font,
    border_width=4,
    hover_color=h_color
)
check_upper.place(x=60, y=550)
#check_upper.select()

check_lower = ctk.CTkCheckBox(
    app,
    command=update_characters,
    variable=lower_var,
    onvalue=1,
    offvalue=0,
    text=" a - z",
    checkbox_height=p_height,
    checkbox_width=50,
    font=p_font,
    border_width=4,
    hover_color=h_color
)
check_lower.place(x=231, y=550)
#check_lower.select()

check_numbers = ctk.CTkCheckBox(
    app,
    command=update_characters,
    variable=numbers_var,
    onvalue=1,
    offvalue=0,
    text=" 0 - 9",
    checkbox_height=p_height,
    checkbox_width=50,
    font=p_font,
    border_width=4,
    hover_color=h_color
)
check_numbers.place(x=403, y=550)
#check_numbers.select()

check_special = ctk.CTkCheckBox(
    app,
    command=update_characters,
    variable=special_var,
    onvalue=1,
    offvalue=0,
    text=" !@#^&*",
    checkbox_height=p_height,
    checkbox_width=50,
    font=p_font,
    border_width=4,
    hover_color=h_color
)
check_special.place(x=575, y=550)
#check_special.select()

app.mainloop()
