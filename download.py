from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
def location():
    global folder_name
    folder_name=filedialog.askdirectory()
def Download():
    choice=qualities.get()
    url=enter_url.get()    
    yt=YouTube(url)
    
    if(choice==quality[0]):
        select=yt.streams.filter(progressive=True).first()
    elif(choice==quality[1]):
        select=yt.streams.filter(progressive=True,file_extension='mp4').last()
    else:
        select=yt.streams.filter(only_audio=True).first()
    select.download(folder_name)            
src=Tk()
src.title('Youtube Downloader')
src.geometry("500x600")
label=Label(src,text='URL:',font=("Ariel",16))
label.grid()
enter_url_var=StringVar()
enter_url=Entry(src,width=60,textvariable=enter_url_var)
enter_url.grid()
select=Label(src,text="Select the path",font=("Ariel",15))
select.grid()
file_path=Button(src,width=15,bg="blue",fg="white",text="file path",command=location)
file_path.grid()
label2=Label(src,text="select the quality",font=("Ariel",15))
label2.grid()
quality=["best","worst","audio"]
qualities=ttk.Combobox(src,values=quality)
qualities.grid()

download_button=Button(src,text="download",width=17,font=("Ariel",16),fg="brown",bg="orange",command=Download)

download_button.grid()
src.mainloop()

