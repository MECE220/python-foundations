# finance_tracker.py
# A personal finance tracker using OOP + file I/O + rich

import datetime
import json
import os
from rich.console import Console
from rich.table import Table
import utils

console = Console()

class Transaction:
    def __init__(self, amount, category, description, transaction_type):
        self.amount = abs(float(amount))
        self.category = category
        self.description = description
        self.type = transaction_type        # "income" or "expense"
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "type": self.type,
            "date": self.date
        }

class FinanceTracker:
    def __init__(self, owner, filename="finance_data.json"):
        self.owner = owner
        self.filename = filename
        self.__transactions = []
        self.__load_data()

    def __load_data(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    for item in data:
                        t = Transaction(
                            item['amount'],
                            item['category'],
                            item['description'],
                            item['type']
                        )
                        t.date = item['date']
                        self.__transactions.append(t)
                console.print(f"[green]Loaded {len(self.__transactions)} transactions[/green]")
        except (json.JSONDecodeError, KeyError):
            console.print("[yellow]Starting with fresh data[/yellow]")

    def __save_data(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump([t.to_dict() for t in self.__transactions], f, indent=2)
        except IOError:
            console.print("[red]Error: Could not save data[/red]")

    def add_income(self, amount, category, description):
        try:
            t = Transaction(amount, category, description, "income")
            self.__transactions.append(t)
            self.__save_data()
            console.print(f"[green]✓ Income added: {utils.format_currency(t.amount)}[/green]")
        except ValueError:
            console.print("[red]Error: Invalid amount[/red]")

    def add_expense(self, amount, category, description):
        try:
            t = Transaction(amount, category, description, "expense")
            self.__transactions.append(t)
            self.__save_data()
            console.print(f"[red]✓ Expense added: {utils.format_currency(t.amount)}[/red]")
        except ValueError:
            console.print("[red]Error: Invalid amount[/red]")

    def get_balance(self):
        income = sum(t.amount for t in self.__transactions if t.type == "income")
        expenses = sum(t.amount for t in self.__transactions if t.type == "expense")
        return income, expenses, income - expenses

    def show_summary(self):
        income, expenses, balance = self.get_balance()
        balance_color = "green" if balance >= 0 else "red"

        utils.print_header(f"Finance Report — {self.owner}")

        table = Table(show_header=True, header_style="bold")
        table.add_column("Date", width=17)
        table.add_column("Type", width=8)
        table.add_column("Category", width=12)
        table.add_column("Description", width=20)
        table.add_column("Amount", width=12, justify="right")

        for t in self.__transactions[-20:]:    # show last 10
            color = "green" if t.type == "income" else "red"
            table.add_row(
                t.date,
                f"[{color}]{t.type}[/{color}]",
                t.category,
                t.description,
                f"[{color}]{utils.format_currency(t.amount)}[/{color}]"
            )

        console.print(table)
        console.print(f"\n  Total Income  : [green]{utils.format_currency(income)}[/green]")
        console.print(f"  Total Expenses: [red]{utils.format_currency(expenses)}[/red]")
        console.print(f"  Balance       : [{balance_color}]{utils.format_currency(balance)}[/{balance_color}]")


# --- Main Program ---
tracker = FinanceTracker("Reiko")

# Add sample transactions
tracker.add_income(5000, "Salary", "Monthly salary")
tracker.add_income(500, "Freelance", "Python tutoring")
tracker.add_expense(1200, "Rent", "Monthly rent")
tracker.add_expense(300, "Food", "Groceries")
tracker.add_expense(50, "Learning", "Udemy course")
tracker.add_expense(100, "Transport", "Monthly commute")

tracker.show_summary()