import requests

def get_market_news():

    # Placeholder version
    # API integration will be added later

    return [
        {
            "title": "Bitcoin market update",
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
