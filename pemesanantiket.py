import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def pesan_tiket():
    film_terpilih = var_film.get()
    jumlah_tiket = var_jumlah_tiket.get()

    if film_terpilih == "":
        messagebox.showerror("Error", "Pilih film terlebih dahulu.")
    elif jumlah_tiket == 0:
        messagebox.showerror("Error", "Jumlah tiket tidak boleh nol.")
    else:
        total_harga = harga_film[film_terpilih] * jumlah_tiket
        info_pesan = f"Film: {film_terpilih}\nJumlah Tiket: {jumlah_tiket}\nTotal Harga: Rp.{total_harga}"
        messagebox.showinfo("Pemesanan Berhasil", info_pesan)

# Daftar film dan harga per tiket
film_options = ["Conjuring", "KKN Desa Penari", "Siksa Kubur"]
harga_film = {"Conjuring": 45000, "KKN Desa Penari": 35000, "Siksa Kubur": 40000}

# Membuat GUI
root = tk.Tk()
root.title("Pemesanan Tiket Film")

# Variabel untuk menyimpan pilihan pengguna
var_film = tk.StringVar()
var_film.set(film_options[0])  # Pilih film pertama secara default

var_jumlah_tiket = tk.IntVar()
var_jumlah_tiket.set(1)  # Set jumlah tiket menjadi satu secara default

# Label dan Dropdown untuk pilihan film
label_film = tk.Label(root, text="Pilih Film:")
label_film.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

dropdown_film = tk.OptionMenu(root, var_film, *film_options)
dropdown_film.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

# Label dan Entry untuk jumlah tiket
label_jumlah_tiket = tk.Label(root, text="Jumlah Tiket:")
label_jumlah_tiket.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_jumlah_tiket = tk.Entry(root, textvariable=var_jumlah_tiket, width=5)
entry_jumlah_tiket.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

# Tombol pesan tiket
tombol_pesan = tk.Button(root, text="Pesan Tiket", command=pesan_tiket)
tombol_pesan.grid(row=2, column=0, columnspan=2, pady=10)

style = ttk.Style('solar')
root.geometry("230x170")
root.resizable(False, False)

# Menjalankan loop utama Tkinter
root.mainloop()
