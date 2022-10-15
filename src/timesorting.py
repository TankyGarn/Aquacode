import datetime

#take away the time of day; input: "2007/09/18 00:00:00+00", output: "2007/09/18"
def removetime(date_time):
    date_ymdt = date_time.split(" ")
    return date_ymdt[0]

#split date into year, month, day; input : "2007/09/18", output [2007,09,18]
def datelist(date):
    datelist = date.split("/")
    return datelist

#give a list with [year,month,date] returns the weeknumber:  input:  [2022,10,13] return: [41,2022]
def toWeek(datelist):
    week = datetime.date(int(datelist[0]),int(datelist[1]),int(datelist[2])).isocalendar()[1]
    year = int(datelist[0])
    year_week = [year,week]
    return year_week

# A funciton to combine the other functions into a single input instead of multiple
def fromDateToWeek(inputdate):
    return toWeek(datelist(removetime(inputdate)))


