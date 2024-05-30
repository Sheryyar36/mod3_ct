
curr_hr = int(input('Enter current hour:'))
curr_min = int(input('Enter current minute:'))

curr_time = {curr_hr: curr_min}

alarm_hrs= int(input('Enter many hours would you like to set the alarm in:'))
alarm_mins= int(input('Enter many min would you like to set the alarm in:'))

alarm_hr_adj = (curr_hr + alarm_hrs + ((curr_min + alarm_mins)// 60)) % 24
alarm_min_adj = ((curr_min + alarm_mins) % 60)

alarm_time = {alarm_hr_adj: alarm_min_adj}
print('alarm set from {} to {}'.format(curr_time, alarm_time))
