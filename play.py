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

from preprocess_data import doYelp
from preprocess_data import doIMDB


# ---------------------------------------------------------------------------------------------------
#   Load data and scrub
# ---------------------------------------------------------------------------------------------------


# @Use: change `inPath` to path where your [yelp_academic_dataset_review.json] data is
yelp_path  = '/Users/lingxiao/Desktop/NLP/Code/Papers/HAN/assets/yelp_review_short.json'
imdb_path  = '/Users/lingxiao/Desktop/NLP/Code/Papers/HAN/assets/imdb_words_short.txt'
imdb_train = '/Users/lingxiao/Desktop/NLP/Code/Papers/HAN/assets/imdb_train_words.txt'
imdb_test  = '/Users/lingxiao/Desktop/NLP/Code/Papers/HAN/assets/imdb_test_words.txt'


doIMDB(imdb_train, 'imdb_train_words_clean')
doIMDB(imdb_test , 'imdb_test_words_clean' )


