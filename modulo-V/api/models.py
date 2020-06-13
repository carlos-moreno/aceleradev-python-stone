from django.core.exceptions import ValidationError
from django.core.validators import (
    MinLengthValidator,
)
from django.db import models


def validate_level(level_value):
    if level_value not in ["CRITICAL", "DEBUG", "ERROR", "WARNING", "INFO"]:
        raise ValidationError(
            f"{level_value} not a valid level.", params={"level_value": level_value}
        )


class User(models.Model):
    name = models.CharField("nome", max_length=50)
    last_login = models.DateTimeField("último login", auto_now=True)
    email = models.EmailField("e-mail")
    password = models.CharField(
        "senha",
        max_length=50,
        validators=[MinLengthValidator(8)],
    )

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField("nome", max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField("versão", max_length=5)
    address = models.GenericIPAddressField("endereço", protocol="IPv4")

    class Meta:
        db_table = "agent"

    def __str__(self):
        return self.name


class Event(models.Model):
    LEVELS = [(level, level) for level in ['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']]

    level = models.CharField("nível", max_length=20, choices=LEVELS, validators=[validate_level])
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateField(auto_now_add=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "event"

    def __str__(self):
        return self.level


class Group(models.Model):
    name = models.CharField("nome", max_length=50)

    class Meta:
        db_table = "group"

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "group_user"

    def __str__(self):
        return f"{self.group.name} - {self.user.name}"
