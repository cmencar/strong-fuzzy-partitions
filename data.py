class TrapSeries:
    def __init__(self, trap_list):
        self.trap_list = trap_list
        self.n = len(trap_list)
        self.it_flag = 0

    def add_trap(self, trap):
        assert isinstance(trap, TrapezoidalSFP)
        self.trap_list = self.trap_list + [trap]
        self.n += 1

    def vectorize(self):
        result = []
        first_trap = self.trap_list[0]
        result += [first_trap.a, first_trap.b, first_trap.c, first_trap.d]

        for i in range(1, len(self.trap_list) - 1):
            trap = self.trap_list[i]
            result += [trap.c, trap.d]

        last_trap = self.trap_list[-1]
        result += [last_trap.c, last_trap.d]
        return result

    def __iter__(self):
        return self

    def next(self):
        if self.it_flag == self.n:
            self.it_flag = 0
            raise StopIteration
        else:
            self.it_flag += 1
            return self.trap_list[self.it_flag - 1]


class TrapezoidalSFP:
    def __init__(self, a, b, c, d):
        assert self._well_formed_tsfp(a, b, c, d), \
            'Not well formed tsfp ({}, {}, {}, {})'.format(a, b, c, d)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_fuzzy_value(self, x):
        if self.a < x < self.b:
            return (x - self.a) / (self.b - self.a)
        elif self.b <= x <= self.c:
            return 1
        elif self.c < x < self.d:
            return (x - self.d) / (self.c - self.d)
        else:
            return 0

    @staticmethod
    def _well_formed_tsfp(a, b, c, d):
        return a <= b <= c <= d

    def __str__(self):
        return '({}, {}, {}, {})'.format(self.a, self.b, self.c, self.d)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

