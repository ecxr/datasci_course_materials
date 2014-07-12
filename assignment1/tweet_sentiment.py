import sys
import json

def print_sentiment(scores, tweet_file):
    for line in tweet_file:
        pyresponse = json.loads(line)
        if pyresponse.has_key("text"):
            text = pyresponse["text"]
            words = text.split()
            total = 0
            for word in words:
                if scores.has_key(word):
                    total += scores[word]
            print total
        else:
            print 0

def read_sentiment(afinnfile):
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        # The file is tab-delimited. "\t" means "tab character"
        term, score  = line.split("\t")  
        scores[term] = int(score)  # Convert the score to an integer.
    # print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = read_sentiment(sent_file)
    print_sentiment(scores, tweet_file)

if __name__ == '__main__':
    main()
