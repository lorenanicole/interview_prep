def timeConversion(s: str) -> str:
    timeComponents = s.split(':')
    amOrPm = timeComponents[-1]
    timeComponents[-1] = timeComponents[-1].strip(amOrPm)

    if 'AM' == amOrPm:
        return f'{timeComponents[0]}:{timeComponents[1]}:{timeComponents[2].strip("amOrPm")}'
    
    hourOfDay = int(timeComponents[0])
    hourOfDay += 12

    return f'{hourOfDay}:{timeComponents[1]}:{timeComponents[2].strip("amOrPm")}'

print(timeConversion('07:05:45PM') == '19:05:45')

