from tkinter import *
import time

def destroy():
    window.destroy()

# Comparing two text entries to see if user writes
def text_check(sec_check):
    window.update()
    first_check = text.get('1.0', END)

    if first_check == sec_check:
        return True
    else:
        return False

# Create countdown 5 seconds timer
def countdown(count):
    # change text in label
    seconds['text'] = f'Countdown: {count}\n'

    if count > 0:
        the_same = True
        sec_time = time.time()
        sec_check = text.get('1.0', END)
        window.after(500)
        # Check text after 0.5 sec
        if time.time() - sec_time >= 0.1:
            the_same = text_check(sec_check)
        if count > 0 and the_same:
            window.after(1000, countdown, count - 1)
        elif count > 0 and the_same == False:
            count = 5
            window.after(1000, countdown, count)
    elif count == 0:
        text.delete('1.0', END)
        countdown(5)


# Timer for 3 minutes
def countdown_minutes(count):
    minute = count//60
    minutes['text'] = f'Time left: {minute} minute(s) and {count%60} seconds'

    if count > 0:
        window.after(1000,countdown_minutes, count-1)

    # Save text from entry to a file and destroy all the labels
    else:
        with open('Your Text.txt', 'w') as data:
            data.write(text.get('1.0', END))

        text.destroy()
        labelend = Label(text='Succesfully saved to file')
        labelend.pack()
        seconds.destroy()
        description.destroy()
        minutes.destroy()
        button = Button(text='Exit', command = destroy)
        button.pack()




# Creating Tk window, labels and text editor
window = Tk()
window.config(padx = 5, pady= 15)
window.title('Text Disappearing Program')

description = Label(text ='Write your text. You\'ve got 3 minutes of writing then it will save to text file.'
                          '\n\n WARNING!! After 5 secs of not writing the whole text will disappear!!\n')
description.pack()

seconds = Label(window)
seconds.pack()

text = Text(window, height = 20, width = 50, padx= 10, pady=10)
text.pack()

minutes = Label(window)
minutes.pack()

countdown_minutes(180)
countdown(5)



window.mainloop()

