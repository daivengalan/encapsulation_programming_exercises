import tkinter as tk
from tkinter import ttk
from fan_class import Fan

class FanPanel:
    SPEED_LABELS = {Fan.SLOW: "SLOW", Fan.MEDIUM: "MEDIUM", Fan.FAST: "FAST"}
    COLORS = ["blue", "red", "yellow", "green", "white", "orange"]

    def __init__(self, parent, title, fan):
        self.fan = fan
        self.frame = tk.LabelFrame(parent, text=title,
                                   font=("Arial", 11, "bold"),
                                   padx=12, pady=10)

        self.status_label = tk.Label(self.frame, text=self._status_text(),
                                     font=("Courier", 9), justify="left",
                                     bg="#f5f5f5", relief="sunken",
                                     width=28, anchor="w", padx=6, pady=4)
        self.status_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        self.power_btn = tk.Button(self.frame, text=self._power_text(),
                                   width=12, font=("Arial", 10, "bold"),
                                   command=self.toggle_power)
        self.power_btn.grid(row=1, column=0, columnspan=2, pady=(0, 10))
        self._update_power_btn()

        tk.Label(self.frame, text="Speed:", font=("Arial", 9)).grid(
            row=2, column=0, sticky="w")
        self.speed_var = tk.StringVar(value=self.SPEED_LABELS[fan.get_speed()])
        speed_menu = ttk.Combobox(self.frame, textvariable=self.speed_var,
                                  values=["SLOW", "MEDIUM", "FAST"],
                                  state="readonly", width=10)
        speed_menu.grid(row=2, column=1, pady=3)
        speed_menu.bind("<<ComboboxSelected>>", self.change_speed)

        tk.Label(self.frame, text="Radius:", font=("Arial", 9)).grid(
            row=3, column=0, sticky="w")
        self.radius_var = tk.DoubleVar(value=fan.get_radius())
        radius_spin = tk.Spinbox(self.frame, from_=1.0, to=50.0,
                                 increment=0.5, textvariable=self.radius_var,
                                 width=10, command=self.change_radius)
        radius_spin.grid(row=3, column=1, pady=3)

        tk.Label(self.frame, text="Color:", font=("Arial", 9)).grid(
            row=4, column=0, sticky="w")
        self.color_var = tk.StringVar(value=fan.get_color())
        color_menu = ttk.Combobox(self.frame, textvariable=self.color_var,
                                  values=self.COLORS,
                                  state="readonly", width=10)
        color_menu.grid(row=4, column=1, pady=3)
        color_menu.bind("<<ComboboxSelected>>", self.change_color)

    def _status_text(self):
        f = self.fan
        speed_str = self.SPEED_LABELS.get(f.get_speed(), "?")
        state_str = "ON" if f.get_is_on() else "OFF"
        return (f" Speed  : {speed_str}\n"
                f" Radius : {f.get_radius()} units\n"
                f" Color  : {f.get_color()}\n"
                f" Power  : {state_str}")

    def _power_text(self):
        return "Turn OFF" if self.fan.get_is_on() else "Turn ON"

    def _update_power_btn(self):
        if self.fan.get_is_on():
            self.power_btn.config(bg="#D71920", fg="white", text="Turn OFF")
        else:
            self.power_btn.config(bg="#cccccc", fg="#333333", text="Turn ON")

    def _refresh(self):
        self.status_label.config(text=self._status_text())

    def toggle_power(self):
        self.fan.set_is_on(not self.fan.get_is_on())
        self._update_power_btn()
        self._refresh()

    def change_speed(self, event=None):
        mapping = {"SLOW": Fan.SLOW, "MEDIUM": Fan.MEDIUM, "FAST": Fan.FAST}
        self.fan.set_speed(mapping[self.speed_var.get()])
        self._refresh()

    def change_radius(self):
        try:
            self.fan.set_radius(float(self.radius_var.get()))
            self._refresh()
        except ValueError:
            pass

    def change_color(self, event=None):
        self.fan.set_color(self.color_var.get())
        self._refresh()

class FanApp:
    def __init__(self, root):
        self.root = root
        root.title("Fan Utility Simulation")
        root.geometry("480x340")
        root.resizable(False, False)

        tk.Label(root, text="Fan Utility Simulation",
                 font=("Arial", 14, "bold")).pack(pady=(16, 10))

        panels_frame = tk.Frame(root)
        panels_frame.pack(padx=16, fill="both", expand=True)

        primary_fan = Fan(speed=Fan.FAST, radius=10.0, color="yellow", is_on=True)
        secondary_fan = Fan(speed=Fan.MEDIUM, radius=5.0, color="blue", is_on=False)

        self.panel1 = FanPanel(panels_frame, "Primary Fan", primary_fan)
        self.panel1.frame.pack(side="left", padx=(0, 8), fill="both", expand=True)

        self.panel2 = FanPanel(panels_frame, "Secondary Fan", secondary_fan)
        self.panel2.frame.pack(side="left", fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = FanApp(root)
    root.mainloop()
