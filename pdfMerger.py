from tkinter import Tk, Frame, Button, Label, Listbox, messagebox
from tkinter.filedialog import askopenfilenames, asksaveasfilename
from tkinter import ttk
from PyPDF4 import PdfFileMerger


def merge_pdfs():
    root = Tk()
    root.title("PDF Merger")
    root.geometry("400x400")
    root.resizable(True, True)

    style = ttk.Style()
    style.configure("TButton", padding=6, relief="flat", background="#4287f5", foreground="white")
    style.configure("TLabel", font=("Arial", 12), background="#f5f5f5")
    style.configure("TListbox", font=("Arial", 10), background="#f5f5f5")
    style.configure("TFrame", background="#f5f5f5")

    def select_files():
        input_files = askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if input_files:
            selected_files_label.config(text="Selected Files: {}".format(len(input_files)))
            merge_button.config(state="normal")
            file_listbox.delete(0, "end")
            for file in input_files:
                file_listbox.insert("end", file)
        else:
            selected_files_label.config(text="No files selected")
            merge_button.config(state="disabled")
            file_listbox.delete(0, "end")

    def merge():
        input_files = file_listbox.get(0, "end")
        if not input_files:
            return

        output_file = asksaveasfilename(filetypes=[("PDF Files", "*.pdf")],
                                        defaultextension=".pdf",
                                        initialfile="merged_file.pdf")

        if not output_file:
            return

        merger = PdfFileMerger()

        for file in input_files:
            merger.append(file)

        merger.write(output_file)
        merger.close()

        messagebox.showinfo("Merge Complete", "PDF files merged successfully!")

        # Reset UI
        selected_files_label.config(text="No files selected")
        merge_button.config(state="disabled")
        file_listbox.delete(0, "end")

    # Create UI elements
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    title_label = ttk.Label(frame, text="PDF Merger")
    title_label.pack(pady=10)

    select_button = ttk.Button(frame, text="Select PDF Files", command=select_files)
    select_button.pack(pady=10)

    selected_files_label = ttk.Label(frame, text="No files selected")
    selected_files_label.pack()

    file_listbox = Listbox(frame, height=5, width=50)
    file_listbox.pack(pady=10)

    merge_button = ttk.Button(frame, text="Merge PDFs", command=merge, state="disabled")
    merge_button.pack(pady=10)

    root.mainloop()


merge_pdfs()
