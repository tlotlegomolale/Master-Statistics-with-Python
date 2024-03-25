# 1+2 import libaries

import noshmishmosh
import numpy as np

# 4 how many users visit the site in a typical week

all_visitors = noshmishmosh.customer_visits

# 5 how many visitors to the site ultimately end up buying a meal or set of meals in a typical week

paying_visitors = noshmishmosh.purchasing_customers

#5 lenght of both list

total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

#7+8 Calculate + Print Baseline =18.6

baseline_percent = (paying_visitor_count/total_visitor_count)*100
print(baseline_percent)

#9 the money spent by each customer in a typical week

payment_history = noshmishmosh.money_spent

#9 how many purchases it would take to reach $1240 in additional revenue = 26.543655913978498

average_payment = np.mean(payment_history)
print(average_payment)

#9 how many purchases it would take to reach $1240 in additional revenue = 47

new_customers_needed = np.ceil(1240/average_payment)
print(new_customers_needed)

#12 the additional percent of weekly visitors who must make a purchase in order to make this change worthwhile = 9.4
percentage_point_increase =(new_customers_needed/total_visitor_count)*100

print(percentage_point_increase)

#13+14 mde = 50.53763440860215

mde = (percentage_point_increase/baseline_percent)*100
print(mde)

#15

significance_threshold = 0.10

#16

ab_sample_size = 490
