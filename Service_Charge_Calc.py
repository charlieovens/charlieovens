#coding=utf-8
from datetime import datetime, date, timedelta
import numpy as np
import sys

print("What is the Annual Service charge payable?")
Ann_SC = float(input())
d_rate = float(Ann_SC / 365)
d_rate_2dp = np.round(d_rate, decimals=2)


#demand date

demand_date = input("What is the demand date in the format dd/mm/yyyy: ")
demand_date_str = str(demand_date)
day, month, year = demand_date.split('/')
SC_demand = date(int(year),int(month),int(day))
print("Demand date is: " + str(SC_demand))

#Completion date

comp_date = input("What is the completion date in the format dd/mm/yyyy: ")
day1,month1,year1 = comp_date.split('/')
completion_date = date(int(year1),int(month1),int(day1))
print("The completion date is " + str(completion_date))

#number of days between

def days_between(d1, d2) :
    d1 = SC_demand
    d2 = completion_date
    return abs((d2 - d1).days)

app_period = days_between(SC_demand, completion_date)

print("Service Charge period is: " + str(app_period) + " days")
print("Daily Rate: £" + str(d_rate_2dp))

#Total SC apportionment

total_app = d_rate_2dp * app_period
print("Total SC Apportionment is: £" + str(total_app))

#Adding a ground rent apportionment

def deciding(G) :
    while G in GR_input == 'y' :
        break
    else :
        sys.exit("Thanks for using the calculator!")

GR_input = input("Is there a Ground Rent apportionment? Enter y for yes, n for no: ")

deciding(GR_input)


def datesame1(a) :
   for a in gr_date_same :
        if gr_date_same == 'y' :
            GR_cost = input("What is the annual Ground Rent? ")
            dailygr = np.round((float(GR_cost) / 365), decimals=2)
            print("Daily Rate: £" + str(dailygr))
            total_gr_app = np.round((dailygr * app_period), decimals=2)
            print("Total GR Apportionment is: £" + str(total_gr_app))
            break
        else :
            new_dd = input("Please enter the demand date in the format dd/mm/yy ")
            day3, month3, year3 = new_dd.split('/')
            new_form_dd = date(int(year3),int(month3),int(day3))
            print("The GR demand date is: " + str(new_form_dd))
            gr_app_period = days_between(completion_date, new_form_dd)
            GR_cost = input("What is the annual Ground Rent? ")
            dailygr = np.round((float(GR_cost) / 365), decimals=2)
            print("Daily Rate: £" + str(dailygr))
            total_gr_app = np.round((dailygr * gr_app_period), decimals=2)
            print("Total GR Apportionment is: £" + str(total_gr_app))

gr_date_same = input("Is the Ground Rent Demanded on the same day as Service Charge? Enter y for yes, n for no: ")

datesame1(gr_date_same)