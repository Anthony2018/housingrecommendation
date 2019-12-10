import os
from setuptools import setup, find_packages
PACKAGES = find_packages()
 DES='''
Project proview
Millions of hosts and travelers choose to list their space and book unique accommodations 
anywhere in the world. Hosts could share their passions and interests with both travelers 
and locals by renting their houses and travelers could experience local culture and traditions 
deeply. Travelers need to know the local environment and reviews of their potential 
accommodations, such as the location, safety and grade. 
For landlord, they expect to get a reasonable and competitive 
price before they poll accommodations online. As a web-based marketplace, this 
tool will be helpful to both travelers and landlords in dealing with their accommodations.
Use Cases
Use case 1
Detailed listing information on map view
Database with listing information and location User interface that allows users to select 
area Map view that allows users to visualize all rooms location in this area

Use case 2
Recommend top 10 rooms for customers
Database with guests’ review scores User interface that allows users to input the info 
about the room User interface that allows users to select the order of recommendations 
Map view that allows users to visualize the recommendations’ location

Use case 3
Recommend room price for landlord
Database with price of houses around it User interface 
that allows users to input the info about the room to improve the 
accuracy of predicted price Map view that allows users to visualize 
all houses or the similar rooms around it.
 ''''

opts = dict(name="housingrecommendation",
            description= DES,
            url="https://github.com/adonis-wyc/housingrecommendation",
            license="MIT"
            author="Yucehn Wang,Xintong Xu, Yuhan Gao, Jinlin Xiang",
            author_email="mark96@uw.edu",
            version= "__version__ 1.0",
            packages='PACKAGES',
            install_requires='REQUIRES',
            requires=["numpy", "pandas", "sklearn"])


if __name__ == '__main__':
    setup(**opts)
