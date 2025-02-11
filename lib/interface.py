from functions import *
import customtkinter as ctk

def nothing():
    print()


app = ctk.CTk()
app.title('PassGen')
app.geometry("800x440")

    # Generate password button
button = ctk.CTkButton(app, text="Generate Password", width=340, height=50, corner_radius=5, hover_color='#1E90FF', text_color='yellow', font=("Helvetica", 30))
button.place(x=60, y=50)

    # Password Display
entry_password = ctk.CTkEntry(app, width=580, height=50, corner_radius=5, font=("Helvetica", 30), text_color='yellow')
entry_password.place(x=60, y=150)

    # Password Length Input
password_length = ctk.CTkEntry(app,placeholder_text="Password Length", width=680, height=50, corner_radius=5, font=("Helvetica", 30))
password_length.place(x=60, y=250)

    # Character Selection Checkboxes
check_upper = ctk.CTkCheckBox(app, text="A - Z", font=("Helvetica", 30), border_width=2, hover_color='#1E90FF')
check_upper.place(x=60, y=350)
check_lower = ctk.CTkCheckBox(app, text="a - z", font=("Helvetica", 30), border_width=2, hover_color='#1E90FF')
check_lower.place(x=256, y=350)
check_numbers = ctk.CTkCheckBox(app, text="0 - 9", font=("Helvetica", 30), border_width=2, hover_color='#1E90FF')
check_numbers.place(x=437, y=350)
check_special = ctk.CTkCheckBox(app, text="!@#^&*", font=("Helvetica", 30), border_width=2, hover_color='#1E90FF')
check_special.place(x=620, y=350)

    # Refresh and copy buttons
btn_refresh = ctk.CTkButton(app, text="⟳", width=50, height=50, command=nothing(), corner_radius=5, border_width=0, fg_color='transparent', hover_color='#1E90FF', text_color='yellow', font=("Helvetica", 30))
btn_refresh.place(x=640, y=150)
btn_copy = ctk.CTkButton(app, text="📋", width=50, height=50, command=nothing(), corner_radius=5, border_width=0, fg_color='transparent', hover_color='#1E90FF', text_color='yellow', font=("Helvetica", 30))
btn_copy.place(x=690, y=150)

app.mainloop()
