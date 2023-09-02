#!/usr/bin/env python3

class Time(object):

    def set_time(time_object, hour, minute, second):
        time_object.hour = hour
        time_object.minute = minute
        time_object.second = second


    def show_time(time_object):
        print('This time is {:02d}:{:02d}:{:02d}'.format(time_object.hour, time_object.minute, time_object.second))


a = Time()
Time.set_time(a, 13, 43, 6)
Time.show_time(a)

b = Time()
Time.set_time(b, 21, 8, 36)
Time.show_time(b)

c = Time()
Time.set_time(c, 3, 4, 7)
Time.show_time(c)
