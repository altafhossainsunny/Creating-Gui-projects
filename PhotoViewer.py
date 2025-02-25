from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import os
print(os.getcwd())
root = Tk()
root.title("Image viewer")
root.geometry("400x600")
root.configure(background = 'black')
path = r"C:\Users\MD ALTAF HOSSAIN\OneDrive\Desktop\Python practise\kinter\Gallary.jpg" 
'''Sir please change the path according to your
image path'''
img = Image.open(path)
img = ImageTk.PhotoImage(img)
root.iconphoto(False,img)
Directory_label = Label(root,text ='Enter the directory where the images ar stored :',font=('times new roman',14),bg="black",fg="white")
Directory_label.pack(pady=(10,10))
Input_Directory = Entry(root,font=('verdana',10),bg='lightgray',width=47)
Input_Directory.pack(ipady=4,pady=(1,10))
img_array = []
current_index = 0
img_label = Label(root, bg="black") 
img_label.pack(pady=10)

def list_files():
    global img_array, current_index

    directory = Input_Directory.get().strip()
    if not os.path.exists(directory):
        messagebox.showerror("Error", "Invalid directory path!")
        return
    
    files = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    if not files:
        messagebox.showerror("Error", "No image files found in the directory!")
        return
    
    img_array = []
    for file in files:
        img_path = os.path.join(directory, file)
        img = Image.open(img_path).resize((400, 400)) 
        img_array.append(ImageTk.PhotoImage(img))
    
    current_index = 0  # Start from the first image
    show_image()
def show_image():
    if img_array:
        img_label.config(image=img_array[current_index])

def next_image():
    """ Show the next image """
    global current_index
    if img_array and current_index < len(img_array) - 1:
        current_index += 1
        show_image()

def prev_image():
    """ Show the previous image """
    global current_index
    if img_array and current_index > 0:
        current_index -= 1
        show_image()
list_button = Button(root, text='Load Images', font=('Italic', 10), bg='white', fg='black', width=20, height=2, command=list_files)
list_button.pack(pady=10)
prev_button = Button(root, text="<< Previous", font=('Italic', 10), bg='gray', fg='white', width=10, height=2, command=prev_image)
prev_button.pack(side=LEFT, padx=20, pady=10)
next_button = Button(root, text="Next >>", font=('Italic', 10), bg='gray', fg='white', width=10, height=2, command=next_image)
next_button.pack(side=RIGHT, padx=20, pady=10)
root.mainloop()