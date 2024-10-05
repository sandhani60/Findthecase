from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import cv2
import os
import datetime

class case_details:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x770+0+0")
        self.root.title("FIND THE CASE")

        # Variables for data entry
        self.var_casetype = StringVar()
        self.var_dep = StringVar()
        self.var_country = StringVar()
        self.var_town = StringVar()
        self.var_Name = StringVar()
        self.var_caseid = StringVar()
        self.var_gender = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_age = IntVar()

        title_lbl = Label(self.root, text="CASE DETAILS", font=("times new roman", 35, "bold"), bg="RED", fg="BLACK")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        frame = Frame(self.root, bd=2)
        frame.place(x=5, y=55, width=1500, height=700)

        # Left Frame - Case Details
        left_frame_data = LabelFrame(frame, bd=2, text='Case Details', font=('times new roman', 14, 'bold'))
        left_frame_data.place(x=20, y=50, width=670, height=500)

        case_1 = Label(left_frame_data, text="Case Type", font=("times new roman", 12, "bold"))
        case_1.grid(row=0, column=0, padx=10)
        case_1_combo = ttk.Combobox(left_frame_data, textvariable=self.var_casetype, font=("times new roman", 12, "bold"), state="readonly")
        case_1_combo['values'] = ("Select Case Type", 'Robbery', 'Murder', 'Cheating', 'Other Case')
        case_1_combo.current(0)
        case_1_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Other case details widgets...

        case_age = Label(left_frame_data, text="Age", font=("times new roman", 12, "bold"))
        case_age.grid(row=5, column=0, padx=10)
        case_age_entry = ttk.Entry(left_frame_data, textvariable=self.var_age, font=("times new roman", 12))
        case_age_entry.grid(row=5, column=1, padx=2, pady=10, sticky=W)

        case_address = Label(left_frame_data, text="Address", font=("times new roman", 12, "bold"))
        case_address.grid(row=6, column=0, padx=10)
        case_address_entry = ttk.Entry(left_frame_data, textvariable=self.var_address, font=("times new roman", 12))
        case_address_entry.grid(row=6, column=1, padx=2, pady=10, sticky=W)

        # Case Person Details
        case_left_frame = LabelFrame(frame, bd=2, text='Case Person Details', font=('times new roman', 14, 'bold'))
        case_left_frame.place(x=20, y=200, width=670, height=300)

        case_name = Label(case_left_frame, text="Name", font=("times new roman", 13, "bold"))
        case_name.grid(row=0, column=0, padx=5, sticky=W)

        case_entry_name = ttk.Entry(case_left_frame, textvariable=self.var_Name, width=20, font=("times new roman", 13, "bold"))
        case_entry_name.grid(row=0, column=1, padx=5, sticky=W)

        case_gender = Label(case_left_frame, text="Gender", font=("times new roman", 13, "bold"))
        case_gender.grid(row=1, column=0, padx=5, sticky=W)

        case_entry_gender = ttk.Combobox(case_left_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"), state="readonly")
        case_entry_gender['values'] = ('Male', 'Female', 'Other')
        case_entry_gender.current(0)
        case_entry_gender.grid(row=1, column=1, padx=5, sticky=W)

        case_number = Label(case_left_frame, text="Mobile Number", font=("times new roman", 13, "bold"))
        case_number.grid(row=2, column=0, padx=5, sticky=W)

        case_entry_number = ttk.Entry(case_left_frame, textvariable=self.var_mobile, width=20, font=("times new roman", 13, "bold"))
        case_entry_number.grid(row=2, column=1, padx=5, sticky=W)

        case_email = Label(case_left_frame, text="Email", font=("times new roman", 13, "bold"))
        case_email.grid(row=3, column=0, padx=5, sticky=W)

        case_entry_email = ttk.Entry(case_left_frame, textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        case_entry_email.grid(row=3, column=1, padx=5, sticky=W)

        # Button Frame
        btn_frame = Frame(case_left_frame, bd=2, relief=RIDGE, bg="RED")
        btn_frame.place(x=0, y=170, width=660, height=40)

        save_btn = Button(btn_frame, text="Save", font=("times new roman", 13, "bold"), bg="green", fg="white", width=14, command=self.save_data)
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", font=("times new roman", 13, "bold"), bg="blue", fg="white", width=14, command=self.update_data)
        update_btn.grid(row=0, column=1)

        # Image and Voice Storage
        img_voice_frame = LabelFrame(frame, bd=2, text='Image & Voice Storage', font=('times new roman', 14, 'bold'))
        img_voice_frame.place(x=720, y=50, width=750, height=300)

        capture_img_btn = Button(img_voice_frame, text="Capture Image", font=("times new roman", 12), command=self.capture_image)
        capture_img_btn.pack(pady=5)

        record_voice_btn = Button(img_voice_frame, text="Record Voice", font=("times new roman", 12), command=self.record_voice)
        record_voice_btn.pack(pady=5)

        # Database Table
        table_frame = Frame(frame, bd=2, relief=RIDGE)
        table_frame.place(x=20, y=520, width=1450, height=200)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.case_table = ttk.Treeview(table_frame, columns=("case_id", "name", "case_type", "gender", "mobile", "email", "address", "age"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.case_table.xview)
        scroll_y.config(command=self.case_table.yview)

        self.case_table.heading("case_id", text="Case ID")
        self.case_table.heading("name", text="Name")
        self.case_table.heading("case_type", text="Case Type")
        self.case_table.heading("gender", text="Gender")
        self.case_table.heading("mobile", text="Mobile")
        self.case_table.heading("email", text="Email")
        self.case_table.heading("address", text="Address")
        self.case_table.heading("age", text="Age")

        self.case_table['show'] = 'headings'
        self.case_table.column("case_id", width=100)
        self.case_table.column("name", width=150)
        self.case_table.column("case_type", width=100)
        self.case_table.column("gender", width=100)
        self.case_table.column("mobile", width=120)
        self.case_table.column("email", width=200)
        self.case_table.column("address", width=200)
        self.case_table.column("age", width=50)

        self.case_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    def save_data(self):
        if self.var_Name.get() == "" or self.var_mobile.get() == "":
            messagebox.showerror("Error", "Name and Mobile Number are required fields", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="your_password", database="your_database")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO case_details (Name, CaseType, Gender, Mobile, Email, Address, Age) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_Name.get(),
                        self.var_casetype.get(),
                        self.var_gender.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_age.get()
                    )
                )
                conn.commit()
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success", "Case details saved successfully", parent=self.root)
                self.reset()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="your_password", database="your_database")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM case_details")
            data = my_cursor.fetchall()
            if data:
                self.case_table.delete(*self.case_table.get_children())
                for row in data:
                    self.case_table.insert("", END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)

    def update_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="your_password", database="your_database")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "UPDATE case_details SET Name=%s, CaseType=%s, Gender=%s, Mobile=%s, Email=%s, Address=%s, Age=%s WHERE CaseId=%s",
                (
                    self.var_Name.get(),
                    self.var_casetype.get(),
                    self.var_gender.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_caseid.get()
                )
            )
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success", "Case details updated successfully", parent=self.root)
            self.reset()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)

    def capture_image(self):
        # Placeholder for capturing image using OpenCV
        messagebox.showinfo("Info", "Image Capture Placeholder - Implement your image capture logic here", parent=self.root)

    def record_voice(self):
        # Placeholder for recording voice
        messagebox.showinfo("Info", "Voice Recording Placeholder - Implement your voice recording logic here", parent=self.root)

    def reset(self):
        self.var_Name.set("")
        self.var_casetype.set("")
        self.var_gender.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_age.set(0)

if __name__ == "__main__":
    root = Tk()
    obj = case_details(root)
    root.mainloop()
