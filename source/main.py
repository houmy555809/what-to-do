from tkinter import *
from datetime import *
import time
from sys import *
import os.path
copy=Tk()
cr=Label(copy,text="""几度秋V1.0.0.0 加载中
开发者：HMY
版权归开发者所有
Developer：HMY
All rights reserved.
github开源地址：www.github.com/houmy555809/what-to-do""")
cr.pack()
copy.overrideredirect(True)
width=500
height=130
copy.geometry("%dx%d+%d+%d"%(width,height,(copy.winfo_screenwidth()-width)/2,(copy.winfo_screenheight()-height)/2))
def front1():
    copy.attributes("-topmost",True)
    copy.after(10,front1)
copy.after(10,front1)
def start():
    copy.destroy()
    root=Tk()
    root.geometry("500x130-0-40")
    root.resizable(False,False)
    root.overrideredirect(True)
    root.attributes("-alpha",0.5)
    root.iconbitmap(os.path.join(os.getcwd(),"ico.ico"))
    schedule=[
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    warn_stv=StringVar(root,"")
    warn=Label(root,textvariable=warn_stv,font=("Consolas",15),fg="black")
    warn.pack()
    stv=StringVar(root,"")
    lbl=Label(root,textvariable=stv,font=("Consolas",30))
    lbl.pack()
    def front():
        root.attributes('-topmost',True)
        root.after(10,front)
    def is_after(a,b):
        if a[0]!=b[0]:
            return a[0]>b[0]
        if a[1]!=b[1]:
            return a[1]>b[1]
        if a[2]!=b[2]:
            return a[2]>b[2]
    def time_sub(a,b):
        ans=[0,0,0]
        ans[0]+=a[0]-b[0]
        if a[1]<b[1]:
            ans[0]-=1
            ans[1]+=60
        ans[1]+=a[1]-b[1]
        if a[2]<b[2]:
            ans[1]-=1
            ans[2]+=60
        ans[2]+=a[2]-b[2]
        return tuple(ans)
    def refresh():
        time=datetime.today()
        ctime=(time.hour,time.minute,time.second)
        flag=False
        for i in schedule[time.weekday()]:
            if not is_after(i[1],ctime) and is_after(i[2],ctime):
                timebefore=time_sub(i[2],ctime)
                str_tm="距离结束"
                if timebefore[0]>0:
                    str_tm+=str(timebefore[0])+"小时"
                if timebefore[1]>0:
                    str_tm+=str(timebefore[1])+"分钟"
                if timebefore[2]>0:
                    str_tm+=str(timebefore[2])+"秒"
                warn_stv.set(str_tm)
                if time.hour>=10:
                    timestr=str(time.hour)
                else:
                    timestr="0"+str(time.hour)
                timestr+=":"
                if time.minute>=10:
                    timestr+=str(time.minute)
                else:
                    timestr+="0"+str(time.minute)
                timestr+=":"
                if time.second>=10:
                    timestr+=str(time.second)
                else:
                    timestr+="0"+str(time.second)
                stv.set(timestr+"\n当前事项："+i[0])
        root.after(100,refresh)
    root.after(10,front)
    root.after(100,refresh)
    x,y=0,0
    def load():
        with open(os.path.join(os.getcwd(),"schedule.txt"),"r",encoding="UTF-8") as file:
            for s in file.readlines():
                try:
                    s=s.strip("\r\n")
                    s=s.split(" ")
                    trs={"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}
                    day=trs[s[0]]
                    name=s[1]
                    st=s[2].split(":")
                    en=s[3].split(":")
                    st[0],st[1],st[2]=int(st[0]),int(st[1]),int(st[2])
                    en[0],en[1],en[2]=int(en[0]),int(en[1]),int(en[2])
                    schedule[day].append([name,st,en])
                except:
                    pass
            file.close()
    def mouse_motion(event):
        global x,y
        offset_x,offset_y=event.x-x,event.y-y  
        new_x=root.winfo_x()+offset_x
        new_y=root.winfo_y()+offset_y
        new_geometry=f"+{new_x}+{new_y}"
        root.geometry(new_geometry)
    def mouse_press(event):
        global x,y
        count=time.time()
        x,y=event.x,event.y
    def close(event):
        root.destroy()
        exit(0)
    def settings(event):
        settings=Tk()
        settings.iconbitmap(os.path.join(os.getcwd(),"ico.ico"))
        settings.title("设置")
        settings.geometry("500x500")
        def save(event):
            with open(os.path.join(os.getcwd(),"schedule.txt"),"w",encoding="UTF-8") as file:
                file.truncate(0)
                file.write(text.get("1.0",END))
                file.close()
            load()
        save_btn=Label(settings,text="📥")
        save_btn.bind("<Button-1>",save)
        save_btn.place(x=480,y=5)
        save_btn["cursor"]="hand2"
        def msin_savebtn(event):
            save_btn["fg"]="white"
            save_btn["bg"]="lightgray"
        def msot_savebtn(event):
            save_btn["fg"]="black"
            save_btn["bg"]="white"
        save_btn.bind("<Enter>",msin_savebtn)
        save_btn.bind("<Leave>",msot_savebtn)
        text=Text(settings,width=490,height=470)
        with open("schedule.txt","r",encoding="UTF-8") as file:
            text.insert(INSERT,file.read())
            file.close()
        text.place(x=5,y=25)
    close_btn=Label(root,text=" X ")
    close_btn.bind("<Button-1>",close)
    close_btn.place(x=480,y=5)
    close_btn["cursor"]="hand2"
    def msin_closebtn(event):
        close_btn["fg"]="white"
        close_btn["bg"]="red"
    def msot_closebtn(event):
        close_btn["fg"]="black"
        close_btn["bg"]="white"
    close_btn.bind("<Enter>",msin_closebtn)
    close_btn.bind("<Leave>",msot_closebtn)
    setting_btn=Label(root,text="⚙")
    setting_btn.bind("<Button-1>",settings)
    setting_btn.place(x=460,y=5)
    setting_btn["cursor"]="hand2"
    def msin_settingbtn(event):
        setting_btn["fg"]="white"
        setting_btn["bg"]="lightgray"
    def msot_settingbtn(event):
        setting_btn["fg"]="black"
        setting_btn["bg"]="white"
    setting_btn.bind("<Enter>",msin_settingbtn)
    setting_btn.bind("<Leave>",msot_settingbtn)
    root.bind("<B1-Motion>",mouse_motion)
    root.bind("<Button-1>",mouse_press) 
    load()
    root.mainloop()
    exit(0)
copy.after(5000,start)
copy.mainloop()
