import main as m


# NLP pipeline
# 1. Remove unicode symbols
# 2. Remove hyperlinks
# 3. Remove punctuation
# 4. Remove multiple whitespaces
# 5. Lowercase text
# 6. Tokenize text
# 7. Remove stopwords
# 8. Lemmatization

# testing NLP pipeline
test_text = "@elonmusk.@BTCTN @Bitcoin #Bitcoin #Crypto #CryptoNews #cryptocurrencies #cryptotrading #cryptocrash #BNB #Binance #BinanceSmartChain @whale_alert " \
            "I see bitcoin down to 20k 👀 NFA " \
            "Bitcoin is garbage 🗑 " \
            "Tesla sold their bitcoins https://t.co/QHbnV9Oi8T https://t.co/Px3t13zPJ7 https://t.co/UuoIw6rfJv"

print(f"original:\n{test_text}\n")

# step 1
test_text = m.remove_unicode(test_text)
print(f"removed unicode:\n{test_text}\n")

# step 2
test_text = m.remove_hyperlinks(test_text)
print(f"removed hyperlinks:\n{test_text}\n")

# step 3
test_text = m.remove_punctuation(test_text)
print(f"removed punctuation:\n{test_text}\n")

# step 4
test_text = m.to_singular_whitespaces(test_text)
print(f"replaced multiple whitespaces with single whitespace:\n{test_text}\n")

# step 5
test_text = m.to_lowercase(test_text)
print(f"lowercase text:\n{test_text}\n")

# step 6
words = m.tokenize(test_text)
print("tokenized text:")
print(words)
print()

# step 7
words = m.remove_stopwords(words)
print("removed stopwords:")
print(words)
print()

# step 8
words = m.lemmatize(words)
print("lemmatized words:")
print(words)
print()
