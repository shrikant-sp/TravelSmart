import os
import uuid
import requests
from functools import wraps
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# --- Imports for Forgot Password Feature ---
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

# --- New Imports for Social Login (OAuth) ---
from authlib.integrations.flask_client import OAuth
# -----------------------------------------------

load_dotenv()

app = Flask(__name__)
# Security: Change this secret key in production!
app.secret_key = os.getenv('SECRET_KEY', 'default-secret-key-change-in-production')

# --- SESSION CONFIGURATION (Fixes Login Loop/Domain Mismatch) ---
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
# -----------------------------------------------

GOOGLE_PLACES_API_KEY = os.getenv('GOOGLE_PLACES_API_KEY', '')

# --- EMAIL CONFIGURATION & INITIALIZATION ---
PASSWORD_RESET_TIMEOUT = 3600 

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'travelsmart5151@gmail.com')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', 'umnwpqvrizzaodar') 
app.config['MAIL_DEFAULT_SENDER'] = (
    os.getenv('MAIL_DEFAULT_SENDER_NAME', 'TravelSmart Support'),
    os.getenv('MAIL_DEFAULT_SENDER_EMAIL', 'travelsmart5151@gmail.com')
)
mail = Mail(app)

# --- TOKEN SERIALIZER SETUP ---
s = URLSafeTimedSerializer(app.secret_key)

# --- OAUTH CONFIGURATION (SOCIAL LOGIN) ---
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

oauth = OAuth(app)


# --------------------------------------------

# In-memory data stores
users = {}
bookings = []

# Seed destinations - State-wise Indian destinations
destinations = {
    # Andhra Pradesh
    'visakhapatnam': {
        'name': 'Visakhapatnam (Vizag)',
        'state': 'Andhra Pradesh',
        'description': 'Biggest city of Andhra Pradesh with major sea-port and beautiful beaches. Known for Kailasagiri, RK Beach, and Araku Valley nearby.',
        'image_url': 'https://www.famousindia.in/wp-content/uploads/2020/12/Why-is-Visakhapatnam-famous-in-India-1200x675.jpg',
        'source': 'local'
    },
    'tirupati': {
        'name': 'Tirupati',
        'state': 'Andhra Pradesh',
        'description': 'One of India\'s top pilgrimage cities, famous for Tirumala Balaji Temple of Lord Venkateswara. Located at the foothills of Eastern Ghats.',
        'image_url': 'https://wallpaperaccess.com/full/3479485.jpg',
        'source': 'local'
    },
    'vijayawada': {
        'name': 'Vijayawada',
        'state': 'Andhra Pradesh',
        'description': 'Third-largest city located on the Krishna River. Important trade and business center with Kanaka Durga Temple as main attraction.',
        'image_url': 'https://th.bing.com/th/id/OIP.itLQRoZsoRIGpDUOUpnHHQHaDt?w=337&h=174&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3',
        'source': 'local'
    },
    'rajahmundry': {
        'name': 'Rajahmundry',
        'state': 'Andhra Pradesh',
        'description': 'Cultural capital of Andhra Pradesh and birthplace of Telugu language. Located on Godavari River with scenic ghats and historic bridge.',
        'image_url': 'https://th.bing.com/th/id/ODL.c65ebea099f7f2bd7e0c673e3cc079fe?w=310&h=198&c=7&rs=1&bgcl=ffff14&r=0&o=6&dpr=1.3&pid=AlgoBlockDebug',
        'source': 'local'
    },
    
    # Arunachal Pradesh
    'tawang': {
        'name': 'Tawang',
        'state': 'Arunachal Pradesh',
        'description': 'Located at 10,000 ft with 400-year-old Tawang Monastery (one of India\'s largest). Beautiful lakes and snow-covered landscapes.',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/TawangMonastery-ArunachalPradesh-1.jpg/500px-TawangMonastery-ArunachalPradesh-1.jpg',
        'source': 'local'
    },
    'itanagar': {
        'name': 'Itanagar',
        'state': 'Arunachal Pradesh',
        'description': 'Capital of Arunachal Pradesh with Wildlife Sanctuary (400+ bird species), Ita Fort, State Museum, and scenic Ganga Lake.',
        'image_url': 'https://th.bing.com/th/id/OIP.8kVxFn0c5giC9udhkj7CjQHaE8?w=286&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3',
        'source': 'local'
    },
    'ziro': {
        'name': 'Ziro',
        'state': 'Arunachal Pradesh',
        'description': 'UNESCO World Heritage Site, also called the Apatani Plateau. Known for Talley Valley, wildlife sanctuary, and bamboo & pine forests.',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/A_cross_section_of_luch_green_valley_of_Ziro.jpg/500px-A_cross_section_of_luch_green_valley_of_Ziro.jpg',
        'source': 'local'
    },
    
    # Assam
    'kaziranga': {
        'name': 'Kaziranga National Park',
        'state': 'Assam',
        'description': 'UNESCO World Heritage Site famous for one-horned rhinoceros, tigers, elephants. Best for birdwatching with jeep and elephant safaris.',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Beauty_of_Kaziranga_National_Park.jpg/500px-Beauty_of_Kaziranga_National_Park.jpg',
        'source': 'local'
    },
    'guwahati': {
        'name': 'Guwahati',
        'state': 'Assam',
        'description': 'Home to Kamakhya Temple on Nilachal Hill, over 2200 years old. Stunning views of Brahmaputra River and surrounding hills.',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/A_view_from_Nilachal_Hill_in_Guwahati%2C_Assam%2C_India.jpg/500px-A_view_from_Nilachal_Hill_in_Guwahati%2C_Assam%2C_India.jpg',
        'source': 'local'
    },
    
    # Bihar
    'nalanda': {
        'name': 'Nalanda University',
        'state': 'Bihar',
        'description': 'World\'s first residential university built in 5th century AD. Buddha taught here; excavated remains include stupas, temples, red brick architecture.',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Temple_No.-_3%2C_Nalanda_Archaeological_Site.jpg/500px-Temple_No.-_3%2C_Nalanda_Archaeological_Site.jpg',
        'source': 'local'
    },
    'bodh gaya': {
        'name': 'Bodh Gaya',
        'state': 'Bihar',
        'description': 'UNESCO World Heritage Site where Buddha attained enlightenment under the Bodhi Tree. Features the grand Mahabodhi Temple.',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Great_Buddha_Statue%2C_Bodh_Gaya.jpg/500px-Great_Buddha_Statue%2C_Bodh_Gaya.jpg',
        'source': 'local'
    },
    'rajgir': {
        'name': 'Rajgir',
        'state': 'Bihar',
        'description': 'Historic city with Griddhakuta Peak where Buddha delivered sermons. Famous for hot springs believed to have healing properties.',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Naulakha_Mandir.jpg/330px-Naulakha_Mandir.jpg',
        'source': 'local'
    },
    
    # Chhattisgarh
    'chitrakot': {
        'name': 'Chitrakot Waterfall',
        'state': 'Chhattisgarh',
        'description': 'Known as "Niagara Falls of India", 96 ft high and over 1000 ft wide in monsoon. Forest surroundings make it very scenic.',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Chitrakote_Falls.jpg/500px-Chitrakote_Falls.jpg',
        'source': 'local'
    },
    'bhoramdeo': {
        'name': 'Bhoramdeo Temple',
        'state': 'Chhattisgarh',
        'description': 'Known as the "Khajuraho of Chhattisgarh", built between 7th-11th century with beautifully carved religious and erotic sculptures.',
        'image_url': 'https://tse3.mm.bing.net/th/id/OIP.SrwZ9D9zDzVTkSCeOkIRcgHaFX?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    
    # Goa
    'goa': {
        'name': 'Goa',
        'state': 'Goa',
        'description': 'Famous beaches, vibrant nightlife, Portuguese heritage. Known for Dudhsagar Waterfalls, Baga Beach, and water sports.',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/BeachFun.jpg/500px-BeachFun.jpg',
        'source': 'local'
    },
    'baga beach': {
        'name': 'Baga Beach',
        'state': 'Goa',
        'description': 'One of India\'s most famous beaches. Known for nightlife, water sports, beach shacks, and seafood.',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Baga_Beach-India_Goa-Andres_Larin.jpg/500px-Baga_Beach-India_Goa-Andres_Larin.jpg',
        'source': 'local'
    },
    'palolem beach': {
        'name': 'Palolem Beach',
        'state': 'Goa',
        'description': 'Calm, scenic crescent-shaped beach in South Goa. Featured in The Bourne Supremacy. Bamboo huts and peaceful atmosphere.',
        'image_url': 'https://th.bing.com/th/id/R.c9410ae6843b5a9e5ee84124c487d9b2?rik=sgrQoxqsY5kExw&riu=http%3a%2f%2fblog.thomascook.in%2fwp-content%2fuploads%2f2014%2f01%2fAlleppey-Backwaters.jpg&ehk=GqLWb%2bK7InDXLXN1Y%2fLqw5hGwvQqgF7n1Nom%2bwoSN4c%3d&risl=&pid=ImgRaw&r=0',
        'source': 'local'
    },
    'dudhsagar': {
        'name': 'Dudhsagar Waterfalls',
        'state': 'Goa',
        'description': 'One of India\'s tallest and most powerful waterfalls on the Mandovi River. Falls look like "white milk".',
        'image_url': 'https://th.bing.com/th/id/OIP.fpxxWPQZLaCPM6rVsDO9PgHaEL?w=307&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3',
        'source': 'local'
    },
    
    # Gujarat
    'vadodara': {
        'name': 'Vadodara',
        'state': 'Gujarat',
        'description': 'Home to Laxmi Vilas Palace spread across 700 acres, one of India\'s grandest royal palaces with rich decorations and Raja Ravi Varma paintings.',
        'image_url': 'https://tse1.mm.bing.net/th/id/OIP.6jKaunlI9ctTqx5nW7H14wHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    'rann of kutch': {
        'name': 'Great Rann of Kutch',
        'state': 'Gujarat',
        'description': 'One of the world\'s largest salt deserts (over 16,000 sq km). Magical under full-moon light. Best during Rann Utsav festival.',
        'image_url': 'https://www.tripsavvy.com/thmb/nB_VbZj6wGNXdPGYnsnLpyvm9Wc=/2122x1412/filters:fill(auto,1)/GettyImages-537000923-541774dbe2d44759815fdf0719b04685.jpg',
        'source': 'local'
    },
    'gir': {
        'name': 'Gir National Park',
        'state': 'Gujarat',
        'description': 'India\'s only home of the Asiatic Lion. Spread across 1,412 sq km with rich wildlife including crocodiles, hyenas, and sambhar.',
        'image_url': 'https://www.girnationalpark.in/uploads/sasan-gir-jungle.jpg',
        'source': 'local'
    },
    
    # Haryana
    'kurukshetra': {
        'name': 'Kurukshetra',
        'state': 'Haryana',
        'description': 'The Mahabharata battlefield where Lord Krishna gave the Bhagavad Gita. Famous pilgrimage with Brahma Sarovar and Jyotisar.',
        'image_url': 'https://www.adotrip.com/public/images/city/master_images/5e4a34c1f385b-Kurukshetra_Places_to_See.jpg',
        'source': 'local'
    },
    'gurgaon': {
        'name': 'Gurgaon (Gurugram)',
        'state': 'Haryana',
        'description': 'Haryana\'s corporate and technology city mentioned in Mahabharata. Features Sultanpur Bird Sanctuary and Kingdom of Dreams.',
        'image_url': 'https://th.bing.com/th/id/OIP.M68064xZVcy9iPUzWXmnvwHaE7?w=247&h=180&c=7&r=0&o=7&dpr=1.1&pid=1.7&rm=3',
        'source': 'local'
    },
    
    # Himachal Pradesh
    'kullu': {
        'name': 'Kullu',
        'state': 'Himachal Pradesh',
        'description': 'Beautiful valley on River Beas, known as Valley of Gods. Adventure activities include trekking, rafting, paragliding, and skiing.',
        'image_url': 'https://www.adotrip.com/public/images/city/master_images/5e3bd174e7fbf-Kullu_Attractions.jpg',
        'source': 'local'
    },
    'manali': {
        'name': 'Manali',
        'state': 'Himachal Pradesh',
        'description': 'Famous hill station at 6,726 ft with Rohtang Pass, Solang Valley, and Hidimba Temple. Popular honeymoon and adventure destination.',
        'image_url': 'https://digitalnomads.world/wp-content/uploads/2021/06/manali-digital-nomads.jpg',
        'source': 'local'
    },
    'shimla': {
        'name': 'Shimla',
        'state': 'Himachal Pradesh',
        'description': 'Former summer capital of British India with colonial architecture. Famous for The Ridge, Mall Road, and Kufri.',
        'image_url': 'https://deih43ym53wif.cloudfront.net/shimla-india-shutterstock_401682040_782e317f1f.jpeg',
        'source': 'local'
    },
    'dharamshala': {
        'name': 'Dharamshala',
        'state': 'Himachal Pradesh',
        'description': 'Known as "Scotland of India" with snowy mountains on three sides. Features Triund trek, Bhagsu Waterfall, and tea gardens.',
        'image_url': 'https://tse1.mm.bing.net/th/id/OIP.IQibIHk3gT7DoL0UaH8aowHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    'dalhousie': {
        'name': 'Dalhousie',
        'state': 'Himachal Pradesh',
        'description': 'Spread across five hills with pine, oak, and deodar forests. Features Dainkund Peak, Panchpula, and Sach Pass.',
        'image_url': 'https://www.bontravelindia.com/wp-content/uploads/2021/10/Dalhousie-Himachal-Pradesh.jpg',
        'source': 'local'
    },
    'kasauli': {
        'name': 'Kasauli',
        'state': 'Himachal Pradesh',
        'description': 'Small, peaceful hill station at 1,927m with colonial-era architecture. Features Monkey Point and Christ Church.',
        'image_url': 'https://static2.tripoto.com/media/filter/tst/img/709692/TripDocument/1541062228_kasauli.jpeg',
        'source': 'local'
    },
    
    # Jharkhand
    'ranchi': {
        'name': 'Ranchi',
        'state': 'Jharkhand',
        'description': 'The City of Waterfalls - capital of Jharkhand. Known for Dassam Falls, Hundru Falls, and Birsa Zoological Park.',
        'image_url': 'https://indiashorts.com/wp-content/uploads/2023/10/Untitled-design-15.jpg',
        'source': 'local'
    },
    'deoghar': {
        'name': 'Deoghar',
        'state': 'Jharkhand',
        'description': 'Major Hindu pilgrimage town famous for Baba Baidyanath Dham, one of the 12 Jyotirlingas. Known as City of Temples.',
        'image_url': 'https://www.tripadventurer.in/wp-content/uploads/2023/12/Naulakha_Temple-deoghar-1024x524.jpg',
        'source': 'local'
    },
    'netarhat': {
        'name': 'Netarhat',
        'state': 'Jharkhand',
        'description': 'Queen of Chotanagpur - coolest hill station in Jharkhand. Stunning sunsets, forests, and waterfalls at Magnolia Point.',
        'image_url': 'https://res.cloudinary.com/triplouindia/images/w_1024,h_768,c_scale/f_auto,q_auto/v1687655730/2fed6331-f21b-42b3-a3ff-e0e5ca872e74/2fed6331-f21b-42b3-a3ff-e0e5ca872e74.jpg?_i=AA',
        'source': 'local'
    },
    
    # Karnataka
    'bangalore': {
        'name': 'Bangalore (Bengaluru)',
        'state': 'Karnataka',
        'description': 'Silicon Valley of India with IT parks, historic temples, lakes, and palaces. Features Lalbagh Garden and Bangalore Palace.',
        'image_url': 'https://www.agoda.com/wp-content/uploads/2024/01/Featured-image-The-Vidhana-Soudha-in-Bangalore.jpg',
        'source': 'local'
    },
    'mysore': {
        'name': 'Mysore',
        'state': 'Karnataka',
        'description': 'Cultural capital of Karnataka famous for palaces, temples, sandalwood, silk, and Dussehra festival. Features Mysore Palace.',
        'image_url': 'https://cdn.britannica.com/58/124658-050-28314DA4/Maharaja-Palace-Mysuru-Karnataka-India.jpg',
        'source': 'local'
    },
    'coorg': {
        'name': 'Coorg (Kodagu)',
        'state': 'Karnataka',
        'description': 'Beautiful hill district on Western Ghats famous for coffee plantations, Abbey Falls, and Golden Temple (Namdroling Monastery).',
        'image_url': 'https://www.abhibus.com/blog/wp-content/uploads/2023/04/Best-places-to-visit-in-Coorg-1536x906.jpg',
        'source': 'local'
    },
    'hampi': {
        'name': 'Hampi',
        'state': 'Karnataka',
        'description': 'UNESCO World Heritage Site with ruins of Vijayanagar Empire. Stunning stone temples including Virupaksha Temple and Stone Chariot.',
        'image_url': 'https://tse4.mm.bing.net/th/id/OIP.0CylvRGKskK6K88VjJOeiQHaFb?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    'gokarna': {
        'name': 'Gokarna',
        'state': 'Karnataka',
        'description': 'Temple town with famous beach destination. Known for Mahabaleshwar Shiva Temple and quiet beaches like Om Beach and Kudle Beach.',
        'image_url': 'https://static2.tripoto.com/media/filter/tst/img/OgData/1537153061_faacebook2_11.png',
        'source': 'local'
    },
    
    # Kerala
    'munnar': {
        'name': 'Munnar',
        'state': 'Kerala',
        'description': 'Hill paradise at 1524m in Western Ghats. Famous for tea plantations, green valleys, lakes, and waterfalls. Top honeymoon destination.',
        'image_url': 'https://www.revv.co.in/blogs/wp-content/uploads/2021/02/Munnar-HD-Image.jpg',
        'source': 'local'
    },
    'kerala backwaters': {
        'name': 'Kerala Backwaters',
        'state': 'Kerala',
        'description': 'Network of lakes, canals, rivers, and lagoons. Famous for houseboat cruises, paddy fields, and village life observation.',
        'image_url': 'https://th.bing.com/th/id/R.544b10a9cf71d3d2d57756fffdcd78e0?rik=ZYcbATTS6b11Vg&riu=http%3a%2f%2fblog.thomascook.in%2fwp-content%2fuploads%2f2014%2f01%2fAlleppey-Backwaters.jpg&ehk=173lZKChTtBcSnEE5%2bJx0mzAP2EUUPRdZ%2feHoHWVzDE%3d&risl=&pid=ImgRaw&r=0',
        'source': 'local'
    },
    'kumarakom': {
        'name': 'Kumarakom',
        'state': 'Kerala',
        'description': 'Famous bird sanctuary on Vembanad Lake - the biggest lake in Kerala. Great for boating, sunset views, and Ayurvedic massage.',
        'image_url': 'https://tse3.mm.bing.net/th/id/OIP.aHmOYWk3YatOWzBwZXvkXwAAAA?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    'thekkady': {
        'name': 'Thekkady',
        'state': 'Kerala',
        'description': 'Best place to see wildlife in Kerala with Periyar Wildlife Sanctuary. Elephants, bison, tigers, and deer with boat rides on Periyar Lake.',
        'image_url': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/09/6b/09/70/thekkady.jpg?w=1600&h=-1&s=1',
        'source': 'local'
    },
    'kovalam': {
        'name': 'Kovalam',
        'state': 'Kerala',
        'description': 'Kerala\'s most famous beach destination with three beaches - Lighthouse Beach, Hawah Beach, and Samudra Beach.',
        'image_url': 'https://th.bing.com/th/id/R.1988d1610294d3f5f7fe49a7d6acbd3a?rik=2HmQ8S0DAOoOlw&riu=http%3a%2f%2fwww.ekeralatourism.net%2fwp-content%2fuploads%2f2018%2f01%2fKovalam-Beach.jpg&ehk=JURyx4lNqhdskfNNIFtyexFhy4GHTq%2bLAPzRyDsi6Js%3d&risl=&pid=ImgRaw&r=0',
        'source': 'local'
    },
    
    # Madhya Pradesh
    'bhopal': {
        'name': 'Bhopal',
        'state': 'Madhya Pradesh',
        'description': 'The City of Lakes - capital of MP. Features Upper Lake, Bhimbetka Rock Shelters, Taj-ul-Masjid, and Van Vihar National Park.',
        'image_url': 'https://static.toiimg.com/photo/msid-26208093,width-96,height-65.cms',
        'source': 'local'
    },
    'khajuraho': {
        'name': 'Khajuraho',
        'state': 'Madhya Pradesh',
        'description': 'UNESCO World Heritage Site famous for stunning temples with Nagaro-style architecture and intricate carvings.',
        'image_url': 'https://www.tripsavvy.com/thmb/m0UXW7btnS100RvrmI35bfOYWwg=/3000x2000/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-540115304-c91172725e8143898e263a3500b19d39.jpg',
        'source': 'local'
    },
    'ujjain': {
        'name': 'Ujjain',
        'state': 'Madhya Pradesh',
        'description': 'One of seven holy Hindu pilgrimage cities, hosts Kumbh Mela. Features Mahakaleshwar Jyotirlinga and Jantar Mantar.',
        'image_url': 'https://www.adotrip.com/public/images/city/5e40fe27353d9-Ujjain%20Tours.jpg',
        'source': 'local'
    },
    'sanchi': {
        'name': 'Sanchi',
        'state': 'Madhya Pradesh',
        'description': 'UNESCO Buddhist Heritage famous for ancient stupas, monasteries, and pillars from 3rd century BC. Features Great Stupa and Ashoka Pillar.',
        'image_url': 'https://i.pinimg.com/originals/f4/8b/35/f48b358413f5bd56371885aebbd6acf7.jpg',
        'source': 'local'
    },
    'orchha': {
        'name': 'Orchha',
        'state': 'Madhya Pradesh',
        'description': 'Land of Bundela Kings with palaces, temples, and cenotaphs along Betwa River. Features Orchha Fort and Jehangir Mahal.',
        'image_url': 'https://www.lasociedadgeografica.com/blog/uploads/2018/11/que-ver-en-orchha-palacio-de-jahangir-c-makalu.jpg',
        'source': 'local'
    },
    
    # Maharashtra
    'mumbai': {
        'name': 'Mumbai',
        'state': 'Maharashtra',
        'description': 'City of Dreams and financial capital of India. Famous for Gateway of India, Marine Drive, Bollywood, and Elephanta Caves.',
        'image_url': 'https://www.mistay.in/travel-blog/content/images/2021/07/Roam-around-the-top-7-historical-monuments-of-Mumbai--Taj-Mahal-Palace-I-MiStay.jpeg',
        'source': 'local'
    },
    'pune': {
        'name': 'Pune',
        'state': 'Maharashtra',
        'description': 'Cultural capital of Maharashtra with historic forts, educational institutions, and thriving IT industry.',
        'image_url': 'https://www.tripsavvy.com/thmb/jQWlo8De0KDjeXPQd1ie-5Q7JeY=/2116x1417/filters:fill(auto,1)/GettyImages-521733846_Darkroom-125adbb08a044a2db915fefc1eb741b2.jpg',
        'source': 'local'
    },
    'Chhatrapati Sambhaji Nagar (aurangabad)': {
        'name': 'Chhatrapati Sambhaji Nagar (aurangabad)',
        'state': 'Maharashtra',
        'description': 'Heritage capital home to Ajanta & Ellora Caves. Rich Mughal and Maratha history with Bibi ka Maqbara and Daulatabad Fort.',
        'image_url': 'https://s7ap1.scene7.com/is/image/incredibleindia/ellora-caves-chhatrapati-sambhaji-nagar-maharashtra-attr-hero-5?qlt=82&ts=1727010646173',
        'source': 'local'
    },
    'mahabaleshwar': {
        'name': 'Mahabaleshwar',
        'state': 'Maharashtra',
        'description': 'Strawberry hill station with valleys and stunning viewpoints. Features Arthur\'s Seat, Venna Lake, and Mapro Garden.',
        'image_url': 'https://tse2.mm.bing.net/th/id/OIP.WYI6Fpz69kpw_RdT4kM2wwHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    'lonavala': {
        'name': 'Lonavala',
        'state': 'Maharashtra',
        'description': 'Popular hill station near Mumbai-Pune with misty hills. Features Bhushi Dam, Karla & Bhaja Caves, and Tiger\'s Leap.',
        'image_url': 'https://static.wixstatic.com/media/b4110a_ea4bea85d57a4ab4a419dc3472352f1b~mv2.jpg/v1/fill/w_1000,h_583,al_c,q_85,usm_0.66_1.00_0.01/b4110a_ea4bea85d57a4ab4a419dc3472352f1b~mv2.jpg',
        'source': 'local'
    },
    'nashik': {
        'name': 'Nashik',
        'state': 'Maharashtra',
        'description': 'Wine capital and Kumbh Mela city. Mix of temples, heritage, and vineyards with Trimbakeshwar Temple and Sula Vineyards.',
        'image_url': 'https://image3.mouthshut.com/images/imagesp/925640629s.jpg',
        'source': 'local'
    },
    
    # Manipur
    'imphal': {
        'name': 'Imphal',
        'state': 'Manipur',
        'description': 'Heart of Manipur Valley with lush valleys, forests, and lakes. Features Kangla Fort, Loktak Lake, and Keibul Lamjao National Park.',
        'image_url': 'https://www.adotrip.com/public/images/city/5c3dca6b782e2-Imphal%20Places%20to%20See.jpg',
        'source': 'local'
    },
    
    # Meghalaya
    'shillong': {
        'name': 'Shillong',
        'state': 'Meghalaya',
        'description': 'Scotland of the East - capital with rolling hills, pine forests, and waterfalls. Only hill station accessible from all sides in India.',
        'image_url': 'https://travenjo.com/wp-content/uploads/2022/06/Lyngksiar-Falls-1-gaimg.jpg?x36626',
        'source': 'local'
    },
    'cherrapunji': {
        'name': 'Cherrapunji',
        'state': 'Meghalaya',
        'description': 'One of the wettest places on earth. Famous for Living Root Bridges, Nohkalikai Falls, and Mawsmai Cave.',
        'image_url': 'https://pickyourtrail.com/blog/wp-content/uploads/2020/05/16154657975_13e70c7e0c_k.jpg',
        'source': 'local'
    },
    
    # Nagaland
    'kohima': {
        'name': 'Kohima',
        'state': 'Nagaland',
        'description': 'Historic capital at 1500m with beautiful valleys and rich Angami culture. Features Dzukou Valley and World War II Cemetery.',
        'image_url': 'https://tse4.mm.bing.net/th/id/OIP.q2eAAKLmlKd6ZP3aY8Yj4gHaD4?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    
    # Odisha
    'bhubaneswar': {
        'name': 'Bhubaneswar',
        'state': 'Odisha',
        'description': 'Temple City of India, over 2500 years old. Features Lingaraja Temple, Udayagiri Caves, and Nandankanan Zoo.',
        'image_url': 'https://www.tripsavvy.com/thmb/RZHX4AI0kzPSlVxUEVh6kBgVa1I=/3827x2551/filters:no_upscale():max_bytes(150000):strip_icc()/28739339484_ce718f7e72_o-591b0b9c5f9b58f4c0d3aeb1.jpg',
        'source': 'local'
    },
    'puri': {
        'name': 'Puri',
        'state': 'Odisha',
        'description': 'Major pilgrimage site famous for Jagannath Temple, beaches, and annual Rath Yatra. Features Chilika Lake nearby.',
        'image_url': 'https://2.bp.blogspot.com/-1oQbhOx_0B8/VtkT4MJ6RVI/AAAAAAAAIPI/if0iMBzjylA/s1600/Jagannath-Temple-FI.jpg',
        'source': 'local'
    },
    'konark': {
        'name': 'Konark',
        'state': 'Odisha',
        'description': 'Home to iconic 13th-century Sun Temple, a UNESCO World Heritage Site. Features Chandrabhaga Beach.',
        'image_url': 'https://www.worldhistory.org/uploads/images/5256.jpg',
        'source': 'local'
    },
    
    # Punjab
    'amritsar': {
        'name': 'Amritsar',
        'state': 'Punjab',
        'description': 'Home of the Golden Temple (Harmandir Sahib). Features Jallianwala Bagh, Wagah Border ceremony, and rich Sikh heritage.',
        'image_url': 'https://www.tripsavvy.com/thmb/X7JHLl_I7D8rDyPKdPm5j5rQyBs=/2122x1413/filters:fill(auto,1)/GettyImages-142737748-5af5332a642dca0037b452da.jpg',
        'source': 'local'
    },
    'chandigarh': {
        'name': 'Chandigarh',
        'state': 'Punjab/Haryana',
        'description': 'India\'s best-planned city. Features Rock Garden, Sukhna Lake, Rose Garden, and Le Corbusier architecture.',
        'image_url': 'https://www.travelholicq.com/wp-content/uploads/2018/08/Places-To-Visit-In-Chandigarh.jpg',
        'source': 'local'
    },
    
    # Rajasthan
    'jaipur': {
        'name': 'Jaipur',
        'state': 'Rajasthan',
        'description': 'The Pink City founded in 1727. Known for Amber Fort, Hawa Mahal, City Palace, Jantar Mantar, and vibrant markets.',
        'image_url': 'https://tse1.mm.bing.net/th/id/OIP.euKrP-68urIIYQJr299sdAHaEK?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    'udaipur': {
        'name': 'Udaipur',
        'state': 'Rajasthan',
        'description': 'City of Lakes founded in 1553. Famous for City Palace, Pichola Lake, Jag Mandir, and romantic beauty.',
        'image_url': 'https://www.tripsavvy.com/thmb/saxdtK__W0j14gkQ2tEjjAkEB-Y=/2121x1414/filters:fill(auto,1)/GettyImages-956035876-76efc27d14d24032a3f3d1fcefdc4413.jpg',
        'source': 'local'
    },
    'jodhpur': {
        'name': 'Jodhpur',
        'state': 'Rajasthan',
        'description': 'The Blue City near Thar Desert. Known for Mehrangarh Fort, Umaid Bhawan Palace, and blue houses.',
        'image_url': 'https://th.bing.com/th/id/R.8eaa0657fb2ab8b91c3b61a0e6da2605?rik=QxWp5sf1mk%2fuTg&riu=http%3a%2f%2fgeringerglobaltravel.com%2fwp-content%2fuploads%2f2015%2f06%2fshutterstock_87125977-1-copy.jpg&ehk=OhF0pKYD9NrBLeXXgmXAO0DcrJ6bg4E7qyvyYiTxEJU%3d&risl=1&pid=ImgRaw&r=0',
        'source': 'local'
    },
    'jaisalmer': {
        'name': 'Jaisalmer',
        'state': 'Rajasthan',
        'description': 'The Golden City with sandstone architecture and Thar Desert. Features Living Fort, Sam Sand Dunes, and havelis.',
        'image_url': 'https://www.srmholidays.in/wp-content/uploads/2022/05/5-days-Jodhpur-Jaisalmer-tour-packages.jpg',
        'source': 'local'
    },
    'pushkar': {
        'name': 'Pushkar',
        'state': 'Rajasthan',
        'description': 'Holy city with sacred Pushkar Lake. Famous for Brahma Temple, ghats, and world-famous camel fair.',
        'image_url': 'https://voyagesurmesureeninde.com/wp-content/uploads/2020/08/Pushkar-1-1140x760.jpg',
        'source': 'local'
    },
    'mount abu': {
        'name': 'Mount Abu',
        'state': 'Rajasthan',
        'description': 'Only hill station of Rajasthan in Aravalli Range. Features Dilwara Jain Temples, Nakki Lake, and Guru Shikhar.',
        'image_url': 'https://tse4.mm.bing.net/th/id/OIP.F6o18M91p0CGC0-6jhniTwHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    'ranthambore': {
        'name': 'Ranthambore',
        'state': 'Rajasthan',
        'description': 'Famous for Ranthambore National Park and tiger safaris. Features UNESCO Ranthambore Fort and wildlife.',
        'image_url': 'https://www.savaari.com/blog/wp-content/uploads/2019/09/ranthambore-national-park.jpg',
        'source': 'local'
    },
    
    # Sikkim
    'gangtok': {
        'name': 'Gangtok',
        'state': 'Sikkim',
        'description': 'Capital of Sikkim with stunning Himalayan views. Features monasteries, MG Marg, and gateway to Kanchenjunga treks.',
        'image_url': 'https://chikucab.com/blog/wp-content/uploads/2020/01/Gangtok5.jpg',
        'source': 'local'
    },
    'tsomgo lake': {
        'name': 'Tsomgo Lake',
        'state': 'Sikkim',
        'description': 'Sacred glacier lake at 3,780m. Features yak rides, frozen lake views in winter, and alpine surroundings.',
        'image_url': 'https://nanchiblog.files.wordpress.com/2020/04/tsomgo-lake-changu-lake-from-top-sikkim.jpg?w=1024',
        'source': 'local'
    },
    'nathu la': {
        'name': 'Nathu La Pass',
        'state': 'Sikkim',
        'description': 'Old Silk Route Gateway at 4,310m connecting India with Tibet. Features Indo-China border and snow-covered views.',
        'image_url': 'https://tse1.mm.bing.net/th/id/OIP.wehJNbJbfoo34BpZEZBx4wHaDl?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    
    # Tamil Nadu
    'chennai': {
        'name': 'Chennai',
        'state': 'Tamil Nadu',
        'description': 'Cultural gateway of South India. Features Marina Beach, Fort St. George, Kapaleeshwarar Temple, and rich heritage.',
        'image_url': 'https://cctravel.dk/wp-content/uploads/2019/10/2400-x-1600-9.jpg',
        'source': 'local'
    },
    'ooty': {
        'name': 'Ooty',
        'state': 'Tamil Nadu',
        'description': 'Queen of Hill Stations at 7,347 ft in Nilgiris. Known for tea estates, Botanical Garden, and UNESCO Toy Train.',
        'image_url': 'https://www.clubmahindra.com/blog/media/section_images/ultimate-o-8ac88a2da056a3d.jpg',
        'source': 'local'
    },
    'kodaikanal': {
        'name': 'Kodaikanal',
        'state': 'Tamil Nadu',
        'description': 'Princess of Hill Stations famous for cool climate, lakes, and forests. Features Kodaikanal Lake and Coaker\'s Walk.',
        'image_url': 'https://www.clubmahindra.com/blog/media/section_images/shuttersto-5b647848aeda6cf.jpg',
        'source': 'local'
    },
    'madurai': {
        'name': 'Madurai',
        'state': 'Tamil Nadu',
        'description': 'One of the oldest continuously inhabited cities. Famous for Meenakshi Amman Temple and Thirumalai Nayakkar Palace.',
        'image_url': 'https://img.freepik.com/premium-photo/night-view-meenakshi-temple_847439-22994.jpg',
        'source': 'local'
    },
    'rameshwaram': {
        'name': 'Rameshwaram',
        'state': 'Tamil Nadu',
        'description': 'Part of Char Dham linked to Ramayana. Features Ramanathaswamy Temple, Pamban Bridge, and Dhanushkodi Beach.',
        'image_url': 'https://4.bp.blogspot.com/-sYR-73_r4Ws/V_-kd4YrF2I/AAAAAAAAFb8/5QJbZGTZdIsptRgD3RbTpa0zb7hV5TUcACLcB/s1600/Rameshwaram%2BTemple%2BHD%2BPictures.jpg',
        'source': 'local'
    },
    'kanyakumari': {
        'name': 'Kanyakumari',
        'state': 'Tamil Nadu',
        'description': 'Southernmost tip of India where three seas meet. Features Vivekananda Rock Memorial and sunrise-sunset views.',
        'image_url': 'https://kanyakumaritourism.in/images/places-to-visit/headers/vivekananda-rock-memorial-kanyakumari-tourism-entry-fee-timings-holidays-reviews-header.jpg',
        'source': 'local'
    },
    
    # Telangana
    'hyderabad': {
        'name': 'Hyderabad',
        'state': 'Telangana',
        'description': 'City of Pearls and Nizams. Features Charminar, Golconda Fort, Ramoji Film City, and rich heritage.',
        'image_url': 'https://www.holidify.com/images/bgImages/HYDERABAD.jpg',
        'source': 'local'
    },
    'warangal': {
        'name': 'Warangal',
        'state': 'Telangana',
        'description': 'Historical capital of Kakatiyas. Features Thousand Pillar Temple, Warangal Fort, and UNESCO Ramappa Temple.',
        'image_url': 'https://assets.traveltriangle.com/blog/wp-content/uploads/2018/05/sri-v-temple.jpg',
        'source': 'local'
    },
    
    # Uttar Pradesh
    'agra': {
        'name': 'Agra',
        'state': 'Uttar Pradesh',
        'description': 'Home to iconic Taj Mahal, one of Seven Wonders. Also features Agra Fort, Fatehpur Sikri, and Mughal heritage.',
        'image_url': 'https://tse1.mm.bing.net/th/id/OIP.yQV9YN97q7-pD-MDLHFaJAHaEK?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    'lucknow': {
        'name': 'Lucknow',
        'state': 'Uttar Pradesh',
        'description': 'City of Nawabs famous for nawabi culture, cuisine, and architecture. Features Bara Imambara and Rumi Darwaza.',
        'image_url': 'https://www.treebo.com/blog/wp-content/uploads/2017/05/Places-to-Visit-in-Lucknow.jpg',
        'source': 'local'
    },
    'varanasi': {
        'name': 'Varanasi',
        'state': 'Uttar Pradesh',
        'description': 'Spiritual capital of India, one of world\'s oldest living cities. Famous for Ganges ghats and Kashi Vishwanath Temple.',
        'image_url': 'https://fthmb.tqn.com/FP6jyvdwWsCJg0s-z7oB-3EB8P8=/2124x1413/filters:fill(auto,1)/455239385-56a3bf985f9b58b7d0d3965d.jpg',
        'source': 'local'
    },
    'prayagraj': {
        'name': 'Prayagraj (Allahabad)',
        'state': 'Uttar Pradesh',
        'description': 'One of holiest cities at Triveni Sangam - meeting point of Ganga, Yamuna, and mythical Saraswati rivers.',
        'image_url': 'https://www.adotrip.com/public/images/events/5c5d27851db3d-Prayagraj%20kumbh%20mela%20Trip.jpg',
        'source': 'local'
    },
    'sarnath': {
        'name': 'Sarnath',
        'state': 'Uttar Pradesh',
        'description': 'Where Lord Buddha delivered his first sermon. Major Buddhist pilgrimage with Dhamek Stupa and deer park.',
        'image_url': 'https://www.tripsavvy.com/thmb/7qzOzf0uxgWftXpuTKguvLjJ6KE=/2121x1414/filters:fill(auto,1)/GettyImages-11277274181-f11cfdb1a6514121aa39eea112917faf.jpg',
        'source': 'local'
    },
    'ayodhya': {
        'name': 'Ayodhya',
        'state': 'Uttar Pradesh',
        'description': 'Birthplace of Lord Rama, one of Hinduism\'s most sacred cities. Features Ram Janmabhoomi Temple and Hanuman Garhi.',
        'image_url': 'https://thefederal.com/h-upload/2024/02/21/519937-ram-temple-ayodhya.webp',
        'source': 'local'
    },
    'vrindavan': {
        'name': 'Vrindavan',
        'state': 'Uttar Pradesh',
        'description': 'Land of Lord Krishna\'s childhood filled with ancient temples. Features Banke Bihari Temple and ISKCON Temple.',
        'image_url': 'https://www.adotrip.com/public/images/city/master_images/5e3d3c434964b-Vrindavan_Attractions.jpg',
        'source': 'local'
    },
    'mathura': {
        'name': 'Mathura',
        'state': 'Uttar Pradesh',
        'description': 'Birthplace of Lord Krishna, one of seven holiest Hindu cities. Features Krishna Janmabhoomi and Dwarkadhish Temple.',
        'image_url': 'https://assets.cntraveller.in/photos/62219e5f5934c6bf974e2a69/16:9/w_1280,c_limit/mathura%20lead%20(1).jpg',
        'source': 'local'
    },
    
    # Uttarakhand
    'dehradun': {
        'name': 'Dehradun',
        'state': 'Uttarakhand',
        'description': 'Capital of Uttarakhand between Ganges and Yamuna. Features Robber\'s Cave, FRI, and Rajaji National Park.',
        'image_url': 'https://th.bing.com/th/id/R.0353217e75605e4cff5a24b906c3f12d?rik=e99SX1JoddluNw&riu=http%3a%2f%2fwww.countryholidaysinnsuites.co.in%2fwp-content%2fuploads%2f2018%2f11%2fdehradun-getty-720x540.jpg&ehk=eIjAv2lRTw2egzXgz1%2bE%2fm3sC5PaqngiPJIb4bYDk%2fY%3d&risl=&pid=ImgRaw&r=0',
        'source': 'local'
    },
    'rishikesh': {
        'name': 'Rishikesh',
        'state': 'Uttarakhand',
        'description': 'Yoga Capital of the World at Ganga confluence. Known for Laxman Jhula, rafting, bungee jumping, and spiritual retreats.',
        'image_url': 'https://tse2.mm.bing.net/th/id/OIP.pEpXeqWpd7TyQQkT1YeDtQHaE8?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    'mussoorie': {
        'name': 'Mussoorie',
        'state': 'Uttarakhand',
        'description': 'Queen of Hills at 6000 ft with scenic hills and colonial charm. Features Kempty Falls, Gun Hill, and Mall Road.',
        'image_url': 'https://kanatalheights.com/wp-content/uploads/2021/03/mussorroe.jpg',
        'source': 'local'
    },
    'nainital': {
        'name': 'Nainital',
        'state': 'Uttarakhand',
        'description': 'Lake District of India around iconic Naini Lake. Features Naina Peak, Snow View Point, and Nainital Zoo.',
        'image_url': 'https://tse1.mm.bing.net/th/id/OIP.5VUkSIviLdpJB_w2c3eomAHaEP?rs=1&pid=ImgDetMain&o=7&rm=3',
        'source': 'local'
    },
    'haridwar': {
        'name': 'Haridwar',
        'state': 'Uttarakhand',
        'description': 'Gateway to the Gods, holy city for Kumbh Mela. Features Har Ki Pauri, Mansa Devi Temple, and Ganga aarti.',
        'image_url': 'https://th.bing.com/th/id/R.846f4b0a5c43b19b4a2ef7376375bd0c?rik=wQAQiFktLLwDwQ&riu=http%3a%2f%2f4.bp.blogspot.com%2f-jhfbMKRGP50%2fTah-MnK7QVI%2fAAAAAAAAALs%2fmDi3HS2VPEA%2fs1600%2fharidwar%252Btempleof%252Bindia%252Bpictures%252Bdownload.jpg&ehk=Sz0L%2bMTzI%2bRGNMhwA8mLTO4jwSYcVq3LmhAoLngBtWM%3d&risl=&pid=ImgRaw&r=0',
        'source': 'local'
    },
    'kedarnath': {
        'name': 'Kedarnath',
        'state': 'Uttarakhand',
        'description': 'One of holiest Hindu pilgrimage sites in Garhwal Himalayas. Features Kedarnath Temple and Vasuki Tal.',
        'image_url': 'https://th.bing.com/th/id/R.1b126549d821cb66b1095e71d4fae908?rik=PDd%2fAgPLQaGSjw&riu=http%3a%2f%2fwww.allgudthings.com%2fwp-content%2fuploads%2f2019%2f05%2fKedarnath-Temple-Front..jpg&ehk=dFldvCD5G7KvGeFRhlc1FR54vq8BLNt28DDAgDsSrw4%3d&risl=&pid=ImgRaw&r=0',
        'source': 'local'
    },
    'badrinath': {
        'name': 'Badrinath',
        'state': 'Uttarakhand',
        'description': 'Sacred shrine of Lord Vishnu, one of Char Dhams. Features Badrinath Temple and Tapt Kund hot springs.',
        'image_url': 'https://www.holidify.com/images/cmsuploads/compressed/EntranceofthebeautifulBadrinathTemple1_20191224124938_20191224125002.jpg',
        'source': 'local'
    },
    'auli': {
        'name': 'Auli',
        'state': 'Uttarakhand',
        'description': 'Skiing destination with panoramic Himalayan views. Features cable car, meadows, and adventure sports.',
        'image_url': 'https://assets-news.housing.com/news/wp-content/uploads/2022/08/17000902/AULI-FEATURE-compressed.jpg',
        'source': 'local'
    },
    
    # West Bengal
    'kolkata': {
        'name': 'Kolkata',
        'state': 'West Bengal',
        'description': 'Cultural Capital of India with rich history and colonial architecture. Features Victoria Memorial and Howrah Bridge.',
        'image_url': 'https://www.lasociedadgeografica.com/blog/uploads/2016/11/que-ver-en-calcuta-victoria-memorial-e292b8wikipedia-commons.jpg',
        'source': 'local'
    },
    'darjeeling': {
        'name': 'Darjeeling',
        'state': 'West Bengal',
        'description': 'Queen of the Hills with tea gardens and Kangchenjunga views. Features Tiger Hill, Toy Train, and Peace Pagoda.',
        'image_url': 'https://www.holidaymonk.com/wp-content/uploads/2021/07/Darjeeling.jpg',
        'source': 'local'
    },
    'kalimpong': {
        'name': 'Kalimpong',
        'state': 'West Bengal',
        'description': 'Quiet Himalayan retreat known for orchids, nurseries, and Buddhist monasteries. Features Deolo Hill views.',
        'image_url': 'https://voiceofadventure.com/wp-content/uploads/2022/06/Kalimpong-1.jpg',
        'source': 'local'
    },
    'sundarbans': {
        'name': 'Sundarbans',
        'state': 'West Bengal',
        'description': 'UNESCO World Heritage mangrove forest, home to Royal Bengal Tigers. Best explored by boat safari.',
        'image_url': 'https://uploads-ssl.webflow.com/6094741aba31b56efe984fb1/60ae1baac0ebd54a76a891ab_DJI_0068.jpg',
        'source': 'local'
    },
    
    # Andaman and Nicobar Islands
    'port blair': {
        'name': 'Port Blair',
        'state': 'Andaman and Nicobar Islands',
        'description': 'Capital with Cellular Jail (Kala Pani), India\'s most iconic freedom-struggle landmark. Features light and sound show.',
        'image_url': 'https://www.oyorooms.com/travel-guide/wp-content/uploads/2019/04/Ross-Island.webp',
        'source': 'local'
    },
    'havelock island': {
        'name': 'Havelock Island',
        'state': 'Andaman and Nicobar Islands',
        'description': 'Home to Radhanagar Beach, declared Asia\'s Best Beach. Crystal-clear turquoise water and scuba diving.',
        'image_url': 'https://lp-cms-production.imgix.net/2019-06/GettyImages-526836625_medium.jpg?sharp=10&vib=20&w=1200&auto=compress&fit=crop&fm=auto&h=800',
        'source': 'local'
    },
    
    # Delhi
    'delhi': {
        'name': 'Delhi',
        'state': 'Delhi',
        'description': 'India\'s capital blending ancient history with modern life. Features Red Fort, India Gate, Qutub Minar, and Lotus Temple.',
        'image_url': 'https://delhimessenger.in/wp-content/uploads/2023/03/Collage-Maker-18-Mar-2023-11-12-AM-9321.jpg',
        'source': 'local'
    },
    
    # Puducherry
    'puducherry': {
        'name': 'Puducherry',
        'state': 'Puducherry',
        'description': 'French colonial heritage with Auroville and Sri Aurobindo Ashram. Features Promenade Beach and spiritual retreats.',
        'image_url': 'https://pondicherrytourism.co.in/images/places-to-visit/header/immaculate-conception-cathedral-puducherry-entry-fee-timings-holidays-reviews-header.jpg',
        'source': 'local'
    },
    'auroville': {
        'name': 'Auroville',
        'state': 'Puducherry',
        'description': 'Experimental universal township - City of Dawn. Features Matrimandir golden meditation center and international community.',
        'image_url': 'https://media.cntraveller.in/wp-content/uploads/2018/02/Auroville.jpg',
        'source': 'local'
    },
    
    # Ladakh
    'leh': {
        'name': 'Leh',
        'state': 'Ladakh',
        'description': 'High-altitude desert town with Buddhist monasteries. Features Leh Palace, Shanti Stupa, and gateway to Ladakh adventures.',
        'image_url': 'https://www.tripsavvy.com/thmb/wUwZ5Jhn8IvUElV22GYYl-93APQ=/950x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-166815386-3421ad5bc2e948eea121c1b5824cb792.jpg',
        'source': 'local'
    },
    'pangong lake': {
        'name': 'Pangong Lake',
        'state': 'Ladakh',
        'description': 'High-altitude lake famous for changing colors. Featured in 3 Idiots movie. Stunning Himalayan backdrop.',
        'image_url': 'https://www.tripsavvy.com/thmb/8QDjDX-6m24g46gKeEJEK78G_Vg=/2121x1414/filters:fill(auto,1)/GettyImages-929581480-5b437b9b46e0fb0037899d82.jpg',
        'source': 'local'
    },
    'nubra valley': {
        'name': 'Nubra Valley',
        'state': 'Ladakh',
        'description': 'Cold desert valley with sand dunes and double-humped camels. Features Diskit Monastery and Khardung La pass.',
        'image_url': 'https://devilonwheels.com/wp-content/uploads/2014/10/258.jpg',
        'source': 'local'
    },
    
    # Jammu & Kashmir
    'srinagar': {
        'name': 'Srinagar',
        'state': 'Jammu & Kashmir',
        'description': 'Summer capital with Dal Lake houseboats and Mughal gardens. Features Shikara rides and Shankaracharya Temple.',
        'image_url': 'https://voiceofguides.com/wp-content/uploads/2021/05/Srinagar-raisa-nastukova-unsplash-1024x683.jpg',
        'source': 'local'
    },
    'gulmarg': {
        'name': 'Gulmarg',
        'state': 'Jammu & Kashmir',
        'description': 'Meadow of Flowers and skiing paradise. Features Asia\'s highest gondola and stunning mountain views.',
        'image_url': 'https://wallpaperaccess.com/full/9470510.jpg',
        'source': 'local'
    },
    'pahalgam': {
        'name': 'Pahalgam',
        'state': 'Jammu & Kashmir',
        'description': 'Valley of Shepherds and base for Amarnath Yatra. Features Betaab Valley and Lidder River.',
        'image_url': 'https://www.vibrantfootsteps.com/wp-content/uploads/2023/06/20230602_072849-PS-scaled.jpg',
        'source': 'local'
    },
}


# Helper functions
def get_user():
    """Get current logged in user"""
    email = session.get('user_email')
    if email and email in users:
        return users[email]
    return None


def login_required(f):
    """Decorator for routes that require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not get_user():
            flash('Please login to access this page.', 'error')
            return redirect(url_for('index', section='login'))
        return f(*args, **kwargs)
    return decorated_function


def admin_required(f):
    """Decorator for routes that require admin"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = get_user()
        if not user or not user.get('is_admin'):
            flash('Admin access required.', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


def get_level_info(points):
    """Calculate level based on points"""
    if points >= 300:
        return 'Globe Trotter', 300, None, 0, 100
    elif points >= 150:
        return 'Frequent Explorer', 150, 300, points - 150, (points - 150) / 150 * 100
    elif points >= 50:
        return 'Rookie Traveler', 50, 150, points - 50, (points - 50) / 100 * 100
    else:
        return 'Newbie', 0, 50, points, points / 50 * 100


def search_google_places(query):
    """Search Google Places API for destination info"""
    if not GOOGLE_PLACES_API_KEY:
        return None
    
    try:
        search_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
        params = {
            'query': f'{query} India tourist destination',
            'key': GOOGLE_PLACES_API_KEY
        }
        response = requests.get(search_url, params=params)
        data = response.json()
        
        if data.get('status') == 'OK' and data.get('results'):
            place = data['results'][0]
            
            image_url = f'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600'
            if place.get('photos'):
                photo_ref = place['photos'][0]['photo_reference']
                image_url = f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=600&photoreference={photo_ref}&key={GOOGLE_PLACES_API_KEY}'
            
            description_parts = []
            if place.get('formatted_address'):
                description_parts.append(place['formatted_address'])
            if place.get('rating'):
                description_parts.append(f"Rating: {place['rating']}/5")
            
            return {
                'name': place.get('name', query.title()),
                'state': 'External',
                'description': ' | '.join(description_parts) if description_parts else f'Discover the beauty of {query.title()}',
                'image_url': image_url,
                'source': 'google'
            }
    except Exception as e:
        print(f"Google Places API error: {e}")
    
    return None


def get_all_states():
    """Get sorted list of all unique states"""
    states = set()
    for dest in destinations.values():
        if dest.get('state') and dest['state'] != 'External':
            states.add(dest['state'])
    return sorted(list(states))


@app.route('/')
def index():
    """Main page - serves the single page application"""
    search_query = request.args.get('search', '').strip()
    section = request.args.get('section', 'home')
    search_result = None
    
    if search_query:
        key = search_query.lower()
        if key in destinations:
            search_result = destinations[key]
        else:
            for dest_key, dest in destinations.items():
                if key in dest_key or key in dest['name'].lower():
                    search_result = dest
                    break
        
        if not search_result:
            google_result = search_google_places(search_query)
            if google_result:
                destinations[search_query.lower()] = google_result
                search_result = google_result
    
    current_user = get_user()
    user_bookings = []
    points = 0
    level_name = 'Newbie'
    level_max = 50
    points_to_next = 50
    progress = 0
    token = request.args.get('token')
    
    if current_user:
        user_bookings = [b for b in bookings if b['user_email'] == current_user['email']]
        points = current_user.get('reward_points', 0)
        level_name, _, level_max_val, points_diff, progress = get_level_info(points)
        level_max = level_max_val if level_max_val is not None else points
        points_to_next = level_max - points
    
    return render_template('index.html',
                           current_user=current_user,
                           destinations=destinations,
                           states=get_all_states(),
                           search_query=search_query,
                           search_result=search_result,
                           user_bookings=user_bookings,
                           all_bookings=bookings,
                           users=users,
                           points=points,
                           level_name=level_name,
                           level_max=level_max,
                           points_to_next=points_to_next,
                           progress=progress,
                           section=section,
                           token=token)


@app.route('/login', methods=['POST'])
def login():
    """Login route"""
    email = request.form.get('email', '').strip().lower()
    password = request.form.get('password', '')
    
    if email in users and check_password_hash(users[email]['password'], password):
        session['user_email'] = email
        flash('Welcome back!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Invalid email or password.', 'error')
        return redirect(url_for('index', section='login'))


@app.route('/signup', methods=['POST'])
def signup():
    """Signup route"""
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip().lower()
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')
    
    if not name or not email or not password:
        flash('All fields are required.', 'error')
        return redirect(url_for('index', section='signup'))
    
    if password != confirm_password:
        flash('Passwords do not match.', 'error')
        return redirect(url_for('index', section='signup'))
    
    if len(password) < 6:
        flash('Password must be at least 6 characters.', 'error')
        return redirect(url_for('index', section='signup'))
    
    if email in users:
        flash('Email already registered.', 'error')
        return redirect(url_for('index', section='signup'))
    
    users[email] = {
        'name': name,
        'email': email,
        'password': generate_password_hash(password),
        'is_admin': email == 'admin@travelsmart.com',
        'reward_points': 0,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    
    session['user_email'] = email
    flash('Account created successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    """Logout route"""
    session.pop('user_email', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))


@app.route('/save-booking', methods=['POST'])
@login_required
def save_booking():
    """Save a new booking"""
    user = get_user()
    
    booking_type = request.form.get('booking_type', '')
    destination = request.form.get('destination', '').strip()
    travel_date = request.form.get('travel_date', '')
    
    if not booking_type or not destination or not travel_date:
        flash('All fields are required.', 'error')
        return redirect(url_for('index', section='bookings'))
    
    booking = {
        'id': str(uuid.uuid4())[:8].upper(),
        'user_email': user['email'],
        'booking_type': booking_type,
        'destination': destination,
        'travel_date': travel_date,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    bookings.append(booking)
    
    users[user['email']]['reward_points'] += 50
    
    flash(f'Booking saved! You earned 50 points.', 'success')
    return redirect(url_for('index', section='bookings'))


@app.route('/api/search')
def api_search():
    """API endpoint for destination search"""
    query = request.args.get('q', '').strip().lower()
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    
    if query in destinations:
        return jsonify(destinations[query])
    
    for dest_key, dest in destinations.items():
        if query in dest_key or query in dest['name'].lower():
            return jsonify(dest)
    
    google_result = search_google_places(query)
    if google_result:
        destinations[query] = google_result
        return jsonify(google_result)
    
    return jsonify({'error': 'Destination not found'}), 404

# -----------------------------------------------
# --- FORGOT PASSWORD ROUTES ---
# -----------------------------------------------

@app.route('/forgot', methods=['GET', 'POST'])
def forgot_password():
    """
    Handles displaying the forgotten password form (GET) 
    and processing the request to send the reset link (POST).
    """
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        
        if email not in users:
            # Generic success message for security to prevent email enumeration
            flash('If an account exists with that email, a password reset link has been sent.', 'info')
            return redirect(url_for('index', section='login'))

        # 1. Generate Token
        token = s.dumps(email, salt='password-reset-salt')
        
        # 2. Build Reset Link
        reset_url = url_for('reset_password', token=token, _external=True)
        
        # 3. Send Email
        try:
            msg = Message(
                subject="Password Reset Request for TravelSmart",
                recipients=[email],
                body=f"Hello,\n\n"
                     f"You have requested a password reset for your TravelSmart account. "
                     f"Please click on the link below to reset your password:\n\n"
                     f"{reset_url}\n\n"
                     f"This link will expire in {PASSWORD_RESET_TIMEOUT/60} minutes.\n\n"
                     f"If you did not request a password reset, please ignore this email."
            )
            mail.send(msg)
            flash('A password reset link has been sent to your email.', 'success')
        except Exception as e:
            print(f"SMTP Error: {e}")
            flash(f'Error sending email. Please check the MAIL_USERNAME and MAIL_PASSWORD configuration.', 'error')
        
        return redirect(url_for('index', section='login'))
    
    # If GET, redirect to the index page to display the 'forgot' section form
    return redirect(url_for('index', section='forgot'))


@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """
    Validates the token and allows the user to set a new password.
    """
    try:
        # 1. Validate and load email from token
        email = s.loads(
            token,
            salt='password-reset-salt',
            max_age=PASSWORD_RESET_TIMEOUT
        )
    except SignatureExpired:
        flash('The password reset link has expired.', 'error')
        return redirect(url_for('index', section='forgot'))
    except Exception:
        flash('The password reset link is invalid or corrupted.', 'error')
        return redirect(url_for('index', section='forgot'))
    
    if email not in users:
        flash('User account not found.', 'error')
        return redirect(url_for('index', section='forgot'))

    if request.method == 'POST':
        new_password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not new_password or not confirm_password:
            flash('All password fields are required.', 'error')
            return redirect(url_for('reset_password', token=token))
            
        if new_password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('reset_password', token=token))
        
        if len(new_password) < 6:
            flash('Password must be at least 6 characters.', 'error')
            return redirect(url_for('reset_password', token=token))

        # 2. Update Password
        users[email]['password'] = generate_password_hash(new_password)
        flash('Your password has been successfully reset! Please log in.', 'success')
        return redirect(url_for('index', section='login'))

    # If GET request, render the index with the 'reset' section view and pass the decoded email
    return render_template('index.html', 
                           section='reset', 
                           token=token, 
                           email=email,
                           # Pass minimal context data needed for index.html structure
                           current_user=get_user(),
                           destinations=destinations,
                           states=get_all_states(),
                           search_query="",
                           user_bookings=[],
                           all_bookings=bookings,
                           users=users) 

# --- SOCIAL LOGIN ROUTES ---

@app.route('/login/<provider>')
def social_login(provider):
    """Redirects user to the social provider"""
    if provider not in ['google', 'microsoft', 'facebook']:
        flash('Provider not supported', 'error')
        return redirect(url_for('index', section='login'))
    
    # Create the redirect URI (e.g., http://localhost:5000/auth/google/callback)
    redirect_uri = url_for('auth_callback', provider=provider, _external=True)
    return getattr(oauth, provider).authorize_redirect(redirect_uri)


@app.route('/auth/<provider>/callback')
def auth_callback(provider):
    """Handles the return from the provider"""
    try:
        client = getattr(oauth, provider)
        token = client.authorize_access_token()
        
        user_info = None
        email = None
        name = None

        # Extract user info based on provider
        if provider == 'google':
            user_info = token.get('userinfo')
            email = user_info.get('email')
            name = user_info.get('name')
            
        elif provider == 'microsoft':
            user_info = token.get('userinfo')
            # Fallback if userinfo is empty (sometimes happens with MS Graph)
            if not user_info:
                resp = client.get('https://graph.microsoft.com/v1.0/me')
                user_info = resp.json()
            email = user_info.get('email') or user_info.get('userPrincipalName')
            name = user_info.get('displayName')

        elif provider == 'facebook':
            # Facebook Graph API call
            resp = client.get('me?fields=id,name,email,picture')
            user_info = resp.json()
            email = user_info.get('email')
            name = user_info.get('name')

        if not email:
            flash(f'Could not retrieve email from {provider}.', 'error')
            return redirect(url_for('index', section='login'))

        # --- DATABASE LOGIC ---
        # Check if user exists, if not, create them
        if email not in users:
            # Create a passwordless user (or random password)
            users[email] = {
                'name': name,
                'email': email,
                'password': generate_password_hash(str(uuid.uuid4())), # Random secure password
                'is_admin': False,
                'reward_points': 0,
                'provider': provider, # Track which provider they used
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
            }
        
        # Log the user in
        session['user_email'] = email
        flash(f'Successfully logged in with {provider.capitalize()}!', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        print(f"OAuth Error: {e}")
        flash('Authentication failed. Please try again.', 'error')
        return redirect(url_for('index', section='login'))


if __name__ == '__main__':
    # Add a default admin user for testing
    if 'admin@travelsmart.com' not in users:
        users['admin@travelsmart.com'] = {
            'name': 'Admin User',
            'email': 'admin@travelsmart.com',
            'password': generate_password_hash('password'), # Default password 'password'
            'is_admin': True,
            'reward_points': 500,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
    app.run(debug=True)