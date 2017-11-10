import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from series_utilities import split_in_trap


def trap_plot_2d(trap_series, cuts, min_max):
    gs = gridspec.GridSpec(3, 4)
    ax_cuts = plt.subplot(gs[0:-1, 1:])
    ax_trapx = plt.subplot(gs[-1, 1:])
    ax_trapy = plt.subplot(gs[:-1, 0])

    draw_cuts(ax_cuts, cuts, min_max)
    draw_trap_series_x(ax_trapx, trap_series[0], min_max[0])
    draw_trap_series_y(ax_trapy, trap_series[1], min_max[1])

    plt.show()


def trap_plot(trap_series, cuts):
    MIN = min([cuts[0][0], cuts[1][0]])
    MAX = max(cuts[0][-1], cuts[0][-1])

    plt.close('all')

    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
    draw_trap_series_y(ax1, trap_series, [MIN, MAX])
    draw_cuts(ax2, cuts, [MIN, MAX])
    draw_trap_series_x(ax4, trap_series, [MIN, MAX])

    plt.show()


def draw_cuts(ax, cuts, min_max):
    MIN_X = min_max[0][0]
    MAX_X = min_max[0][1]
    MIN_Y = min_max[1][0]
    MAX_Y = min_max[1][1]

    [ax.plot([cut, cut], [MIN_Y, MAX_Y], '--r') for cut in cuts[0]]
    [ax.plot([MIN_X, MAX_X], [cut, cut], '--b') for cut in cuts[1]]


def draw_trap_series_x(ax, trap_series, min_max):
    def draw_trap_x(ax, trap, min_max):
        A = 0
        B = 1
        C = 2
        D = 3
        MIN = min_max[0]
        MAX = min_max[1]

        ax.plot([trap[A], trap[B]], [MAX, MIN], '-r')
        ax.plot([trap[B], trap[C]], [MIN, MIN], '-r')
        ax.plot([trap[C], trap[D]], [MIN, MAX], '-r')

    # Real (simple) implementation
    [draw_trap_x(ax, trap, min_max) for trap in split_in_trap(trap_series)]


def draw_trap_series_y(ax, trap_series, min_max):
    def draw_trap_y(ax, trap, min_max):
        A = 0
        B = 1
        C = 2
        D = 3
        MIN = min_max[0]
        MAX = min_max[1]

        ax.plot([MIN, MAX], [trap[A], trap[B]], '-b')
        ax.plot([MAX, MAX], [trap[B], trap[C]], '-b')
        ax.plot([MAX, MIN], [trap[C], trap[D]], '-b')

    # Real (simple) implelentation
    [draw_trap_y(ax, trap, min_max) for trap in split_in_trap(trap_series)]

