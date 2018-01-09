def calculate_accuracys(dataset):
    num_good_classification = 0
    num_classified = 0
    for point in dataset:
        if isinstance(point[-1], str):
            num_classified = num_classified + 1
            if point[-2] == point[-1]:
                num_good_classification = num_good_classification + 1
    if num_classified == 0:
        accuracy_perc = "nessuna classificazione"
    else:
        accuracy_perc = str(float(num_good_classification) / num_classified * 100) + '%'
    return accuracy_perc
