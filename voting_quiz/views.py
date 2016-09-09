# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Intro_poll(Page):
    timeout_seconds = 300


class Questions1_5(Page):

    form_model = models.Player
    form_fields = ['question_1','question_2','question_3','question_4','question_5']


class Questions6_10(Page):

    form_model = models.Player
    form_fields = ['question_6','question_7','question_8','question_9','question_10']

    def before_next_page(self):
        self.player.set_score()


class Feedback1_5(Page):
    pass


class Feedback6_10(Page):
    def before_next_page(self):
        self.player.set_votes()


class Voting(Page):

    form_model = models.Player
    form_fields = ['votacion',]


class Survey(Page):

    form_model = models.Player
    form_fields = ['gender','year','education','voto_presidenciales','political','beliefs_correct','convinced','beliefs_election','email']


class Results(Page):
    def vars_for_template(self):
        # Filling the data for HighCharts graph

        series = []

        transaction_prices = [g.sale_price for g in self.group.in_all_rounds()]
        series.append({
            'name': 'Transaction Price',
            'data': transaction_prices})

        for player in self.group.get_players():
            payoffs = [p.payoff for p in player.in_all_rounds()]
            series.append(
                {'name': 'Earnings for %s' % player.role().capitalize(),
                 'data': payoffs})
        highcharts_series = safe_json(series)

        round_numbers = safe_json(list(range(1, Constants.num_rounds + 1)))

        return {
            'highcharts_series': highcharts_series,
            'round_numbers': round_numbers
}

page_sequence = [
    Intro_poll,
    Questions1_5,
    Questions6_10,
    Feedback1_5,
    Feedback6_10,
    Voting,
    Survey,
]
