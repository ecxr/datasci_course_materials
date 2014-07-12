import sys
import json

def make_new_sentiments(scores, tweet_file):
    new_scores = {}
    for line in tweet_file:
        pyresponse = json.loads(line)
        if pyresponse.has_key("text"):
            text = pyresponse["text"]
            words = text.split()
            total = 0
            
            # derive sentiment of tweet using known words
            for word in words:
                if scores.has_key(word):
                    total += scores[word]

            # derive sentiment of unknown words in tweet
            for word in words:
                if not(scores.has_key(word)):
                    # if we already have the word, increment count and score
                    if new_scores.has_key(word):
                        (word_score, count) = new_scores[word]
                        new_scores[word] = (word_score + total, count + 1)
                    # new word, initialize sentiment and count
                    else:
                        new_scores[word] = (float(total), 1)

    # print new terms, use average sentiment for new words
    for word in new_scores:
        (total, count) = new_scores[word]
        print(word + " " + str(total / count))

def lines(fp):
    print str(len(fp.readlines()))

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
    make_new_sentiments(scores, tweet_file)

if __name__ == '__main__':
    main()

