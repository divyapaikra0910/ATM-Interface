import tkinter as tk
from tkinter import messagebox

class ATMInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Interface")
        self.balance = 1000  # Initial balance
        self.pin = "1234"  # Default PIN

        # GUI here
        self.label_title = tk.Label(master, text="Welcome to MyBank ATM", font=("Helvetica", 16, "bold"))
        self.label_title.pack(pady=10)

        self.label_pin = tk.Label(master, text="Enter PIN:")
        self.label_pin.pack()

        self.entry_pin = tk.Entry(master, show="*")
        self.entry_pin.pack()

        self.button_authenticate = tk.Button(master, text="Authenticate", command=self.authenticate)
        self.button_authenticate.pack(pady=10)

        # for authentication
        self.label_balance = tk.Label(master, text="Balance: $1000")
        self.label_balance.pack()

        self.entry_amount = tk.Entry(master)
        self.entry_amount.pack()

        self.button_deposit = tk.Button(master, text="Deposit", command=self.deposit)
        self.button_deposit.pack()

        self.button_withdraw = tk.Button(master, text="Withdraw", command=self.withdraw)
        self.button_withdraw.pack()

        self.button_return_card = tk.Button(master, text="Return Card", command=self.return_card)
        self.button_return_card.pack()

        # main components here
        self.hide_additional_components()

    def authenticate(self):
        entered_pin = self.entry_pin.get()
        if entered_pin == self.pin:
            self.show_additional_components()
            self.entry_pin.config(state=tk.DISABLED)
            self.button_authenticate.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Authentication Failed", "Invalid PIN. Please try again.")

    def update_balance_label(self):
        self.label_balance.config(text=f"Balance: ${self.balance}")

    def deposit(self):
        try:
            amount = float(self.entry_amount.get())
            if amount > 0:
                self.balance += amount
                self.update_balance_label()
                messagebox.showinfo("Deposit", f"Amount $ {amount} deposited successfully.")
            else:
                messagebox.showwarning("Invalid Amount", "Please enter a valid positive amount.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid numerical amount.")

    def withdraw(self):
        try:
            amount = float(self.entry_amount.get())
            if 0 < amount <= self.balance:
                self.balance -= amount
                self.update_balance_label()
                messagebox.showinfo("Withdrawal", f"Amount $ {amount} withdrawn successfully.")
            else:
                messagebox.showwarning("Invalid Amount", "Please enter a valid amount within your balance.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid numerical amount.")

    def return_card(self):
        self.master.destroy()

    def show_additional_components(self):
        self.label_balance.pack()
        self.entry_amount.pack()
        self.button_deposit.pack()
        self.button_withdraw.pack()
        self.button_return_card.pack()

    def hide_additional_components(self):
        self.label_balance.pack_forget()
        self.entry_amount.pack_forget()
        self.button_deposit.pack_forget()
        self.button_withdraw.pack_forget()
        self.button_return_card.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    atm_interface = ATMInterface(root)
    root.mainloop()
