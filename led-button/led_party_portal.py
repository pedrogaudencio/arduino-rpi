from time import sleep
from arduino_gateway import Portal


def led_switch():
    ledState = False
    buttonState = gate.digitalRead(buttonPin)
    print("Our button state is: {}".format(buttonState))
    if buttonState:
        if ledState:
            gate.digitalWrite(ledPin, gate.LOW)
            ledState = False
            print("LED OFF")
            sleep(1)
        else:
            gate.digitalWrite(ledPin, gate.HIGH)
            ledState = True
            print("LED ON")
            sleep(1)


def button_fallback():
    gate.digitalWrite(ledPin, gate.LOW)


if __name__ == "__main__":
    portal = Portal()
    portal.open()
    gate = portal.gate

    ledPin = 7
    buttonPin = 8
    buttonState = 0

    gate.pinMode(ledPin, gate.OUTPUT)
    gate.pinMode(buttonPin, gate.INPUT)

    portal.loop(led_switch, button_fallback)
