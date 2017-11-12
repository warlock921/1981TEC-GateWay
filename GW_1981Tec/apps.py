# GW_1981Tec/apps.py
from suit.apps import DjangoSuitConfig
from django.apps import AppConfig


class Gw1981TecConfig(AppConfig):
    name = 'GW_1981Tec'

class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'