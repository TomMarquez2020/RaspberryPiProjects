from gpiozero import MotionSensor

pir = MotionSensor(4)

while True: 
    pir.wait_for_motion(2)
    if pir.motion_detected:
        print("moved")
    pir.wait_for_no_motion(2)

