class TrapezoidalSFP:
    def __init__(self, a, b, c, d):
        assert self._well_formed_tsfp(a, b, c, d), \
            'Not well formed tsfp ({}, {}, {}, {})'.format(a, b, c, d)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_value(self, x):
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
