from datetime import datetime

import numpy

def helloworld():
    print('helloworld')

if __name__ == '__main__':
    helloworld()

    time = datetime.strptime('2022-01-02 16:30', '%Y-%m-%d %H:%M')
    print(time)
    week = time.weekday()
    hour = time.hour + time.minute / 60
    time = [week, hour]
    print(time)