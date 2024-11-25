import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import subprocess
import os
import webbrowser
from PIL import Image, ImageTk
import pygame

class Windows95Clone:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows 95 Clone")
        pygame.mixer.init()
        try:
            pygame.mixer.music.load("win95.mp3")
            pygame.mixer.music.play()
        except:
            print("Startup sound file not found")
        
        self.root.attributes('-fullscreen', True)
        try:
            bg_image = Image.open("background.png")
            bg_image = bg_image.resize((self.root.winfo_screenwidth(), 
                                      self.root.winfo_screenheight()-40))
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            
            self.desktop = tk.Label(root, image=self.bg_photo)
            self.desktop.pack(expand=True, fill='both')
        except:
            self.desktop = tk.Frame(root, bg='teal')
            self.desktop.pack(expand=True, fill='both')
        
        self.taskbar = tk.Frame(root, bg='silver', height=30)
        self.taskbar.pack(side='bottom', fill='x')
        self.taskbar.pack_propagate(False)
        
        try:
            start_img = Image.open("start_button.png")
            start_img = start_img.resize((80, 30)) 
            self.start_photo = ImageTk.PhotoImage(start_img)
            self.start_button = tk.Button(self.taskbar, image=self.start_photo,
                                        command=self.toggle_start_menu,
                                        relief='raised', bd=1,
                                        bg='silver')
        except:
            self.start_button = tk.Button(self.taskbar, text="START",
                                        command=self.toggle_start_menu,
                                        relief='raised', bg='silver')
        
        self.start_button.pack(side='left', padx=2, pady=2)
        

        self.time_label = tk.Label(self.taskbar, bg='silver', font=('Arial', 9))
        self.time_label.pack(side='right', padx=5)
        self.update_time()
        
        self.start_menu = None
        self.start_menu_visible = False

    def update_time(self):
        current_time = datetime.now().strftime('%I:%M %p')
        current_date = datetime.now().strftime('%d/%m/%Y')
        self.time_label.config(text=f"{current_date} {current_time}")
        self.root.after(1000, self.update_time)

    def toggle_start_menu(self):
        if self.start_menu_visible:
            self.hide_start_menu()
        else:
            self.show_start_menu()

    def show_start_menu(self):
        if self.start_menu is None:
            self.start_menu = tk.Frame(self.root, bg='silver', relief='raised', bd=2)
            
            side_label = tk.Label(self.start_menu, text="W\nI\nN\nD\nO\nW\nS\n95", 
                                bg='navy', fg='white', font=('Arial', 10, 'bold'),
                                width=4, height=4)
            side_label.pack(side='left', fill='y')

            menu_container = tk.Frame(self.start_menu, bg='silver')
            menu_container.pack(side='left', fill='both', expand=True)
   
            separator = tk.Frame(menu_container, bg='black', height=2)
            separator.pack(fill='x', pady=2)

            options = [
                ("Notepad", self.launch_notepad),
                ("File Explorer", self.launch_file_explorer),
                ("Terminal", self.launch_terminal),
                ("Internet Explorer", self.launch_edge),
                ("Calculator", self.launch_calculator),
                ("Device Info", self.show_device_info),
                ("Shut Down", self.shutdown)
            ]
            
            for text, command in options:
                btn_frame = tk.Frame(menu_container, bg='silver')
                btn_frame.pack(fill='x')
                
                btn = tk.Button(btn_frame, text=text, anchor='w',
                              width=25, relief='flat', bg='silver',
                              font=('Arial', 10), pady=4,
                              command=command if command else lambda: None)
                btn.pack(side='left', padx=(5, 10))
                
                if text in ["Notepad", "File Explorer", "Terminal", 
                           "Internet Explorer", "Calculator", "Device Info"]:
                    arrow = tk.Label(btn_frame, text="►", bg='silver')
                    arrow.pack(side='right', padx=5)
        
        menu_width = 300  
        menu_height = 400  
        self.start_menu.place(x=0, 
                            y=self.root.winfo_height() - 30 - menu_height,
                            width=menu_width,
                            height=menu_height)
        self.start_menu_visible = True

    def show_device_info(self):
        self.hide_start_menu()
        messagebox.showinfo("System Information",
                          "Microsoft Windows 95\n"
                          "Copyright © 1981-1995 Microsoft Corp.\n"
                          "Built by Ghruank Kothare\n"
                          "Build: 950 C\n"
                          "System: Intel 486DX\n"
                          "Memory: 16 MB RAM")

    def hide_start_menu(self):
        if self.start_menu:
            self.start_menu.place_forget()
            self.start_menu_visible = False

    def launch_notepad(self):
        self.hide_start_menu()
        try:
            subprocess.Popen(['python', 'notepad.py'])
        except Exception as e:
            tk.messagebox.showerror("Error", f"Could not launch Notepad: {str(e)}")

    def launch_file_explorer(self):
        self.hide_start_menu()
        try:
            subprocess.Popen(['python', 'fileexplorer.py'])
        except Exception as e:
            tk.messagebox.showerror("Error", f"Could not launch File Explorer: {str(e)}")

    def launch_terminal(self):
        self.hide_start_menu()
        try:
            subprocess.Popen(['python', 'terminal.py'])
        except Exception as e:
            tk.messagebox.showerror("Error", f"Could not launch File Explorer: {str(e)}")

    def launch_edge(self):
        self.hide_start_menu()
        try:
            webbrowser.get('microsoft-edge').open('http://www.google.com')
        except Exception:
            webbrowser.open('http://www.google.com')

    def launch_calculator(self):
        self.hide_start_menu()
        try:
            subprocess.Popen(['python', 'calculator.py'])
        except Exception as e:
            tk.messagebox.showerror("Error", f"Could not launch Calculator: {str(e)}")

    def shutdown(self):
        self.root.quit()

def main():
    root = tk.Tk()
    app = Windows95Clone(root)
    root.mainloop()

if __name__ == "__main__":
    main()