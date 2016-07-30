#!/usr/bin/python

import sys

debug = True

bag_of_words = sys.argv[1]
features_file = sys.argv[2]

resume_words = dict()
resume_features = dict()

with open(bag_of_words) as f:
    content = f.readlines()
for line in content:
    parts = line.rsplit()
    if len(parts) > 1:
        resume_words[parts[0]] = int(parts[1])

with open(features_file) as f:
    content = f.readlines()
for line in content:
    parts = line.split()
    if len(parts) > 1:
        resume_features[parts[0]] = parts[1]


features_score = 0.0
bag_of_words_score = 0.0

# compute features score
if "gpa" in resume_features:
    if "max_gpa" in resume_features:
        max_gpa = float(resume_features["max_gpa"])
    else:
        max_gpa = 4.0
    gpa = float(resume_features["gpa"])
    gpa_bonus = gpa/max_gpa*100
    features_score += gpa_bonus


# compute bag of words score
word_bonuses = {'stanford': 10, 
                'mit': 10,
                'c++': 2,
                'java': 2,
                'compilers': 2,
                'architecture': 1,
                'optimization': 3,
                'databases': 1,
                'linux': 2,
                'windows': -5,
                'senior': 2,
                'principle': 3,
                'contractor': -2,
                'awards': 3,
                'prizes': 3,
                'honors': 3,
                'valadictorian': 10
                }

total_word_bonus=0.0
for word in word_bonuses:
    if word_bonuses[word]>0:
        total_word_bonus+=word_bonuses[word]

for word in word_bonuses:
    if word in resume_words:
        bag_of_words_score += word_bonuses[word]
        if debug == True:
            print "bonus for", word, "is", word_bonuses[word]
        
bag_of_words_score /= total_word_bonus
bag_of_words_score *= 100

print "bag_of_word_score:", bag_of_words_score
print "features score:", features_score
print "combined score:", (bag_of_words_score+features_score)/2

    

