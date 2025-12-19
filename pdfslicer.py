import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter


def select_pdf():
    file_path = filedialog.askopenfilename(
        title="انتخاب فایل PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if file_path:
        pdf_path_var.set(file_path)


def extract_pages():
    try:
        pdf_path = pdf_path_var.get()
        start_page = int(start_page_var.get()) - 1
        end_page = int(end_page_var.get()) - 1

        if not pdf_path:
            messagebox.showerror("خطا", "لطفاً یک PDF انتخاب کنید.")
            return

        reader = PdfReader(pdf_path)
        writer = PdfWriter()

        total_pages = len(reader.pages)

        if start_page < 0 or end_page >= total_pages or start_page > end_page:
            messagebox.showerror("خطا", "شماره صفحات معتبر نیست.")
            return

        for i in range(start_page, end_page + 1):
            writer.add_page(reader.pages[i])

        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="ذخیره PDF خروجی"
        )

        if save_path:
            with open(save_path, "wb") as f:
                writer.write(f)
            messagebox.showinfo("موفقیت", "فایل جدید با موفقیت ذخیره شد.")

    except Exception as e:
        messagebox.showerror("خطا", f"مشکلی رخ داد:\n{e}")


# ------------------- GUI -------------------

root = tk.Tk()
root.title("PDF Page Extractor")
root.geometry("400x250")

pdf_path_var = tk.StringVar()
start_page_var = tk.StringVar()
end_page_var = tk.StringVar()

tk.Label(root, text="انتخاب فایل PDF:").pack(pady=5)
tk.Entry(root, textvariable=pdf_path_var, width=45).pack()
tk.Button(root, text="انتخاب فایل", command=select_pdf).pack(pady=5)

tk.Label(root, text="صفحه شروع:").pack()
tk.Entry(root, textvariable=start_page_var).pack()

tk.Label(root, text="صفحه پایان:").pack()
tk.Entry(root, textvariable=end_page_var).pack()

tk.Button(root, text="استخراج صفحات", command=extract_pages, bg="#4CAF50", fg="white").pack(pady=15)

root.mainloop()
