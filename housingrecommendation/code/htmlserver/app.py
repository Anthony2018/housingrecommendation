'''
This python module is the supporter of Flask framework
'''
import datahandle as dh
import pandas as pd
import json
import requests
from geojson import Point, Feature
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)

def get_marker_points(df):
    '''
    Return the list of GeoJSON points
    @input: dataframe df
    @return list of points 
    '''
    points = []
    for index, row in df.iterrows():
        point = Point([row['longitude'], row['latitude']])
        properties = {
            'url': str(row['listing_url']),
            'title': row['name'],
            'price': row['price'],
            'accommodates': row['accommodates'],
            'room_type': row['room_type'],
            'thumbnail_url': str(row['picture_url'])
        }
        feature = Feature(geometry = point, properties = properties)
        points.append(feature)
    return points

@app.route('/')
def index():
    '''
    Return the main landing page
    '''
    return render_template('landing.html')

@app.route('/prediction')
def prediction():
    '''
    Return the use case 3 (price prediction) page
    '''
    return render_template('prediction.html')

@app.route('/homeview')
def viewallhouse():
    '''
    Return the use case 1 (view all house) page
    '''
    points_list = get_marker_points(dh.get_raw_useful_listing_df())
    return render_template('home_view.html', points_list = points_list)   

@app.route('/recommendation.html', methods=['GET', 'POST'])
@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    '''
    Return the use case 2 (house recommendation) page
    It will get the user input from webpage and then process and pass 
    the input to datahandle package
    '''
    if request.method == 'POST':
        zipcode = request.form.get('zipcode')
        nights = request.form.get('nights')
        price = request.form.get('price')
        accommodates = request.form.get('accommodates')
        room_type = request.form.get('room_type')
        score = request.form.get('score')
        is_verified_host = request.form.get('verified_host')
        is_need_license = request.form.get('need_license')
        results_limit = request.form.get('results_limit')

        nights = None if nights == "" else int(nights)
        price =  None if price == "" else "$" + price
        accommodates = None if accommodates == "" else int(accommodates)
        room_type =  None if room_type == "" else room_type
        score = None if score == "" else int(score)
        is_verified_host = True if is_verified_host == "True" else None
        is_need_license = True if is_need_license == "True" else None
        results_limit = None if results_limit == "" else int(results_limit)

        df_table = dh.primary_recommend_search(zipcode, accommodates, price, score, None,\
            is_verified_host, room_type, None, None, None, None, nights, None, None, \
            is_need_license, results_limit)
        if df_table.empty:
            return render_template('not_found.html')

        points_list = get_marker_points(df_table)

        return render_template('recommendation.html', points_list = points_list,\
            house_list = df_table)
    return render_template('index.html')