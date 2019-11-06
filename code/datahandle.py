import pandas as pd
import numpy as np 

listing_url = "https://raw.githubusercontent.com/adonis-wyc/housingrecommendation/master/data/listings.csv"
review_url = "https://raw.githubusercontent.com/adonis-wyc/housingrecommendation/master/data/reviews.csv"
raw_listing_df = pd.read_csv(listing_url)
raw_review_df = pd.read_csv(review_url)

useful_listing_df = raw_listing_df[['id', 'listing_url', 'name', 'description', 'thumbnail_url',\
'host_id', 'host_url', 'host_name', 'host_since', 'host_response_rate', 'host_is_superhost',\
'host_listings_count', 'host_identity_verified', 'street', 'zipcode', 'latitude', 'longitude',\
'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'bed_type', 'amenities', 'square_feet',\
'price', 'weekly_price', 'monthly_price', 'security_deposit', 'cleaning_fee', 'guests_included',\
'minimum_nights', 'maximum_nights', 'review_scores_rating', 'review_scores_accuracy', \
'review_scores_cleanliness', 'requires_license', 'reviews_per_month']]

def get_raw_dataframe():
    return useful_listing_df

def show_raw_head():
    '''
    Return the head of useful_listing_df dataframe
    '''
    return useful_listing_df.head()

def basic_recommend_search(zipcode, accommodates = None, price = None, review_scores_rating = None):
    '''
    Recommend house by using basic 4 parameters (zipcode, accommodates, price, overall_rating)
    Parameter: String zipcode, Integer accommodates, String price, Integer review_scores_rating
    Return: dataframe, where zipcode == input, accommodates >= input, price <= input, scores <= input
    '''
    temp_df = useful_listing_df[useful_listing_df['zipcode'] == zipcode]
    if accommodates != None:
        temp_df = temp_df[temp_df['accommodates'] >= accommodates]
    if price != None:
        temp_df = temp_df[temp_df['price'] <= price]
    return temp_df

if __name__ == "__main__":
    get_raw_dataframe()


