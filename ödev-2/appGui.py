#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.scrolledframe import ScrolledFrame


class StudentlistingWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(StudentlistingWidget, self).__init__(master, **kw)
        panedwindow1 = ttk.Panedwindow(self, orient="horizontal")
        frame4 = ttk.Frame(panedwindow1)
        frame4.configure(height=200, padding=10, width=200)
        labelframe4 = ttk.Labelframe(frame4)
        labelframe4.configure(
            height=200,
            text='Öğrenci listesi adresi',
            width=200)
        self.entryStudentListFileAdress = ttk.Entry(labelframe4)
        self.entryStudentListFileAdress.pack(
            expand="true", fill="x", padx=10, pady=5, side="left")
        self.buttonSelectFromFiles = ttk.Button(labelframe4)
        self.buttonSelectFromFiles.configure(
            cursor="hand2", text='Dosyalardan seç')
        self.buttonSelectFromFiles.pack(
            ipadx=5, ipady=5, padx=5, pady=5, side="left")
        self.buttonSelectFromFiles.configure(command=self.selectListFileAdress)
        labelframe4.pack(fill="x", side="top")
        labelframe5 = ttk.Labelframe(frame4)
        labelframe5.configure(
            height=200,
            padding=5,
            text='Öğrenci bilgisi',
            width=200)
        label6 = ttk.Label(labelframe5)
        label6.configure(text='Öğrenci ismi yazınız')
        label6.pack(anchor="w", side="top")
        frame6 = ttk.Frame(labelframe5)
        frame6.configure(height=200, width=200)
        label3 = ttk.Label(frame6)
        label3.configure(text='isim soyisim : ')
        label3.pack(side="left")
        self.entryStudentName = ttk.Entry(frame6)
        self.entryStudentName.pack(
            expand="true", fill="x", padx=5, side="left")
        frame6.pack(expand="true", fill="x", side="top")
        label4 = ttk.Label(labelframe5)
        label4.configure(
            text='birden fazla öğrenci girmek için öğrenci isimlerini virgül( , ) ile ayırınız.')
        label4.pack(side="left")
        labelframe5.pack(expand="false", fill="x", pady=10, side="top")
        labelframe6 = ttk.Labelframe(frame4)
        labelframe6.configure(
            height=200,
            padding=10,
            text='işlemler',
            width=200)
        self.buttonAddStudent = ttk.Button(labelframe6)
        self.buttonAddStudent.configure(cursor="hand2", text='Öğrenciyi ekle')
        self.buttonAddStudent.pack(ipadx=5, ipady=5, side="left")
        self.buttonAddStudent.configure(command=self.addStudentToList)
        self.buttonDeleteStudent = ttk.Button(labelframe6)
        self.buttonDeleteStudent.configure(
            cursor="hand2", text='Öğrenciyi sil')
        self.buttonDeleteStudent.pack(ipadx=5, ipady=5, side="left")
        self.buttonDeleteStudent.configure(command=self.deleteStudentFromList)
        self.buttonGetStudentNumber = ttk.Button(labelframe6)
        self.buttonGetStudentNumber.configure(
            cursor="hand2", text='Numarasını öğren')
        self.buttonGetStudentNumber.pack(ipadx=5, ipady=5, side="left")
        self.buttonGetStudentNumber.configure(command=self.printStudentNumber)
        labelframe6.pack(fill="x", side="top")
        label7 = ttk.Label(frame4)
        label7.configure(
            font="{consolas} 10 {}",
            foreground="#999",
            text='https://github.com/ZEGenc')
        label7.pack(side="bottom")
        frame4.pack(expand="true", fill="both", side="top")
        panedwindow1.add(frame4, weight="1")
        frame5 = ttk.Frame(panedwindow1)
        frame5.configure(height=200, padding=10, width=200)
        scrolledframe1 = ScrolledFrame(frame5, scrolltype="both")
        scrolledframe1.configure(usemousewheel=True)
        self.textStudentList = tk.Text(scrolledframe1.innerframe)
        self.textStudentList.configure(height=10, width=10)
        _text_ = '- liste seçtiğinizde burada görünür\n- seçtiğinizde veya değiştirdiğinizde yenileyiniz'
        self.textStudentList.insert("0.0", _text_)
        self.textStudentList.pack(expand="true", fill="both", side="top")
        scrolledframe1.pack(expand="true", fill="both", side="top")
        self.buttonRefreshStudentList = ttk.Button(frame5)
        self.buttonRefreshStudentList.configure(cursor="hand2", text='Yenile')
        self.buttonRefreshStudentList.pack(
            ipadx=10, ipady=5, pady=10, side="top")
        self.buttonRefreshStudentList.configure(
            command=self.refreshStudentList)
        frame5.pack(side="top")
        panedwindow1.add(frame5, weight="1")
        panedwindow1.pack(expand="true", fill="both", side="top")
        self.configure(height=600, width=1000)
        self.pack(expand="true", fill="both", side="top")
        self.pack_propagate(0)

    def selectListFileAdress(self):
        pass

    def addStudentToList(self):
        pass

    def deleteStudentFromList(self):
        pass

    def printStudentNumber(self):
        pass

    def refreshStudentList(self):
        pass