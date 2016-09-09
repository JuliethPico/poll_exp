# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    timeout_seconds = 300


class Voting(Page):
    form_model = models.Player
    form_fields = ['votacion']


class Q1(Page):
    form_model = models.Player
    form_fields = ['question_1']

    def is_displayed(self):
        return self.player.treatment != 3


class Q1_response(Page):

    def is_displayed(self):
        return self.player.treatment != 3

    def vars_for_template(self):
        if self.player.question_1 == 1:
            response = 'Verdadero'
        else:
            response = 'Falso'
        return {'response': response}


class Q2(Page):
    form_model = models.Player
    form_fields = ['question_2']

    def is_displayed(self):
        return self.player.treatment != 3


class Q2_response(Page):

    def is_displayed(self):
        return self.player.treatment != 3

    def vars_for_template(self):
        if self.player.question_2 == 1:
            response = 'Verdadero'
        else:
            response = 'Falso'
        return {'response': response}


class Q3(Page):
    form_model = models.Player
    form_fields = ['question_3']

    def is_displayed(self):
        return self.player.treatment != 3

class Q3_response(Page):

    def is_displayed(self):
        return self.player.treatment != 3

    def vars_for_template(self):
        if self.player.question_3 == 1:
            response = 'Verdadero'
        else:
            response = 'Falso'
        return {'response': response}


class Q4(Page):
    form_model = models.Player
    form_fields = ['question_4']

    def is_displayed(self):
        return self.player.treatment != 3


class Q4_response(Page):

    def is_displayed(self):
        return self.player.treatment != 3

    def vars_for_template(self):
        if self.player.question_4 == 1:
            response = 'Verdadero'
        else:
            response = 'Falso'
        return {'response': response}


class Q5(Page):
    form_model = models.Player
    form_fields = ['question_5']

    def is_displayed(self):
            return self.player.treatment != 3


class Q5_response(Page):

    def is_displayed(self):
        return self.player.treatment != 3

    def vars_for_template(self):
        if self.player.question_5 == 1:
            response = 'Verdadero'
        else:
            response = 'Falso'
        return {'response': response}


class Q6(Page):
    form_model = models.Player
    form_fields = ['question_6']

    def is_displayed(self):
            return self.player.treatment != 3


class Q6_response(Page):

    def is_displayed(self):
        return self.player.treatment != 3

    def vars_for_template(self):
        if self.player.question_6 == 1:
            response = 'Verdadero'
        else:
            response = 'Falso'
        return {'response': response}


class Q7(Page):
    form_model = models.Player
    form_fields = ['question_7']

    def is_displayed(self):
        return self.player.treatment != 3


class Q7_response(Page):

    def is_displayed(self):
        return self.player.treatment != 3

    def vars_for_template(self):
        if self.player.question_7 == 1:
            response = 'Verdadero'
        else:
            response = 'Falso'
        return {'response': response}


class Q8(Page):
    form_model = models.Player
    form_fields = ['question_8']

    def is_displayed(self):
            return self.player.treatment != 3


class Q8_response(Page):

    def is_displayed(self):
        return self.player.treatment != 3

    def vars_for_template(self):
        if self.player.question_8 == 1:
            response = 'Verdadero'
        else:
            response = 'Falso'
        return {'response': response}


class Q9(Page):
    form_model = models.Player
    form_fields = ['question_9']

    def is_displayed(self):
        return self.player.treatment != 3


class Q9_response(Page):

    def is_displayed(self):
        return self.player.treatment != 3

    def vars_for_template(self):
        if self.player.question_9 == 1:
            response = 'Verdadero'
        else:
            response = 'Falso'
        return {'response': response}


class Q10(Page):
    form_model = models.Player
    form_fields = ['question_10']

    def is_displayed(self):
        return self.player.treatment != 3

class Q10_response(Page):

    def is_displayed(self):
        return self.player.treatment != 3

    def vars_for_template(self):
        if self.player.question_10 == 1:
            response = 'Verdadero'
        else:
            response = 'Falso'
        return {'response': response}

    def before_next_page(self):
        self.player.set_score()


class Survey(Page):

    form_model = models.Player
    form_fields = ['gender','year','status','voto_presidenciales','political','beliefs_correct','convinced','beliefs_election','email']


page_sequence = [
    Introduction,
    Voting,
    Q1,
    Q1_response,
    Q2,
    Q2_response,
    Q3,
    Q3_response,
    Q4,
    Q4_response,
    Q5,
    Q5_response,
    Q6,
    Q6_response,
    Q7,
    Q7_response,
    Q8,
    Q8_response,
    Q9,
    Q9_response,
    Q10,
    Q10_response,
    Survey,
]
