# calibrate_so100b.py
from lerobot.common.robots.so100b_follower import SO100BFollowerConfig, SO100BFollower
from lerobot.common.motors.modbus_rtu import ModbusRTUMotorsBusConfig

cfg = SO100BFollowerConfig(
    id="desk_arm",
    port="/dev/tty.usbmodem58FD0172321",
    rail=ModbusRTUMotorsBusConfig(
        port="/dev/tty.usbserial-BG00Q7CQ",
        motors={"rail": (1, "NEMA17_MKS42D")},
    ),
)

robot = SO100BFollower(cfg)
robot.connect(calibrate=False)   # ouvre les ports seulement
robot.calibrate()                # demande de placer le bras mid-range, etc.
robot.disconnect()
