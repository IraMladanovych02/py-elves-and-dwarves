def calculate_team_total_rating(team):
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()











