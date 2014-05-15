from flask import Flask, render_template, request
import re
import os
import nltk
import collections
from nltk.corpus import stopwords

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    '''
    '''
    print request.form
    text_to_parse = request.form['text_to_parse']
    text = nltk.word_tokenize(text_to_parse)
    text = [w for w in text if not w in stopwords.words('english')]
    print text
    output = nltk.pos_tag(text)

    #print output

    noun_list = []
    verb_list = []

    for element in output:
        if "NN" in str(element[1]):
            noun_list.append(element[0])
        if "VB" in str(element[1]):
            verb_list.append(element[0])

    #print noun_list
    #print verb_list

    noun_counter = collections.Counter(noun_list)
    noun_counts = noun_counter.most_common()
    #print noun_counts

    verb_counter = collections.Counter(verb_list)
    verb_counts = verb_counter.most_common()
    #print verb_counts

    keywords = "Nouns : " + str(noun_counts) + " | " + "Verbs : " + str(verb_counts)

    result_dict = dict(
        keywords = keywords
        )
    #print keywords
    return render_template('results.html', data=result_dict)
if __name__ == '__main__':
    app.run(debug=True)
