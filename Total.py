from timeit import default_timer as timer
elapsed_time = timer()
print(elapsed_time)

total = 0
for num in range(101):
    total = total + num
print(total)

print(elapsed_time)
