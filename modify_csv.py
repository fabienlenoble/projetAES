import sys
if(len(sys.argv) != 2):
    print('input a file name in the command line')
else:    
    with open(sys.argv[1], "rt") as fin:
        fin.readline()
        with open(sys.argv[1]+"replaced.csv", "wt") as fout:
            fout.write('medallion,hack_license,vendor_id,rate_code,store_and_fwd_flag,pickup_date,pickup_time,dropoff_date,dropoff_time,passenger_count,trip_time_in_secs,trip_distance,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude\n')
            for line in fin:
                fout.write(line.replace(' ', ','))