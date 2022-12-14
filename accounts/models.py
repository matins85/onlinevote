from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import OnlinevoteUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from accounts.utils import image_resize


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class OnlinevoteUser(AbstractUser):
    """ OnlinevoteUser model """

    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = OnlinevoteUserManager()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email


class Year(BaseModel):
    """ Year model """

    year = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.year


class School(BaseModel):
    """ School model """

    school = models.CharField(max_length=250, unique=True)

    def departments(self):
        return Department.objects.filter(school=self)

    def __str__(self):
        return self.school


class Department(BaseModel):
    """ Department model """

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school_depart')
    department = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.department


class AspirantPosition(BaseModel):
    """ Aspirant Position model """

    POSITION_TYPE = (
        ('sug', 'SUG'),
        ('department', 'DEPARTMENT'),
    )
    LEVEL_TYPE = (
        ('nd', 'nd'),
        ('hnd', 'hnd'),
    )

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='aspirant_depart')
    position = models.CharField(max_length=250)
    position_type = models.CharField(max_length=50, choices=POSITION_TYPE)
    level = models.CharField(max_length=50, choices=LEVEL_TYPE)

    def aspirant_members(self):
        return RegisteredVoters.objects.filter(level='hnd').filter(department=self.department)\
            .filter(aspirant=True).filter(verified_aspirant=True).filter(position=self)

    def aspirant_members2(self):
        return RegisteredVoters.objects.filter(level='nd').filter(department=self.department)\
            .filter(aspirant=True).filter(verified_aspirant=True).filter(position=self)

    def __str__(self):
        return f"department: {self.department} | position: {self.position} | position-type:{self.position_type} " \
               f"| level: {self.level}"


class RegisteredVoters(BaseModel):
    """ Registered voters model """

    LEVEL_TYPE = (
        ('nd', 'nd'),
        ('hnd', 'hnd'),
    )

    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=250)
    # profile = models.ImageField(upload_to='onlinevote/voters')
    profile = models.TextField()
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True, related_name='year_year')
    matric = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='department_school')
    aspirant = models.BooleanField(default=False)
    verified_aspirant = models.BooleanField(default=False)
    point = models.PositiveIntegerField(default=0)
    position = models.ForeignKey(AspirantPosition, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='voter_position')
    level = models.CharField(max_length=50, choices=LEVEL_TYPE)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        try:
            image_resize(self.profile, 500, 500)
        except Exception as e:
            pass
        super().save(*args, **kwargs)
