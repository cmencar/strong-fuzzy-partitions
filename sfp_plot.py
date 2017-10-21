import matplotlib.pyplot as plt

A = 0
B = 1
C = 2
D = 3


def plot_trapeze_series(cuts, min_max, trap_series, depth):
    _check_input(cuts, min_max, trap_series, depth)
    _draw_axes(min_max, depth)
    _draw_cuts(cuts)

    for trap in trap_series:
        _draw_trapeze(trap, depth, '-r')

    plt.show()


def _check_input(cuts, min_max, trapeze_series, depth):
    assert isinstance(cuts, list), 'Cuts is not a list'
    assert len(min_max) == 2, 'min_max param accepts only 2 values'
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


def _draw_trapeze(trap, depth, color):
    plt.plot((trap[A], trap[B]), (0, -depth), color)
    plt.plot((trap[B], trap[C]), (-depth, -depth), color)
    plt.plot((trap[C], trap[D]), (-depth, 0), color)
