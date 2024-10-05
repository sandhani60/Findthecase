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

