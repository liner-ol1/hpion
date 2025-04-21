from ttime import times
hh = int(input("Введите кол-во часрв, которое хотите перевести:")
         print(hh, "часов =", times(hh), "секунд.")
         from ttime import minutes
mm = int(input("Введите кол-во минут, которое хотите перевести: ")
         print(mm, "минуту =", minutes(mm), "секунд.")

def times(hours):
         seconds = 3600*hours
         return seconds

def minutes(mins):
         seconds = 60*mins
         return seconds
