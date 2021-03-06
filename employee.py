from tkinter import *

class Employee:
    def __init__(self, root):
        self.root= root
        self.root.title("Employee salary data")
        self.root.geometry("1350x700+0+0")
        root.config(bg= "white")
        title= Label(self.root, text= "Employee Salary Data", font= ("times new roman", 30, "bold"), bg= "#262626", fg= "white", pady=10).place(x=0, y=0, relwidth=1)
        
        
        #-----------------------FRAME1---------------------------------
        self.var_id= StringVar()
        self.var_name= StringVar()
        self.var_age= StringVar()
        self.var_dob= StringVar()
        self.var_contact= StringVar()
        self.var_designation= StringVar()
        self.var_experience= StringVar()
        self.var_doj= StringVar()
        self.var_lwd= StringVar()
        
        
        
        Frame1= Frame(self.root, bd=3, relief= RIDGE, bg= "white")
        Frame1.place(x= 0, y= 70, height= 630, width= 750)
        title2= Label(Frame1, text= "Employee Details", font= ("arial", 20), bg= "lightgray", fg= "black", anchor= "w", padx= 10).place(x=0, y= 0, relwidth= 1)
        
        
        #-----------------Row1----------------------------------
        lbl_id= Label(Frame1, text= "Employee ID", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 60)
        
        txt_id= Entry(Frame1, font= ("arial", 15),textvariable= self.var_id,bg= "azure", fg= "black",width= "35").place(x=180,y= 60)
        
        btn_search= Button(Frame1, text= "Search", font= ("arial", 15), bg= "white", fg= "black" ,width= "10").place(x=600, y= 50)
        
        #-----------------Row2----------------------------------
        
        lbl_name= Label(Frame1, text= "Name", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 120)
        
        txt_name= Entry(Frame1, font= ("arial", 15), textvariable= self.var_name, bg= "azure", fg= "black" ,width= "45").place(x=180, y= 120)
        
        #-----------------Row3----------------------------------
        lbl_age= Label(Frame1, text= "Age", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 180)
        
        txt_age= Entry(Frame1, font= ("arial", 15), textvariable= self.var_age, bg= "azure", fg= "black",width= "45").place(x=180, y= 180)
        
        #-----------------Row4----------------------------------
        lbl_dob= Label(Frame1, text= "Date of birth", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 240)
        
        txt_dob= Entry(Frame1, font= ("arial", 15), textvariable= self.var_dob, bg= "azure", fg= "black" ,width= "45").place(x=180, y= 240)
         
         #-----------------Row5----------------------------------
        
        lbl_contact= Label(Frame1, text= "Contact No.", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 300)
        
        txt_contact= Entry(Frame1, font= ("arial", 15), textvariable= self.var_contact, bg= "azure", fg= "black" ,width= "45").place(x=180, y= 300)
        
        #-----------------Row6----------------------------------
        lbl_designation= Label(Frame1, text= "Designation", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 360)
        
        txt_designation= Entry(Frame1, font= ("arial", 15), textvariable= self.var_designation, bg= "azure", fg= "black" ,width= "45").place(x=180, y= 360)
        
        #-----------------Row7----------------------------------
        lbl_experience= Label(Frame1, text= "Experience", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 420)
        
        txt_experience= Entry(Frame1, font= ("arial", 15), textvariable= self.var_experience, bg= "azure", fg= "black" ,width= "45").place(x=180, y= 420)
        
        #-----------------Row8----------------------------------
        lbl_doj= Label(Frame1, text= "Date of joining", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 480)
        
        txt_doj= Entry(Frame1, font= ("arial", 15), textvariable= self.var_doj, bg= "azure", fg= "black" ,width= "45").place(x=180, y= 480)
        
        #-----------------Row9----------------------------------
        lbl_lwd= Label(Frame1, text= "Last working day", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 540)
        
        txt_lwd= Entry(Frame1, font= ("arial", 15), textvariable= self.var_lwd, bg= "azure", fg= "black" ,width= "45").place(x=180, y= 540)
        
        
        
        #-----------------------FRAME2---------------------------------
        
        self.var_basic_salary= StringVar()
        self.var_pf= StringVar()
        self.var_hra= StringVar()
        self.var_allowances= StringVar()
        self.var_incometax= StringVar()
        self.var_netsalary= StringVar()
        
        
        
        Frame2= Frame(self.root, bd=3, relief= RIDGE, bg= "white")
        Frame2.place(x= 750, y= 70, height= 400, width= 600)
        title2= Label(Frame2, text= "Employee Salary Details", font= ("arial", 20), bg= "lightgray", fg= "black", anchor= "w", padx= 10).place(x=0, y= 0, relwidth= 1)
        
        
        #--------------------Row1--------------------------------------
        lbl_basic= Label(Frame2, text= "Basic Salary", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 60)
        
        txt_basic= Entry(Frame2, font= ("arial", 15), textvariable= self.var_basic_salary, bg= "azure", fg= "black", width= "15").place(x=130,y= 65, width= 150)
        
        lbl_pf= Label(Frame2, text= "PF", font= ("arial", 15), bg= "white", fg= "black").place(x=350, y= 60)
        
        txt_pf= Entry(Frame2, font= ("arial", 15), textvariable= self.var_pf, bg= "azure", fg= "black", width= "15").place(x=420,y= 65, width= 150)
        
        #--------------------Row2--------------------------------------
        lbl_hra= Label(Frame2, text= "HRA", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 120)
        
        txt_hra= Entry(Frame2, font= ("arial", 15),textvariable= self.var_hra, bg= "azure", fg= "black", width= "15").place(x=130,y= 125, width= 150)
        
        lbl_allowances= Label(Frame2, text= "Allowances", font= ("arial", 15), bg= "white", fg= "black").place(x=300, y= 120)
        
        txt_allowances= Entry(Frame2, font= ("arial", 15), textvariable= self.var_allowances, bg= "azure", fg= "black", width= "15").place(x=420,y= 125, width= 150)
        
        
        #--------------------Row3--------------------------------------
        
        lbl_tax= Label(Frame2, text= "Income Tax", font= ("arial", 15), bg= "white", fg= "black").place(x=10, y= 180)
        
        txt_tax= Entry(Frame2, font= ("arial", 15), textvariable= self.var_incometax,  bg= "azure", fg= "black", width= "15").place(x=130,y= 185, width= 150)
        
        lbl_allowances= Label(Frame2, text= "Net Salary", font= ("arial", 15), bg= "white", fg= "black").place(x=300, y= 180)
        
        txt_allowances= Entry(Frame2, font= ("arial", 15), textvariable= self.var_netsalary, bg= "azure", fg= "black", width= "15").place(x=420,y= 185, width= 150)
        
        
        #-----------------------Row4-----------------------------------
        
        btn_calculate= Button(Frame2, text= "Calculate", command= self.calculate, font= ("arial", 15), bg= "yellow", fg= "black" ,width= "10").place(x=150, y= 250)
        btn_add= Button(Frame2, text= "Add", font= ("arial", 15), bg= "green", fg= "black" ,width= "10").place(x=300, y= 250)
        btn_clear= Button(Frame2, text= "Clear", font= ("arial", 15), bg= "white", fg= "black" ,width= "10").place(x=450, y= 250)
        
        
        
        #-----------------------FRAME3---------------------------------
        Frame3= Frame(self.root, bd=3, relief= RIDGE, bg= "white")
        Frame3.place(x= 750, y= 400, height= 350, width= 600)
        title2= Label(Frame3, text= "Salary Receipt", font= ("arial", 20), bg= "lightgray", fg= "black", anchor= "w", padx= 10).place(x=0, y= 0, relwidth= 1)
        
        sal_frame= Frame(Frame3, bd=2, relief= RIDGE, bg= "azure")
        sal_frame.place(x= 0, y= 40, height= 220, relwidth=1)
        
        btn_print= Button(Frame3, text= "Print", font= ("arial", 15), bg= "deepskyblue", fg= "black" ,width= "10").place(x=480, y= 258)
        
        scroll_y= Scrollbar(sal_frame, orient= VERTICAL)
        scroll_y.pack(fill= Y, side= RIGHT)
        
        self.txt_salary_receipt= Text(sal_frame, font= ("times new roman", 15), bg= "azure", yscrollcommand= scroll_y.set)
        self.txt_salary_receipt.pack(fill= BOTH, expand=1)
        scroll_y.config(command= self.txt_salary_receipt.yview)


    def calculate(self):
        
        #------------------Frame1 variables--------------------
        
        print(self.var_id.get(),
        self.var_name.get(),
        self.var_age.get(),
        self.var_dob.get(),
        self.var_contact.get(),
        self.var_designation.get(),
        self.var_experience.get(),
        self.var_doj.get(),
        self.var_lwd.get(),
        
        #---------------------Frame2 variables--------------------
        
        self.var_basic_salary.get(),
        self.var_pf.get(),
        self.var_hra.get(),
        self.var_allowances.get(),
        self.var_incometax.get(),
        self.var_netsalary.get(),
        )
        

root = Tk()
obj= Employee(root)
root.mainloop()







