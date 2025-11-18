import mysql.connector
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk , messagebox

from tkcalendar import DateEntry


sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "Rowdy@26",
    database = "library_management"
)

def main_window():
    root = Tk()
    root.geometry("900x900")
    root.title("Library Management System")
    root.state('zoomed')
    root.attributes('-fullscreen', False)

    # Main Notebook

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both",expand=True)

    tab1 = Frame(notebook,background="lightblue")
    tab2 = Frame(notebook,background="lightpink")
    tab3 = Frame(notebook,background="lightyellow")
    tab4 = Frame(notebook,background="lightblue")
    tab5 = Frame(notebook,background="Black")

    notebook.add(tab1,text="Home")
    notebook.add(tab2,text="Users")
    notebook.add(tab3,text="Books")
    notebook.add(tab4,text="Transactions")
    notebook.add(tab5,text="Report")


    img = Image.open("library.jpg").convert("RGB")
    img = img.resize((2000,900))
    bg_img = ImageTk.PhotoImage(img)

    bg_label = Label(tab1,image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    label1 = Label(tab1,text="Library Management System",font=("Arial",40,"bold"))
    label1.place(x=400,y=100)

    label2 = Label(tab2,text="USER DETAILS",font=("Arial",12,"bold"),background="light pink")
    label2.place(x=670,y=20)

    label3 = Label(tab3,text="BOOK DETAILS",font=("Arial",12,"bold"),background="light yellow")
    label3.place(x=670,y=20)

    label4 = Label(tab4,text="TRANSACTION DETAILS",font=("Arial",12,"bold"),background="light blue")
    label4.place(x=670,y=20)

    label5 = Label(tab5,text="REPORT",font=("Arial",16,"bold"),background="black",foreground="White")
    label5.place(x=670,y=20)


    # User Notebook

    notebook1 = ttk.Notebook(tab2)
    notebook1.pack(fill="both",expand=True,padx=40,pady=50)

    user1 = Frame(notebook1, width=300, height=200, bd=2, relief="groove",background="light yellow")
    user1.place(relx=0.5, rely=0.5, anchor="center")
    user1.pack_propagate(False)
    user2 = Frame(notebook1, width=200, height=200, bd=2, relief="groove",background="light green")
    user2.place(relx=0.5, rely=0.5, anchor="center")
    user2.pack_propagate(False)
    user3 = Frame(notebook1, width=200, height=200, bd=2, relief="groove",background="lightblue")
    user3.place(relx=0.5, rely=0.5, anchor="center")
    user3.pack_propagate(False)
    user4 = Frame(notebook1,width=200,height=200,bd=2,relief="groove",background="#E6E6FA")
    user4.place(relx=0.5,rely=0.5,anchor="center")
    user4.pack_propagate(False)

    notebook1.add(user1,text = "add user")
    notebook1.add(user2,text="view user")
    notebook1.add(user3,text="update User details")
    notebook1.add(user4,text="Delete user details")

    def submit_user():
            name = user_name.get()
            mail = email.get()
            phone_no = phone.get()
            type_user = user_type.get()
            address_det = address.get("1.0", "end-1c")
            cursor = sql.cursor()
            query = "Insert into users(user_name,email,phone,user_type,address)values(%s,%s,%s,%s,%s); "
            data=(name,mail,phone_no,type_user,address_det)
            cursor.execute(query,data)
            sql.commit()
            messagebox.showinfo("Data Insert","successfully inserted")


    def clear_user():
        user_name.delete(0,END)
        email.delete(0,END)
        phone.delete(0,END)
        user_type.delete(0,END)
        address.delete("1.0", "end")

    #add user

    lab1 = Label(user1,text="User Name",foreground="black",font=("Arial",12,"bold"),background="light yellow")
    lab1.place(x=300,y=50)

    user_name = Entry(user1,width=30,highlightcolor="black",highlightthickness=2)
    user_name.place(x=450,y=50)

    lab2 = Label(user1,text="E mail",foreground="black",font=("Arial",12,"bold"),background="light yellow")
    lab2.place(x=300,y=100)

    email = Entry(user1,width=30,highlightcolor="black",highlightthickness=2)
    email.place(x=450,y=100)

    lab3 = Label(user1, text="Phone", foreground="black", font=("Arial", 12, "bold"), background="light yellow")
    lab3.place(x=300, y=150)

    phone = Entry(user1,width=30,highlightcolor="black",highlightthickness=2)
    phone.place(x=450,y=150)

    lab4 = Label(user1, text="User type", foreground="black", font=("Arial", 12, "bold"), background="light yellow")
    lab4.place(x=300, y=200)

    user_type = ttk.Combobox(user1,values=["Staff","Student","Employee"])
    user_type.place(x=450,y=200)

    user_type.set("select")

    lab5 = Label(user1, text="Address", foreground="black", font=("Arial", 12, "bold"), background="light yellow")
    lab5.place(x=300, y=270)

    address = Text(user1,width=30,height=5,highlightcolor="black",highlightthickness=2)
    address.place(x=450,y=250)

    btn1 = Button(user1,text="Submit",command=submit_user,background="red",foreground="white",font=("Arial",12,"bold"),activebackground="yellow",activeforeground="red",width=8)
    btn1.place(x=350,y=400)

    btn2 = Button(user1,text="Clear",command=clear_user,background="green",foreground="white",font=("Arial",12,"bold"),activebackground="white",activeforeground="black",width=8)
    btn2.place(x=500,y=400)

    #view user

    user_cols = ("user_id", "user_name", "email", "phone", "user_type", "address")

    user_table = ttk.Treeview(user2, columns=user_cols, show="headings")

    for col_name in user_cols:
        user_table.heading(col_name, text=col_name)
        user_table.column(col_name, anchor="center", width=130)

    user_scrollbar = ttk.Scrollbar(user2, orient="vertical", command=user_table.yview)
    user_table.configure(yscrollcommand=user_scrollbar.set)

    user_scrollbar.pack(side="right", fill="y")
    user_table.pack(fill="both", expand=True, pady=10)

    def clear_data_user():
        for item in user_table.get_children():
            user_table.delete(item)


    def load_data_user():
        try:
            clear_data_user()
            cursor = sql.cursor()
            cursor.execute("SELECT * FROM users;")
            rows = cursor.fetchall()

            print("Rows fetched:", rows)  # Debug print — check terminal
            if not rows:
                messagebox.showinfo("Info", "No users found in database.")
            else:
                for row in rows:
                    user_table.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load users: {e}")

    Button(user2, text="Data", command=load_data_user, bg="lightblue").pack(pady=5)
    Button(user2, text="Clear", command=clear_data_user, bg="lightgray").pack(pady=5)

    #update user
    # ---- UPDATE USER ----
    update_user_label = Label(user3, text="Update User Details", font=("Arial", 16, "bold"), bg="lightblue")
    update_user_label.place(x=600, y=50)

    update_user_id_label = Label(user3, text="User ID", font=("Arial", 12, "bold"), bg="lightblue")
    update_user_id_label.place(x=600, y=100)

    update_user_id_entry = Entry(user3, width=30)
    update_user_id_entry.place(x=750, y=100)

    update_user_field_label = Label(user3, text="Choose field to update", font=("Arial", 12, "bold"), bg="lightblue")
    update_user_field_label.place(x=600, y=150)

    update_user_field_choice = ttk.Combobox(
        user3,
        values=["user_name", "email", "phone", "user_type", "address"],
        state="readonly"
    )
    update_user_field_choice.place(x=600, y=200)
    update_user_field_choice.set("Select")

    update_user_value_label = Label(user3, font=("Arial", 12, "bold"), bg="lightblue")
    update_user_value_label.place(x=600, y=300)

    update_user_value_entry = Entry(user3, width=30)
    update_user_value_entry.place(x=700, y=300)

    def submit_update_user():
        choice = update_user_field_choice.get()
        if choice == "Select":
            messagebox.showerror("Error", "Please choose a field")
            return
        update_user_value_label.config(text=choice)

        def update_user():
            user_id = update_user_id_entry.get()
            value = update_user_value_entry.get()
            if not user_id or not value:
                messagebox.showerror("Error", "Both ID and value required")
                return

            cursor = sql.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            if not cursor.fetchone():
                messagebox.showerror("Error", f"No user found with ID {user_id}")
                return

            cursor.execute(f"UPDATE users SET {choice}=%s WHERE user_id=%s", (value, user_id))
            sql.commit()
            messagebox.showinfo("Success", f"{choice} updated successfully")

        update_user_btn = Button(user3, text="Update", bg="green", fg="white", width=8, command=update_user)
        update_user_btn.place(x=1000, y=300)

        update_user_clear_btn = Button(user3, text="Clear", command=lambda: update_user_value_entry.delete(0, END),
                                       bg="white", fg="black", width=8)
        update_user_clear_btn.place(x=1100, y=300)

    submit_user_btn = Button(user3, text="Submit", command=submit_update_user, font=("Arial", 12, "bold"),
                             bg="red", fg="white")
    submit_user_btn.place(x=600, y=250)

    # ---- DELETE USER ----
    delete_label = Label(user4, text="Delete User Details", font=("Arial", 12, "bold"), bg="lightblue")
    delete_label.place(x=600, y=50)

    delete_user_id_label = Label(user4, text="User ID", font=("Arial", 12, "bold"), bg="lightblue")
    delete_user_id_label.place(x=600, y=100)

    delete_user_id_entry = Entry(user4, width=30)
    delete_user_id_entry.place(x=750, y=100)

    def submit_delete_user():
        user_id = delete_user_id_entry.get()
        if not user_id:
            messagebox.showerror("Error", "Please enter User ID")
            return

        cursor = sql.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        if cursor.fetchone():
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            sql.commit()
            messagebox.showinfo("Success", "User deleted successfully")
        else:
            messagebox.showerror("Error", "User ID not found")

    delete_btn = Button(user4, text="Delete", command=submit_delete_user, font=("Arial", 12, "bold"), bg="red",
                        fg="white")
    delete_btn.place(x=600, y=200)

    delete_clear_btn = Button(user4, text="Clear", command=lambda: delete_user_id_entry.delete(0, END),
                              font=("Arial", 12, "bold"), bg="red", fg="white")
    delete_clear_btn.place(x=700, y=200)

    # Book Notebook
    notebook2 = ttk.Notebook(tab3)
    notebook2.pack(fill="both",expand=True,pady=50,padx=40)

    book1 = Frame(notebook2,width=300,height=200,bd=2,relief="groove",background="light blue")
    book1.place(relx=0.5,rely=0.5,anchor="center")
    book1.pack_propagate(False)
    book2 = Frame(notebook2,width=200,height=200,bd=2,relief="groove",background="light pink")
    book2.place(relx=0.5,rely=0.5,anchor="center")
    book2.pack_propagate(False)
    book3=Frame(notebook2,width=200,height=200,bd=2,relief="groove",background="light green")
    book3.place(relx=0.5,rely=0.5,anchor="center")
    book3.pack_propagate(False)
    book4 = Frame(notebook2,width=200,height=200,bd=2,relief="groove",background="#E6E6FA")
    book4.place(relx=0.5,rely=0.5,anchor="center")
    book4.pack_propagate(False)


    notebook2.add(book1,text="add books")
    notebook2.add(book2,text="view books")
    notebook2.add(book3,text="update books")
    notebook2.add(book4,text="delete books")

    def submit_books():
        book = book_name.get()
        auth = author.get()
        cate = category.get()
        quantity = spin.get()
        cursor = sql.cursor()
        query = "Insert into books(title,author,category,quantity)values(%s,%s,%s,%s); "
        data = (book,auth,cate,quantity)
        cursor.execute(query, data)
        sql.commit()
        messagebox.showinfo("Data Insert", "successfully inserted")

    def clear_books():
        book_name.delete(0, END)
        author.delete(0, END)
        category.delete(0, END)
        spin.delete(0, END)

    #add book


    lab1 = Label(book1, text="title", foreground="black", font=("Arial", 12, "bold"), background="light blue")
    lab1.place(x=300, y=50)

    book_name = Entry(book1, width=30, highlightcolor="black", highlightthickness=2)
    book_name.place(x=450, y=50)

    lab2 = Label(book1, text="author", foreground="black", font=("Arial", 12, "bold"), background="light blue")
    lab2.place(x=300, y=100)

    author = Entry(book1, width=30, highlightcolor="black", highlightthickness=2)
    author.place(x=450, y=100)

    lab3 = Label(book1, text="category", foreground="black", font=("Arial", 12, "bold"), background="light blue")
    lab3.place(x=300, y=150)

    category = Entry(book1, width=30, highlightcolor="black", highlightthickness=2)
    category.place(x=450, y=150)

    lab4 = Label(book1, text="quantity", foreground="black", font=("Arial", 12, "bold"), background="light blue")
    lab4.place(x=300, y=200)

    spin = Spinbox(book1, from_=0, to=50, width=5, font=("Arial", 12))
    spin.place(x=450,y=200)

    btn1 = Button(book1, text="Submit", command=submit_books, background="red", foreground="white",
                  font=("Arial", 12, "bold"), activebackground="yellow", activeforeground="red", width=8)
    btn1.place(x=350, y=300)

    btn2 = Button(book1, text="Clear", command=clear_books, background="green", foreground="white",
                  font=("Arial", 12, "bold"), activebackground="white", activeforeground="black", width=8)
    btn2.place(x=500, y=300)

    #view book details
    book_cols = ("book_id", "title", "author", "category", "quantity")


    book_table = ttk.Treeview(book2, columns=book_cols, show="headings")

    for col_name in book_cols:
        book_table.heading(col_name, text=col_name)
        book_table.column(col_name, anchor="center", width=130)

    book_scrollbar = ttk.Scrollbar(book2, orient="vertical", command=book_table.yview)
    book_table.configure(yscrollcommand=book_scrollbar.set)

    book_scrollbar.pack(side="right", fill="y")
    book_table.pack(fill="both", expand=True, pady=10)

    def clear_data_book():
        for item in book_table.get_children():
            book_table.delete(item)

    def load_data_book():
        try:
            clear_data_book()
            cursor = sql.cursor()
            cursor.execute("SELECT * FROM books;")
            rows = cursor.fetchall()

            print("Rows fetched:", rows)  # Debug print
            if not rows:
                messagebox.showinfo("Info", "No books found in database.")
            else:
                for row in rows:
                    book_table.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load books: {e}")

    Button(book2, text="Data", command=load_data_book, bg="lightblue").pack(pady=5)
    Button(book2, text="Clear", command=clear_data_book, bg="lightgray").pack(pady=5)

    #update book details

    # ---- UPDATE BOOK ----
    update_label = Label(book3, text="Update Book Details", font=("Arial", 16, "bold"), bg="lightblue")
    update_label.place(x=600, y=50)

    update_book_id_label = Label(book3, text="Book ID", font=("Arial", 12, "bold"), bg="lightblue")
    update_book_id_label.place(x=600, y=100)

    update_book_id_entry = Entry(book3, width=30)
    update_book_id_entry.place(x=750, y=100)

    update_field_label = Label(book3, text="Choose field to update", font=("Arial", 12, "bold"), bg="lightblue")
    update_field_label.place(x=600, y=150)

    update_field_choice = ttk.Combobox(book3, values=["title", "author", "category", "quantity"],
                                       state="readonly")
    update_field_choice.place(x=600, y=200)
    update_field_choice.set("Select")

    # Value entry and buttons (create once)
    update_value_label = Label(book3, font=("Arial", 12, "bold"), bg="lightblue")
    update_value_label.place(x=600, y=300)
    update_value_entry = Entry(book3, width=30)
    update_value_entry.place(x=700, y=300)

    def submit_update_book():
        choice = update_field_choice.get()
        if choice == "Select":
            messagebox.showerror("Error", "Please choose a field")
            return
        update_value_label.config(text=choice)

        def update_book():
            book_id = update_book_id_entry.get()
            value = update_value_entry.get()
            if not book_id or not value:
                messagebox.showerror("Error", "Both ID and value required")
                return

            cursor = sql.cursor()
            cursor.execute("SELECT * FROM books WHERE book_id = %s", (book_id,))
            if not cursor.fetchone():
                messagebox.showerror("Error", f"No book found with ID {book_id}")
                return

            cursor.execute(f"UPDATE books SET {choice}=%s WHERE book_id=%s", (value, book_id))
            sql.commit()
            messagebox.showinfo("Success", f"{choice} updated successfully")

        update_btn = Button(book3, text="Update", bg="green", fg="white", width=8, command=update_book)
        update_btn.place(x=1000, y=300)

        update_clear_btn = Button(book3, text="Clear", command=lambda: update_value_entry.delete(0, END),
                                  bg="white", fg="black", width=8)
        update_clear_btn.place(x=1100, y=300)

    submit_btn = Button(book3, text="Submit", command=submit_update_book, font=("Arial", 12, "bold"),
                        bg="red", fg="white")
    submit_btn.place(x=600, y=250)

    # Delete Book
    del_label = Label(book4, text="Delete Book Details", font=("Arial", 16, "bold"), foreground="Black",
                      background="#E6E6FA")
    del_label.place(x=600, y=50)

    del_book_id_label = Label(book4, text="book_id", font=("Arial", 12, "bold"), background="#E6E6FA")
    del_book_id_label.place(x=600, y=100)

    del_book_entry = Entry(book4, width=30)
    del_book_entry.place(x=700, y=100)

    def submit_delete_books():
        try:
            del_id = del_book_entry.get()
            if not del_id:
                messagebox.showerror("Error", "Please enter a Book ID")
                return

            cursor = sql.cursor()
            cursor.execute("SELECT * FROM books WHERE book_id = %s;", (del_id,))
            value = cursor.fetchone()
            if value:
                cursor.execute("DELETE FROM books WHERE book_id = %s;", (del_id,))
                sql.commit()
                messagebox.showinfo("Success", "Deleted Successfully")
            else:
                messagebox.showerror("Error", "Id not Present")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid id: {e}")

    delete_btn = Button(book4, text="Delete", command=submit_delete_books, font=("Arial", 12, "bold"), background="red",
                        foreground="white", width=8, activebackground="yellow", activeforeground="red")
    delete_btn.place(x=600, y=200)

    clear_del_btn = Button(book4, text="Clear", command=lambda: del_book_entry.delete(0, END),
                           font=("Arial", 12, "bold"), background="red", foreground="white", width=8,
                           activebackground="yellow", activeforeground="red")
    clear_del_btn.place(x=700, y=200)

    # Transaction Tab

    notebook3 = ttk.Notebook(tab4)
    notebook3.pack(fill="both",expand=True,padx=40,pady=50)

    trans1 = Frame(notebook3,width=300,height=200,bd=2,relief="groove",background="light yellow")
    trans1.place(relx=0.5,rely=0.5,anchor="center")
    trans1.pack_propagate(False)
    trans2 = Frame(notebook3,width=200,height=200,bd=2,relief="groove",background="light green")
    trans2.place(relx=0.5,rely=0.5,anchor="center")
    trans2.pack_propagate(False)
    trans3 = Frame(notebook3,width=200,height=200,bd=2,relief="groove",background="lightpink")
    trans3.place(rely=0.5,relx=0.5,anchor="center")
    trans3.pack_propagate(False)
    trans4 = Frame(notebook3,width=200,height=200,bd=2,relief="groove",background="#E6E6FA")
    trans4.place(relx=0.5,rely=0.5,anchor="center")
    trans4.pack_propagate(False)

    notebook3.add(trans1,text="add transaction")
    notebook3.add(trans2,text="view transaction")
    notebook3.add(trans3,text="update transaction details")
    notebook3.add(trans4,text="Delete transaction details")

    def clear_trans():
        user_id.delete(0,END)
        book_id.delete(0,END)
        issue_cal.delete(0,END)
        due_cal.delete(0,END)
        return_cal.delete(0,END)
        status.delete(0,END)

    def submit_trans():
        user = user_id.get()
        book = book_id.get()
        issue_date = issue_cal.get_date()
        due_date = due_cal.get_date()
        return_date = return_cal.get_date()
        status_in = status.get()

        cursor = sql.cursor()
        query = "Insert into transactions (user_id,book_id,issue_date,due_date,return_date,status_in) values(%s,%s,%s,%s,%s,%s);"
        data = (user,book,issue_date,due_date,return_date,status_in)
        cursor.execute(query,data)
        sql.commit()
        messagebox.showinfo("data Insert","Successfully Inserted")


    #add Transaction

    labo1 = Label(trans1,text="user_id",foreground="black",background="light yellow",font=("Arial",12,"bold"))
    labo1.place(x=300,y=50)

    user_id = Entry(trans1,width=30,highlightcolor="black",highlightthickness=2)
    user_id.place(x=450,y=50)

    labo2 = Label(trans1,text="book_id",foreground="black",font=("Arial",12,"bold"),background="light yellow")
    labo2.place(x=300,y=100)

    book_id = Entry(trans1,width=30,highlightcolor="black",highlightthickness=2)
    book_id.place(x=450,y=100)

    labo3 = Label(trans1,text="issue_date",foreground="black",font=("Arial",12,"bold"),background="light yellow")
    labo3.place(x=300,y=150)

    issue_cal = DateEntry(trans1,width=20, date_pattern='dd-mm-yyyy',background="black")
    issue_cal.place(x=450,y=150)

    issue_cal.delete(0, END)
    issue_cal.insert(0, "DD-MM-YYYY")

    lab4 = Label(trans1,text="due_date",foreground="black",font=("Arial",12,"bold"),background="light yellow")
    lab4.place(x=300,y=200)

    due_cal = DateEntry(trans1,width=20, date_pattern='dd-mm-yyyy',background="black")
    due_cal.place(x=450,y=200)

    due_cal.delete(0, END)
    due_cal.insert(0, "DD-MM-YYYY")

    lab5 = Label(trans1,text="return_date",foreground="black",font=("Arial",12,"bold"),background="light yellow")
    lab5.place(x=300,y=250)

    return_cal = DateEntry(trans1,width=20, date_pattern='dd-mm-yyyy',background="black")
    return_cal.place(x=450,y=250)

    return_cal.delete(0, END)
    return_cal.insert(0, "DD-MM-YYYY")

    lab6 = Label(trans1,text="status in ",foreground="black",font=("Arial",12,"bold"),background="light yellow")
    lab6.place(x=300,y=300)

    status = ttk.Combobox(trans1,values=["Returned","Pending","Permission"],state="readonly")
    status.place(x=450,y=300)
    status.set("Select")

    btn1 = Button(trans1,text="Submit",command=submit_trans,background="red",foreground="white",font=("Arial",12,"bold"),activebackground="yellow",activeforeground="red",width=8)
    btn1.place(x=300,y=350)

    btn2 = Button(trans1,text="Clear",command=clear_trans,background="green",foreground="white",font=("Arial",12,"bold"),activebackground="white",activeforeground="black",width=8)
    btn2.place(x=450,y=350)

    #view transaction

    trans_cols = ("transaction_id", "user_id", "book_id", "issue_date", "due_date", "return_date", "status_in")
    trans_table = ttk.Treeview(trans2, columns=trans_cols, show="headings")

    for col_name in trans_cols:
        trans_table.heading(col_name, text=col_name)
        trans_table.column(col_name, anchor="center", width=130)

    trans_scrollbar = ttk.Scrollbar(trans2, orient="vertical", command=trans_table.yview)
    trans_table.configure(yscrollcommand=trans_scrollbar.set)

    trans_scrollbar.pack(side="right", fill="y")
    trans_table.pack(fill="both", expand=True, pady=10)

    def clear_data_trans():
        for item in trans_table.get_children():
            trans_table.delete(item)

    def load_data_trans():
        try:
            clear_data_trans()
            cursor = sql.cursor()
            cursor.execute("SELECT * FROM transactions;")
            rows = cursor.fetchall()

            print("Rows fetched:", rows)  # Debug print — check terminal
            if not rows:
                messagebox.showinfo("Info", "No transactions found in database.")
            else:
                for row in rows:
                    trans_table.insert("", "end", values=row)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load transactions: {e}")

    Button(trans2, text="Data", command=load_data_trans, bg="lightblue").pack(pady=5)
    Button(trans2, text="Clear", command=clear_data_trans, bg="lightgray").pack(pady=5)

    #update transaction

    # Update Transaction
    update_label = Label(trans3, text="Update Transaction Details", font=("Arial", 16, "bold"), background="lightpink")
    update_label.place(x=600, y=50)

    transaction_id_label = Label(trans3, text="transaction_id", font=("Arial", 12, "bold"), background="lightpink")
    transaction_id_label.place(x=600, y=100)

    transaction_id_entry = Entry(trans3, width=30)
    transaction_id_entry.place(x=750, y=100)

    up_label = Label(trans3, text="Choose the value to be changed", font=("Arial", 12, "bold"), background="lightpink")
    up_label.place(x=600, y=150)

    field_choice = ttk.Combobox(trans3,
                                values=["user_id", "book_id", "issue_date", "due_date", "return_date", "status_in"],
                                state="readonly")
    field_choice.place(x=600, y=200)
    field_choice.set("Select")

    def submit_update_trans():
        choice = field_choice.get()
        if choice == "Select":
            messagebox.showerror("Error", "Please choose a field to update")
            return

        field_label = Label(trans3, text=choice, font=("Arial", 12, "bold"), background="lightpink", foreground="black")
        field_label.place(x=600, y=300)

        value_entry = Entry(trans3, width=30)
        value_entry.place(x=700, y=300)

        def update_transaction():
            transact_id = transaction_id_entry.get()
            entry_value = value_entry.get()

            if not transact_id or not entry_value:
                messagebox.showerror("Error", "Both Id and value are required")
                return

            cursor = sql.cursor()
            cursor.execute("SELECT * FROM transactions WHERE transaction_id = %s", (transact_id,))
            record = cursor.fetchone()
            if not record:
                messagebox.showerror("Error", f"No Record found with Id {transact_id}")
                return

            query = f"UPDATE transactions SET {choice} = %s WHERE transaction_id = %s;"
            cursor.execute(query, (entry_value, transact_id))
            sql.commit()
            messagebox.showinfo("Success", f"{choice} updated Successfully")

        update_btn = Button(trans3, text="Update", command=update_transaction, background="green", foreground="white",
                            width=8)
        update_btn.place(x=1000, y=300)

        clear_btn = Button(trans3, text="Clear", command=lambda: value_entry.delete(0, END), background="white",
                           foreground="black", width=8)
        clear_btn.place(x=1100, y=300)

    submit_btn = Button(trans3, text="Submit", command=submit_update_trans, font=("Arial", 12, "bold"),
                        background="red", foreground="white", width=8, activebackground="yellow",
                        activeforeground="red")
    submit_btn.place(x=600, y=250)

    # Delete Transaction
    del_trans_label = Label(trans4, text="Delete Transaction Details", font=("Arial", 12, "bold"), background="#E6E6FA")
    del_trans_label.place(x=600, y=100)

    del_trans_id_label = Label(trans4, text="transaction_id", font=("Arial", 12, "bold"), background="#E6E6FA")
    del_trans_id_label.place(x=600, y=150)

    del_trans_entry = Entry(trans4, width=30)
    del_trans_entry.place(x=750, y=150)

    def submit_delete_trans():
        try:
            del_id = del_trans_entry.get()
            if not del_id:
                messagebox.showerror("Error", "Please enter a Transaction ID")
                return

            cursor = sql.cursor()
            cursor.execute("SELECT * FROM transactions WHERE transaction_id = %s;", (del_id,))
            value = cursor.fetchone()
            if value:
                cursor.execute("DELETE FROM transactions WHERE transaction_id = %s;", (del_id,))
                sql.commit()
                messagebox.showinfo("Success", "Deleted Successfully")
            else:
                messagebox.showerror("Error", "Id not present")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid id: {e}")

    delete_btn = Button(trans4, text="Delete", command=submit_delete_trans, font=("Arial", 12, "bold"),
                        background="red", foreground="white", width=8, activebackground="yellow",
                        activeforeground="red")
    delete_btn.place(x=600, y=200)

    clear_del_btn = Button(trans4, text="Clear", command=lambda: del_trans_entry.delete(0, END),
                           font=("Arial", 12, "bold"), background="red", foreground="white", width=8,
                           activebackground="yellow", activeforeground="red")
    clear_del_btn.place(x=700, y=200)

    # Report

    def show_report():
        Report_butn.destroy()
        notebook4 = ttk.Notebook(tab5)
        notebook4.pack(fill="both",expand=True,pady=50,padx=40)

        rep1 = Frame(notebook4,width=300,height=200,bd=2,relief="groove",background="white")
        rep1.place(relx=0.5,rely=0.5,anchor="center")
        rep1.pack_propagate(False)
        notebook4.add(rep1,text="Report")

        lb1 = Label(rep1,text= "Count ",font=("Arial",12,"bold"),foreground="black",bg="white")
        lb1.place(x=100,y=50)


        cursor = sql.cursor()
        query1 = "select count(*) from users where user_name is not null ;"
        cursor.execute(query1)
        res = cursor.fetchone()
        total_user = res[0]

        lb2 = Label(rep1,text=f"Total users: {total_user}",foreground="red",bg="white",font=("Arial",12,"bold"))
        lb2.place(x=100,y=100)

        cursor = sql.cursor()
        query1 = "select count(*) from books where title is not null ;"
        cursor.execute(query1)
        res = cursor.fetchone()
        total_book = res[0]

        lb2 = Label(rep1,text=f"Total books: {total_book}",foreground="red",bg="white",font=("Arial",12,"bold"))
        lb2.place(x=100,y=150)


        cursor = sql.cursor()
        query1 = "select count(*) from transactions;"
        cursor.execute(query1)
        res = cursor.fetchone()
        total_trans = res[0]

        lb2 = Label(rep1,text=f"Total transaction: {total_trans}",foreground="red",bg="white",font=("Arial",12,"bold"))
        lb2.place(x=100,y=200)

        lb2 = Label(rep1, text="Return Status", foreground="black",bg="white", font=("Arial", 12, "bold"))
        lb2.place(x=600, y=50)

        user_status = StringVar()
        status_drop = OptionMenu(rep1,user_status,"Returned","pending","permission")
        user_status.set("select status")
        status_drop.place(x=600,y=100)

        result = Label(rep1,text=" ",font=("Arial",12,"bold"),fg = "red",bg = "white")
        result.place(x=600,y=200)

        def status():
            cursor = sql.cursor()
            choice = user_status.get()
            query2 = f"select count(*) from transactions where status_in = '{choice}';"
            cursor.execute(query2)
            res1 = cursor.fetchone()
            total_status = res1[0]

            result.config(text=f"Total {choice} : {total_status}")

        btn = Button(rep1,text="count",command=status,background="green",foreground="white",activeforeground="red",activebackground="yellow",width=8,font=("Arial",12,"bold"))
        btn.place(x=600,y=150)

        def show_delay():
            cursor = sql.cursor()
            query = "SELECT user_id, DATEDIFF(return_date, due_date) AS days_delay FROM transactions WHERE return_date IS NOT NULL;"
            cursor.execute(query)
            result = cursor.fetchall()

            # clear existing rows
            for row in tree.get_children():
                tree.delete(row)

            # insert new rows
            for row in result:
                tree.insert("", "end", values=row)

        # Label
        lb2 = Label(rep1, text="Delayed List", foreground="black", bg="white", font=("Arial", 12, "bold"))
        lb2.place(x=900, y=50)

        # Button
        btn = Button(rep1, text="Show delays", font=("Arial", 10, "bold"), width=10,
                     command=show_delay, background="yellow", foreground="black",
                     activeforeground="red", activebackground="yellow")
        btn.place(x=900, y=100)

        # Frame for Treeview + Scrollbars
        table_frame = Frame(rep1, bg="white")
        table_frame.place(x=900, y=150, width=220, height=120)  # small fixed area

        # Treeview setup
        col = ("user_id", "Days_Delayed")
        tree = ttk.Treeview(table_frame, columns=col, show="headings")

        tree.heading("user_id", text="User Id")
        tree.heading("Days_Delayed", text="Days Delayed")

        tree.column("user_id", width=80, anchor="center")
        tree.column("Days_Delayed", width=100, anchor="center")

        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Layout inside frame
        tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        # Expand treeview within frame
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

    Report_butn = Button(tab5,text="Show Report",font=("Arial",16,"bold"),command=show_report,background="red",foreground="white",activeforeground="red",activebackground="yellow")
    Report_butn.place(x=650,y=50)



    root.mainloop()


tk = Tk()
tk.geometry("900x900")
tk.title("Login")

def submit():
    username= ent1.get()
    password = ent2.get()
    if username == "admin" and password =="1234":
        messagebox.showinfo("login","Successfully Logined")
        tk.destroy()
        main_window()
    else:
        messagebox.showerror("login","login failed")
def clear():
    ent1.delete(0,END)
    ent2.delete(0,END)

lab1 = Label(tk,text="Library Management System",foreground="Black",font=("Arial",30,"bold"))
lab1.place(x=400,y=50)

lab1 = Label(tk,text="Login",foreground="Red",font=("Arial",30,"bold"))
lab1.place(x=600,y=150)

lab2 =Label(tk,text="Username",foreground="black",font=("Arial",12,"bold"))
lab2.place(x=500,y=250)

ent1 = Entry(tk,width=30)
ent1.place(x=600,y=250)

lab3 = Label(tk,text="Password",foreground="black",font=("Arial",12,"bold"))
lab3.place(x=500,y=300)

ent2 = Entry(tk,width=30)
ent2.place(x=600,y=300)
ent2.config(show="*")

btn = Button(tk,text="Submit",command=submit,foreground="white",background="red",activebackground="yellow",activeforeground="red",width=10,padx=10,pady=10,font=("Arial",12,"bold"))
btn.place(x=550,y=350)

btn = Button(tk,text="Clear",command=clear,foreground="white",background="green",activeforeground="black",activebackground="white",width=10,pady=10,padx=10,font=("Arial",12,"bold"))
btn.place(x=700,y=350)


tk.mainloop()