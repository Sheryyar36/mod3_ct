
curr_hr = int(input('Enter current hour:'))

alarm_hrs= int(input('Enter many hours would you like to set the alarm in:'))

alarm_hr_adj = (curr_hr + alarm_hrs) % 24


print('alarm set from {} to {}'.format(curr_hr, alarm_hr_adj))
