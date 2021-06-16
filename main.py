import credentials as crd
import tweepy as tp
import nltk
from nltk.corpus import stopwords as sw
from nltk.stem import WordNetLemmatizer as wnl
from wordcloud import WordCloud as wc, STOPWORDS
import matplotlib.pyplot as plt
import string
import re


# nltk.download()


def search_tweets():
    # parameters for searching tweets
    search_term = "#Crypto"
    language = "en"
    start_date = "2021-06-04"
    retweet_filter = " -filter:retweets"
    tweet_mode = "extended"
    max_amount = 3
    api = tp.API(crd.authenticate_twitter_app())

    # search tweets
    search_term = search_term + retweet_filter
    searched_tweets = tp.Cursor(api.search, q=search_term, lang=language, since=start_date,
                                tweet_mode=tweet_mode).items(max_amount)

    # collect useful attributes from tweets in searched_tweets
    collected_tweets = []
    for tweet in searched_tweets:
        collected_tweets.append(
            [tweet.user.screen_name, tweet.user.location, tweet.created_at, tweet.source, tweet.full_text])
    return collected_tweets


def print_tweets_all_data(collected_tweets):
    # print useful data from collected_tweets
    for tweet in collected_tweets:
        print("---------- Begin of tweet ----------")
        for tweet_attribute_index in range(0, len(tweet)):
            if tweet[tweet_attribute_index] != "":
                print(tweet[tweet_attribute_index])
            else:
                print("no value")
        print("---------- End of tweet ------------")
        print("\n")


def extract_tweets_texts(collected_tweets):
    # extract text from collected_tweets
    tweets_text = []
    for tweet in collected_tweets:
        for tweet_attribute_index in range(0, len(tweet)):
            if tweet_attribute_index == 4:
                tweets_text.append(tweet[tweet_attribute_index])

    return tweets_text


def print_tweets_texts(tweets_text):
    for text_index in range(0, len(tweets_text)):
        print(f"---------- Begin of text {text_index} ------------")
        print(tweets_text[text_index])
        print(f"---------- End of text {text_index} ------------")
        print("\n")


def remove_unicode(text):
    pattern = re.compile(pattern="["u"\U00010000-\U0001FFFF""]+", flags=re.UNICODE)
    return pattern.sub(r"", text)


def remove_hyperlinks(text):
    text_length = len(text)
    link_prefix = "https://t.co/"
    link_prefix_length = len(link_prefix)
    link_content_length = 10
    count = 0
    link_index_ranges = []
    for ti in range(0, text_length - link_prefix_length - link_content_length + 1):
        for pi in range(0, link_prefix_length):
            if link_prefix[pi] == text[ti + pi]:
                count += 1
                if count == link_prefix_length:
                    link_index_ranges.append([ti, ti + pi + link_content_length])
            else:
                count = 0
    # print(link_index_ranges)

    for pair_index in reversed(range(0, len(link_index_ranges))):
        # print(link_index_ranges[pair_index][0], link_index_ranges[pair_index][1])
        text = text[:link_index_ranges[pair_index][0]] + text[link_index_ranges[pair_index][1] + 1:]

    return text


def remove_punctuation(text):
    resulting_text = ""
    for character in text:
        if character not in string.punctuation:
            resulting_text += character
    return resulting_text


def to_singular_whitespaces(text):
    resulting_text = ""
    previous_character = ""
    for current_character in text:
        if (current_character != " ") or (current_character == " " and previous_character != " "):
            resulting_text += current_character
            previous_character = current_character
    return resulting_text


def to_lowercase(text):
    return str(text).lower()


def tokenize(text):
    return nltk.word_tokenize(text)


def remove_stopwords(word_list):
    stopwords = set(sw.words("english"))
    stopwords.add("to")
    for word in word_list:
        if word in stopwords:
            word_list.remove(word)
    return word_list


def lemmatize(word_list):
    lemma = wnl()
    for wli in range(0, len(word_list)):
        word_list[wli] = lemma.lemmatize(word_list[wli], pos="v")
    return word_list


def generate_word_cloud(all_word_lists):
    data = ""
    for word_list in all_word_lists:
        for word in word_list:
            data += (word + " ")

    swd = set(STOPWORDS)
    swd.add("crypto")
    word_cloud = wc(max_words=20, stopwords=swd).generate(data)
    plt.figure()
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    # search and prints all data from all collected tweets
    found_tweets = search_tweets()
    # print_tweets_all_data(found_tweets)

    # extracts and prints only text from collected tweets
    extracted_texts = extract_tweets_texts(found_tweets)
    # print_tweets_texts(extracted_texts)

    # NLP pipeline
    # 1. Remove unicode symbols
    # 2. Remove hyperlinks
    # 3. Remove punctuation
    # 4. Remove multiple whitespaces
    # 5. Lowercase text
    # 6. Tokenize text
    # 7. Remove stopwords
    # 8. Lemmatization

    processing_texts = extracted_texts
    print("original:")
    print(processing_texts)  # 1D list
    print()

    # step 1
    processing_texts = [remove_unicode(text) for text in processing_texts]
    print("without unicode:")
    print(processing_texts)  # 1D list
    print()

    # step 2
    processing_texts = [remove_hyperlinks(text) for text in processing_texts]
    print("without hyperlinks:")
    print(processing_texts)  # 1D list
    print()

    # step 3
    processing_texts = [remove_punctuation(text) for text in processing_texts]
    print("without punctuation:")
    print(processing_texts)  # 1D list
    print()

    # step 4
    processing_texts = [to_singular_whitespaces(text) for text in processing_texts]
    print("only single whitespaces:")
    print(processing_texts)  # 1D list
    print()

    # step 5
    processing_texts = [to_lowercase(text) for text in processing_texts]
    print("only lowercase:")
    print(processing_texts)  # 1D list
    print()

    # step 6
    processing_texts = [tokenize(text) for text in processing_texts]
    print("tokenized:")
    print(processing_texts)  # 2D list
    print()

    # step 7
    processing_texts = [remove_stopwords(words) for words in processing_texts]
    print("without stopwords:")
    print(processing_texts)  # 2D list
    print()

    # step 8
    processing_texts = [lemmatize(words) for words in processing_texts]
    print("lemmatized:")
    print(processing_texts)  # 2D list
    print()

    # Show word cloud
    generate_word_cloud(processing_texts)
