import tkinter
import speedtest

def speed_test():
    Ld.config(text="00")
    Lu.config(text="00")
    sp.update()
    sP= speedtest.Speedtest()
    sP.get_servers()
    down=str(round(sP.download()/(10**6),2))+" Mbps"
    up=str(round(sP.upload()/(10**6),2))+" Mbps"
    Ld.config(text=down)
    Lu.config(text=up)

sp=tkinter.Tk()
sp.title("Internet Speed Test")
sp.geometry("500x600")
sp.config(bg="lightblue")
L_title=tkinter.Label(sp,text="Internet Speed Test",font=("Time new Roman",25,"bold"),height=2 ,width=20,border=5,relief="solid")
L_title.pack(pady=30)

L1=tkinter.Label(sp,text="Downloading Speed",font=("Time new Roman",21,"bold"),bg="lightblue")
L1.pack(pady=25)

Ld=tkinter.Label(sp,text="00",font=("Time new Roman",25,"bold"),bg="lightblue",border=4,relief="ridge")
Ld.pack(pady=17)

L2=tkinter.Label(sp,text="Upload Speed",font=("Time new Roman",21,"bold"),bg="lightblue",border=2)
L2.pack(pady=25)

Lu=tkinter.Label(sp,text="00",font=("Time new Roman",25,"bold"),bg="lightblue",border=4,relief="ridge")
Lu.pack(pady=17)

button=tkinter.Button(sp,text="Click here",font=("Time new Roman",14,"bold"),border=3,relief="solid",height=1,command=speed_test)
button.pack(pady=18)

sp.mainloop()