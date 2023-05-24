from tkinter import*
import requests
root = Tk()
def get_weather():
    city = cityField.get()
    people = citField.get()
    #key = '113d64cb9832ad67ed377288b0e1e1ec'
    url = 'https://www.boredapi.com/api/activity'
    params = {'activity': 'key', 'type': city, 'participants': people, '4':'4', '5':'5','6':'6'}
    result = requests.get(url, params=params)
    weather = result.json()
    print(weather)
    info['text'] = f'{str(weather["activity"])}'
    #info['text'] = f'{str(weather["type"])}:{weather["activity"]}'
root['bg'] = '#1C434D'
root.title('do')
root.geometry('1000x800')
root.resizable(width=False, height=False)
frame_to = Frame(root, bg='#1C434D', bd=0)
frame_to.place(relx=0.5, rely=0.8, relwidth=0.5, relheight=0.5)
frame_top = Frame(root, bg='#1C434D', bd=0)
frame_top.place(relx=0.5, rely=0.8, relwidth=0.5, relheight=0.5)
frame_bottom = Frame(root, bg='#1C434D')
frame_tope = Frame(root, bg='#1C434D', bd=0)
frame_tope.place(relx=0., rely=0.8, relwidth=0.5, relheight=0.5)
frame_bottom.place(relx=0.0, rely=0.55, relwidth=1, relheight=0.2)
frame_val= Frame(root, bg='#1C434D')
frame_val.place(relx=0.0, rely=0.3, relwidth=0.5, relheight=0.15)
frame_vale= Frame(root, bg='#1C434D')
frame_vale.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.15)
#frame_bottom2 = Frame(root, bg='#1C434D', bd=0)
#frame_bottom2.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.5)
cityField = Entry(frame_top, bg='#1C434D', fg="white", font="gilroy 15 bold")
cityField.pack()
citField = Entry(frame_tope, bg='#1C434D', fg="white", font="gilroy 15 bold")
citField.pack()
infora=Label(frame_vale, text='Enter the type of activity you prefer\n\neducation,recreational,social,\ndiy,charity,cooking,\nrelaxation,music,busywork', bg='#1C434D', font="gilroy 15 bold",bd=0, fg="white")
infora.pack()
infor=Label(frame_val, text='Enter the participants', bg='#1C434D', font="gilroy 15 bold",bd=0, fg="white")
infor.pack()
info = Label(frame_bottom, text='do\n', bg='#1C434D', font="gilroy 15 bold",bd=0, fg="white")
info.pack()
Top=PhotoImage(file="im.png")
#Label(root, image=Top , bg ='#1C434D').pack
frame = Frame(root, bg='#1C434D', bd=0)
frame.place(relx =0.06, rely=0.02, relwidth=0.9, relheight=0.2)
title = Label(frame, image=Top, bg='#1C434D').pack(pady = (10,0))

button = PhotoImage(file="img.png",)
#Button = Button(root, image=button, bg = '#1C434D', bd = 0,activebackground='#1C434D', cursor="hand2",command=get_doing())
btn = Button(frame_bottom, image=button, bg = '#1C434D',bd = 0,activebackground='#1C434D', command=get_weather)
btn.pack()
#btn2 = Button(frame_top, text='Посмотреть погоghh', command=get_weather)
#btn.pack()

#info2 = Label(frame_bottom2, text='Погода в городе', bg='#1C434D', font=170)
#info2.pack()
root.mainloop()

