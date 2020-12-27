# Election_Analysis

## Project Overview
Through a partnerhsip with the Colorado Board of Elections, we were tasked with supporting the final eleciton count and audit of a local congressional election.  Data was to be presented in a clear, conside way and our final code is required to be made public to enable subsquent reviews.  The primary tasks were:
1. Count the total number of votes cast.
2. Provide a complete list of candidates who receied votes.
3. Calculate the percentage of votes that each candidate won.
4. Calculate the total number of votes each candidate won.
5. Determine the winner fo the election based on popular vote count. 


## Election-Audit Results
The analysis of the election show that:
- There were **369,711** votes cast in the election

- Listed below are the counties included in this election and the distribution of votes among them:
  - Arapahoe: 24,801 (6.7%)
  - **Denver: 306,055 (82.8%)**
  - Jefferson: 38,855 (10.5%)
  
  **BOLD** denotes county with largest number of votes
  
- The candidates were:
  - Charles Casper Sotckham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham recieved **85,213 votes**, representing **23.0%** of total votes cast. 
  - Diana DeGette recieved **272,892 votes**, representing **73.8%** of total votes cast.
  - Raymon Anthony Doane recieved **11,606 votes**, representing **3.1%** of total votes cast.
- The winner of the election was:
  - Diana DeGette, who recieved **272,892 votes**, representing **73.8%** of total votes cast.

## Election-Audit Summary
The Python code utilized in this audit can be repurposed to support the analysis of other election data that is stored in .CSV files.  The variables were designed to analyze the frequency of key election inputs - unique vote counts, candidate names, geographic identifiers - that can easily be modified to tally different information.  

Our analysis includes county-level performance.  Refernces to county could easily be modified to reference a region, district, or city. The code below builds the *county_list* to include all unique counties that were represented by voters in the election and then counts votes attributed to each county (*county_votes*).  This functionality could easily be applied to other geographic identifiers.

Determine if a county matches any existing county in the county list.
  
```if county_name not in county_list:```

If it is a new county, add it to the list of counties.
  
```county_list.append(county_name)```
  
Begin tracking the county's vote count by initializing all votes in each county to zero.
    
```county_votes[county_name] = 0```
    
Add a vote to that county's vote count while cycling through each row in the .CSV file.
  
```county_votes[county_name] += 1```

While this election featured three candidates, this code will automatically build the list of potential candidates (*candidate_options* variable) to reflect all instances of a candidate's name.  The commands below will continue to add a new *candidate_name* to the *candidate_options* list if it is not already currently reflected in the *candidate_options* list.  

  
If the candidate does not match any existing candidate,
  
```if candidate_name not in candidate_options:```
  
Add the candidate name to the candidate list.
      
```candidate_options.append(candidate_name)```

One potential modification will be linked to the data structure in the .CSV file. Our data captures *county_name* in the second column (*county_name = row[1]*) and *candidate_name* in the third column (*candidate_name = row[2]*). This could be quikcly updated to reference a different column if geograhpic or candidate information is captured somewhere else in the data file.

## Resources
- Data source: election_results.csv
- Software: Python 3.8.5, Visual Studio Code 1.52.1
