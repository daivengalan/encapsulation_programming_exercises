import tkinter as tk
from car_class import Car

class CarApp:
    def __init__(self, root):
        self.root = root
        self.car = Car(2026, "Mustang GT")
        self.accel_count = 0
        self.brake_count = 0

        root.title("Car Simulation")
        root.geometry("400x480")
        root.resizable(False, False)

        tk.Label(root, text="2026 Mustang GT",
                 font=("Arial", 16, "bold")).pack(pady=(20, 4))

        self.speed_label = tk.Label(root, text="Speed: 0 km/h",
                                    font=("Arial", 22, "bold"), fg="red")
        self.speed_label.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Accelerate", width=12, height=2,
                  bg="#D71920", fg="white", font=("Arial", 11, "bold"),
                  command=self.accelerate).pack(side="left", padx=8)

        tk.Button(btn_frame, text="Brake", width=12, height=2,
                  bg="#1a73e8", fg="white", font=("Arial", 11, "bold"),
                  command=self.brake).pack(side="left", padx=8)

        tk.Button(root, text="Reset", width=10,
                  command=self.reset).pack(pady=4)

        tk.Label(root, text="Event Log", font=("Arial", 10, "bold")).pack()
        self.log = tk.Text(root, height=12, width=44, state="disabled",
                           font=("Courier", 9), bg="#f5f5f5")
        self.log.pack(padx=16, pady=6)

        self._log("System ready.")

    def accelerate(self):
        self.car.accelerate()
        self.accel_count += 1
        spd = self.car.get_speed()
        self.speed_label.config(text=f"Speed: {spd} km/h")
        self._log(f"[ACCEL #{self.accel_count}]  Speed → {spd} km/h")

    def brake(self):
        self.car.brake()
        self.brake_count += 1
        spd = self.car.get_speed()
        self.speed_label.config(text=f"Speed: {spd} km/h")
        self._log(f"[BRAKE #{self.brake_count}]  Speed → {spd} km/h")

    def reset(self):
        self.car = Car(2026, "Mustang GT")
        self.accel_count = 0
        self.brake_count = 0
        self.speed_label.config(text="Speed: 0 km/h")
        self.log.config(state="normal")
        self.log.delete("1.0", "end")
        self.log.config(state="disabled")
        self._log("System reset.")

    def _log(self, message):
        self.log.config(state="normal")
        self.log.insert("end", message + "\n")
        self.log.see("end")
        self.log.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarApp(root)
    root.mainloop()