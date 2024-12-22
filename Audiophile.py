#Author: Arda Demir
#build Date: 22/12/2024

#Modules
from pytubefix import YouTube
from pytubefix import Playlist
import customtkinter
from customtkinter import CTkToplevel
from PIL import Image
from tkinter import filedialog
import os
import sys

#take relative resources paths
def resource_path(relative_path):
    try:
        base_path= sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#create root windows preferences
#default gray color: #2b2b2b
app = customtkinter.CTk()
iconPath = resource_path('icon.ico')
app.iconbitmap(iconPath)
app.geometry("500x500")
app.minsize(500, 500)
app.resizable(1,1)
app.title("Audiophile V1.0")

mode = "dark"
customtkinter.set_appearance_mode(mode)

#creates frames for each section
imageFrame = customtkinter.CTkFrame(master=app, corner_radius=0, border_width=0, fg_color="transparent")
linkFrame = customtkinter.CTkFrame(master=app, corner_radius=0, border_width=0, fg_color="transparent")
pathFrame = customtkinter.CTkFrame(master=app, corner_radius=0, border_width=0, fg_color="transparent")
ctrlFrame = customtkinter.CTkFrame(master=app, corner_radius=0, border_width=0, fg_color="transparent")
progressFrame = customtkinter.CTkFrame(master=app, corner_radius=0, border_width=0, fg_color="transparent")
StatusFrame = customtkinter.CTkFrame(master=app, corner_radius=0, border_width=0, fg_color="transparent")


#upload title icon
iconPathTitle = resource_path('icon_title.ico')
icon = customtkinter.CTkImage(dark_image=Image.open(iconPathTitle),
                                    size=(32, 32))

#title label
icon_label = customtkinter.CTkLabel(imageFrame,
                                    image=icon, 
                                    text="Audiophile",
                                    fg_color="transparent",
                                    text_color= "#ff8503",
                                    compound="left",
                                    padx = 10,
                                    font=customtkinter.CTkFont(family="Bauhaus 93", size=18))

icon_label.grid(row=0, column=0, padx=(75,5), pady=5, sticky="we")

#change appearance mode
def change_event():
    global mode
    if mode == "dark":
        customtkinter.set_appearance_mode("light")
        mode = "light"
        changeButton.configure(text="Dark")
    else:
        customtkinter.set_appearance_mode("dark")
        mode = "dark"
        changeButton.configure(text="Light")
        
#appearance change button
changeButton = customtkinter.CTkButton(imageFrame, 
                                    text="Light", 
                                    command=change_event, 
                                    border_color="#000000",
                                    fg_color="#ff8503",  
                                    hover_color="#FFBF00", 
                                    corner_radius=10,
                                    width=15, 
                                    height=15,
                                    font=customtkinter.CTkFont(family="garamond", size=10, weight="bold"))

changeButton.grid(row=0, column=1, padx=(5,5), pady=5, sticky="e")

#entry field for youtube video/playlist URL
linkEntry = customtkinter.CTkEntry(linkFrame, 
                                    width=480, 
                                    placeholder_text="Link of video or playlist...",
                                    text_color="#ff8503", 
                                    placeholder_text_color="dark gray",
                                    font=customtkinter.CTkFont(family="garamond", size=13, weight="bold"))

linkEntry.pack(fill="x", expand= 1, padx= (5,5), pady=(0,5))

#path entry for donwloaded files to store
pathEntry= customtkinter.CTkEntry(pathFrame, 
                                    width=480,  
                                    placeholder_text="Path... (leave blank for current one)", 
                                    text_color="#ff8503", 
                                    placeholder_text_color="#ff8503",
                                    font=customtkinter.CTkFont(family="garamond", size=13, weight="bold"))

pathEntry.insert(0,os. getcwd())
pathEntry.grid(row=1, column=0, padx=(5,0), pady=5, sticky="we")

#path selector function called by button
def path_event():
    path = filedialog.askdirectory()
    pathEntry.delete(0, customtkinter.END)
    pathEntry.insert(0, path)

#path selector button
pathButton = customtkinter.CTkButton(pathFrame, 
                                    text=" . . . ", 
                                    command=path_event, 
                                    border_color="#000000",
                                    fg_color="#ff8503",  
                                    hover_color="#FFBF00", 
                                    corner_radius=10,
                                    width=15, 
                                    height=15,
                                    font=customtkinter.CTkFont(family="garamond", size=10, weight="bold"))

pathButton.grid(row=1, column=1, padx=(5,5), pady=5, sticky="we")

def autocheck_event():
    if autoCheckCheckbox.get() == 1:
        autoCheckCheckbox.configure(text="autocheck", text_color="#ff8503")
    else:
        autoCheckCheckbox.configure(text="autocheck?", text_color="dark grey")

#autocheck checkbox
autoCheck_var = customtkinter.BooleanVar(value=False)
autoCheckCheckbox = customtkinter.CTkCheckBox(ctrlFrame,
                                             text="autocheck?",
                                             variable=autoCheck_var,
                                             command=autocheck_event,
                                             checkbox_width=20,
                                             checkbox_height=20,
                                             border_width=1,
                                             corner_radius=0,
                                             onvalue=True,
                                             offvalue=False,
                                             fg_color="#ff8503",
                                             hover_color="#FFBF00",
                                             text_color="dark grey",
                                             font=customtkinter.CTkFont(family="garamond", size=13, weight="bold"))

autoCheckCheckbox.grid(row=0, column=1, padx=(0,0), pady=5)

#playlist interval selection create selection boxes if switch turned on, hide them when turned off
def select_event():
    if switch_var.get() == "on":
        videoNumberStart.grid(row=0, column=3, padx=(0,0), pady=5)
        videoNumberEnd.grid(row=0, column=4, padx=(0,0), pady=5)
        selectSwitch.configure(text="interval ", text_color="#ff8503")
        
    else:
        videoNumberStart.grid_forget()
        videoNumberEnd.grid_forget()
        selectSwitch.configure(text="interval? ", text_color="dark grey")

switch_var = customtkinter.StringVar(value="off")
selectSwitch = customtkinter.CTkSwitch(ctrlFrame,
                                    text="interval? ",
                                    text_color="dark grey",
                                    command=select_event,
                                    variable=switch_var, onvalue="on", offvalue="off",
                                    width=1,
                                    progress_color="#ff8503",
                                    button_hover_color="#FFBF00",
                                    font=customtkinter.CTkFont(family="garamond", size=13, weight="bold"))

selectSwitch.grid(row=0, column=2, padx=(0,0), pady=5)

videoNumberStart = customtkinter.CTkEntry(ctrlFrame, 
                                    width=50, 
                                    placeholder_text="Start",
                                    text_color="#ff8503", 
                                    placeholder_text_color="#ff8503",
                                    font=customtkinter.CTkFont(family="garamond", size=13, weight="bold"))


videoNumberEnd = customtkinter.CTkEntry(ctrlFrame, 
                                    width=50, 
                                    placeholder_text="End",
                                    text_color="#ff8503", 
                                    placeholder_text_color="#ff8503",
                                    font=customtkinter.CTkFont(family="garamond", size=13, weight="bold"))


#file format
formatSwtch = customtkinter.CTkSegmentedButton(ctrlFrame, 
                                                values=["Mp3", "Mp4"], 
                                                selected_color="#ff8503", 
                                                selected_hover_color="#FFBF00",
                                                font=customtkinter.CTkFont(family="garamond", size=13, weight="bold"))

formatSwtch.set("Mp3") # default: MP3
formatSwtch.grid(row=0, column=5, padx=(25,5), pady=5)

# video download function called by its button (REDESIGN)
def download_event():
    fPath = pathEntry.get()
    Link = linkEntry.get()
    format = formatSwtch.get()
    auto_check = autoCheck_var.get()            # Get the state of the auto-check checkbox
    
    # Get list of existing files in the target directory with specific formats
    existing_files_mp4 = {file_name[:-4] for file_name in os.listdir(fPath) if file_name.endswith(".mp4")}
    existing_files_mp3 = {file_name[:-4] for file_name in os.listdir(fPath) if file_name.endswith(".mp3")}
    
    if Link[24:32] == "playlist":               #checks url for playlist keyword. If there is, program runs that part
        yt = Playlist(Link)
        if switch_var.get() == "off" or int(videoNumberStart.get()) == int(videoNumberEnd.get()):           #if pl interval switch if off program downloads all videos from pl
            start = 0
            end = len(yt.videos)
        else:                                   #if switch is on program downloads pnly interval
            if int(videoNumberStart.get()) <= 0 or int(videoNumberStart.get()) > len(yt.videos):
                start = 0
            else:
                start = int(videoNumberStart.get())-1
            if int(videoNumberEnd.get()) <= int(videoNumberStart.get()) or int(videoNumberEnd.get()) > len(yt.videos):
                end = len(yt.videos)
            else:
                end = int(videoNumberEnd.get())
        videocount = (end - start)
        value = 0.0
        progressbar.set(0)
        statusBox.configure(state="normal")
        statusBox.insert("end",f'\n--------------------------------------------------------------------------------------------------------------------\nDownloading From Playlist: {yt.title}')
        statusBox.yview("end")
        statusBox.update()
        
        for video in yt.videos[start:end]:          #for MP4 files
            title = video.title
            if auto_check:
                if format == "Mp4" and title in existing_files_mp4:  # Skip MP4 if already exists
                    statusBox.insert("end", f'\nSkipping: {title} (MP4 already exists)')
                    statusBox.yview("end")
                    statusBox.update()
                    videocount-=1
                    continue
                elif format == "Mp3" and title in existing_files_mp3:  # Skip MP3 if already exists
                    statusBox.insert("end", f'\nSkipping: {title} (MP3 already exists)')
                    statusBox.yview("end")
                    statusBox.update()
                    videocount-=1
                    continue

            if format == "Mp4":
                statusBox.insert("end",f'\nDownloading: {video.title}')
                statusBox.yview("end")
                statusBox.update()
                video = video.streams.get_highest_resolution()
                video.download(fPath)
                value += (100/videocount)/100
                progressbar.set(value)
            elif format == "Mp3":                   #for MP3 files
                statusBox.insert("end",f'\nDownloading: {video.title}')
                statusBox.yview("end")
                statusBox.update()
                audio = video.streams.get_audio_only()
                audio.download(fPath, mp3=True)
                value += (100/videocount)/100
                progressbar.set(value)

    else:                           #if link isn't include playlist keyword program assume its a single video
        yt = YouTube(Link)
        title = yt.title
        videocount = 1
        statusBox.configure(state="normal")
        statusBox.insert("end",f'\n--------------------------------------------------------------------------------------------------------------------\nDownloading: {yt.title}')
        statusBox.yview("end")
        statusBox.update()
        
        if auto_check:
            if format == "Mp4" and title in existing_files_mp4:  # Skip MP4 if already exists
                statusBox.insert("end", f'\nSkipping: {title} (MP4 already exists)')
                statusBox.yview("end")
                statusBox.update()
                videocount-=1
                return
            elif format == "Mp3" and title in existing_files_mp3:  # Skip MP3 if already exists
                statusBox.insert("end", f'\nSkipping: {title} (MP3 already exists)')
                statusBox.yview("end")
                statusBox.update()
                videocount-=1
                return

        if format == "Mp4":
            video = yt.streams.get_highest_resolution()
            video.download(fPath)
            progressbar.set(1)

        elif format == "Mp3":
            audio = yt.streams.get_audio_only()
            audio.download(fPath, mp3=True)
            progressbar.set(1)

    videocount = str(videocount)
    statusBox.insert("end", "\nDone!  | " + videocount +" file(s) downloaded to " + fPath)
    statusBox.yview("end")
    statusBox.update()
    statusBox.configure(state="disable")

#download button
downloadButton = customtkinter.CTkButton(ctrlFrame,
                                        text="Download",
                                        command=download_event,
                                        fg_color="#ff8503",
                                        border_color="#000000",
                                        hover_color="#FFBF00",
                                        width=30,
                                        font=customtkinter.CTkFont(family="garamond", size=13, weight="bold"))

downloadButton.grid(row=0, column=6, padx=(5,0), pady=5)


#a status box for show processes 
statusBox = customtkinter.CTkTextbox(StatusFrame,
                                       text_color="#ff8503",
                                       font=customtkinter.CTkFont(family="garamond", size=13, weight="bold")
                                       )
statusBox.configure(state="disabled")
statusBox.pack(fill="both", expand=1, padx=(5,5), pady=(0,10))

#a bar for process
progressbar = customtkinter.CTkProgressBar(progressFrame, orientation="horizontal",
                                           width=435,
                                           height= 5,
                                           mode="determinate",
                                           progress_color="#ff8503")
progressbar.set(0)
progressbar.grid(row=0, column=0, padx=(5,0), pady=5, sticky="we")

#cleans up status box
def clean_event():
    statusBox.configure(state="normal")
    statusBox.delete(0.0, customtkinter.END)
    statusBox.configure(state="disable")
    progressbar.set(0)

#clean button
cleanButton = customtkinter.CTkButton(progressFrame,
                                         text= "CLR",
                                         command=clean_event,
                                         fg_color="#ff8503",
                                         border_color="#000000",
                                         hover_color="#FFBF00",
                                         corner_radius=10,
                                         width=15, 
                                         height=15,
                                         font=customtkinter.CTkFont(family="garamond", size=10, weight="bold"))
cleanButton.grid(row=0, column=1, padx=(5,5), pady=5, sticky="we")

#-------------ABOUT WINDOW--------------
def aboutWindow(event=None):
    about = CTkToplevel(app)
    about.title("About")
    about.geometry("250x125")
    about.resizable(0,0)
    about.after(250, lambda: about.iconbitmap(iconPath))
    aboutLabel = customtkinter.CTkLabel(about,
                                    image=icon,  
                                    text="About Audiophile",
                                    fg_color="transparent",
                                    text_color= "#ff8503",
                                    compound="left",
                                    padx = 10,
                                    font=customtkinter.CTkFont(family="garamond", size=19, weight="bold"))
    
    aboutLabel.pack(fill="x", padx= (10,10), pady=(10,10))
    
    createdLabel = customtkinter.CTkLabel(about, 
                                    text="Designed by Arda Demir · 2024",
                                    fg_color="transparent",
                                    text_color= "#ff8503",
                                    compound="left",
                                    padx = 10,
                                    font=customtkinter.CTkFont(family="garamond", size=16, weight="bold"))
    createdLabel.pack(fill="x", padx= (10,10), pady=(10,10))

app.bind('<Control-F1>', aboutWindow)

#layout things
imageFrame.grid_columnconfigure(0, weight=1)
imageFrame.grid_columnconfigure(1, weight=0)
imageFrame.grid_rowconfigure(0, weight=1)

pathFrame.grid_columnconfigure(0, weight=1)
pathFrame.grid_columnconfigure(1, weight=0)
pathFrame.grid_rowconfigure(0, weight=1)

progressFrame.grid_columnconfigure(0, weight=1)
progressFrame.grid_columnconfigure(1, weight=0)
progressFrame.grid_rowconfigure(0, weight=1)

ctrlFrame.grid_columnconfigure(0, weight=1)
ctrlFrame.grid_columnconfigure(7, weight=1)

imageFrame.pack(fill="x", expand=0)
linkFrame.pack(fill="x",expand=0)
pathFrame.pack(fill="x",expand=0)
ctrlFrame.pack(fill="x", expand=0)
progressFrame.pack(fill="x", expand=0)
StatusFrame.pack(fill="both", expand=1)

app.mainloop()
