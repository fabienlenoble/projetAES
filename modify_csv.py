with open("tripData2013/trip_data_1/trip_data_1.csv", "rt") as fin:
    with open("tripData2013/trip_data_1/trip_data_1_replaced.csv", "wt") as fout:
        for line in fin:
            fout.write(line.replace(' ', ','))