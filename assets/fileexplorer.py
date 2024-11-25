from tkinter import *
from time import sleep as slp
import os
import shutil as sl
import datetime as dt
from tkinter import simpledialog as sd
from tkinter import messagebox as msg
from tkinter.ttk import Separator
import subprocess

class Win95Explorer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer - Windows 95")
        self.root.geometry("800x600")
        self.root.configure(bg='#c0c0c0')
        
        self.WIN95_GRAY = '#c0c0c0'
        self.WIN95_DARK = '#808080'
        self.WIN95_LIGHT = '#ffffff'
        
        self.setup_menu()
        self.setup_toolbar()
        self.setup_main_content()
        self.setup_status_bar()
        
        self.current_path = os.path.join(os.path.expanduser("~"), "Documents")
        self.path_entry.insert(0, self.current_path)
        self.refresh_file_list()

    def setup_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Folder", command=self.create_new_folder)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        edit_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Copy", command=self.copy_file)
        edit_menu.add_command(label="Delete", command=self.delete_item)

    def setup_toolbar(self):
        address_frame = Frame(self.root, bg=self.WIN95_GRAY)
        address_frame.pack(fill=X, padx=5, pady=5)
        
        Label(address_frame, text="Address:", bg=self.WIN95_GRAY).pack(side=LEFT, padx=5)
        self.path_entry = Entry(address_frame, relief="sunken", width=70)
        self.path_entry.pack(side=LEFT, fill=X, expand=True, padx=5)
        
        Button(address_frame, text="Go", command=self.refresh_file_list, 
               relief="raised", width=6).pack(side=LEFT, padx=5)

    def setup_main_content(self):
        main_frame = Frame(self.root, bg=self.WIN95_GRAY)
        main_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        sidebar = Frame(main_frame, bg=self.WIN95_GRAY, width=100)
        sidebar.pack(side=LEFT, fill=Y, padx=(0, 5))
        
        quick_access = [
            ("Desktop", lambda: self.change_directory("Desktop")),
            ("Documents", lambda: self.change_directory("Documents")),
            ("Downloads", lambda: self.change_directory("Downloads")),
            ("Pictures", lambda: self.change_directory("Pictures")),
            ("Music", lambda: self.change_directory("Music")),
            ("Videos", lambda: self.change_directory("Videos"))
        ]
        
        for text, command in quick_access:
            Button(sidebar, text=text, command=command,
                   relief="raised", width=12).pack(pady=2)
        
        list_frame = Frame(main_frame, bg=self.WIN95_LIGHT, relief="sunken", bd=1)
        list_frame.pack(side=LEFT, fill=BOTH, expand=True)
        
        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.file_list = Listbox(list_frame, yscrollcommand=scrollbar.set,
                                bg="white", font=("Courier", 10))
        self.file_list.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.config(command=self.file_list.yview)
        
        self.file_list.bind('<Double-Button-1>', lambda e: self.open_item())

    def setup_status_bar(self):
        status = Frame(self.root, relief="sunken", bd=1)
        status.pack(fill=X, side=BOTTOM, pady=(5, 0))
        self.status_label = Label(status, text="Ready", bd=1, relief="sunken", anchor=W)
        self.status_label.pack(fill=X)

    def refresh_file_list(self):
        self.file_list.delete(0, END)
        path = self.path_entry.get()
        
        try:
            items = os.listdir(path)
            for item in items:
                if os.path.isdir(os.path.join(path, item)):
                    self.file_list.insert(END, f"[DIR] {item}")
                else:
                    self.file_list.insert(END, item)
            self.status_label.config(text=f"{len(items)} items found")
        except Exception as e:
            msg.showerror("Error", f"Cannot access path: {str(e)}")

    def create_new_folder(self):
        folder_name = sd.askstring("New Folder", "Enter folder name:")
        if folder_name:
            try:
                os.mkdir(os.path.join(self.path_entry.get(), folder_name))
                self.refresh_file_list()
            except Exception as e:
                msg.showerror("Error", f"Cannot create folder: {str(e)}")

    def delete_item(self):
        selection = self.file_list.curselection()
        if not selection:
            return
            
        item_name = self.file_list.get(selection[0]).replace("[DIR] ", "")
        path = os.path.join(self.path_entry.get(), item_name)
        
        if msg.askyesno("Confirm Delete", f"Are you sure you want to delete {item_name}?"):
            try:
                if os.path.isdir(path):
                    sl.rmtree(path)
                else:
                    os.remove(path)
                self.refresh_file_list()
            except Exception as e:
                msg.showerror("Error", f"Cannot delete item: {str(e)}")

    def copy_file(self):
        selection = self.file_list.curselection()
        if not selection:
            return
            
        item_name = self.file_list.get(selection[0]).replace("[DIR] ", "")
        src_path = os.path.join(self.path_entry.get(), item_name)
        timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        dst_path = os.path.join(self.path_entry.get(), f"Copy_{timestamp}_{item_name}")
        
        try:
            if os.path.isdir(src_path):
                sl.copytree(src_path, dst_path)
            else:
                sl.copy2(src_path, dst_path)
            self.refresh_file_list()
        except Exception as e:
            msg.showerror("Error", f"Cannot copy item: {str(e)}")

    def open_item(self):
        selection = self.file_list.curselection()
        if not selection:
            return
            
        item_name = self.file_list.get(selection[0]).replace("[DIR] ", "")
        path = os.path.join(self.path_entry.get(), item_name)
        
        if os.path.isdir(path):
            self.path_entry.delete(0, END)
            self.path_entry.insert(0, path)
            self.refresh_file_list()
        else:
            try:
                if os.name == 'nt':
                    os.startfile(path)
                else: 
                    subprocess.run(["open" if os.name == 'darwin' else "xdg-open", path])
            except Exception as e:
                msg.showerror("Error", f"Cannot open file: {str(e)}")

    def change_directory(self, folder):
        new_path = os.path.join(os.path.expanduser("~"), folder)
        self.path_entry.delete(0, END)
        self.path_entry.insert(0, new_path)
        self.refresh_file_list()

if __name__ == "__main__":
    root = Tk()
    app = Win95Explorer(root)
    root.mainloop()
