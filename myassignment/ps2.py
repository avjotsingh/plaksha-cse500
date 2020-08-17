#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""[application description here]"""

__author__ = "Kingshuk Dasgupta (rextrebat/kdasgupta)"
__version__ = "0.0pre0"

def months_to_down_payment(total_cost, portion_down_payment, current_savings,
                           r, annual_salary, portion_saved):
    down_payment = portion_down_payment * total_cost
    mos = 0
    while (current_savings < down_payment):
        mos += 1
        interest = current_savings * r / 12
        savings = portion_saved * annual_salary / 12
        current_savings += interest + savings
    return mos


def months_to_down_payment_inc(total_cost, portion_down_payment, current_savings,
                           r, annual_salary, portion_saved, semi_annual_raise):
    down_payment = portion_down_payment * total_cost
    mos = 0
    while (current_savings < down_payment):
        mos += 1
        interest = current_savings * r / 12
        savings = portion_saved * annual_salary / 12
        current_savings += interest + savings
        if mos%6 == 0:
            annual_salary *= 1 + semi_annual_raise
    return mos


def get_savings(current_savings, r, annual_salary, portion_saved,
                           semi_annual_raise, mos):
    for m in range(mos):
        interest = current_savings * r / 12
        savings = portion_saved * annual_salary / 12
        current_savings += interest + savings
        if m%6 == 0:
            annual_salary *= 1 + semi_annual_raise
    return current_savings

def get_rate(low, high):
    return ((low + high)/2) / 10000.0

def best_savings_rate(total_cost, portion_down_payment, current_savings,
                           r, annual_salary, semi_annual_raise, mos):
    epsilon = 100
    numGuesses = 0
    low = 0
    high = 10000
    ans = get_rate(low, high)
    required_down_payment = portion_down_payment * total_cost
    available_down_payment = get_savings(current_savings, r, annual_salary,
                                         ans, semi_annual_raise, mos)
    while abs(required_down_payment - available_down_payment) > epsilon:
        print('low =', low, 'high =', high, 'ans =', ans)
        numGuesses += 1
        if available_down_payment > required_down_payment:
            # adjust down
            high = round(ans * 10000)
        else:
            low = round(ans * 10000)
        ans = get_rate(low, high)
        available_down_payment = get_savings(current_savings, r, annual_salary,
                                            ans, semi_annual_raise, mos)

    return (ans, numGuesses)





mos = months_to_down_payment(1000000, 0.25, 0, 0.04, 120000, 0.1)
print("Months: " + str(mos))

mos = months_to_down_payment_inc(800000, 0.25, 0, 0.04, 80000, 0.1, 0.03)
print("Months: " + str(mos))

best_rate, numGuesses = best_savings_rate(1000000, 0.25, 0, 0.04, 150000, 0.07, 36)
print("Saving Rate:", best_rate, "Guesses:", numGuesses)

best_rate, numGuesses = best_savings_rate(1000000, 0.25, 0, 0.04, 300000, 0.07, 36)
print("Saving Rate:", best_rate, "Guesses:", numGuesses)
