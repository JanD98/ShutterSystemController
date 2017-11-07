from time import gmtime, strftime

class Model:

    TEMP = 1
    LIGHT = 2
    STATUS = 3

    ROLLDOWN = 1
    ROLLUP = 0

    def __init__(self):
        self.historyledger = {}
        self.temp = ''
        self.light = ''
        self.status = ''
        self.max_setting_temp = 100
        self.max_setting_light = 100
        self.min_setting_temp = 0
        self.min_setting_light = 0

    def update_model(self, data):
        try:
            time = strftime("%H:%M:%S", gmtime())
            for lists in data:
                id = lists[0]
                value = lists[1]
                if int(id) == self.TEMP:
                    self.temp = value
                if int(id) == self.LIGHT:
                    self.light = value

            self.historyledger[time] = {Model.TEMP: self.temp, Model.LIGHT: self.light}
        except IOError:
            print("Invalid data from Arduino")


