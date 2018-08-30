import ipdb

from argument_names import argument_names as an


class Method:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.number_times = kwargs[an.number_times]
        self.number_items = kwargs[an.number_items]
        self.small_test = kwargs[an.small_test]
        self.precision = kwargs[an.precision]
        self.durations = 0
        self.my_dict = self.init_data()
        self.inv_dict = None

    def compute_avg_run_times(self):
        pass

    def init_data(self):
        if self.small_test:
            self.number_times = 1
            self.number_items = 1
            return {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
        else:
            return dict(zip(range(1, self.number_items + 1),
                            range(-self.number_items, 0)))

    def print_duration(self, count, duration):
        print('#{} Duration: {:.{}f}'.format(count, duration, self.precision))

    def print_avg_run_times(self):
        print('Avg: {:.{}f} seconds'.format((self.durations / self.number_items),
                                            self.precision))

