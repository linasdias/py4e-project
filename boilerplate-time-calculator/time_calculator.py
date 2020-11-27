weekdays = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]

def get_days(th, day, form):
    nd = 0
    dayrt = ''

    while th >= 24: #24 hours
        th = th - 24
        nd = nd + 1

    if day == '': #AM/PM control
        nd = (nd + 1 if th >= 12 and form == 'PM' else nd)

        if nd == 1:
            dayrt = "(next day)"
        elif nd > 1:
            dayrt = f"{nd} days later"
        return th if th != 0 else 12, dayrt
    else:
        dayrt = ''
        indexofday = weekdays.index(day)

        nd = (nd + 1 if th >= 12 and form == 'PM' else nd)

        if (nd + indexofday) >= len(weekdays):
            temp = nd
            nd = nd % 7
            if indexofday == len(weekdays) - 1:
              dayrt = (weekdays[nd - 1] + ' (next day)' if temp == 1 else weekdays[nd - 1] + f" ({temp} days later)")
            else:  
              dayrt = (weekdays[nd] + ' (next day)' if temp == 1 else weekdays[nd] + f" ({temp} days later)")
        elif nd == 0:
            dayrt = day

        elif nd == 1:
            dayrt = (weekdays[nd + indexofday] + " next day")
        else:
             dayrt = (weekdays[nd + indexofday] + f" ({nd} days later)")
        return th if th != 0 else 12, dayrt


def add_time(start, duration, day=''):
    ini = start.split(" ")
    n = ini[0]
    form = ini[1]
    starttime = n.split(':')
    hours = starttime[0]
    mins = starttime[1]
    addedtime = duration.split(':')
    addedhrs = addedtime[0]
    addedmins = addedtime[1]
    th = int(hours) + int(addedhrs)
    tm = int(mins) + int(addedmins)
    returnedstr = ''

    # + hrs if total minutes exceed 60
    if (tm > 60):
        th += tm // 60
        tm %= 60

    th, returnedstr = get_days(int(th), day.lower(), form)

    # right AMPM form
    if form == 'AM':
        if th >= 12:
            form = 'PM'
    elif form == 'PM':
        if th >= 12:
            form = "AM"

    if th > 12:
        th = th - 12

    if tm < 10:
        tm = str(tm).rjust(2, '0')

    if returnedstr != '':
        print("{0}:{1} {2}, {3}".format(th, tm, form, returnedstr))
    else:
        print("{0}:{1}, {2}".format(th, tm, form, returnedstr))
