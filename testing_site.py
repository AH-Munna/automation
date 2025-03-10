from time import sleep


tries = int(input("Enter number of tries: "))

k = 0
_sum = 0
print(f'trying to find ', end=': ')
while(k < tries):
    print(int((tries - k)/3), end=', ', flush=True)
    sleep(0.3)
    _sum += int((tries - k)/3)
    print("sum: ", _sum, end=', ', flush=True)
    k = k + 1