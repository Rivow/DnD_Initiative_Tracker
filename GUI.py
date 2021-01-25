def pop_up(message):

    root = Tk()
    root.title('Initiative')
    w = 800  # popup window width
    h = 600  # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    m = Listbox(root)
    for e in message:
        m.insert(END, e[0].name)
    m.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=m.yview())

    # w = Label(root, text=m, width=120, height=10)
    # w.config(font=('Courier', 18))
    # w.pack(expand=True)
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack(side=BOTTOM)
    mainloop()
