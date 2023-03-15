import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
from appGui import StudentlistingWidget

class Scripts(StudentlistingWidget):
    def __init__(self, *args, **kwargs):
        StudentlistingWidget.__init__(self, *args, **kwargs)



    def selectListFileAdress(self):
        fileadress = filedialog.askopenfilename(title="Liste dosyası seçiniz" ,filetypes=[("TXT files","*.txt"), ("All files","*.*")])
        self.entryStudentListFileAdress.insert(0, fileadress)

    def addStudentToList(self):
        isim = self.entryStudentName.get()
        fileAdress = self.entryStudentListFileAdress.get()
        if isim == "":
            tk.messagebox.showerror(title="Hata", message="İsim bilgisi boş")
        elif fileAdress == "":
            tk.messagebox.showerror(title="Hata", message="Dosya adresi boş")
        else:
            try:
                with open(fileAdress, "a", encoding="utf-8") as listFile:
                    for i in isim.split(","):
                        listFile.write(f"\n{i}")

            except:tk.messagebox.showerror(title="Hata", message="İsim Eklenemedi")

    def deleteStudentFromList(self):
        isim = self.entryStudentName.get()
        fileAdress = self.entryStudentListFileAdress.get()
        if isim == "":
            tk.messagebox.showerror(title="Hata", message="İsim bilgisi boş")
        elif fileAdress == "":
            tk.messagebox.showerror(title="Hata", message="Dosya adresi boş")
        else:
            try:
                with open(fileAdress, "r+", encoding="utf-8") as listFile:
                    readedfile = listFile.read()
                    studentlist = readedfile.split("\n")
                    for i in isim.split(","):
                        studentlist.remove(isim)
                    file = open(fileAdress, "w", encoding="utf-8")
                    for s in studentlist:
                        file.write(f"{s}\n")
                    file.close()

            except:tk.messagebox.showerror(title="Hata", message="İsim silinemedi")

    def printStudentNumber(self):
        isim = self.entryStudentName.get()
        fileAdress = self.entryStudentListFileAdress.get()
        with open(fileAdress, "r", encoding="utf-8") as listFile:
            readedfile = listFile.read()
            studentlist = readedfile.split("\n")
            tk.messagebox.showinfo(title="Bilgi", message=f"{isim} - {studentlist.index(isim)}\n")
            studentlist.index(isim)

    def refreshStudentList(self):
        fileAdress = self.entryStudentListFileAdress.get()
        if fileAdress == "":
            tk.messagebox.showerror(title="Hata", message="Dosya adresi boş")
        else:
            try:
                self.textStudentList.delete("0.0","end")
                with open(fileAdress, "r", encoding="utf-8") as listFile:
                    readedfile = listFile.read()
                    studentlist = readedfile.split("\n")

                    i = 0
                    for student in studentlist:
                        self.textStudentList.insert("0.0", f"{i} - {student}\n")
                        i +=1
            except:tk.messagebox.showerror(title="Hata", message="Seçilen dosya okunamadı")
