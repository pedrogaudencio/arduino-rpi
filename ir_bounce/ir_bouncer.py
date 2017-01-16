from time import sleep
from ..arduino_gateway import Portal


def read_ir():
    ir_value = gate.digitalRead(ir_receiver)
    print("ir_receiver: {}".format(ir_receiver))
    print("IR value: {}".format(ir_value))
    sleep(1)
    # if ir_value:
    #         gate.digitalWrite(ir_transmitter, gate.LOW)
    #         print("Sent value: {}".format(ir_value))
    #         sleep(2)


if __name__ == "__main__":
    portal = Portal()
    portal.open()
    gate = portal.gate

    ir_receiver = 6
    ir_transmitter = 11

    gate.pinMode(ir_receiver, gate.INPUT)
    gate.pinMode(ir_transmitter, gate.OUTPUT)

    portal.loop(read_ir)
