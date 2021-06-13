'''
You live 4 miles from university.
The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
How long will the bus journey take? Alternatively, you could run to university.
You jog the first mile at 7mph; then run the next two at 15mph; before jogging the last at 7mph again.
Will this be quicker or slower than the bus?
'''

distance = 4
total_time_bus = (4/25) * 0+(210)
print(f"Time taken by bus to Uni {total_time_bus} minutes")
total_time_jog = (4/(2 * (715) / (7+15))) * 60
print(f"Time taken to jogg to Uni {total_time_jog} minutes")
if (total_time_jog < total_time_bus):
    print(f"Therefore,its faster to jog to Uni")
else:
    print(f"Therefore,its faster to take a bus to Uni")