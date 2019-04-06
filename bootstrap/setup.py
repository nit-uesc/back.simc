import os
import sys

if not os.path.exists('public'):
    os.makedirs('public')

if not os.path.exists('public/json'):
    os.makedirs('public/json')

if not os.path.exists('public/xml'):
    os.makedirs('public/xml')

if not os.path.exists('public/thumbs-70x70'):
    os.makedirs('public/thumbs-70x70')
 
if not os.path.exists('public/thumbs-150x150'):
    os.makedirs('public/thumbs-150x150')

# if not os.path.exists('src/processed_data/corpus'):
#     os.makedirs('src/processed_data/corpus')
#
# if not os.path.exists('src/processed_data/summary'):
#     os.makedirs('src/processed_data/summary')
