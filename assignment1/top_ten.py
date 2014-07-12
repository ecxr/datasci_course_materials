import sys
import json
from collections import OrderedDict

def generate_top_tags(tweet_file):
    tag_count = {}
    for line in tweet_file:
        pyresponse = json.loads(line)
        if pyresponse.has_key('entities'):
            tags = pyresponse['entities']['hashtags']
            for tag in tags:
                if tag_count.has_key(tag['text']):
                    tag_count[tag['text']] = tag_count[tag['text']] + 1
                else:
                    tag_count[tag['text']] = 1
    

    ordered_tags = reversed(OrderedDict(sorted(tag_count.items(), key=lambda t: t[1])))
    i = 0
    for tag in ordered_tags:
        print(tag + " " + str(tag_count[tag]))
        i += 1
        if i >= 10:
            break

def main():
    tweet_file = open(sys.argv[1])
    generate_top_tags(tweet_file)


if __name__ == '__main__':
    main()
