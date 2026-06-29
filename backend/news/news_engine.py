def get_market_news():

    return [
        {
            "title": "Market Stable",
            "sentiment": "NEUTRAL"
        }
    ]


def news_score(news):

    score = 0

    for item in news:

        if item["sentiment"] == "POSITIVE":
            score += 1

        elif item["sentiment"] == "NEGATIVE":
            score -= 1

    return score
