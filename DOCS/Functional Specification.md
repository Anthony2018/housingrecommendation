# Housing Recommendation

​                                                                                  Team: Yuchen Wang, Yuhan Gao, Jinlin Xiang, Xintong Xu

## Background

Millions of hosts and travelers choose to list their space and book unique accommodations anywhere in the world. Hosts could share their passions and interests with both travelers and locals by renting their houses and travelers could experience local culture and traditions deeply. Travelers need to know the local environment and reviews of their potential accommodations, such as the location, safety and grade. For landlord, they expect to get a reasonable and competitive price before they poll accommodations online. As a web-based marketplace, this tool will be helpful to both travelers and landlords in dealing with their accommodations.

## Who are the users and what do they know?

### Travelers and hosts

 They would like to rent an accommodation in the specific area
 They should know Zoom, Hover and Select Tool on map view
 They should have experience using visualization tool


## What information users want from the system?

### • Travelers

 All available accommodations in specific area.
 Is my expected housing type and amenities within my budget?
 which area has higher/lower price?
 which area has higher/lower rating?
 How about the review of previous travelers?

### • Hosts

 How other people priced around me, relative to dimensions such as amenities and location?
 Are there certain neighborhoods that are substantially more expensive than others?
 What is the reasonable and competitive price of my houses or rooms?

## Data sources

The following Airbnb activity is included in this Seattle dataset:

* Listings, including full descriptions and average review score, 4 columns
* Reviews, including unique id for each reviewer and detailed comments, 92 columns

* Calendar, including listing id and the price and availability for that day, 6 columnsAfter selecting, the dataset review was deleted to 38 columns.
(from https://www.kaggle.com/airbnb/seattle#reviews.csv)

## Use Cases

### Use case 1

#### Detailed listing information on map view

 Database with listing information and location
User interface that allows users to select area
Map view that allows users to visualize all rooms location in this area

### Use case 2

#### Recommend top 10 rooms for customers

Database with guests’ review scores
User interface that allows users to input the info about the room
User interface that allows users to select the order of recommendations
Map view that allows users to visualize the recommendations’ location

### Use case 3

#### Recommend room price for landlord

Database with price of houses around it
User interface that allows users to input the info about the room to
improve the accuracy of predicted price
Map view that allows users to visualize all houses or the similar rooms
around it
