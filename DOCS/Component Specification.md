## Software Components

### data_manager.py

It will get the raw data from URL we provided and will clean and choose useful data we will needed. It will also provide some useful methods for querying needed data subsets and return needed data to frontend components.

#### Methods: 

​    get_raw_dataframe()

​    show_raw_head()

​    basic_recommend_search(zipcode, accommodates = None, price = None, review_scores_rating = None)



### visualization_manager.py  

It will operate like the frontend manager that will get the data from backend data manager and visualize the data for user.  



## Interactions to accomplish use cases:

### Use case 1: Detailed listing information on map view  

The data manager will provide two method to help get raw useful data without any search and recommendation.  

raw_data  ---->  data cleaning and selection ---->  useful_listing_df ----> return data



###Use case 2: Recommend top 10 rooms for customers  

The data manager will provide methods to handle the search query from frontend user input and return need data structure to frontend.

raw_data ----> cleaning and selection ----> useful_listing_df ----> selection and search query ----> return data



### Use case 3: Recommend room price for landlord  

We will use Machine Learning to pridict the recommend price, so the data manager will call for additional Machine Learning Handler package to use ML and return data to frontend.

raw_data ----> cleaning and selection ----> useful_listing_df ----> ML package ----> return data to frontend



##Preliminary Plan

####Tasks:

- Finish writing data_manager.py to provide needed methods.
- Finish writing machine learning handle package to predict recommend data
- Finish writing visualization_manager.py to handle data from backend to frontend and make visualization.