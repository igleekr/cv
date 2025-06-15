#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 09:38:47 2025

@author: kingsleylee
"""

# Independent Samples T-Test


# IMPORT REQUIRED PACAGES

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, norm


# CREATE MOCK DATA

sample_A = norm.rvs(loc = 500, scale = 100, size = 250, random_state = 42).astype(int)

sample_B = norm.rvs(loc = 550, scale = 150, size = 100, random_state = 42).astype(int)


plt.hist(sample_A, density = True, alpha = 0.5)
plt.hist(sample_B, density = True, alpha = 0.5)
plt.show()

sample_A_mean = sample_A.mean()
sample_B_mean = sample_B.mean()
print(sample_A_mean, sample_B_mean)



# SET THE HYPOTHESIS & ACCEPTANCE CRITERIA

null_hypothesis = "The mean of the sample_A is equal to the mean of sample_B"
alternate_hypothesis = "The mean of the sample_A is different to the mean of sample_B"

acceptance_criteria = 0.05



# EXECUTE THE HYPOTHESIS TEST

t_statistic, p_value = ttest_ind(sample_A, sample_B)
print(t_statistic, p_value)



# PRINT THE RESULTS (p-value)

if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than our acceptance criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than our acceptance criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}")



# ******** WELCH'S T-TEST ********


"""

Welch's T-Test:
 - is more reliable than the regular T-Test whenever sample sizes and variances are
   unequal btn groups
 - gives the same results when the sample sizes and variances are equal
 - always apply instead of regular T-test statistic
 
"""

# EXECUTE THE HYPOTHESIS TEST

t_statistic, p_value = ttest_ind(sample_A, sample_B, equal_var = False)
print(t_statistic, p_value)



# PRINT THE RESULTS (p-value)

if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than our acceptance criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than our acceptance criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}")









































