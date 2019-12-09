import pandas as pd
import numpy as np 

# listing_url = "https://raw.githubusercontent.com/adonis-wyc/housingrecommendation/master/data/listings.csv"
# review_url = "https://raw.githubusercontent.com/adonis-wyc/housingrecommendation/master/data/reviews.csv"
raw_listing_df = pd.read_csv('listings.csv') # raw listing dataframe with 96 columns
raw_review_df = pd.read_csv('reviews.csv') # raw review dataframe with 6 columns

# Select needed 38 columns into useful_listing_df
useful_listing_df = raw_listing_df[['id', 'listing_url', 'name', 'description', 'thumbnail_url',
'picture_url','host_id', 'host_url', 'host_name', 'host_since', 'host_response_rate', 'host_is_superhost',\
'host_listings_count', 'host_identity_verified', 'street', 'zipcode', 'latitude', 'longitude',\
'room_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'bed_type', 'amenities', 'square_feet',\
'price', 'weekly_price', 'monthly_price', 'security_deposit', 'cleaning_fee', 'guests_included',\
'minimum_nights', 'maximum_nights', 'review_scores_rating', 'review_scores_accuracy', \
'review_scores_cleanliness', 'requires_license', 'reviews_per_month']]

pd.set_option('mode.chained_assignment', None)
useful_listing_df['host_is_superhost'] = raw_listing_df.host_is_superhost == 't'
useful_listing_df['host_identity_verified'] = raw_listing_df.host_identity_verified == 't'
useful_listing_df['requires_license'] = raw_listing_df.requires_license == 't'

def get_raw_useful_listing_df():
    '''
    Return the raw useful_listing  dataframe
    '''
    return useful_listing_df

def show_raw_head():
    '''
    Return the head of useful_listing_df dataframe
    '''
    return useful_listing_df.head()

def primary_recommend_search(zipcode: str, accommodates: int = None, price: str = None, \
    review_scores_rating: int = None, host_is_superhost: bool = None, host_identity_verified: bool = None, \
    room_type: str = None, bathrooms: float = None, bedrooms: int = None, cleaning_fee: str = None, \
    guests_included: int = None, nights: int = None, review_scores_cleanliness: int = None, \
    review_scores_accuracy: int = None, requires_license: bool = None, limit: int = None,\
    sorting_list: list = ['review_scores_rating', 'price'], sorting_way: list = [False, True]):
    '''
    Recommend house by using many more parameters than basic search, but all of these parameters are set to None
    defaultly except for zipcode, so you could get result by enter at least one parameter zipcode
    If you do not want any parameter take effects, just let this parameter as none
    Default sorting_list = ['review_scores_rating', 'price'], sorting_way = [False, True] for ascending
    @Return: dataframe
    '''
    temp_df = useful_listing_df[useful_listing_df['zipcode'] == zipcode]
    if accommodates != None:
        temp_df = temp_df[temp_df['accommodates'] >= accommodates]
    if price != None:
        temp_df = temp_df[temp_df['price'] <= price]
    if review_scores_rating != None:
        temp_df = temp_df[temp_df['review_scores_rating'] >= review_scores_rating]
    if host_is_superhost != None:
        temp_df = temp_df[temp_df['host_is_superhost'] == host_is_superhost]
    if host_identity_verified != None:
        temp_df = temp_df[temp_df['host_identity_verified'] == host_identity_verified]
    if room_type != None:
        temp_df = temp_df[temp_df['room_type'] == room_type]
    if bathrooms != None:
        temp_df = temp_df[temp_df['bathrooms'] >= bathrooms]
    if bedrooms != None:
        temp_df = temp_df[temp_df['bedrooms'] >= bedrooms]
    if cleaning_fee != None:
        temp_df = temp_df[(temp_df['cleaning_fee'] <= cleaning_fee) | (temp_df['cleaning_fee'].isna())]
    if guests_included != None:
        temp_df = temp_df[temp_df['guests_included'] >= guests_included]
    if nights != None:
        temp_df = temp_df[(temp_df['minimum_nights'] <= nights) & (temp_df['maximum_nights'] >= nights)]
    if review_scores_cleanliness != None:
        temp_df = temp_df[temp_df['review_scores_cleanliness'] >= review_scores_cleanliness]
    if review_scores_accuracy != None:
        temp_df = temp_df[temp_df['review_scores_accuracy'] >= review_scores_accuracy]
    if requires_license != None:
        temp_df = temp_df[temp_df['requires_license'] == requires_license]
    temp_df = temp_df.sort_values(sorting_list, ascending = sorting_way)
    if limit != None:
        temp_df = temp_df.head(limit)
    return temp_df


def basic_recommend_search(zipcode: str, accommodates: int = None, price: str = None, \
    review_scores_rating: int = None, limit: int = None, sorting_list: list = ['review_scores_rating', 'price'], \
    sorting_way: list = [False, True]):
    '''
    Recommend house by using basic 4 parameters (zipcode, accommodates, price, overall_rating)
    and sorting by 2 parameters (sorting_list, sorting_way), and these two list should have same length
    The default sorting_list = ['review_scores_rating', 'price'], default sorting_way = [False, True] for ascending

    @Parameter: String zipcode, Integer accommodates, String price, Integer review_scores_rating

    @Sorting parameter: List sorting_list, List sorting_way

    @Return: useful_listing_df, where zipcode == input, accommodates >= input, price <= input, scores >= input
    '''
    temp_df = useful_listing_df[useful_listing_df['zipcode'] == zipcode]
    if accommodates != None:
        temp_df = temp_df[temp_df['accommodates'] >= accommodates]
    if price != None:
        temp_df = temp_df[temp_df['price'] <= price]
    if review_scores_rating != None:
        temp_df = temp_df[temp_df['review_scores_rating'] >= review_scores_rating]
    temp_df = temp_df.sort_values(sorting_list, ascending = sorting_way)
    if limit != None:
        temp_df = temp_df.head(limit)
    return temp_df

if __name__ == "__main__":
    get_raw_dataframe()


