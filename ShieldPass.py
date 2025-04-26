import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip
from ttkbootstrap import Style

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("安全密码生成器")
        self.root.geometry("450x450")
        self.style = Style(theme='flatly')
        
        # 主框架
        self.main_frame = ttk.Frame(root, padding=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 标题
        self.title_label = ttk.Label(
            self.main_frame, 
            text="密码生成器", 
            font=('Helvetica', 16, 'bold'),
            bootstyle="primary"
        )
        self.title_label.pack(pady=(0, 20))
        
        # 设置框架
        self.settings_frame = ttk.LabelFrame(
            self.main_frame, 
            text="生成设置", 
            padding=(15, 10)
        )
        self.settings_frame.pack(fill=tk.X, pady=(0, 20))
        
        # 密码长度设置
        self.length_frame = ttk.Frame(self.settings_frame)
        self.length_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.length_label = ttk.Label(
            self.length_frame, 
            text="密码长度:", 
            width=12
        )
        self.length_label.pack(side=tk.LEFT)
        
        self.length_var = tk.IntVar(value=12)
        self.length_slider = ttk.Scale(
            self.length_frame, 
            from_=8, 
            to=32, 
            variable=self.length_var,
            command=lambda e: self.length_display.config(text=str(int(self.length_var.get()))),
            bootstyle="info"
        )
        self.length_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        self.length_display = ttk.Label(
            self.length_frame, 
            text="12", 
            width=3,
            bootstyle="info"
        )
        self.length_display.pack(side=tk.LEFT)
        
        # 密码数量设置
        self.count_frame = ttk.Frame(self.settings_frame)
        self.count_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.count_label = ttk.Label(
            self.count_frame, 
            text="生成数量:", 
            width=12
        )
        self.count_label.pack(side=tk.LEFT)
        
        self.count_var = tk.IntVar(value=3)
        self.count_spinbox = ttk.Spinbox(
            self.count_frame, 
            from_=1, 
            to=10, 
            textvariable=self.count_var,
            width=5,
            bootstyle="info"
        )
        self.count_spinbox.pack(side=tk.LEFT)
        
        # 特殊字符选项
        self.symbols_var = tk.BooleanVar(value=True)
        self.symbols_check = ttk.Checkbutton(
            self.settings_frame, 
            text="包含特殊字符", 
            variable=self.symbols_var,
            bootstyle="round-toggle"
        )
        self.symbols_check.pack(anchor=tk.W, pady=(5, 0))
        
        # 生成按钮
        self.generate_button = ttk.Button(
            self.main_frame, 
            text="生成密码", 
            command=self.generate_passwords,
            bootstyle="success"
        )
        self.generate_button.pack(fill=tk.X, pady=(0, 15))
        
        # 结果框架
        self.result_frame = ttk.LabelFrame(
            self.main_frame, 
            text="生成的密码", 
            padding=(15, 10)
        )
        self.result_frame.pack(fill=tk.BOTH, expand=True)
        
        # 结果文本框
        self.result_text = tk.Text(
            self.result_frame, 
            height=6, 
            wrap=tk.WORD,
            font=('Consolas', 10),
            padx=10,
            pady=10
        )
        self.result_text.pack(fill=tk.BOTH, expand=True)
        
        # 复制按钮
        self.copy_button = ttk.Button(
            self.main_frame, 
            text="复制到剪贴板", 
            command=self.copy_to_clipboard,
            bootstyle="secondary"
        )
        self.copy_button.pack(fill=tk.X, pady=(10, 0))
    
    def generate_passwords(self):
        """生成密码逻辑"""
        length = self.length_var.get()
        count = self.count_var.get()
        
        # 构建基础字符集（始终包含大小写字母和数字）
        chars = string.ascii_letters + string.digits
        
        # 根据选项添加特殊字符[1](@ref)
        if self.symbols_var.get():
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # 生成密码[1,3](@ref)
        passwords = []
        for _ in range(count):
            password = ''.join(random.choices(chars, k=length))
            passwords.append(password)
        
        # 显示结果
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "\n".join(passwords))
    
    def copy_to_clipboard(self):
        """复制密码到剪贴板"""
        passwords = self.result_text.get(1.0, tk.END).strip()
        if passwords:
            pyperclip.copy(passwords)
            self.copy_button.config(bootstyle="success")
            self.root.after(2000, lambda: self.copy_button.config(bootstyle="secondary"))
        else:
            self.copy_button.config(bootstyle="danger")
            self.root.after(2000, lambda: self.copy_button.config(bootstyle="secondary"))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
