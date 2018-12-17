# projetAES
## Goal
This project is a 30 hours project during which we chose to inject data in the ELK (Elastic Logstash Kibana) stack and analyze it.

Once this is done, we anonymize it and try to evaluate how good we did by putting the new data through the same ELK stack.

We found a dataset of New York taxi trips from 2013 which will be what we will be working on at first.

## Start
add your data to tripData2013 in folders such as trip_data_1.csv which will contain the trip_data_1.csv file itself

run ```python modify_csv.py``` to modify to reformat the date fields in two separate dates in your csv file

run ```python generalize.py``` to anonymize the data