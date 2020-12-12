from django.db import models


class Team(models.Model):
    """
    Team model definitions
    """
    name = models.CharField(max_length=100, unique=True)
    size = models.IntegerField(default=0)
    master_snr_list = models.CharField(max_length=700, null=True, blank=True)
    master_dev_list = models.CharField(max_length=700, null=True, blank=True)
    master_app_list = models.CharField(max_length=700, null=True, blank=True)
    last_sprint = models.CharField(max_length=2500, null=True, blank=True)
    last_last_sprint = models.CharField(max_length=2500, null=True, blank=True)

    def __str__(self):
        return self.name

class Sprint(models.Model):
    """
    Sprint model definitions
    """
    sprint = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        unique_together = (['sprint', 'team'])
    def __str__(self):
        return 'Sprint ' + str(self.sprint) + ' of ' + self.team.name

class Member(models.Model):
    """
    Member model definitions
    """
    name = models.CharField(max_length=25)
    main_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    apprentice = models.BooleanField(default=False)
    developer = models.BooleanField(default=False)
    senior = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' of team ' + self.main_team.name

class SubTeam(models.Model):
    """
    SubTeam model definitions
    """
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    main_team = models.ForeignKey(Team, on_delete=models.CASCADE)
