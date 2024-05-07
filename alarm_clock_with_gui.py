import time
from datetime import datetime, timedelta
from plyer import notification
import winsound
import tkinter as tk
from tkinter import ttk, messagebox

class AlarmClockApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Alarm Clock")
        self.geometry("300x200")

        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()
        self.repeat_var = tk.BooleanVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Hour (0-23):").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.hour_var, width=5).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Minute (0-59):").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self, textvariable=self.minute_var, width=5).grid(row=1, column=1, padx=10, pady=5)

        ttk.Checkbutton(self, text="Repeat", variable=self.repeat_var).grid(row=2, columnspan=2, padx=10, pady=5)

        tk.Button(self, text="Set Alarm", command=self.set_alarm).grid(row=3, columnspan=2, padx=10, pady=5)

    def set_alarm(self):
        try:
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            if not (0 <= hour < 24 and 0 <= minute < 60):
                raise ValueError("Invalid hour or minute")
            
            repeat = self.repeat_var.get()
            
            now = datetime.now()
            alarm_time = datetime(now.year, now.month, now.day, hour, minute)
            if alarm_time < now:
                alarm_time += timedelta(days=1)

            time_difference = alarm_time - now
            time.sleep(time_difference.total_seconds())

            notification.notify(
                title='Alarm',
                message='Wake up!',
                app_icon=None,
                timeout=10,
            )
            winsound.Beep(1000, 1000)

            if repeat:
                self.set_alarm()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid hour and minute.")

if __name__ == "__main__":
    app = AlarmClockApp()
    app.mainloop()
