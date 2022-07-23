from textblob import TextBlob
import json


def write_to_output(dictionary: dict):
    with open('output.json', 'w') as outfile:
        json.dump(dictionary, outfile)


wiki = TextBlob("Python is a terrible, sucky programming language.")
print(wiki.sentiment.polarity)
write_to_output({'foo': 1})
