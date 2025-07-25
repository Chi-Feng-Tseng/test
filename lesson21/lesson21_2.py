import tkinter as tk

def on_button_click():
    print("Hello, Tkinter!")

def create_main_window():
    window = tk.Tk()                #建立主視窗
    window.title("簡單Tkinter範例")  #建立視窗標題
    window.geometry("500x500")      #設定視窗大小

    # 建立按鈕並綁定事件處理函式
    btn = tk.Button(window, text="點我", command=on_button_click, padx=20, pady=20, font=("Arial", 16))
    btn.pack(pady=100)

    return window

def main():
    window = create_main_window()
    window.mainloop()

if __name__ == "__main__":
    main()