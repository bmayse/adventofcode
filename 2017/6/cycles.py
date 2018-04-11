from register import Register

def count_redistributions_to_known_state(data):
    known_configuration_hashes = {}
    populate_hashes_until_first_duplicate(known_configuration_hashes, Register(data))
    return len(known_configuration_hashes)


def get_cycles_in_loop(data):
    known_configuration_hashes = {}
    first_duplicate = populate_hashes_until_first_duplicate(known_configuration_hashes, Register(data))
    return len(known_configuration_hashes.keys()) - known_configuration_hashes[first_duplicate.hash]


def populate_hashes_until_first_duplicate(known_configuration_hashes, register):
    cur = register
    while cur.hash not in known_configuration_hashes.keys():
        known_configuration_hashes[cur.hash] = len(known_configuration_hashes.keys())
        cur = apply_transformation(register)
    return cur


def apply_transformation(register):
    start, to_distribute = get_greatest_index_and_value(register)
    register.content[start] = 0
    for index in range(to_distribute):
        register.content[(start + index + 1) % len(register.content)] += 1
    return Register(register.content)


def get_greatest_index_and_value(register):
    return max(enumerate(register.content), key = lambda tuple: tuple[1])
