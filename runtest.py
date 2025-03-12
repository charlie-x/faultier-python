# Imports & setup faultier & serial
import faultier
import serial
ft = faultier.Faultier()
ser = serial.Serial(ft.get_serial_path(), baudrate=115200)
ser.timeout = 0.3
# Test function
ft.configure_glitcher(
    power_cycle_output = faultier.OUT_MUX0,
    power_cycle_length = 300000
)
ft.power_cycle()
print(ser.read(5))

# Actual glitcher
ft.configure_glitcher(
    trigger_source = faultier.TRIGGER_IN_EXT0,
    trigger_type = faultier.TRIGGER_PULSE_POSITIVE,
    glitch_output = faultier.OUT_CROWBAR
)
for d in range(0, 100000):
    for p in range(0, 10):
        if ser.in_waiting:
            ser.read(ser.in_waiting)
        ft.glitch(delay=d, pulse=p)
        data = ser.read(3)
        if b"X" in data:
            print(f"Success! Delay: {d} Pulse: {p}")
            print(ser.read(50))







