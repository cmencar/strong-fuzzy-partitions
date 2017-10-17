import matplotlib.pyplot as plt
from data import TrapezoidalSFP, TrapSeries


def plot_trapeze_series(cuts, min_max, trapeze_series, depth):
    _check_input(cuts, min_max, trapeze_series, depth)
    _draw_axes(min_max, depth)
    _draw_cuts(cuts)
    for trapeze in trapeze_series:
        _draw_trapeze(trapeze, depth, '-r')

    plt.show()


def _check_input(cuts, min_max, trapeze_series, depth):
    assert isinstance(cuts, list), 'Cuts is not a list'
    assert len(min_max) == 2, 'min_max param accepts only 2 values'
    assert isinstance(trapeze_series, TrapSeries), 'trapeze_series is not a TrapSeries obj'
    assert depth > 0, 'depth cant be less or equal than 0'


def _draw_axes(min_max, depth):
    min_x = min_max[0]
    max_x = min_max[1]
    min_y = -depth
    max_y = (max_x - min_x) / 3

    plt.axhline(y=0, color='k')
    plt.axis([min_x, max_x, min_y, max_y])


def _draw_cuts(cuts):
    for cut in cuts:
        plt.axvline(x=cut, linestyle='--')


def _draw_trapeze(trapeze, depth, color):
    assert isinstance(trapeze, TrapezoidalSFP)
    plt.plot((trapeze.a, trapeze.b), (0, -depth), color)
    plt.plot((trapeze.b, trapeze.c), (-depth, -depth), color)
    plt.plot((trapeze.c, trapeze.d), (-depth, 0), color)
