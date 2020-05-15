# python-turnip
**An ACNH turnip price calculator written in Python 3**

## Included Files: ##

#### main.py ####
- Main input fields for initial buy price and datapoints that feeds data into trends.py
  - *cycleconverter* converts integer of cycle to ux friendly output
  - *cyclepoints* stores the values of each cycle if applicable

#### trends.py ####
- Analyzes datapoints from main.py input and determines trend with minimum and maximum values per cycle
  - *random* - no discernable trend with highs and lows
  - *decreasing* - steady decrease in value throughout the cycles
  - *large spike* - steady decrease in value into a large net increase and back to a steady decrease
  - *small spike* - steady decrease in value into a small net increase and back to a steady decrease

#### output.py ####
- Organizes and reformats analysis from trends.py into a ux friendly output
  - *grapher* creates a graph based off of maximum and minimum available buy prices based off of the values, analysis, and results to be displayed on fileprinter
  - *fileprinter* creates and outputs a text file of the initial values, analysis, and results


**Algorithm Source**
https://docs.google.com/document/d/1bSVNpOnH_dKxkAGr718-iqh8s8Z0qQ54L-0mD-lbrXo/edit#heading=h.7krciw7xapag
-----------------------------------------------------------------------------------------------------------

Created by **Gavin Ng**

*Mr.Fox's Python Programming 1 Spring 2020*
