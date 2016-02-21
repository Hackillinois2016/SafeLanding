# SafeLanding
Utilizes Amadeus and IMO APIs to compile public health information near travel destinations.
The user provides a city of origin, for which Amadeus provides potential tourist destinations accessible by air. The user chooses a city from the possible destinations and  healthcare providers' logs for contagious diseases in the area are found using the IMO mySQL database. The site then generates a graph of these diseases, ranked by number of recently reported cases.


__Dependencies:__  
Flask-0.10.1  
Flask-Scss-0.5  
simplejson  
mySQL  


__Languages:__  
Python-2.7.11  
JavaScript/jQuery/AJAX  
Scss/CSS  
HTML  


__APIs (info required):__  
Amadeus Travel API  
IMO Healthcare API  
