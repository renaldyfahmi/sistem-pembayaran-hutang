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

  def add_debt(self):
        creditor = simpledialog.askstring("Tambah Utang Baru",
                                          "Masukkan nama kreditur:")
        if creditor is None:
            return
        amount_str = simpledialog.askstring("Tambah Utang Baru",
                                            "Masukkan jumlah utang:")
        if amount_str is None:
            return
        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Error", "Jumlah utang harus berupa angka.")
            return
        due_date = simpledialog.askstring(
            "Tambah Utang Baru", "Masukkan tanggal jatuh tempo (YYYY-MM-DD):")
        if due_date is None:
            return

        self.debts.append(Debt(creditor, amount, due_date))
        messagebox.showinfo("Informasi", "Utang berhasil ditambahkan.")

    def add_payment(self):
        if not self.debts:
            messagebox.showwarning("Peringatan",
                                   "Tidak ada utang yang tersedia.")
            return

        options = [
            f"{i+1}. {debt.creditor} - Rp{debt.amount} (Saldo: Rp{debt.get_balance()})"
            for i, debt in enumerate(self.debts)
        ]
        selected_index = simpledialog.askinteger(
            "Tambah Pembayaran",
            "Pilih nomor utang untuk pembayaran:\n" + "\n".join(options),
            minvalue=1,
            maxvalue=len(self.debts))
        if selected_index is None:
            return
        selected_index -= 1
        payment_amount_str = simpledialog.askstring(
            "Tambah Pembayaran", "Masukkan jumlah pembayaran:")
        if payment_amount_str is None:
            return
        try:
            payment_amount = float(payment_amount_str)
        except ValueError:
            messagebox.showerror("Error",
                                 "Jumlah pembayaran harus berupa angka.")
            return
        payment_date = simpledialog.askstring(
            "Tambah Pembayaran", "Masukkan tanggal pembayaran (YYYY-MM-DD):")
        if payment_date is None:
            return

        self.debts[selected_index].add_payment(payment_amount, payment_date)
        new_balance = self.debts[selected_index].get_balance()
        messagebox.showinfo(
            "Informasi",
            f"Pembayaran berhasil ditambahkan.\nSaldo utang terbaru: Rp{new_balance}"
        )

    def show_debts(self):
        if not self.debts:
            messagebox.showwarning("Peringatan",
                                   "Tidak ada utang yang tersedia.")
            return

        info = "\n\n".join(
            f"Kreditur: {debt.creditor}\nJumlah Utang: Rp{debt.amount}\nTanggal Jatuh Tempo: {debt.due_date}\nSaldo Utang: Rp{debt.get_balance()}\nPembayaran:\n"
            + "\n".join(f"  - Rp{payment['amount']} pada {payment['date']}"
                        for payment in debt.payments) for debt in self.debts)
        messagebox.showinfo("Status Utang", info)


if __name__ == "__main__":
    root = tk.Tk()
    app = DebtManagerApp(root)
    root.mainloop()

