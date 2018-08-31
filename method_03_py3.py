import time
import ipdb


def reverse_mapping(f):
    return f.__class__(map(reversed, f.items()))


n_times = 10
n_items = 10000
my_dict = dict(zip(range(1, n_items+1), range(1, n_items+1)))
# my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
inv_dict = {}
durations = 0
for i in range(n_times):
    start_time = time.time()
    inv_dict = reverse_mapping(my_dict)
    duration = time.time() - start_time
    durations += duration
    print(duration)

print("Avg: {} seconds".format(durations/n_times))
ipdb.set_trace()
print(my_dict)
print(inv_dict)
