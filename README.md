# Web Based House Visualization and Recommendation

## Project proview

Millions of hosts and travelers choose to list their space and book unique accommodations anywhere in the world. Hosts could share their passions and interests with both travelers and locals by renting their houses and travelers could experience local culture and traditions deeply. Travelers need to know the local environment and reviews of their potential accommodations, such as the location, safety and grade. For landlord, they expect to get a reasonable and competitive price before they poll accommodations online. As a web-based marketplace, this tool will be helpful to both travelers and landlords in dealing with their accommodations.

## Team Member:

**Yuchen Wang**

**Xintong Xu**

**Yuhan Gao**

**Jinlin Xiang**

## Data Source:

The following Airbnb activity is included in this Seattle dataset:

- Listings, including full descriptions and average review score, 4 columns
- Reviews, including unique id for each reviewer and detailed comments, 92 columns
- Calendar, including listing id and the price and availability for that day, 6 columnsAfter selecting, the dataset review was deleted to 38 columns. (from https://www.kaggle.com/airbnb/seattle#reviews.csv)

## Directory Tree 

```
housingrecommendation
├─ DOCS
│    ├─ Component Specification.md
│    ├─ Functional Specification.md
│    └─ technology_review.pdf
├─ README.md
├─ code
│    ├─ MLCODE
│    │    ├─ Result.csv
│    │    ├─ machine learning data prepare for the house price.ipynb
│    │    └─ machine learning model for the house price.ipynb
│    └─ datahandle.py
├─ data
│    ├─ ML_Result.csv
│    ├─ calendar.csv
│    ├─ listings.csv
│    └─ reviews.csv
├─ example
│    ├─ House-Prices.ipynb
│    └─ folium_demo.ipynb
└─ views
       ├─ home_view.html
       ├─ landing.html
       ├─ prediction.html
       └─ stylesheets
              ├─ landing.css
              └─ main.css
```

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


### Instruction for setup

Application is running on Flask framework, so users need to install corresponding module in advance.

* Install following package

  ```shell
  pip3 install flask
  pip3 install geojson
  pip3 install pandas
  pip3 install numpy
  pip3 install json
  pip3 install requests
  pip3 install sklearn
  ```

* clone the repo: 

  ```shell
  git clone https://github.com/adonis-wyc/housingrecommendation.git
  ```

* Go to htmlserver foler:

  ```shell
  cd housingrecommendation/code/htmlserver
  ```

* run backend server in flask

  ```shell
  flask run
  ```

* type http://127.0.0.1:5000/ in the browser