import collections
def count_words(training_set):
    counts = collections.defaultdict(lambda: [0, 0])
    for message, is_spam in training_set:
        for word in message:
            counts[word][0 if is_spam else 1] += 1
    return counts
print(count_words([(['I','fuck','you'],0),(['Fucking','shit'],0)]))

