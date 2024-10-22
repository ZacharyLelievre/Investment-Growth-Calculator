import tkinter as tk
from tkinter import messagebox
import matplotlib
matplotlib.use('TkAgg')  # Ensure Matplotlib uses Tkinter backend
import matplotlib.pyplot as plt

def calculate_investment():
    try:
        initial_investment = int(entry_amount.get())
        monthly_investment = int(entry_monthly.get())
        yearly_investment = int(entry_yearly.get())
        interest_rate = float(entry_rate.get())
        period_years = int(entry_years.get())

        total = []
        year = []

        firstYear = 0
        current_balance = 0
        million = True
        # hundred = True
        current_balance += initial_investment

        for i in range(period_years):
            current_balance += (monthly_investment * 12) + yearly_investment
            current_balance += current_balance * interest_rate

            total.append(current_balance)
            firstYear += 1
            year.append(firstYear)

            if current_balance > 1000000 and million:
                million = False
                onemillion = current_balance
                onemillion_Year = firstYear

            # if(current_balance > 100000 and hundred):
            #     hundred= False
            #     onehundred =current_balance
            #




        plt.plot(year, total)
        plt.title('Investment Growth Over Time')
        plt.xlabel('Years')
        plt.ylabel('Total Balance')
        plt.show()

        total_label.config(text=f"Total Balance at the End: ${current_balance:.2f}")
        yearMillion.config(text=f"Year: {onemillion_Year}, Amount: ${onemillion:.2f}")


    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Investment Calculator")

# Create and place the labels and entry widgets

tk.Label(root, text="Entry Investment:").grid(row=0, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1)

tk.Label(root, text="Monthly Investment:").grid(row=1, column=0)
entry_monthly = tk.Entry(root)
entry_monthly.grid(row=1, column=1)

tk.Label(root, text="Yearly Investment:").grid(row=2, column=0)
entry_yearly = tk.Entry(root)
entry_yearly.grid(row=2, column=1)

tk.Label(root, text="Interest Rate:").grid(row=3, column=0)
entry_rate = tk.Entry(root)
entry_rate.grid(row=3, column=1)

tk.Label(root, text="Investment Period (Years):").grid(row=4, column=0)
entry_years = tk.Entry(root)
entry_years.grid(row=4, column=1)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_investment)
calculate_button.grid(row=5, column=0)

# Create and place the total balance label
total_label = tk.Label(root, text="Total Balance at the End: $0.00")
total_label.grid(row=5, column=1)

yearMillion= tk.Label(root, text="The year you would hit one million")
yearMillion.grid(row=6, column=1)

# Run the main loop
root.mainloop()