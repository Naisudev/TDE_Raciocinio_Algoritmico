userHour = int(input("Digite somente a hora: "))
userMin = int(input("Digite somente os minutos: "))
userSec = int(input("Digite somente os segundos: "))
minSec = userMin * 60
hourMin = userHour * 60
hourSec = hourMin * 60
daySec = userSec + minSec + hourSec
dayMin = hourMin + userMin
print("Os minutos transcorridos no dia de hoje foram:", dayMin)
print("Os segundos transcorridos no dia de hoje foram:" , daySec)