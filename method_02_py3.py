import time
import ipdb

n_times = 10
n_items = 10000
my_dict = dict(zip(range(1, int(n_items/2)+1), range(1, int(n_items/2)+1)))
my_dict.update(dict(zip(range(int(n_items/2)+1, n_items+1), range(1, int(n_items/2)+1))))
# my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'd', 6: 'c'}
inv_dict = {}
durations = 0
for i in range(n_times):
    start_time = time.time()
    inv_dict = {}
    for k, v in my_dict.items():
        inv_dict[v] = inv_dict.get(v, [])
        inv_dict[v].append(k)
    duration = time.time() - start_time
    durations += duration
    print(duration)

print("Avg: {} seconds".format(durations/n_times))
ipdb.set_trace()
print(my_dict)
print(inv_dict)
