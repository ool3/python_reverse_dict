import time
import ipdb

n_times = 10
n_items = 10000
my_dict = dict(zip(range(1,n_items+1), range(1, n_items+1)))
# my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
inv_dict = {}
durations = 0
for i in range(n_times):
    start_time = time.time()
    inv_dict = {v: k for k, v in my_dict.items()}
    duration = time.time() - start_time
    durations += duration
    print(duration)

print("Avg: {} seconds".format(durations/n_times))
ipdb.set_trace()
print(my_dict)
print(inv_dict)
