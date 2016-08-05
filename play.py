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

from preprocess_data import toUnicode
from preprocess_data import scrub
from preprocess_data import yelp
from preprocess_data import doYelp


# ---------------------------------------------------------------------------------------------------
#   Load data per yelp example
# ---------------------------------------------------------------------------------------------------


# @Use: change `inPath` to path where your [yelp_academic_dataset_review.json] data is
inPath = ''
doYelp(inPath, 'outX', 'outy')

