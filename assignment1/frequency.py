import sys
import json

def generate_frequency(tweet_file):
    word_count = {}
    total_words = 0
    for line in tweet_file:
        pyresponse = json.loads(line)
        if pyresponse.has_key("text"):
            text = pyresponse["text"]
            words = text.split()
            for word in words:
                total_words += 1
                if word_count.has_key(word):
                    word_count[word] = word_count[word] + 1
                else:
                    word_count[word] = 1
    
    # print("Total words = " + str(total_words))

    for word in word_count:
        print(word + " " + "%.5f" % float(word_count[word] / total_words))

def main():
    tweet_file = open(sys.argv[1])
    generate_frequency(tweet_file)


if __name__ == '__main__':
    main()
