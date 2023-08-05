import tkinter
from tkinter import *
import pymysql.cursors
from tkinter import ttk

class StudentData:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1500x800')
        title1=Label(self.root,text='Welcome to Narayana Tech house',font=('CASTELLAR',30),border=6,relief=RAISED,bg='green',fg='white')
        title1.pack(fill='x')
        #main window taking as two parts DataEntryFrame and another is DasaDisplayFrame

        self.rollnoVar =StringVar()
        self.fnameVar =StringVar()
        self.lnameVar =StringVar()
        self.emailidVar =StringVar()
        self.cnameVar =StringVar()
        self.mobileVar= StringVar()
        self.feeVar = StringVar()
        self.inameVar = StringVar()
        self.locationVar = StringVar()

        
      
        #creating DataentryFrame
        
        DataEntryFrame=Frame(self.root,bg='green')
        DataEntryFrame.place(x=10,y=70,width=450,height=720)
        
        #creating DisplayDataFrame
        
        DataDisplayFrame= Frame(self.root,bg='green')
        DataDisplayFrame.place(x=470,y=70,width=1020,height=720)

        #workin on DataEntryFrame
        
        title2=Label(DataEntryFrame,text='Data Entry Here!!!',font=('cambria',20),bg='green',fg='white',border=5,relief=RAISED)
        title2.grid(row=0,columnspan=2,padx=100,pady=10)

        #rollno:
        lb1RollNo=Label(DataEntryFrame,text='RollNumber:',font=('cambria',15),bg='green',fg='white')
        lb1RollNo.grid(row=1,column=0,sticky='w' )

        entryRollNo=Entry(DataEntryFrame,font=('Cambria',15),textvariable=self.rollnoVar)
        entryRollNo.grid(row=1,column=1,pady=10)

        #First Name:
        lb1fname=Label(DataEntryFrame,text='FirstName:',font=('cambria',15),bg='green',fg='white')
        lb1fname.grid(row=2,column=0,sticky='w' )

        entryfname=Entry(DataEntryFrame,font=('Cambria',15),textvariable=self.fnameVar)
        entryfname.grid(row=2,column=1,pady=10)

        #Last Name:
        lb1lname=Label(DataEntryFrame,text='LastName:',font=('cambria',15),bg='green',fg='white')
        lb1lname.grid(row=3,column=0,sticky='w' )

        entrylname=Entry(DataEntryFrame,font=('Cambria',15),textvariable=self.lnameVar)
        entrylname.grid(row=3,column=1,pady=10)

        #Email ID:
        lb1email=Label(DataEntryFrame,text='EmailID:',font=('cambria',15),bg='green',fg='white')
        lb1email.grid(row=4,column=0,sticky='w' )

        entryemail=Entry(DataEntryFrame,font=('Cambria',15),textvariable=self.emailidVar)
        entryemail.grid(row=4,column=1,pady=10)

        #Course Name:
        lb1cname=Label(DataEntryFrame,text='CourseName:',font=('cambria',15),bg='green',fg='white')
        lb1cname.grid(row=5,column=0,sticky='w' )

        entrycname=Entry(DataEntryFrame,font=('Cambria',15),textvariable=self.cnameVar)
        entrycname.grid(row=5,column=1,pady=10)

        #Mobile Number:
        lb1mnumber=Label(DataEntryFrame,text='MobileNumber:',font=('cambria',15),bg='green',fg='white')
        lb1mnumber.grid(row=6,column=0,sticky='w' )

        entrymnumber=Entry(DataEntryFrame,font=('Cambria',15),textvariable=self.mobileVar)
        entrymnumber.grid(row=6,column=1,pady=10)

        #Fee:
        lb1fee=Label(DataEntryFrame,text='CourseFee:',font=('cambria',15),bg='green',fg='white')
        lb1fee.grid(row=7,column=0,sticky='w' )

        entryfee=Entry(DataEntryFrame,font=('Cambria',15),textvariable=self.feeVar)
        entryfee.grid(row=7,column=1,pady=10)

        #Institute name:
        lb1iname=Label(DataEntryFrame,text='InstituteName:',font=('cambria',15),bg='green',fg='white')
        lb1iname.grid(row=8,column=0,sticky='w' )

        entryiname=Entry(DataEntryFrame,font=('Cambria',15),textvariable=self.inameVar)
        entryiname.grid(row=8,column=1,pady=10)

        #Location:
        lb1location=Label(DataEntryFrame,text='Location:',font=('cambria',15),bg='green',fg='white')
        lb1location.grid(row=9,column=0,sticky='w' )

        entrymnumber=Entry(DataEntryFrame,font=('Cambria',15),textvariable=self.locationVar)
        entrymnumber.grid(row=9,column=1,pady=10)

        #working on Button Frame
        btnFrame=Frame(DataEntryFrame, border=5, relief=RAISED, bg='green')
        btnFrame.place(x=10, y=520, width=430, height=120)
        
        #creating Add button
        
        btnAdd=Button(btnFrame,text='Add',command=self.adding ,font=('cambria',15),bg='red',fg='yellow')
        btnAdd.grid(row=0,column=0,pady=30,padx=16)

        #Creating Update button

        btnAdd=Button(btnFrame,text='Update',command=self.updating,font=('cambria',15),bg='red',fg='yellow')
        btnAdd.grid(row=0,column=1,pady=30,padx=16)

        #creating delete button

        btnAdd=Button(btnFrame,text='Delete',command=self.deleting,font=('cambria',15),bg='red',fg='yellow')
        btnAdd.grid(row=0,column=2,pady=30,padx=16)

        #creating clear button
        
        btnAdd=Button(btnFrame,text='Clear',command=self.clearing ,font=('cambria',15),bg='red',fg='yellow')
        btnAdd.grid(row=0,column=3,pady=30,padx=16)

        #working with data display Frame
        title3=Label(DataDisplayFrame, text='Data Display Here!!',bg='green',fg='white',font=('cambria',20),border=5, relief=RAISED)
        title3.place(x=350, y=10)
        
        tableFrame =Frame(DataDisplayFrame,bg='green',border=5,relief=RAISED)
        tableFrame.place(x=30,y=70, width= 850,height= 420)

        self.studentsinfo=ttk.Treeview(tableFrame, columns=('Roll_NO','First_Name','Last_Name','EmailId','Course_Name','Mobile','Fee','Iname','Location'))
        self.studentsinfo.heading('Roll_NO', text='Roll No')
        self.studentsinfo.heading('First_Name', text='First Name')
        self.studentsinfo.heading('Last_Name', text='Last Name')
        self.studentsinfo.heading('EmailId', text='Email Id')
        self.studentsinfo.heading('Course_Name', text='Course Name')
        self.studentsinfo.heading('Mobile', text='Contact')
        self.studentsinfo.heading('Fee', text='Course Fee')
        self.studentsinfo.heading('Iname', text='Institute Name')
        self.studentsinfo.heading('Location', text='Location')

        self.studentsinfo['show'] ='headings'
        

        self.studentsinfo.column('Roll_NO', width=90)
        self.studentsinfo.column('First_Name',width=90)
        self.studentsinfo.column('Last_Name',width=90)
        self.studentsinfo.column('EmailId',width=115)
        self.studentsinfo.column('Course_Name',width=90)
        self.studentsinfo.column('Mobile',width=90)
        self.studentsinfo.column('Fee',width=90)
        self.studentsinfo.column('Iname',width=90)
        self.studentsinfo.column('Location',width=90)

        self.fetching()
        self.studentsinfo.bind('<ButtonRelease-1>',self.getting_row)
        self.studentsinfo.pack()
    
    


    def adding(self):
        connection = pymysql.connect(host='localhost',user ='root',password='root',db='studentdatadb')
        c=connection.cursor()
        c.execute('insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                  (
                   self.rollnoVar.get(),
                   self.fnameVar.get(),
                   self.lnameVar.get(),
                   self.emailidVar.get(),
                   self.cnameVar.get(),
                   self.mobileVar.get(),
                   self.feeVar.get(),
                   self.inameVar.get(),
                   self.locationVar.get()
                     )
                )
        connection.commit()
        self.fetching()
        self.clearing()
        connection.close()
        
    def clearing(self):
         self.rollnoVar.set('')
         self.fnameVar.set('')
         self.lnameVar.set('')
         self.emailidVar.set('')
         self.cnameVar.set('')
         self.mobileVar.set('')
         self.feeVar.set('')
         self.inameVar.set('')
         self.locationVar.set('')

    def fetching(self):
        connection = pymysql.connect(host='localhost',user ='root',password='root',db='studentdatadb')
        c=connection.cursor()
        c.execute('select *from studentdata')
        data=c.fetchall()
        self.studentsinfo.delete(*self.studentsinfo.get_children())
        for i in data:
            self.studentsinfo.insert('',END,values=i)
            connection.commit()
        connection.close()
    def getting_row(self,a):
        cursor_row = self.studentsinfo.focus()
        content =self.studentsinfo.item(cursor_row)
        row = content['values']
        self.rollnoVar.set(row[0])
        self.fnameVar.set(row[1])
        self.lnameVar.set(row[2])
        self.emailidVar.set(row[3])
        self.cnameVar.set(row[4])
        self.mobileVar.set(row[5])
        self.feeVar.set(row[6])
        self.inameVar.set(row[7])
        self.locationVar.set(row[8])

    def updating(self):
        connection = pymysql.connect(host='localhost',user ='root',password='root',db='studentdatadb')
        c=connection.cursor()
        c.execute('update studentdata set First_Name=%s, Last_Name=%s, EmailId=%s, Course_Name=%s, Mobile=%s, Fee=%s, Iname=%s, Location=%s where Roll_No=%s',
                  (
                      self.fnameVar.get(),
                      self.lnameVar.get(),
                      self.emailidVar.get(),
                      self.cnameVar.get(),
                      self.mobileVar.get(),
                      self.feeVar.get(),
                      self.inameVar.get(),
                      self.locationVar.get(),
                      self.rollnoVar.get()
                      )
                  )
        connection.commit()
        self.fetching()
        self.clearing()
        connection.close()
        
    def deleting(self):

        connection = pymysql.connect(host='localhost',user ='root',password='root',db='studentdatadb')
        c=connection.cursor()
        c.execute('delete from studentdata where Roll_No=%s',self.rollnoVar.get())
        connection.commit()
        self.fetching()
        self.clearing()
        connection.close()
        
        
                                              
root=Tk()
obj=StudentData(root)
    
