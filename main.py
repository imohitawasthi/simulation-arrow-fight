
import random

PROBABILITY_SHOT = 40
PARKOUR_SKILL = 30
TOTAL_HEALTH = 100
SHOT_DAMAGE = 5
MISS_DAMAGE = 2


def main(t_rounds, t_players):

    player_health = {}

    for i in range(t_rounds):
        print("round: ", i)

        players_completed = []
        for y in range(t_players):

            while len(players_completed) < y:
                possible_player = random.randint(1, t_players)

                print("player% ", possible_player)
                if possible_player not in players_completed:
                    players_completed.append(possible_player)
                    possible_target = None
                    while True:
                        possible_target = random.randint(1, t_players)
                        if possible_target != possible_player:
                            break

                    is_shot_complete = int(random.random() * 100) < PROBABILITY_SHOT
                    is_parkour_success = int(random.random() * 100) < PARKOUR_SKILL

                    if is_parkour_success is False and is_shot_complete is True:
                        if player_health.get(possible_target) is None or (
                                player_health.get(possible_target) is not None and player_health.get(possible_target) > 0):

                            player_health[possible_target] = 100 if possible_target not in player_health else player_health[possible_target] - SHOT_DAMAGE

                            print("Good Shot: ", possible_target)
                        else:
                            print("Player is Dead")
                    else:
                        if player_health.get(possible_player) is None or (
                                player_health.get(possible_player) is not None and player_health.get(possible_player) > 0):
                            player_health[possible_player] = 100 if possible_player not in player_health else player_health[possible_player] - MISS_DAMAGE
                            print("OOPS Missed", possible_target)
                        else:
                            print("Player not in condition of shooting")


    print("Game Complete", player_health)


if __name__ == '__main__':

    # rounds = int(input("Total number of rounds fired"))
    # players = int(input("Total number of players"))

    rounds = 100
    players = 5
    main(rounds, players)
