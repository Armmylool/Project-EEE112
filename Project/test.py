import tkinter as ttk

def open_file():
    file_path = "Food.txt"  # กำหนดชื่อไฟล์ที่ต้องการเปิด
    with open(file_path, 'r',encoding='utf-8') as file:
        content = file.read()
        text_box.delete(1.0, ttk.END)  # ล้างข้อความที่อยู่ใน Text widget
        text_box.insert(ttk.END, content)  # เพิ่มข้อมูลจากไฟล์ลงใน Text widget

# สร้างหน้าต่าง Tkinter
window = ttk.Tk()
window.title("Open File Example")

# สร้างปุ่ม
open_button = ttk.Button(window, text="Open File", command=open_file)
open_button.pack()

# สร้าง Text widget เพื่อแสดงข้อมูล
text_box = ttk.Text(window)
text_box.pack()

# เริ่มต้นรันหน้าต่าง Tkinter
window.mainloop()