# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# | 
# | Module   : Calling processing data functions here
# | Creator  : Xiao Ling
# | Date     : 8/4/2016
# |             
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


from __future__ import print_function
from __future__ import unicode_literals

import json

from preprocess_data import yelp
from preprocess_data import scrub
from preprocess_data import doYelp
from preprocess_data import toUnicode


import os.path


# ---------------------------------------------------------------------------------------------------
#   Load data per yelp example
# ---------------------------------------------------------------------------------------------------


# @Use: change `inPath` to path where your [yelp_academic_dataset_review.json] data is
inPath = '/Users/lingxiao/Desktop/NLP/Code/Papers/HAN/assets/review_short.json'
# doYelp(inPath, 'outX', 'outy')

# ---------------------------------------------------------------------------------------------------
#   refactor
# ---------------------------------------------------------------------------------------------------


xs1 = u'{"votes": {"funny": 0, "useful": 0, "cool": 0}, "user_id": "PUFPaY9KxDAcGqfsorJp3Q", "review_id": "Ya85v4eqdd6k9Od8HbQjyA", "stars": 4, "date": "2012-08-01", "text": "Mr Hoagie is an institution. Walking in, it does seem like a throwback to 30 years ago, old fashioned menu board, booths out of the 70s, and a large selection of food. Their speciality is the Italian Hoagie, and it is voted the best in the area year after year. I usually order the burger, while the patties are obviously cooked from frozen, all of the other ingredients are very fresh. Overall, its a good alternative to Subway, which is down the road.", "type": "review", "business_id": "5UmKMjUEUNdYWqANhGckJw"}'
xs2 = u'{"votes": {"funny": 0, "useful": 0, "cool": 0}, "user_id": "PUFPaY9KxDAcGqfsorJp3Q", "review_id": "Ya85v4eqdd6k9Od8HbQjyA", "starss": 4, "date": "2012-08-01", "texts": "Mr Hoagie is an institution. Walking in, it does seem like a throwback to 30 years ago, old fashioned menu board, booths out of the 70s, and a large selection of food. Their speciality is the Italian Hoagie, and it is voted the best in the area year after year. I usually order the burger, while the patties are obviously cooked from frozen, all of the other ingredients are very fresh. Overall, its a good alternative to Subway, which is down the road.", "type": "review", "business_id": "5UmKMjUEUNdYWqANhGckJw"}'
# xs = toUnicode (xs)
# xs = json.loads(xs)      

# if xs.get('text') and xs.get('stars'):
#     X  = scrub    (xs    ['text' ] )
#     y  = toUnicode(str(xs['stars']))









