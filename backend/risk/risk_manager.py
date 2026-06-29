def calculate_risk(balance):

    risk = balance * 0.01

    return round(risk, 2)


def stop_loss(entry):

    return round(entry * 0.98, 2)


def take_profit(entry):

    return round(entry * 1.04, 2)
