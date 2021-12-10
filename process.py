log_file = open("um-server-01.txt") 

# line one is opening the um-server file and saving it to a variable named log_file to be used later 


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon": #changed day to show Monday orders
            print(line)


# line 6 is a function called sales_report which takes in log_file(the file we opened a moment ago) as its argument. In the function, it loops over each line in the log_file and returns a copy of each line with the trailing characters removed. It then loops over every line again and saves the day of the order to a variable called day. If the day is equal to the day specified, an order will be printed in the console.

sales_reports(log_file)

#line 16 calls the sales_reports function with log_file as its argument

def melons_above_ten(log_file):
    for line in log_file:
        line = line.rstrip()
        amount = line[16:18]
        if int(amount) > 10:
            print(line)

melons_above_ten(log_file)

# function on line 20 prints orders where more than 10 melons were ordered

log_file.close()

# line 31 closes the file