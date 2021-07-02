def act_one():
    return begin()


def begin():
    choice = input()
    if choice == 'Top':
        return begin_elevator()
    else:
        return begin_zipline()


def begin_elevator():
    return vile_one()


def begin_zipline():
    return vile_one()


def vile_one():
    choice = input()
    if choice == 'Rescue':
        return ending_one()
    else:
        return tigress()


def ending_one():
    return 'O Jogo Terminou (1)'


def tigress():
    choice = input()
    if choice == 'Sneak':
        return tigress_dogs()
    else:
        return tigress_orange()


def tigress_dogs():
    return tigress_orange()


def tigress_orange():
    choice = input()
    if choice == 'Help':
        return acme_one()
    else:
        return acme_one()


def acme_one():
    choice = input()
    if choice == 'Ride':
        return ending_two()
    else:
        return 'Começar Ato 2'


def ending_two():
    return 'O Jogo Terminou (2)'
