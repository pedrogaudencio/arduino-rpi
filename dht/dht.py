from nanpy import DHT
from time import sleep

if __name__ == "__main__":
    while True:
        dhts = [
            DHT(6, DHT.DHT11),
            DHT(7, DHT.DHT11),
            DHT(8, DHT.DHT11)
        ]

        # for i, dht in enumerate(dhts):
        #     print("DHT %d" % i)
        #     print("Temperature is %.2f degrees Celcius" % dht.readTemperature(False))
        #     print("Temperature is %.2f degrees Fahrenheit" % dht.readTemperature(True))
        #     print("Humidity is %.2f %%" % dht.readHumidity())

        dht = dhts[1]
        t_celcius = dht.readTemperature()
        t_fahrenheit = dht.readTemperature(True)
        humidity = dht.readHumidity()
        print("Temperature is %.2f degrees Celcius" % t_celcius)
        print("Temperature is %.2f degrees Fahrenheit" % t_fahrenheit)
        print("Humidity is %.2f %%" % humidity)

        sleep(2)
