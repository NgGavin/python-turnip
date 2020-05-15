# python-turnip
An ACNH turnip price calculator written in Python 3

## Included Files: ##

#### main.py ####
- Main input fields for initial buy price and datapoints that feeds data into trends.py
  - *cycleconverter* converts integer of cycle to ux friendly output
  - *cyclepoints* stores the values of each cycle if applicable

#### trends.py ####
- Analyzes datapoints from main.py input and determines trend with minimum and maximum values per cycle
- *Random* - no discernable trend with highs and lows
- *Decreasing* - steady decrease in value throughout the cycles
- *Large Spike* - steady decrease in value into a large net increase and back to a steady decrease
- *Small Spike* - steady decrease in value into a small net increase and back to a steady decrease

#### output.py ####
- Organizes and reformats analysis from trends.py into a ux friendly output


Created by **Gavin Ng**

*Mr.Fox's Python Programming 1 Spring 2020*