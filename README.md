# Election_Analysis

## A. Overview of Election Audit

The purpose of this election audit analysis is to assist a Colorado Board of election employee to make such election audit using the tabulated results for US Congressional election in Colorado where the objective is to: 

1. Obtain the total number of votes
2. Obtain number of votes and the percentage of votes by County 
3. Identify the County with the largest number of votes
4. Have a Breakdown of number and percentage of votes by candidate
5. Identify the election winner along with percentage and number of votes obtained by him/her

## B. Election Audit Results:

1. Total Votes: 369,711
2. County Votes:
    I. Jefferson: 10.5% (38,855)
    II. Denver: 82.8% (306,055)
    III. Arapahoe: 6.7% (24,801)
3. Largest Turnout: Denver
    County Voters: 306,055
4. Number and percentage of votes by candidate
  Charles Casper Stockham: 23.0% (85,213)
  Diana DeGette: 73.8% (272,892)
  Raymon Anthony Doane: 3.1% (11,606)
5. Election winner with percentage and number of votes
  Winner: Diana DeGette
  Winning Vote Count: 272,892
  Winning Percentage: 73.8%
  
## C. Election-Audit Summary

As seen the code we have created has the ability to obtain in matter of seconds important information about an election process but most importantly helps to bring speed in the result of the election or in other words the winner.

As we know a lot of time is invested on count votes by the three existing methods: Hand, Machine and computer votes. This Python code brings a more simplified and fast way to obtain the results allowing two things:

1. Have a more careful and exhaustive vote count (since for processing the results is minimized through the code)
2. Deliver and announce the winner as soon as voting count is reflected on a .csv file in the required structure

Once we have understander the benefits of the python code it now can be used on several kinds of election by small modifications (not on the structure) but in the information used on the source (.csv file). For example, if we are using it for a senatorial election, we should only change the name of the candidates and the geographies, or if we wanted to use it for presidential elections, then it would also need to change the names, counties and if needed additional columns could be added like states, if that happens small modifications should be made to current code.

