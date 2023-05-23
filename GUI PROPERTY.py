#!/usr/bin/env python
# coding: utf-8

# In[10]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[8]:


#!/usr/bin/env python
# coding: utf-8

# In[20]:


#!/usr/bin/env python
# coding: utf-8

# In[13]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import tkinter as tk
from tkinter import*
from tkinter import messagebox
import random,os,tempfile,smtplib

# function

def clear():
    sofaEntry.delete (0, END)
    mejatamuEntry.delete (0, END)
    lemaribuffetEntry. delete (0, END)
    mejatvEntry.delete (0, END)
    mejamakanEntry.delete (0, END)
    kursiEntry.delete (0, END)

    kasurEntry.delete (0, END)
    lemaripakaianEntry.delete (0, END)
    mejariasEntry.delete (0, END)
    setkmEntry.delete (0, END)
    wcEntry.delete (0, END)
    wastafelEntry.delete (0, END)

    kulkasEntry.delete (0, END)
    komporEntry.delete (0, END)
    setmasakEntry.delete (0, END)
    wastafeldprEntry.delete (0, END)
    kabinetEntry.delete (0, END)
    setmakanEntry.delete (0, END)
    
    sofaEntry.insert (0, 0)
    mejatamuEntry.insert (0, 0)
    lemaribuffetEntry. insert (0, 0)
    mejatvEntry.insert (0, 0)
    mejamakanEntry.insert (0, 0)
    kursiEntry.insert (0, 0)

    kasurEntry.insert (0, 0)
    lemaripakaianEntry.insert (0, 0)
    mejariasEntry.insert (0, 0)
    setkmEntry.insert (0, 0)
    wcEntry.insert (0, 0)
    wastafelEntry.insert (0, 0)

    kulkasEntry.insert (0, 0)
    komporEntry.insert (0, 0)
    setmasakEntry.insert (0, 0)
    wastafeldprEntry.insert (0, 0)
    kabinetEntry.insert (0, 0)
    setmakanEntry.insert (0, 0)
    
    taxrumahEntry.delete(0, END)
    taxkamarEntry.delete(0, END)
    taxdapurEntry.delete(0, END)
    
    hargarumahEntry.delete(0, END)
    hargakamarEntry.delete(0, END)
    hargadapurEntry.delete(0, END)
    
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    NoBayarEntry.delete(0, END)
    
    textarea.delete(1.0,END)


def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent')
        except:
            messagebox.showerror('Error', 'Something went wrong. Please try again.')

    root1 = Toplevel()
    root1.title('Send Gmail')
    root1.config(bg='gray20')
    root1.resizable(0, 0)

    senderFrame = LabelFrame(root1, text='Pengirim', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
    senderFrame.grid(row=0, column=0, padx=10, pady=8)

    senderLabel = Label(senderFrame, text="Email Pengirim", font=('arial', 14, 'bold'), bg='gray20', fg='white')
    senderLabel.grid(row=0, column=0, padx=40, pady=20)

    senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
    senderEntry.grid(row=0, column=1, padx=10, pady=8)

    passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bg='gray20', fg='white')
    passwordLabel.grid(row=1, column=0, padx=10, pady=8)

    passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
    passwordEntry.grid(row=1, column=1, padx=10, pady=8)

    recipientFrame = LabelFrame(root1, text='Penerima', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
    recipientFrame.grid(row=1, column=0, padx=10, pady=8)

    recieverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='gray20', fg='white')
    recieverLabel.grid(row=0, column=0, padx=10, pady=8)

    recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
    recieverEntry.grid(row=0, column=1, padx=10, pady=8)

    messageLabel = Label(recipientFrame, text="Pesan", font=('arial', 14, 'bold'), bg='gray20', fg='white')
    messageLabel.grid(row=1, column=0, padx=10, pady=8)

    email_textarea = Text(recipientFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN, width=42, height=11,
                          wrap=WORD)
    email_textarea.grid(row=2, column=0, columnspan=2)
    email_textarea.delete(1.0, END)
    email_textarea.insert(END, textarea.get(1.0, END).replace('=', '').replace('-', '').replace('\t\t\t', '\t\t'))

    sendButton = Button(root1, text='Kirim', font=('arial', 14, 'bold'), width=15, command=send_gmail)
    sendButton.grid(row=3, column=0, pady=20)

    root1.mainloop()


def print_bill():
    if textarea.get(1.0,END)=='/n':
        messagebox.showerror('Error', 'Bill is empty')
        
    else:
        file=tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')


if not os.path.exists('bills'):
      os.mkdir('bills')

def save_bill():
      global billnumber
      result=messagebox.askyesno('Konfirmasi','Apakah kamu mau menyimpan struk ini?')
      if result:
            bill_content=textarea.get(1.0,END)
            file=open(f'bills/ {billnumber}.txt','w')
            file.write(bill_content)
            file.close()
            messagebox.showinfo('Berhasil',f'Nomor struk{billnumber} berhasil disimpan')
            billnumber = random.randint(500,1000)

billnumber=random.randint(500,1000)

def bill_area(): #menampilkan pesan kesalahan menggunakan modul messagebox.
    if nameEntry.get()=='' or phoneEntry.get()=='': 
         messagebox.showerror('Error','Struk customer gagal ditampilkan')
    elif hargarumahEntry.get()=='' or hargakamarEntry.get()=='' or hargadapurEntry.get()=='': 
         messagebox.showerror('Error','Pilih produk untuk menampilkan struk')
    elif hargarumahEntry.get()=='Rp.0' or hargakamarEntry.get()=='Rp.0' or hargadapurEntry.get()=='Rp.0': 
         messagebox.showerror('Error','Pilih produk untuk menampilkan struk')
    else:
        textarea.delete(1.0,END)

        #teks yang ditampilkan struk dari data yang telah diinput
        textarea.insert(END,'\t** Terima Kasih sudah berbelanja **\n')
        textarea.insert(END,f'\nNo Struk: {billnumber}\n')
        textarea.insert(END,f'\nNama Customer: {nameEntry.get()}\n')
        textarea.insert(END,f'\nNo.HP Customer: {phoneEntry.get()}\n')
        textarea.insert(END,'\n==================================================')
        textarea.insert(END,'Produk\t\tJumlah produk\t\t\tHarga')
        textarea.insert(END,'\n==================================================')

        #struk perhitungan harga kebutuhan rumah
        if sofaEntry.get()!='0':
              textarea.insert(END,f'\nSofa\t\t\t{sofaEntry.get()}\t\tRp.{hargasofa}')
        if mejatamuEntry.get()!='0':
              textarea.insert(END,f'\nMeja Tamu\t\t\t{mejatamuEntry.get()}\t\tRp.{hargamejatamu}')
        if mejatvEntry.get()!='0':
              textarea.insert(END,f'\nMeja TV\t\t\t{mejatvEntry.get()}\t\tRp.{hargamejatv}')
        if lemaribuffetEntry.get()!='0':
              textarea.insert(END,f'\nLemari Buffet\t\t\t{lemaribuffetEntry.get()}\t\tRp.{hargalemaribuffet}')
        if mejamakanEntry.get()!='0':
              textarea.insert(END,f'\nMeja Makan\t\t\t{mejamakanEntry.get()}\t\tRp.{hargamejamakan}')
        if kursiEntry.get()!='0':
              textarea.insert(END,f'\nKursi Berpelapis\t\t\t{kursiEntry.get()}\t\tRp.{hargakursiberpelapis}')

        #struk perhitungan harga kebutuhan kamar mandi & kamar tidur
        if kasurEntry.get()!='0':
              textarea.insert(END,f'\nKasur\t\t\t{kasurEntry.get()}\t\tRp.{hargakasur}')
        if lemaripakaianEntry.get()!='0':
              textarea.insert(END,f'\nLemari Pakaian\t\t\t{lemaripakaianEntry.get()}\t\tRp.{hargalemaripakaian}')
        if mejariasEntry.get()!='0':
              textarea.insert(END,f'\nMeja Rias\t\t\t{mejariasEntry.get()}\t\tRp.{hargamejarias}')
        if setkmEntry.get()!='0':
              textarea.insert(END,f'\nSet Perabotan KM\t\t\t{setkmEntry.get()}\t\tRp.{hargasetkm}')
        if wcEntry.get()!='0':
              textarea.insert(END,f'\nWC\t\t\t{wcEntry.get()}\t\tRp.{hargawc}')
        if wastafelEntry.get()!='0':
              textarea.insert(END,f'\nWastafel\t\t\t{wastafelEntry.get()}\t\tRp.{hargawastafel}')

        #struk perhitungan harga kebutuhan dapur
        if kulkasEntry.get()!='0':
              textarea.insert(END,f'\nKulkas\t\t\t{kulkasEntry.get()}\t\tRp.{hargakulkas}')
        if komporEntry.get()!='0':
              textarea.insert(END,f'\nKompor\t\t\t{komporEntry.get()}\t\tRp.{hargakompor}')
        if setmasakEntry.get()!='0':
              textarea.insert(END,f'\nSet Peralatan Masak\t\t\t{setmasakEntry.get()}\t\tRp.{hargasetmasak}')
        if wastafeldprEntry.get()!='0':
              textarea.insert(END,f'\nWastafel Dapur\t\t\t{wastafeldprEntry.get()}\t\tRp.{hargawastafeldpr}')
        if kabinetEntry.get()!='0':
              textarea.insert(END,f'\nKabinet Dapur\t\t\t{kabinetEntry.get()}\t\tRp.{hargakabinet}')
        if setmakanEntry.get()!='0':
              textarea.insert(END,f'\nSet Peralatan Makan\t\t\t{setmakanEntry.get()}\t\tRp.{hargasetmakan}')
        textarea.insert(END,'\n--------------------------------------------------')

        #tax 
        if taxrumahEntry.get()!='Rp.0.0':
              textarea.insert(END,f'\nTax Kebutuhan Rumah\t\t\t\t{taxrumahEntry.get()}')
        if taxkamarEntry.get()!='Rp.0.0':
              textarea.insert(END,f'\nTax Kebutuhan Kamar\t\t\t\t{taxkamarEntry.get()}')
        if taxdapurEntry.get()!='Rp.0.0':
              textarea.insert(END,f'\nTax Kebutuhan Dapur\t\t\t\t{taxdapurEntry.get()}')
        textarea.insert(END,f'\n\nTotal Pembayaran \t\t\t\tRp.{totalbill}')
        textarea.insert(END,'\n--------------------------------------------------')
        save_bill()
#fungsi 
def total():
    global hargasofa,hargamejatamu,hargamejatv,hargalemaribuffet,hargamejamakan,hargakursiberpelapis
    global hargakasur,hargalemaripakaian,hargamejarias,hargasetkm,hargawc,hargawastafel
    global hargakulkas,hargakompor,hargasetmasak,hargawastafeldpr,hargakabinet,hargasetmakan
    global totalbill

    #perhitungan harga kebutuhan rumah
    hargasofa=int (sofaEntry.get()) * 4000000
    hargamejatamu=int (mejatamuEntry.get()) * 1500000
    hargamejatv=int (mejatvEntry.get()) * 500000
    hargalemaribuffet=int (lemaribuffetEntry.get()) * 2500000
    hargamejamakan=int (mejamakanEntry.get()) * 1000000
    hargakursiberpelapis=int (kursiEntry.get()) * 200000

    totalhargarumah=hargasofa+hargamejatamu+hargamejatv+hargalemaribuffet+hargamejamakan+hargakursiberpelapis
    hargarumahEntry.delete(0,END)
    hargarumahEntry.insert(0, 'Rp' + str(totalhargarumah))
    rumahtax = totalhargarumah * 0.1
    taxrumahEntry.delete(0,END)
    taxrumahEntry.insert(0, 'Rp' + str(rumahtax))


    #perhitungan harga kebutuhan kamar mandi & kamar tidur
    hargakasur=int (kasurEntry.get()) * 800000
    hargalemaripakaian=int (lemaripakaianEntry.get()) * 1000000
    hargamejarias=int (mejariasEntry.get()) * 600000
    hargasetkm=int (setkmEntry.get()) * 400000
    hargawc=int (wcEntry.get()) * 200000
    hargawastafel=int (wastafelEntry.get()) * 700000

    totalhargakamar=hargakasur+hargalemaripakaian+hargamejarias+hargasetkm+hargawc+hargawastafel
    hargakamarEntry.delete(0,END)
    hargakamarEntry.insert(0,'Rp' + str(totalhargakamar))
    kamartax = totalhargakamar * 0.1
    taxkamarEntry.delete(0,END)
    taxkamarEntry.insert(0,'Rp' + str(kamartax))


    #perhitungan harga kebutuhan dapur
    hargakulkas=int (kulkasEntry.get()) * 2800000
    hargakompor=int (komporEntry.get()) * 900000
    hargasetmasak=int (setmasakEntry.get()) * 800000
    hargawastafeldpr=int (wastafeldprEntry.get()) * 500000
    hargakabinet=int (kabinetEntry.get()) * 1200000
    hargasetmakan=int (setmakanEntry.get()) * 750000

    totalhargadapur=hargakulkas+hargakompor+hargasetmasak+hargawastafeldpr+hargakabinet+hargasetmakan
    hargadapurEntry.delete(0,END)
    hargadapurEntry.insert(0,'Rp' + str(totalhargadapur))
    dapurtax = totalhargadapur * 0.1
    taxdapurEntry.delete(0,END)
    taxdapurEntry.insert(0,'Rp' + str(dapurtax))

    #totalbill
    totalbill=totalhargarumah+totalhargakamar+totalhargadapur+rumahtax+kamartax+dapurtax


#GUI
root=Tk()
root.title("Creative Interiors")
root.geometry('1152x864')
headingLabel=Label(root,text='Creative Interiors',font=('times new roman',30,'bold')
                  ,bg='NavajoWhite3',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text="Detail Pembelian",font=('times new roman',15,'bold')
                                 ,bg='NavajoWhite3',bd=8,relief=GROOVE)
customer_details_frame.pack(fill=X,pady=10)

nameLabel=Label(customer_details_frame,text='Nama',font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='No HP',font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

NoBayarLabel=Label(customer_details_frame,text='No Pembayaran',font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
NoBayarLabel.grid(row=0,column=4,padx=20,pady=2)
NoBayarEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
NoBayarEntry.grid(row=0,column=5,padx=8)

#products frame
productsFrame=Frame(root)
productsFrame.pack(pady=10)

#kebutuhan rumah
rumahFrame=LabelFrame(productsFrame,text="Kebutuhan Rumah",font=('times new roman',15,'bold')
                        ,bg='NavajoWhite3',bd=8,relief=GROOVE)
rumahFrame.grid(row=0,column=0)

sofaLabel=Label(rumahFrame,text="Sofa",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
sofaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

sofaEntry=Entry(rumahFrame, font=('times new roman',15,'bold'),width=10,bd=5)
sofaEntry.grid(row=0,column=1,pady=9,padx=10)
sofaEntry.insert(0,0)

mejatamuLabel=Label(rumahFrame,text="Meja Tamu",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
mejatamuLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

mejatamuEntry=Entry(rumahFrame, font=('times new roman',15,'bold'),width=10,bd=5)
mejatamuEntry.grid(row=1,column=1,pady=9,padx=10)
mejatamuEntry.insert(0,0)

mejatvLabel=Label(rumahFrame,text="Meja TV",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
mejatvLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

mejatvEntry=Entry(rumahFrame, font=('times new roman',15,'bold'),width=10,bd=5)
mejatvEntry.grid(row=2,column=1,pady=9,padx=10)
mejatvEntry.insert(0,0)

lemaribuffetLabel=Label(rumahFrame,text="Lemari Buffet",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
lemaribuffetLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

lemaribuffetEntry=Entry(rumahFrame, font=('times new roman',15,'bold'),width=10,bd=5)
lemaribuffetEntry.grid(row=3,column=1,pady=9,padx=10)
lemaribuffetEntry.insert(0,0)

mejamakanLabel=Label(rumahFrame,text="Meja Makan",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
mejamakanLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

mejamakanEntry=Entry(rumahFrame, font=('times new roman',15,'bold'),width=10,bd=5)
mejamakanEntry.grid(row=4,column=1,pady=9,padx=10)
mejamakanEntry.insert(0,0)

kursiLabel=Label(rumahFrame,text="Kursi Berpelapis",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
kursiLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

kursiEntry=Entry(rumahFrame, font=('times new roman',15,'bold'),width=10,bd=5)
kursiEntry.grid(row=5,column=1,pady=9,padx=10)
kursiEntry.insert(0,0)

#kebutuhan kamar
kamarFrame=LabelFrame(productsFrame,text="Kebutuhan Kamar Tidur & Kamar Mandi",font=('times new roman',15,'bold')
                        ,bg='NavajoWhite3',bd=8,relief=GROOVE)
kamarFrame.grid(row=0,column=1)

kasurLabel=Label(kamarFrame,text="Kasur",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
kasurLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

kasurEntry=Entry(kamarFrame, font=('times new roman',15,'bold'),width=10,bd=5)
kasurEntry.grid(row=0,column=1,pady=9,padx=10)
kasurEntry.insert(0,0)

lemaripakaianLabel=Label(kamarFrame,text="Lemari Pakaian",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
lemaripakaianLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

lemaripakaianEntry=Entry(kamarFrame, font=('times new roman',15,'bold'),width=10,bd=5)
lemaripakaianEntry.grid(row=1,column=1,pady=9,padx=10)
lemaripakaianEntry.insert(0,0)

mejariasLabel=Label(kamarFrame,text="Meja Rias",font=('times new roman',15,'bold'),bg='NavajoWhite3',
            fg='white')
mejariasLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

mejariasEntry=Entry(kamarFrame, font=('times new roman',15,'bold'),width=10,bd=5)
mejariasEntry.grid(row=2,column=1,pady=9,padx=10)
mejariasEntry.insert(0,0)

setkmLabel=Label(kamarFrame,text="Set Perabotan Kamar Mandi",font=('times new roman',15,'bold'),bg='NavajoWhite3',
            fg='white')
setkmLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

setkmEntry=Entry(kamarFrame, font=('times new roman',15,'bold'),width=10,bd=5)
setkmEntry.grid(row=3,column=1,pady=9,padx=10)
setkmEntry.insert(0,0)

wcLabel=Label(kamarFrame,text="WC",font=('times new roman',15,'bold'),bg='NavajoWhite3',
            fg='white')
wcLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

wcEntry=Entry(kamarFrame, font=('times new roman',15,'bold'),width=10,bd=5)
wcEntry.grid(row=4,column=1,pady=9,padx=10)
wcEntry.insert(0,0)

wastafelLabel=Label(kamarFrame,text="Wastafel",font=('times new roman',15,'bold'),bg='NavajoWhite3',
            fg='white')
wastafelLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

wastafelEntry=Entry(kamarFrame, font=('times new roman',15,'bold'),width=10,bd=5)
wastafelEntry.grid(row=5,column=1,pady=9,padx=10)
wastafelEntry.insert(0,0)

#kebutuhan dapur
dapurFrame=LabelFrame(productsFrame,text="Kebutuhan Dapur",font=('times new roman',15,'bold')
                        ,bg='NavajoWhite3',bd=8,relief=GROOVE)
dapurFrame.grid(row=0,column=2)

kulkasLabel=Label(dapurFrame,text="Kulkas",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
kulkasLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

kulkasEntry=Entry(dapurFrame, font=('times new roman',15,'bold'),width=10,bd=5)
kulkasEntry.grid(row=0,column=2,pady=9,padx=10)
kulkasEntry.insert(0,0)

komporLabel=Label(dapurFrame,text="Kompor Masak",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
komporLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

komporEntry=Entry(dapurFrame, font=('times new roman',15,'bold'),width=10,bd=5)
komporEntry.grid(row=1,column=2,pady=9,padx=10)
komporEntry.insert(0,0)

setmasakLabel=Label(dapurFrame,text="Set Peralatan Masak",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
setmasakLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

setmasakEntry=Entry(dapurFrame, font=('times new roman',15,'bold'),width=10,bd=5)
setmasakEntry.grid(row=2,column=2,pady=9,padx=10)
setmasakEntry.insert(0,0)

wastafeldprLabel=Label(dapurFrame,text="Wastafel Dapur",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
wastafeldprLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wastafeldprEntry=Entry(dapurFrame, font=('times new roman',15,'bold'),width=10,bd=5)
wastafeldprEntry.grid(row=3,column=2,pady=9,padx=10)
wastafeldprEntry.insert(0,0)

kabinetLabel=Label(dapurFrame,text="Kabinet Dapur",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
kabinetLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

kabinetEntry=Entry(dapurFrame, font=('times new roman',15,'bold'),width=10,bd=5)
kabinetEntry.grid(row=4,column=2,pady=9,padx=10)
kabinetEntry.insert(0,0)

setmakanLabel=Label(dapurFrame,text="Set Peralatan Makan",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
setmakanLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

setmakanEntry=Entry(dapurFrame, font=('times new roman',15,'bold'),width=10,bd=5)
setmakanEntry.grid(row=5,column=2,pady=9,padx=10)
setmakanEntry.insert(0,0)

#bill frame
billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe, text="Struk Belanja",font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=50,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

#Menu pembayaran
billmenuFrame=LabelFrame(root,text="Total Pembayaran",font=('times new roman',15,'bold')
                        ,bg='NavajoWhite3',bd=8,relief=GROOVE)
billmenuFrame.pack()

hargarumahLabel=Label(billmenuFrame,text="Kebutuhan Rumah",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
hargarumahLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
hargarumahEntry=Entry(billmenuFrame, font=('times new roman',15,'bold'),width=10,bd=5)
hargarumahEntry.grid(row=0,column=1,pady=9,padx=10)

hargakamarLabel=Label(billmenuFrame,text="Kebutuhan Kamar Tidur & Kamar Mandi",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
hargakamarLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
hargakamarEntry=Entry(billmenuFrame, font=('times new roman',15,'bold'),width=10,bd=5)
hargakamarEntry.grid(row=1,column=1,pady=9,padx=10)

hargadapurLabel=Label(billmenuFrame,text="Kebutuhan Dapur",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
hargadapurLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
hargadapurEntry=Entry(billmenuFrame, font=('times new roman',15,'bold'),width=10,bd=5)
hargadapurEntry.grid(row=2,column=1,pady=9,padx=10)

#tax frame
taxrumahLabel=Label(billmenuFrame,text="Tax Kebutuhan Rumah",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
taxrumahLabel.grid(row=0,column=2,pady=9,padx=10,sticky='w')
taxrumahEntry=Entry(billmenuFrame, font=('times new roman',15,'bold'),width=10,bd=5)
taxrumahEntry.grid(row=0,column=3,pady=9,padx=10)

taxkamarLabel=Label(billmenuFrame,text="Tax Kebutuhan Kamar",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
taxkamarLabel.grid(row=1,column=2,pady=9,padx=10,sticky='w')
taxkamarEntry=Entry(billmenuFrame, font=('times new roman',15,'bold'),width=10,bd=5)
taxkamarEntry.grid(row=1,column=3,pady=9,padx=10)

taxdapurLabel=Label(billmenuFrame,text="Tax Kebutuhan Dapur",font=('times new roman',15,'bold'),bg='NavajoWhite3',
               fg='white')
taxdapurLabel.grid(row=2,column=2,pady=9,padx=10,sticky='w')
taxdapurEntry=Entry(billmenuFrame, font=('times new roman',15,'bold'),width=10,bd=5)
taxdapurEntry.grid(row=2,column=3,pady=9,padx=10)

#button bill menu frame
buttonFrame=Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton=Button(buttonFrame, text='Total', font=('arial',16,'bold'),bg='NavajoWhite3',
               fg='white',bd=5,width=8,pady=20,padx=5,command=total)
totalButton.grid(row=0, column=0)


strukButton=Button(buttonFrame, text='Struk', font=('arial',16,'bold'),bg='NavajoWhite3',
               fg='white',bd=5,width=8,pady=20,padx=5,command=bill_area)
strukButton.grid(row=0, column=1)

emailButton=Button(buttonFrame, text='Kirim Email', font=('arial',16,'bold'),bg='NavajoWhite3',
               fg='white',bd=5,width=8,pady=20,padx=5, command=send_email)
emailButton.grid(row=0, column=2)

printButton=Button(buttonFrame, text='Print', font=('arial',16,'bold'),bg='NavajoWhite3',
               fg='white',bd=5,width=8,pady=20,padx=5, command=print_bill)
printButton.grid(row=0, column=3)

clearButton=Button(buttonFrame, text='Hapus', font=('arial',16,'bold'),bg='NavajoWhite3',
               fg='white',bd=5,width=8,pady=20,padx=5,command=clear)
clearButton.grid(row=0, column=4)


root.mainloop()


# In[ ]:





# In[ ]:




