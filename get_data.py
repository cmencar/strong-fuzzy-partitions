def get_data(file):
    points = []
    with open(file, 'r') as dataset:
        data = dataset.readlines()
        for i in range(3, len(data)):
            point = []
            data[i] = data[i].split(",")
            tuple = (float(data[i][0]), float(data[i][1]))
            point.append(tuple)
            point.append(data[i][-1][:-1])
            points.append(point)
    return points
