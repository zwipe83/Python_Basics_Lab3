import csv
import datetime

# read temperature data from the file filename, 
# read temperatures only for the month given as argument for month or alla months if month is 0 
# (if no month given all months are included by default)
def read_from_file(filename, month=0, return_dates=False, day=0):
    result_list = []
    #open the file and process it
    with open(filename, "r", newline="") as csv_file:
        
        #csv module will handle the comma-seperated values
        number_day = 1
        for line in csv.DictReader(csv_file):
            #print(line) # uncomment if you want to know how the line appears after interpreted by the csv module

            # Optional task (harder still):
            # Skip the first n days
            if day != 0:
                day -= 1
                continue

            #find out if the current line matches the wanted month
            date = line.get("date")
            temp = float(line.get("temp"))
            if month == 0 or datetime.date.fromisoformat(date).month==month:
                if day == 0 or number_day >= day:
                    if return_dates:
                        result_list.append((date, temp))
                    else:
                        result_list.append(temp)

            number_day += 1

    return result_list