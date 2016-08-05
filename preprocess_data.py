# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# | 
# | Module  : A libarry to pre-process text data
# | Author  : Xiao Ling
# | Date    : 8/4/2016
# |             
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


from __future__ import print_function
from __future__ import unicode_literals


import re
import json
import os.path
from twokenize_py import Tokenizer


# todo: is there an overhead with this?
tok  = Tokenizer()

# ---------------------------------------------------------------------------------------------------
#   Some common cleaning routines (effectful) 
# ---------------------------------------------------------------------------------------------------

# @Use: Given valid file path `inFile` and output file names
#       `outX` for the set of regressors and `outy` for set of regressands,
#       clean and write yelp reviews and stars according to subroutine `yelp`.

# doYelp :: String -> String -> String -> ReaderT _ IO Bool
def doYelp (inPath, outX, outy):
    goXy (yelp, inPath, outX, outy)

# ---------------------------------------------------------------------------------------------------
#   Same common clean routines as above but effect-free
# ---------------------------------------------------------------------------------------------------

# @Use: Given a line of JSON object in string from `xs`
#       so that `xs` has field `text` and `stars`, pull out and scrub the 
#       `text` as X and `stars` as y, return a tuple.

# yelp :: String -> (Unicode, Unicode)
def yelp (xs):
    xs = toUnicode (xs)
    xs = json.loads(xs)      
    X  = scrub     (xs['text'])
    y  = str(xs['stars']).decode('utf-8')
    return (X,y)


# @Use: core process words logic:
#       1. remove white space
#       2. all lower case
#       3. make all numbers in <NUM>
#       4. tokenize according to tworkenize

# scrub :: String -> Unicode
def scrub (xs):

    xs  = toUnicode(xs)

    xs  = xs.strip().lower() 
    xs  = re.sub(" \d+", '<NUM> ', xs)   # todo: ask neville if this regex is kosher
    ys  = tok.tokenize(xs)                   
    ys  = ' '.join(ys)              
    ys  = ys.encode('utf-8')

    return ys

# ---------------------------------------------------------------------------------------------------
#   Main IO loops to read, scrub, and write to disk
# ---------------------------------------------------------------------------------------------------

# @Use: iterate over a file and extract and `clean` the `X` to be saved in file named `outX`
#       and `y` to be saved in file named `outy`
#       return true if input directory specified in `inPath` is valid, false otherwise

# goXy :: (string -> (Unicode, Unicode)) 
#         -> String -> String -> String 
#         -> ReaderT _ IO Bool
def goXy (clean, inPath, outX, outy)
    if os.path.isfile(inPath):
        with open(inPath) as xss, open(outX, mode = 'wb') as Xs, open(outy, mode = 'wb') as ys:
            for xs in xss :
                o = clean(xs)
                Xs.write(o[0])
                Xs.write('\n')
                ys.write(o[1])
                ys.write('\n')
        return True
    else:
        return False


# ---------------------------------------------------------------------------------------------------
#   Utils
# ---------------------------------------------------------------------------------------------------


# @Use: given `xs` of arbitrary type, convert it to unicode
# TOOD: honor the forall quantifier so that it's not a wat??
# toUnicode :: forall a. a -> Unicode
def toUnicode (xs):
    if isinstance(xs, str):
        xs = xs.decode('utf-8')
        return xs
    if isinstance(xs, unicode):
        return xs
    else:
        return str(xs).decode('utf-8')    # wat??      

# ---------------------------------------------------------------------------------------------------
#   To be depricated
#   These functions will be depricated by end of day 8/5/2016
# ---------------------------------------------------------------------------------------------------

# Given valid file path `inFile` and output file name 'outName'
# read in file `xss` and `scrub` it, then write `yys` to disk

# doIMDB :: String -> String -> ReaderT _ IO Bool
def doIMDB (inPath, outX): 
    goX (scrub, inPath, outX)


# todo: get rid of this. do you need this ever?
# Given valid file path `inFile` and output file name 'outName' 
# and normalizing/tokenizing routine `clean`, 
# read in file `xss` and `scrub` it, then write `yys` to local directory
# return [True] if succssful, [False] otherwise

# goX :: (string -> Unicode) -> String -> String -> ReaderT _ IO Bool
def goX (clean, inPath, outName):

    if os.path.isfile(inPath):

        with open (inPath) as xss , open(outName, mode = 'wb') as yys :
            for xs in xss : 
                ys = clean(xs)
                yys.write(ys)
                yys.write('\n')
        return True

    else:
        return False       











