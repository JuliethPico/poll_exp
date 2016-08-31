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
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'voting_quiz'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'voting_quiz/Instructions.html'

    answer_q1 = 1
    answer_q2 = 1
    answer_q3 = 1
    answer_q4 = 1
    answer_q5 = 1
    answer_q6 = 1
    answer_q7 = 1
    answer_q8 = 1
    answer_q9 = 1
    answer_q10 = 1

    votes_factor = 5**0.5


class Subsession(BaseSubsession):
    def before_session_starts(self):
    # randomize to treatments
        for g in self.get_players():
            g.treatment = random.choice([1,2,3])


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    treatment = models.PositiveIntegerField()

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

    num_votos = models.FloatField()

    votacion = models.PositiveIntegerField(choices=[(1, 'Si'),(0, 'No')],
                                              widget=widgets.RadioSelectHorizontal())

    # Function to compute the score from the quiz
    def set_score(self):
        self.score = self.question_1 + self.question_2 + self.question_3 + self.question_4 + self.question_5 + self.question_6 + self.question_7 + self.question_8 + self.question_9 + self.question_10

    # Function to determine the number of votes after the quiz
    def set_votes(self):
        if self.treatment == 1:
            self.num_votos = self.score
        elif  self.treatment == 2:
            if self.score < 5:
                self.num_votos = 0
            else:
                self.num_votos = 5
        elif  self.treatment == 3:
            #self.num_votos = (Constants.votes_factor)*((self.score)**(0.5))
            self.num_votos = (5**0.5)*(self.score**0.5)


    # Questions for the survey
    gender = models.CharField(initial=None, blank=True,
                              choices=['Mujer','Hombre'],
                              verbose_name='',)

    year = models.PositiveIntegerField(initial=None, blank=True,
                                       choices=range(1950, 2000),
                                       verbose_name='',)

    education = models.CharField(initial=None, blank=True,
                          choices=['Primaria','Bachillerato','Técnico','Profesional',
                                   'Especialización, maestría o doctorado'],
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
