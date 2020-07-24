package main

import (
	"fmt"

	"gobot.io/x/gobot"
	"gobot.io/x/gobot/drivers/gpio"
	"gobot.io/x/gobot/platforms/raspi"
)

func main() {
	raspberryPi := raspi.NewAdaptor()
	touchSensor := gpio.NewGroveTouchDriver(raspberryPi, "16")

	work := func() {
		touchSensor.On(gpio.ButtonPush, func(data interface{}) {
			fmt.Println("ボタンが押されています．")
		})
		touchSensor.On(gpio.ButtonPush, func(data interface{}) {
			fmt.Println("ボタンが開放されました．")
		})
	}

	robot := gobot.NewRobot("test",
		[]gobot.Connection{raspberryPi},
		[]gobot.Device{touchSensor},
		work)

	robot.Start()
}
