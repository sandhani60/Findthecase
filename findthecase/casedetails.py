from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import pickle
import base64
import pyttsx3


class case_details:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x770+0+0")
        self.root.title("FIND THE CASE")

        self.var_casetype = StringVar()
        self.var_dep = StringVar()
        self.var_country = StringVar()
        self.var_town = StringVar()
        self.var_Name = StringVar()
        self.var_casetype = StringVar()
        self.var_caseid = StringVar()
        self.var_gender = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()

        title_lbl = Label(self.root, text="CASE DETAILS", font=("times new roman", 35, "bold"), bg="RED", fg="BLACK")
        title_lbl.place(x=0, y=0, width=1500, height=45)
        
        frame = Frame(self.root, bd=2)
        frame.place(x=5, y=55, width=1500, height=600)
        
        # Left Frame
        left_frame = LabelFrame(frame, bd=2, text='case details', font=('times new roman', 14, 'bold'))
        left_frame.place(x=10, y=10, width=700, height=700)
       
        left_frame_data = LabelFrame(frame, bd=2, text='data ', font=('times new roman', 14, 'bold'))
        left_frame_data.place(x=20, y=50, width=670, height=300)

        case_1 = Label(left_frame_data, text="case type", font=("times new roman", 12, "bold"))
        case_1.grid(row=0, column=0, padx=10)
        case_1_combo = ttk.Combobox(left_frame_data, textvariable=self.var_casetype, font=("times new roman", 12, "bold"), state="read only")
        case_1_combo['values'] = ("select case type", 'Robbery', 'Murder', 'cheating', 'other case')
        case_1_combo.current(0)
        case_1_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Department
        case_2 = Label(left_frame_data, text="Dept", font=("times new roman", 12, "bold"))
        case_2.grid(row=0, column=2, padx=10)
        case_2_combo = ttk.Combobox(left_frame_data, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="read only")
        case_2_combo['values'] = ("select department type", 'Robbery', 'police department', 'CBI', 'CID')
        case_2_combo.current(0)
        case_2_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Place of file noticed
        case_3 = Label(left_frame_data, text="country", font=("times new roman", 12, "bold"))
        case_3.grid(row=1, column=0, padx=10)
        case_3_combo = ttk.Combobox(left_frame_data, textvariable=self.var_country, font=("times new roman", 12, "bold"), state="read only")
        case_3_combo['values'] = ("select country ", 'INDIA ', 'IRELAND', 'CANADA', 'OTHER')
        case_3_combo.current(0)
        case_3_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        case_3 = Label(left_frame_data, text="town", font=("times new roman", 12, "bold"))
        case_3.grid(row=1, column=2, padx=10)
        case_3_combo = ttk.Combobox(left_frame_data, textvariable=self.var_town, font=("times new roman", 12, "bold"), state="read only")
        case_3_combo['values'] = ("select country ", 'KAVALI ANDHRA PRADESH', 'CALIFORINA AMERICA', 'CANADA CANADA', 'OTHER')
        case_3_combo.current(0)
        case_3_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Case Person Details
        case_left_frame = LabelFrame(frame, bd=2, text='case person details', font=('times new roman', 14, 'bold'))
        case_left_frame.place(x=20, y=200, width=670, height=300)

        case_name = Label(case_left_frame, text="Name", font=("times new roman", 13, "bold"))
        case_name.grid(row=0, column=0, padx=5, sticky=W)

        case_entry = ttk.Entry(case_left_frame, textvariable=self.var_Name, width=20, font=("times new roman", 13, "bold"))
        case_entry.grid(row=0, column=1, padx=5, sticky=W)

        case_type = Label(case_left_frame, text="Case Type", font=("times new roman", 13, "bold"))
        case_type.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        case_entry = ttk.Entry(case_left_frame, textvariable=self.var_casetype, width=20, font=("times new roman", 13, "bold"))
        case_entry.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        case_id = Label(case_left_frame, text="Case Id", font=("times new roman", 13, "bold"))
        case_id.grid(row=1, column=0, padx=5, pady=10, sticky=W)

        case_entry = ttk.Entry(case_left_frame, textvariable=self.var_caseid, width=20, font=("times new roman", 13, "bold"))
        case_entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        case_gender = Label(case_left_frame, text="Case Gender", font=("times new roman", 13, "bold"))
        case_gender.grid(row=1, column=2, padx=5, sticky=W)

        case_entry = ttk.Entry(case_left_frame, textvariable=self.var_gender, width=20, font=("times new roman", 13, "bold"))
        case_entry.grid(row=1, column=3, padx=5, pady=10, sticky=W)

        case_number = Label(case_left_frame, text="Mobile Number", font=("times new roman", 13, "bold"))
        case_number.grid(row=2, column=0, padx=5, sticky=W)

        case_entry = ttk.Entry(case_left_frame, textvariable=self.var_mobile, width=20, font=("times new roman", 13, "bold"))
        case_entry.grid(row=2, column=1, padx=5, pady=10, sticky=W)

        case_email = Label(case_left_frame, text="Email", font=("times new roman", 13, "bold"))
        case_email.grid(row=2, column=2, padx=5, sticky=W)

        case_entry = ttk.Entry(case_left_frame, textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        case_entry.grid(row=2, column=3, padx=5, pady=10, sticky=W)

        # button
        btn_frame = Frame(case_left_frame, bd=2, relief=RIDGE, bg="RED")
        btn_frame.place(x=0, y=170, width=660, height=40)

        save_btn = Button(btn_frame, text="Save", font=("times new roman", 13, "bold"), bg="green", fg="white", width=14, command=self.save_data)
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", font=("times new roman", 13, "bold"), bg="blue", fg="white", width=14, command=self.update_data)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", font=("times new roman", 13, "bold"), bg="red", fg="white", width=14, command=self.delete_data)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", font=("times new roman", 13, "bold"), bg="purple", fg="white", width=14, command=self.reset)
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(case_left_frame, bd=2, relief=RIDGE, bg="RED")
        btn_frame1.place(x=0, y=230, width=660, height=200)

        exit_btn = Button(btn_frame1, text="Exit", font=("times new roman", 13, "bold"), bg="red", fg="white", width=14, command=self.exit)
        exit_btn.grid(row=0, column=0)

        # Button Frame for Voice and Image operations
        btn_frame2 = Frame(case_left_frame, bd=2, relief=RIDGE, bg="RED")
        btn_frame2.place(x=0, y=280, width=660, height=40)

        # Store Voice Button
        voice_store_btn = Button(btn_frame2, text="Store Voice", font=("times new roman", 13, "bold"), bg="blue", fg="white", width=14, command=self.store_voice)
        voice_store_btn.grid(row=0, column=0, padx=5)

        # Retrieve Voice Button
        voice_retrieve_btn = Button(btn_frame2, text="Retrieve Voice", font=("times new roman", 13, "bold"), bg="blue", fg="white", width=14, command=self.retrieve_voice)
        voice_retrieve_btn.grid(row=0, column=1, padx=5)

        # Store Image Button
        image_store_btn = Button(btn_frame2, text="Store Image", font=("times new roman", 13, "bold"), bg="blue", fg="white", width=14, command=self.store_image)
        image_store_btn.grid(row=0, column=2, padx=5)

        # Retrieve Image Button
        image_retrieve_btn = Button(btn_frame2, text="Retrieve Image", font=("times new roman", 13, "bold"), bg="blue", fg="white", width=14, command=self.retrieve_image)
        image_retrieve_btn.grid(row=0, column=3, padx=5)

        # Print Button
        print_btn = Button(btn_frame1, text="Print", font=("times new roman", 13, "bold"), bg="green", fg="white", width=14, command=self.print)
        print_btn.grid(row=0, column=1, padx=5)


        right_frame = LabelFrame(frame, bd=2, text='case details', font=('times new roman', 14, 'bold'))
        right_frame.place(x=750, y=10, width=700, height=500)

        search_label = Label(right_frame, text="Search By", font=("times new roman", 15, "bold"))
        search_label.grid(row=0, column=0, padx=5, sticky=W)

        self.s_combo = ttk.Combobox(right_frame, font=("times new roman", 12, "bold"), state="read only", width=10)
        self.s_combo['values'] = ("case number", 'name', 'mobile number')
        self.s_combo.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        self.s_entry = ttk.Entry(right_frame, font=("times new roman", 12, "bold"), width=15)
        self.s_entry.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        search_btn = Button(right_frame, text="Search", font=("times new roman", 12, "bold"), bg="blue", fg="white", width=7, command=self.search_data)
        search_btn.grid(row=0, column=3, padx=5)

        showall_btn = Button(right_frame, text="Show All", font=("times new roman", 12, "bold"), bg="green", fg="white", width=7, command=self.fetch_data)
        showall_btn.grid(row=0, column=4, padx=5)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="RED")
        table_frame.place(x=5, y=60, width=680, height=380)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.case_table = ttk.Treeview(table_frame, column=(
        "case id", "name", "case type", "gender", "mobile", "email"),
                                   xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.case_table.xview)
        scroll_y.config(command=self.case_table.yview)

        self.case_table.heading("case id", text="Case ID")
        self.case_table.heading("name", text="Name")
        self.case_table.heading("case type", text="Case Type")
        self.case_table.heading("gender", text="Gender")
        self.case_table.heading("mobile", text="Mobile")
        self.case_table.heading("email", text="Email")

        self.case_table['show'] = 'headings'
        self.case_table.column("case id", width=100)
        self.case_table.column("name", width=100)
        self.case_table.column("case type", width=100)
        self.case_table.column("gender", width=100)
        self.case_table.column("mobile", width=100)
        self.case_table.column("email", width=100)

        self.case_table.pack(fill=BOTH, expand=1)
        self.case_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def save_data(self):
        if self.var_Name.get() == "" or self.var_mobile.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="S@ndhani@1274#",
                                               database="sys")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into sandhani111 values(%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_caseid.get(),
                        self.var_Name.get(),
                        self.var_casetype.get(),
                        self.var_gender.get(),
                        self.var_mobile.get(),
                        self.var_email.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Case Added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="S@ndhani@1274#", database="sys")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from sandhani111")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.case_table.delete(*self.case_table.get_children())
            for i in data:
                self.case_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.case_table.focus()
        content = self.case_table.item(cursor_row)
        data = content['values']

        self.var_caseid.set(data[0])
        self.var_Name.set(data[1])
        self.var_casetype.set(data[2])
        self.var_gender.set(data[3])
        self.var_mobile.set(data[4])
        self.var_email.set(data[5])
    def store_voice(self):
        text_to_speak = "This is a sample voice message to store."
        engine = pyttsx3.init()
        engine.save_to_file(text_to_speak, 'voice_message.wav')
        engine.runAndWait()
        messagebox.showinfo("Success", "Voice stored successfully", parent=self.root)

    def retrieve_voice(self):
        engine = pyttsx3.init()
        engine.say("Hello! Here's your stored voice message.")
        engine.runAndWait()

    def store_image(self):
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            cv2.imwrite("stored_image.jpg", frame)
            messagebox.showinfo("Success", "Image stored successfully", parent=self.root)
        else:
            messagebox.showerror("Error", "Failed to capture image", parent=self.root)
        cam.release()

    def retrieve_image(self):
        image_path = "stored_image.jpg"
        if os.path.exists(image_path):
            img = cv2.imread(image_path)
            cv2.imshow("Stored Image", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            messagebox.showerror("Error", "Image not found", parent=self.root)


    def update_data(self):
        if self.var_Name.get() == "" or self.var_mobile.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this case details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="S@ndhani@1274#",
                                                   database="sys")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update sandhani111 set Name=%s, CaseType=%s, Gender=%s, Mobile=%s, Email=%s where CaseId=%s",
                        (
                            self.var_Name.get(),
                            self.var_casetype.get(),
                            self.var_gender.get(),
                            self.var_mobile.get(),
                            self.var_email.get(),
                            self.var_caseid.get()
                        )
                    )
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Case Details Updated Successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_caseid.get() == "":
            messagebox.showerror("Error", "Case ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Case Delete Page", "Do you want to delete this case", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="S@ndhani@1274#",
                                                   database="sys")
                    my_cursor = conn.cursor()
                    sql = "delete from sandhani111 where CaseId=%s"
                    val = (self.var_caseid.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Case deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def reset(self):
        self.var_caseid.set("")
        self.var_Name.set("")
        self.var_casetype.set("")
        self.var_gender.set("")
        self.var_mobile.set("")
        self.var_email.set("")

    def exit(self):
        self.root.destroy()

    def print(self):
        pass

    def search_data(self):
        if self.s_combo.get() == "" or self.s_entry.get() == "":
            messagebox.showerror("Error", "Search field should not be empty", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="S@ndhani@1274#",
                                               database="sys")
                my_cursor = conn.cursor()

                if self.s_combo.get() == "case number":
                    my_cursor.execute("select * from sandhani111 where CaseId LIKE '%" + str(
                        self.s_entry.get()) + "%'")
                elif self.s_combo.get() == "name":
                    my_cursor.execute("select * from sandhani111 where Name LIKE '%" + str(
                        self.s_entry.get()) + "%'")
                elif self.s_combo.get() == "mobile number":
                    my_cursor.execute("select * from sandhani111 where Mobile LIKE '%" + str(
                        self.s_entry.get()) + "%'")

                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.case_table.delete(*self.case_table.get_children())
                    for row in rows:
                        self.case_table.insert('', END, values=row)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = case_details(root)
    root.mainloop()
