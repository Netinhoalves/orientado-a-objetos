from enum import Enum


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


# diaPreferido = 'sabado'
# piorDia = 'qarta-feira'
# umDiaAleatorio='sábado'

diaPreferido = Weekday.SATURDAY

print(diaPreferido)
print(diaPreferido.name)
print(diaPreferido.value)

outroDia = Weekday(4)
print(outroDia)
