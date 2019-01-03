import sys

def generalize_coordinates(a, decimals, line_number, line):
    try :
        a = float(a)
        if abs(a)>180:
            a = 0
    except ValueError:
        print(line)
        print(line_number)
    return str(a)

def modify():
    if(len(sys.argv) != 2):
        print('input a file name in the command line')
    else:    
        with open(sys.argv[1], "rt") as fin:
            fin.readline()
            i=0
            with open(sys.argv[1]+"replaced.csv", "wt") as fout:
                fout.write('medallion,hack_license,vendor_id,rate_code,store_and_fwd_flag,pickup_date,pickup_time,dropoff_date,dropoff_time,passenger_count,trip_time_in_secs,trip_distance,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude\n')
                for line_number, line in enumerate(fin):
                    r_ = line.replace('\r', '').replace('\n', '').replace(', ', ',').split(',')
                    r = [""] *  len(r_)
                    boolean_break=False
                    for ix, a in enumerate(r_):
                        if i<6 :
                            r[ix] = a
                            print("premiere boucle")
                            i=i+1
                        else :
                            if(ix==0): # medallion
                                r[ix] = a
                            elif(ix==10): # pickup_longitude
                                r[ix] = generalize_coordinates(a, 3, line_number, line)
                                # r[ix] = a
                            elif(ix==11): # pickup_latitude
                                r[ix] = generalize_coordinates(a, 3, line_number, line)
                                # r[ix] = a
                            elif(ix==12): # dropoff_longitude
                                r[ix] = generalize_coordinates(a, 3, line_number, line)
                                # r[ix] = a
                            elif(ix==13): # dropoff_latitude
                                r[ix] = generalize_coordinates(a, 3, line_number, line)
                                # r[ix] = a
                            else:
                                r[ix]  =a
                    
                    if boolean_break==False :
                        tmp_line = ",".join(r)
                        fout.write(tmp_line.replace(' ', ','))
                        fout.write("\n")


modify()
exit(0)