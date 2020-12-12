import astgit
import random
import itertools

def team_randomise(master_snr_list, master_dev_list, master_app_list, last_sprint):
    # randomise the groups to teams
    snr_list = ast.literal_eval(master_snr_list)
    dev_list = ast.literal_eval(master_dev_list)
    app_list = ast.literal_eval(master_app_list)

    team_list1 = []
    team_list2 = []
    team_list3 = []
    team_list = [team_list1, team_list2, team_list3]
    team_factor = (len(snr_list) + len(dev_list) + len(app_list)) / 3

    random.shuffle(snr_list)
    random.shuffle(dev_list)
    random.shuffle(app_list)
    index = random.randrange(1, 3)

    while dev_list:
        team_number = 0
        if isinstance(last_sprint[0], list):
            for team in team_list:
                if len(team) < team_factor:
                    if snr_list:
                        snr = snr_list.pop()
                        team.append(snr)
                    if dev_list:
                        dev = dev_list.pop()
                        team.append(dev)
                    if app_list:
                        if team_number != index:
                            app = app_list.pop()
                            team.append(app)
                        else:
                            pass
                else:
                    pass
                # # check the teams are different to last sprint
                # invalid = check_teams(team, last_sprint[team_number])
                # while invalid:
                #     team = team_randomise(master_snr_list, master_dev_list, master_app_list, last_sprint[team_number])
                #     invalid = check_teams(team, last_sprint[team_number])
                #     print(invalid)
                team_number += 1
        else:
            pass
            # team_list = []
            # if len(last_sprint) < team_factor:
            #     if snr_list:
            #         snr = snr_list.pop()
            #         team_list.append(snr)
            #     if dev_list:
            #         dev = dev_list.pop()
            #         team_list.append(dev)
            #     if app_list:
            #         if team_number != index:
            #             app = app_list.pop()
            #             team_list.append(app)
            #         else:
            #             pass
            #     # check the teams are different to last sprint
            #     invalid = check_teams(team_list, last_sprint)
            #     while invalid:
            #         team = team_randomise(snr_list, dev_list, app_list, last_sprint)
            #         invalid = check_teams(team_list, last_sprint)
            #         print(invalid)
    return team_list


def format_teams(master_snr_list, team_list):
    teams = {}
    num = 1
    for team in team_list:
        for snr in ast.literal_eval(master_snr_list):
            if snr in team:
                teams["team {0}".format(num)] = "{0}'s Team includes: {1}".format(str(snr), str(team))
                print(teams["team {0}".format(num)])
        num += 1
    return teams


def check_teams(team_list, last_sprint):
    for team, last_team in zip(team_list, last_sprint):
        if isinstance(team, list) and isinstance(last_team, list):
            return bool(set(last_team).intersection(set(team)))
        else:
            return bool(True if team in last_sprint else False)