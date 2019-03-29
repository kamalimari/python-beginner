no_of_prisoners = 5
no_of_chocolates = 5
starting_position = 2
remainder = no_of_prisoners % no_of_chocolates
if remainder == 0:
    if starting_position == 1:
        return 