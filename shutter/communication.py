from serial import *
import time
import threading

class SerialCommunication:

    def __init__(self, port):
        self.port = port
        self.baud = 19200
        self.open_connection()
        self.data = []
        self.value = []

    def open_connection(self):
        print("making connection with " + self.port)
        try:
            self.ser = Serial(port=self.port, baudrate=self.baud)
            time.sleep(2)       # wait for the Arduino to connect
            self._connected = True
            read_thread = threading.Thread(target=self.read)
            read_thread.start()
        except SerialException as e:
            self._connected = False
            print(e.strerror)
        return self._connected

    def is_connected(self):
        return self._connected

    def read(self):
        while True:
            line = self.ser.readline().strip()   # add the id byte to the list     # add the value byte to the list
            data = line.decode().split('|')
            for values in data:
                self.value.append(values.split(':'))
            print(self.value)
            if callable(self.trigger):
                self.trigger(self.value)

    def write(self, status: int):
        # Make sure that 1 byte is going to the arduino
        self.ser.write(status.to_bytes(1, byteorder="little"))

    def set_listener(self, func):
        self.trigger = func


if __name__ == '__main__':
    sc = SerialCommunication('COM3')
    sc.read()
