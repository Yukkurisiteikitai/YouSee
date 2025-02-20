from GITthread import main
import time

second = 0
minute = 5
hour = 0
t_lenght = 60 * minute + 3600 * hour + second
print(t_lenght)

while True:
    returnCode = main()
    if returnCode == 0:
        time.sleep(t_lenght)
    if returnCode == 1:
        time.sleep(t_lenght / 3)