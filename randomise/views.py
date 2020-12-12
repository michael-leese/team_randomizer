from django.shortcuts import render
import ast

from.randomise import team_randomise, check_teams, format_teams
from randomise.models import Sprint, Team, SubTeam, Member


def welcome(request):
    message = 'Welcome to Randomizer, lets go randomize!'
    return render(request, 'base.html', {'messages': [message, ]})


def create_teams(request):
    if request.POST:
        team_size = request.POST.get('team_size')
        team = Team.objects.create(name=request.POST.get('team_name'),
                                   size=team_size)
        if team:
            sprint = Sprint.objects.create(sprint=request.POST.get('sprint'),
                                           team=team)
            if sprint:
                messages = ['Please add members to your main team.',
                            'When you are finished adding members you click the Finish button.', ]
                return render(request, 'team_creation.html', {'messages': messages,
                                                              'sprint_number': sprint.sprint,
                                                              'team_name': team.name,
                                                              'team_size': team.size,
                                                              'person_count': list(range(1, int(team.size) + 1))})
    message = 'Please enter your Sprint number and your team name.'
    return render(request, 'team_creation.html', {'messages': [message, ]})


def set_teams(request, number, name, team_size):
    master_snr_list = "["
    master_dev_list = "["
    master_app_list = "["
    if request.POST:
        team = Team.objects.get(name=name)
        sprint = Sprint.objects.get(sprint=number, team=team)

        num = 1
        while num <= (int(team_size)):
            str_num = str(num)
            member_name = 'member_name' + str_num
            apprentice = 'apprentice' + str_num
            developer = 'developer' + str_num
            senior = 'senior' + str_num
            member = Member.objects.create(name=request.POST.get(member_name),
                                           main_team=team,
                                           apprentice=False if request.POST.get(apprentice) is None else True,
                                           developer=False if request.POST.get(developer) is None else True,
                                           senior=False if request.POST.get(senior) is None else True
                                           )
            if member.senior:
                master_snr_list += '"' + member.name + '", '
            elif member.developer:
                master_dev_list += '"' + member.name + '", '
            else:
                master_app_list += '"' + member.name + '", '
            num += 1
        master_app_list += "]"
        master_dev_list += "]"
        master_snr_list += "]"

        team = Team.objects.get(name=name)
        team.last_sprint = str([[], [], []])
        team_list = team_randomise(master_snr_list,
                                   master_dev_list,
                                   master_app_list,
                                   ast.literal_eval(team.last_sprint))

        team.master_app_list = str(master_app_list)
        team.master_dev_list = str(master_dev_list)
        team.master_snr_list = str(master_snr_list)
        team.save()
        teams = format_teams(str(master_snr_list), team_list)

        # team_leads = Member.objects.filter(main_team=team, senior=True).count()
        # number_of_teams = team.size / team_leads
        return render(request, 'teamResults.html', {'messages': ['We have randomized everyone!'],
                                                    'team_name': team.name,
                                                    'teams': teams})


def randomise_teams(request, name):

    team = Team.objects.get(name=name)
    last_sprint = team.last_sprint
    # last_sprint = ast.literal_eval(team.last_sprint)
    team_list = team_randomise(team.master_snr_list,
                               team.master_dev_list,
                               team.master_app_list,
                               ast.literal_eval(last_sprint))
    # check the teams are different to last sprint
    invalid = check_teams(team_list, ast.literal_eval(last_sprint))
    count = 0
    time_out = False
    while invalid:
        if count < 1:
            team_list = team_randomise(team.master_snr_list,
                                       team.master_dev_list,
                                       team.master_app_list,
                                       last_sprint)
            invalid = check_teams(team_list, last_sprint)
            count += 1
        else:
            time_out = True
            invalid = False

    teams = format_teams(str(team.master_snr_list), team_list)
    team.last_last_sprint = team.last_sprint
    team.last_sprint = str(team_list)
    team.save()
    if time_out:
        messages = ['You may have to smaller team, my brains hurting trying to figure out a unique combination!']
    else:
        messages = ['We have randomized everyone!']
    return render(request, 'teamResults.html', {'messages': messages,
                                                'team_name': team.name,
                                                'teams': teams})
