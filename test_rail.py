# test_so100b_real.py
from lerobot.common.robots.so100b_follower import SO100BFollowerConfig, SO100BFollower
from lerobot.common.motors.modbus_rtu import ModbusRTUMotorsBusConfig

cfg = SO100BFollowerConfig(
    id="desk_arm",
    port="/dev/tty.usbmodem58FD0172321",          # USB ACM device for the Feetech bus
    rail=ModbusRTUMotorsBusConfig(
        port="/dev/tty.usbserial-BG00Q7CQ",      # USB-RS485 adapter for the rail
        motors={"rail": (1, "NEMA17_MKS42D")},
    ),
)

robot = SO100BFollower(cfg)

try:
    print("Connecting…")
    robot.connect()        # assumes you already calibrated once
    print("Connected ✔")

    obs = robot.get_observation()
    print("Initial obs keys:", obs.keys())
    print("Rail position :", obs['rail.pos'])

    # --- tiny test motion ---
    small_move = {k: v for k, v in obs.items() if k.endswith(".pos")}
    small_move["wrist_roll.pos"] += 3        # 3 norm-units ≈ ~5 deg if DEGREES
    small_move["rail.pos"] = obs["rail.pos"] - 100000   # 10 steps forward

    print("Sending small action…")
    robot.send_action(small_move)
    print("Action sent ✔")

finally:
    robot.disconnect()
    print("Disconnected.")
