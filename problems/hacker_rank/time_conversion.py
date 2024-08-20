def timeConversion(s: str) -> str:
    timeComponents = s.split(':')
    amOrPm = timeComponents[-1]

    if 'AM' in amOrPm:
        return f'{"00" if timeComponents[0] == "12" else timeComponents[0]}:{timeComponents[1]}:{timeComponents[2].strip("AM")}'
    
    hourOfDay = int(timeComponents[0])
    if hourOfDay < 12:
        hourOfDay += 12

    return f'{hourOfDay}:{timeComponents[1]}:{timeComponents[2].strip("PM")}'

print(timeConversion('07:05:45PM') == '19:05:45')
print(timeConversion('12:05:45AM') == '00:05:45')

