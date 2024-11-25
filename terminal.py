import tkinter as tk
from tkinter import ttk, scrolledtext
import sys
from io import StringIO
import traceback
from datetime import datetime

class Win95Terminal:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Terminal - Windows 95")
        self.root.geometry("640x480")
        self.root.configure(bg='#c0c0c0')

        self.WIN95_GRAY = '#c0c0c0'
        self.WIN95_DARK = '#808080'
        self.WIN95_LIGHT = '#ffffff'
        
        self.setup_menu()
        self.setup_terminal()
        self.setup_status_bar()
        
        self.command_history = []
        self.history_index = 0
        
        welcome_msg = "Python Terminal [Version 1.0]\n"
        welcome_msg += f"(c) Windows 95. Microsoft Corporation.\n\n"
        welcome_msg += "Type 'help()' for help or 'exit()' to exit.\n\n"
        welcome_msg += ">>> "
        self.terminal.insert('1.0', welcome_msg)

        self.prompt_pos = self.terminal.index('end-1c linestart')
        self.prompt = ">>> "

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Clear Terminal", command=self.clear_terminal)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)

    def setup_terminal(self):
        self.terminal = scrolledtext.ScrolledText(
            self.root,
            bg='black',
            fg='light gray',
            font=('Courier', 10),
            insertbackground='white',
            relief='sunken',
            borderwidth=2
        )
        self.terminal.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.terminal.bind('<Return>', self.handle_return)
        self.terminal.bind('<BackSpace>', self.handle_backspace)
        self.terminal.bind('<Key>', self.handle_key)
        self.terminal.bind('<Up>', self.handle_up)
        self.terminal.bind('<Down>', self.handle_down)
        self.terminal.bind('<Button-3>', self.show_context_menu)
        
        self.terminal.bind('<Control-a>', lambda e: 'break')
        self.terminal.bind('<Control-h>', lambda e: 'break')

    def setup_status_bar(self):
        self.status_bar = tk.Label(
            self.root,
            text="Ready",
            bd=1,
            relief='sunken',
            anchor='w',
            bg=self.WIN95_GRAY
        )
        self.status_bar.pack(side='bottom', fill='x')

    def show_context_menu(self, event):
        context_menu = tk.Menu(self.root, tearoff=0)
        context_menu.add_command(label="Copy", command=self.copy_text)
        context_menu.add_command(label="Paste", command=self.paste_text)
        context_menu.add_separator()
        context_menu.add_command(label="Clear All", command=self.clear_terminal)
        
        try:
            context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            context_menu.grab_release()

    def copy_text(self):
        try:
            selected_text = self.terminal.get("sel.first", "sel.last")
            self.root.clipboard_clear()
            self.root.clipboard_append(selected_text)
        except tk.TclError:
            pass

    def paste_text(self):
        try:
            text = self.root.clipboard_get()
            if self.is_cursor_in_input_area():
                self.terminal.insert('insert', text)
        except tk.TclError:
            pass

    def clear_terminal(self):
        self.terminal.delete('1.0', tk.END)
        self.terminal.insert('1.0', ">>> ")
        self.prompt_pos = "1.0"
        self.terminal.mark_set('insert', 'end')
        self.terminal.see('end')

    def get_input_start_index(self):
        return f"{self.prompt_pos}+{len(self.prompt)}c"

    def is_cursor_in_input_area(self):
        cursor_pos = self.terminal.index('insert')
        return self.terminal.compare(cursor_pos, '>=', self.get_input_start_index())

    def get_current_command(self):
        input_start = self.get_input_start_index()
        return self.terminal.get(input_start, 'end-1c')

    def handle_return(self, event):
        command = self.get_current_command().strip()
        self.terminal.insert('end', '\n')
        
        if command == 'exit()':
            self.root.quit()
            return 'break'
            
        if command == 'clear()':
            self.clear_terminal()
            return 'break'
            
        if command == 'help()':
            help_text = "Available commands:\n"
            help_text += "  clear() - Clear the terminal\n"
            help_text += "  exit() - Exit the terminal\n"
            help_text += "  help() - Show this help message\n"
            help_text += "  Any valid Python expression or statement\n"
            self.terminal.insert('end', help_text + "\n")
        elif command:
            self.command_history.append(command)
            self.history_index = len(self.command_history)
            
            old_stdout = sys.stdout
            redirected_output = StringIO()
            sys.stdout = redirected_output
            
            try:
                try:
                    result = eval(command)
                    if result is not None:
                        print(result)
                except SyntaxError:
                    exec(command)
                
                output = redirected_output.getvalue()
                if output:
                    self.terminal.insert('end', output)
            except Exception as e:
                self.terminal.insert('end', f"Error: {str(e)}\n")
            
            sys.stdout = old_stdout

        self.terminal.insert('end', '\n>>> ')
        self.prompt_pos = self.terminal.index('end-1c linestart')
        self.terminal.see('end')
        return 'break'

    def handle_backspace(self, event):
        if not self.is_cursor_in_input_area():
            return 'break'

        if self.terminal.index('insert') <= self.get_input_start_index():
            return 'break'
        
        return  

    def handle_key(self, event):

        if event.state & 4: 
            if event.keysym.lower() in ['c', 'v']:
                return

        if not self.is_cursor_in_input_area():
            self.terminal.mark_set('insert', 'end')
            return 'break'

    def handle_up(self, event):
        if self.command_history:
            self.history_index = max(0, self.history_index - 1)
            if self.history_index < len(self.command_history):
                input_start = self.get_input_start_index()
                self.terminal.delete(input_start, 'end-1c')
                self.terminal.insert(input_start, self.command_history[self.history_index])
        return 'break'

    def handle_down(self, event):
        if self.command_history:
            self.history_index = min(len(self.command_history), self.history_index + 1)
            input_start = self.get_input_start_index()
            self.terminal.delete(input_start, 'end-1c')
            if self.history_index < len(self.command_history):
                self.terminal.insert(input_start, self.command_history[self.history_index])
        return 'break'

if __name__ == "__main__":
    root = tk.Tk()
    app = Win95Terminal(root)
    root.mainloop()