input.onButtonPressed(Button.A, function () {
    while (true) {
        basic.showIcon(IconNames.Giraffe)
        if (RingbitCar.ringbitcar_sonarbit(RingbitCar.Distance_Unit.Distance_Unit_cm) < 10) {
            basic.showIcon(IconNames.Ghost)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    while (true) {
        RingbitCar.running_time(RingbitCar.Direction_run.forward, 10)
        if (RingbitCar.ringbitcar_sonarbit(RingbitCar.Distance_Unit.Distance_Unit_cm) < 10) {
            basic.pause(1000)
            RingbitCar.turnleft()
            basic.pause(1000)
            RingbitCar.running_time(RingbitCar.Direction_run.forward, 10)
        }
        basic.showIcon(IconNames.Heart)
    }
})
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)
