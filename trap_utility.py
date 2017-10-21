
def split_in_trap(trap_series):
    def loop(series, acc):
        if len(series) < 4:
            return acc
        else:
            acc.append(series[0:4])
            return loop(series[2:], acc)

    return loop(trap_series, [])