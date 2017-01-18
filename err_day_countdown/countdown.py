#!/usr/bin/python

import Tkinter as tk
import time
from datetime import datetime, timedelta
'''
Count down to bed time,  then count down to wake up time
'''
class Countdown:
    def __init__(self):
        # create root/main window
        self.root = tk.Tk()
        self.time_str = tk.StringVar()
        label_font = ('helvetica', 20)
        tk.Label(self.root, textvariable=self.time_str, font=label_font, bg='white', 
                 fg='blue', relief='raised', bd=3).pack(fill='x', padx=5, pady=5)

    def get_next_countdown(self):
        now = datetime.now()
        sleep_time = datetime(now.year,now.month,now.day,23,00,0) # sleep at 11:00pm

        if now >= sleep_time:
            # up at 5:00am
            wakeup_time = datetime(now.year,now.month,now.day, 5, 0) + timedelta(days=1)
            time_left = wakeup_time - now
            self.event = 'Wake up in'
        else:
            time_left = sleep_time - now
            self.event = 'Sleep in'
            
        return time_left.seconds

    def count_down(self, seconds_left):
        (mins, sec) = divmod(seconds_left, 60)
        (hr, mins) = divmod(mins, 60)
        sf = self.event + " {:02d}:{:02d}:{:02d}".format(*(hr, mins, sec))
        self.time_str.set(sf)
        time.sleep(1)

    def draw(self):
        while True:
            seconds_left = self.get_next_countdown()
            self.count_down(seconds_left)
            self.root.update()

    def run(self):
        self.draw()
        self.root.mainloop()


c = Countdown()
c.run()



