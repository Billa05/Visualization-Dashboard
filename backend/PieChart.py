import random

def PiechartData(data, keyword):
    word_counts = {}
    for doc in data:
        word = doc[keyword]
        if word != "":
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    FormattedData = []
    for word, count in word_counts.items():
        formatdata = {
            "id": word,
            "label": word,
            "value": count,
            "color": f"hsl({random.randint(100,300)}, 70%, 50%)"
        }
        FormattedData.append(formatdata)

    return FormattedData