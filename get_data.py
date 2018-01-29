def get_data(file):
    points = []
    with open(file, 'r') as dataset:
        data = dataset.readlines()
        for i in range(3, len(data)):  # first three rows in Orange are details about data
            point = []
            data[i] = data[i].split(",")
            data[i][-1] = data[i][-1].replace('\n', '')
            coords = (float(data[i][0]), float(data[i][1]))
            point.append(coords)
            point.append(data[i][-1])
            points.append(point)
    return points
