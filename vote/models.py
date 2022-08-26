from django.db import models
from django.utils import timezone
from accounts.models import Year, Department, RegisteredVoters, AspirantPosition


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class VoteModel(BaseModel):
    """ Vote model """

    start = models.BooleanField(default=False)
    end = models.BooleanField(default=False)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True, related_name='vote_year')
    department = models.OneToOneField(Department, on_delete=models.SET_NULL, null=True,
                                      related_name='vote_department')

    def aspirant(self):
        return AspirantPosition.objects.filter(department=self.department)

    def __str__(self):
        return str(self.department)


class VotersModel(BaseModel):
    """ Voters model """

    choice = models.ForeignKey(RegisteredVoters, on_delete=models.CASCADE, related_name='choice')
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True, related_name='voters_year')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='created_at')
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(RegisteredVoters, on_delete=models.CASCADE, null=True, related_name='created_by')

    def __str__(self):
        return str(self.created_by)
