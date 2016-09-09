# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Cesar Mantilla'

doc = """
Este es un test sobre qué tanto sabe de
los acuerdos del proceso de paz entre el gobierno colombiano y las FARC.
"""


class Constants(BaseConstants):
    name_in_url = 'test_plebiscito'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'test_plebiscito/Instructions.html'

    answer_q1 = 1
    answer_q2 = 1
    answer_q3 = 0
    answer_q4 = 0
    answer_q5 = 1
    answer_q6 = 1
    answer_q7 = 1
    answer_q8 = 0
    answer_q9 = 0
    answer_q10 = 1

    threshold_lab = 90


class Subsession(BaseSubsession):
    def before_session_starts(self):
    # randomize to treatments
        for g in self.get_players():
            g.treatment = random.choice([1,2,3])
            g.lab_invitation = random.randint(0, 100)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    treatment = models.PositiveIntegerField()

    lab_invitation = models.PositiveIntegerField()

    question_1 = models.PositiveIntegerField(choices=[(1, 'Verdadero'),(0, 'Falso')],
                                              widget=widgets.RadioSelectHorizontal())

    question_2 = models.PositiveIntegerField(choices=[(1, 'Verdadero'),(0, 'Falso')],
                                              widget=widgets.RadioSelectHorizontal())

    question_3 = models.PositiveIntegerField(choices=[(1, 'Verdadero'),(0, 'Falso')],
                                              widget=widgets.RadioSelectHorizontal())

    question_4 = models.PositiveIntegerField(choices=[(1, 'Verdadero'),(0, 'Falso')],
                                              widget=widgets.RadioSelectHorizontal())

    question_5 = models.PositiveIntegerField(choices=[(1, 'Verdadero'),(0, 'Falso')],
                                              widget=widgets.RadioSelectHorizontal())

    question_6 = models.PositiveIntegerField(choices=[(1, 'Verdadero'),(0, 'Falso')],
                                              widget=widgets.RadioSelectHorizontal())

    question_7 = models.PositiveIntegerField(choices=[(1, 'Verdadero'),(0, 'Falso')],
                                              widget=widgets.RadioSelectHorizontal())

    question_8 = models.PositiveIntegerField(choices=[(1, 'Verdadero'),(0, 'Falso')],
                                              widget=widgets.RadioSelectHorizontal())

    question_9 = models.PositiveIntegerField(choices=[(1, 'Verdadero'),(0, 'Falso')],
                                              widget=widgets.RadioSelectHorizontal())

    question_10 = models.PositiveIntegerField(choices=[(1, 'Verdadero'),(0, 'Falso')],
                                              widget=widgets.RadioSelectHorizontal())

    score = models.FloatField()

    votacion = models.PositiveIntegerField(choices=[(1, 'Si'),(0, 'No')],
                                              widget=widgets.RadioSelectHorizontal())

    # Function to compute the score from the quiz
    def set_score(self):
        self.score = 10 - abs(self.question_1 - Constants.answer_q1) - abs(self.question_2 - Constants.answer_q2) -abs(self.question_3 - Constants.answer_q3) -abs(self.question_4 - Constants.answer_q4) -abs(self.question_5 - Constants.answer_q5) -abs(self.question_6 - Constants.answer_q6) -abs(self.question_7 - Constants.answer_q7) -abs(self.question_8 - Constants.answer_q8) -abs(self.question_9 - Constants.answer_q9) -abs(self.question_10 - Constants.answer_q10)


    # Questions for the survey
    gender = models.CharField(initial=None, blank=True,
                              choices=['Mujer','Hombre'],
                              verbose_name='',)

    year = models.PositiveIntegerField(initial=None, blank=True,
                                       choices=range(1950, 2000),
                                       verbose_name='',)

    status = models.CharField(initial=None, blank=True,
                          choices=['Estudiante de pregrado','Estudiante de posgrado',
                                   'Egresado','Funcionario'],
                                 verbose_name='',)

    voto_presidenciales = models.CharField(initial=None, blank=True,
                          choices=['Juan Manuel Santos','Oscar Iván Zuluaga',
                                   'Voto en blanco','No voté'],
                                           verbose_name='',)

    political = models.CharField(initial=None, blank=True,
                          choices=['De izquierda',
                                   'Ligeramente de izquierda',
                                   'De centro',
                                   'Ligeramente de derecha',
                                   'De derecha ',
                                   'No lo sé'],
                                 verbose_name='',)

    beliefs_correct = models.PositiveIntegerField(initial=None, blank=True,
                                                  choices=range(0, 11),
                                                  verbose_name='',)

    convinced = models.CharField(initial=None, blank=True,
                          choices=['En ninguna de las preguntas',
                                   'En menos de tres preguntas',
                                   'En al menos seis preguntas',
                                   'En al menos ocho preguntas',
                                   'En todas las preguntas'],
                                 verbose_name='',)

    beliefs_election = models.PositiveIntegerField(initial=None, blank=True,
                                                  choices=range(0, 105,5),
                                                   verbose_name='',)

    email = models.EmailField(max_length=70,blank=True,verbose_name='',)
