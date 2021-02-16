import tkinter 
import pytube


def download(url , res):
    try:
        yt = pytube.YouTube(url)
        video = yt.streams.get_by_resolution(resolution = res)
        print("Video download start..")
        video.download(output_path="../Video" , filename="myvideo")
        print("Video downloaded..")
    except:
        print("Please give input..")

def start():
    root = tkinter.Tk()
    root.title("Downloader")

    label  = tkinter.Label(root , text="YT Video downloader")
    label.pack(padx=20 , pady=10)
    urlInput = tkinter.Entry(root , width="30")
    urlInput.pack(padx=20 , pady=10)

    tkVar = tkinter.StringVar(root)

    choices = {"360p" , "720p"}
    tkVar.set('360p') #set as default

    popupMenu = tkinter.OptionMenu(root , tkVar , *choices)
    tkinter.Label(root , text="Choose resolution").pack()
    popupMenu.pack()

    submit = tkinter.Button(root , text="Submit" , command = lambda : download( urlInput.get() , tkVar.get()))
    submit.pack(padx=20 , pady=5)

    root.mainloop()


if __name__ == "__main__":
    start()