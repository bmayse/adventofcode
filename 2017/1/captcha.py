def captcha_next(challenge):
    response = 0
    for index, cur in enumerate(challenge):
        if cur == challenge[(index + 1) % len(challenge)]:
            response += int(cur)
    return response


def captcha_across(challenge):
    response = 0
    halfway_distance = len(challenge)//2

    for index, cur in enumerate(challenge):
        index_of_next = (index + halfway_distance) % len(challenge)
        if cur == challenge[index_of_next]:
            response += int(cur)
    return response
