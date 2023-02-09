def on_button_pressed_a():
    while True:
        basic.show_icon(IconNames.GIRAFFE)
        if RingbitCar.ringbitcar_sonarbit(RingbitCar.Distance_Unit.DISTANCE_UNIT_CM) < 10:
            basic.show_icon(IconNames.GHOST)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    while True:
        RingbitCar.running_time(RingbitCar.Direction_run.FORWARD, 10)
        if RingbitCar.ringbitcar_sonarbit(RingbitCar.Distance_Unit.DISTANCE_UNIT_CM) < 10:
            basic.pause(10)
            RingbitCar.turnleft()
            basic.pause(10)
            RingbitCar.running_time(RingbitCar.Direction_run.FORWARD, 10)
        basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.B, on_button_pressed_b)

RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)