import tkinter as tk
from tkinter import messagebox


expense_records = []


def record_expense():
    """Reads input fields, validates amount, and adds the expense to records."""
    item = item_entry.get().strip()
    amount_str = amount_entry.get().strip()

    if not item or not amount_str:
        messagebox.showerror("Error", "Please enter both item and amount.")
        return

    try:
      
        amount = float(amount_str)
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be a positive number.")
            return

        
        expense_records.append((item, amount_str))
        messagebox.showinfo("Success", f"Recorded: {item} - ₹{amount_str}")

        # Clear the input fields after successful addition
        item_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a valid number.")


def display_expenses():
    """Clears the text area and displays all recorded expenses with a total."""
    output_text.delete("1.0", tk.END)  # Clear previous content

    if not expense_records:
        output_text.insert(tk.END, "No expenses have been recorded yet.")
        return

    total_amount = 0.0
    output_text.insert(tk.END, "--- Your Expense Log ---\n\n")

    for item, amount_str in expense_records:
        try:
           
            amount = float(amount_str)
            output_text.insert(tk.END, f"{item}: ₹{amount_str}\n")
            total_amount += amount
        except ValueError:
            
            output_text.insert(tk.END, f"{item}: INVALID AMOUNT ({amount_str})\n")

    # Display the calculated total
    output_text.insert(tk.END, f"\n----------------------------------\n")
    output_text.insert(tk.END, f"TOTAL SPENT: ₹{total_amount:.2f}")


app = tk.Tk()
app.title("Finance Tracker Lite")
app.geometry("380x480") # Slightly different size

title_label = tk.Label(app, text="Simple Spending Tracker", font=("Helvetica", 14, "bold"), fg="#1F618D")
title_label.pack(pady=5)


item_label = tk.Label(app, text="Expense Item:")
item_label.pack(pady=2)
item_entry = tk.Entry(app, width=35)
item_entry.pack(padx=10)

amount_label = tk.Label(app, text="Cost (₹):")
amount_label.pack(pady=2)
amount_entry = tk.Entry(app, width=35)
amount_entry.pack(padx=10)


add_button = tk.Button(app, text="ADD TRANSACTION", command=record_expense, width=25, bg="#A9DFBF", fg="black", font=("Arial", 10))
add_button.pack(pady=10)

show_button = tk.Button(app, text="VIEW HISTORY", command=display_expenses, width=25, bg="#FADBD8", fg="black", font=("Arial", 10))
show_button.pack(pady=5)


output_text = tk.Text(app, width=40, height=15, wrap=tk.WORD, bg="#FBFCFC", bd=1, relief=tk.SUNKEN)
output_text.pack(pady=10, padx=10)


app.mainloop()
