import tkinter as tk
from tkinter import simpledialog, messagebox


class Debt:

    def __init__(self, creditor, amount, due_date):
        self.creditor = creditor
        self.amount = amount
        self.due_date = due_date
        self.payments = []

    def add_payment(self, payment_amount, payment_date):
        self.payments.append({'amount': payment_amount, 'date': payment_date})

    def get_balance(self):
        total_paid = sum(payment['amount'] for payment in self.payments)
        return self.amount - total_paid


class DebtManagerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pembayaran Utang")

        self.debts = []

        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=10)

        tk.Button(self.menu_frame,
                  text="Tambah Utang Baru",
                  command=self.add_debt).grid(row=0, column=0, padx=10)
        tk.Button(self.menu_frame,
                  text="Tambah Pembayaran",
                  command=self.add_payment).grid(row=0, column=1, padx=10)
        tk.Button(self.menu_frame,
                  text="Lihat Status Utang",
                  command=self.show_debts).grid(row=0, column=2, padx=10)
        tk.Button(self.menu_frame, text="Keluar",
                  command=self.root.quit).grid(row=0, column=3, padx=10)
