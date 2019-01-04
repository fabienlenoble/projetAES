# coding=utf-8
import sys
import re
import numpy
import pickle
import os
import random
import hashlib
import time
from datetime import datetime, timedelta

"""
fonction de generalisation
"""

# generalise a la semaine
def generalize_date(a):
    date=a.split("-")
    
    if(int(date[2])!=28):
        date[2]=int(date[2])-int(date[2])%7+1
        date[2]='{0:02}'.format(date[2])
        date[2]=str(date[2])
    a="-".join(date)
    return a

# generalise a l'heure
def generalize_hours(a):
    hours=a.split(":")
    a=":".join([hours[0],"00:00"])
    return a

# generalise à la minute
def generalize_trip_time(a):
    a=str(int(a)-int(a)%60)
    return a

# generalise les coordonnées gps
def generalize_coordinates(a, decimals, line_number, line):
    try :
        # a = float(a)
        # if a>400:
        #     a = a - 400
        a = str(round(float(a), decimals))
    except ValueError:
        print(line)
        print(line_number)
    return a
"""
fonction de bruit
"""

def differential_privacy_date(a, noise_range):
    date=a.split("-")
    date_formated=datetime(int(date[0]), int(date[1]), int(date[2]))
    noise=random.randint(-noise_range,noise_range)
    new_date_formated = date_formated + timedelta(days=noise)  
    a=str(new_date_formated.year)+'-'+str('{0:02}'.format(new_date_formated.month))+'-'+str('{0:02}'.format(new_date_formated.day))
    return a 


def generalize() :
    if(len(sys.argv) != 3):
        print('input an input file name and an outpute file name in the command line')
    else:
        infile =  sys.argv[1]
        print ("Input file name: %s" % infile)
        outfile = sys.argv[2]
        print ("Output file name: %s" % outfile)

        out = open(outfile,'w')
        i=0
        fp = open(infile, "r")
        out.write(fp.readline())
        for line_number, line in enumerate(fp):
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
                    elif(ix==1): # hack_license
                        r[ix] = a
                    elif(ix==2): # vendor_id
                        r[ix] = a
                    elif(ix==3): # rate_code
                        r[ix] = a
                    elif(ix==4): # stor_and_fwd_flag
                        r[ix] = a
                    elif(ix==5): # pickup_date
                        r[ix] = generalize_date(a)
                    elif(ix==6): # pickup_hour
                        r[ix] = generalize_hours(a)
                    elif(ix==7): # dropoff_date
                        r[ix] = generalize_date(a)
                    elif(ix==8): # dropoff_hour
                        r[ix] = generalize_hours(a)
                    elif(ix==9): # passenger_count
                        r[ix] = a
                    elif(ix==10): # trip_time_in_secs
                        r[ix] = generalize_trip_time(a)
                    elif(ix==11): # trip_distance
                        r[ix] = a
                    elif(ix==12): # pickup_longitude
                        r[ix] = generalize_coordinates(a, 3, line_number, line)
                        # r[ix] = a
                    elif(ix==13): # pickup_latitude
                        r[ix] = generalize_coordinates(a, 3, line_number, line)
                        # r[ix] = a
                    elif(ix==14): # dropoff_longitude
                        r[ix] = generalize_coordinates(a, 3, line_number, line)
                        # r[ix] = a
                    elif(ix==15): # dropoff_latitude
                        r[ix] = generalize_coordinates(a, 3, line_number, line)
                        # r[ix] = a
                    else:
                        r[ix]  =a

            if boolean_break==False :
                out.write(",".join(r))
                out.write("\n")
        out.close()
        print("done!")

generalize()
exit(0)
