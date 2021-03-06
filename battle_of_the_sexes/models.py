# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range

# </standard imports>


doc = """
This is a 2-player 2-strategy coordination game. The name and story originated
from
<a href="http://books.google.ch/books?id=uqDDAgAAQBAJ&lpg=PP1&ots=S-DC4LemnS&lr&pg=PP1#v=onepage&q&f=false" target="_blank">
    Luce and Raiffa (1957)
</a>.

"""

bibliography = (
    (
        'Luce, R. Duncan, and Howard Raiffa. Games and decisions: '
        'Introduction and critical survey. Courier Dover Publications, 2012.'
    ),
    (
        'Rapoport, Anatol. Two-person game theory. Courier Dover '
        'Publications, 1999.'
    ),
    (
        'Cooper, Russell, et al. "Forward induction in the '
        'battle-of-the-sexes games."The American Economic Review (1993): '
        '1303-1316.'
    ),
    (
        'Cooper, Russell, et al. "Communication in the battle of the sexes '
        'game: some experimental results." The RAND Journal of Economics '
        '(1989): 568-587.'
    )
)


class Constants(BaseConstants):
    name_in_url = 'battle_of_the_sexes'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'battle_of_the_sexes/Instructions.html'

    # """Amount rewarded to husband if football is chosen"""
    football_husband_payoff = opera_wife_payoff = c(300)

    # Amount rewarded to wife if football is chosen
    football_wife_payoff = opera_husband_payoff = c(200)

    # amount rewarded to either if the choices don't match
    mismatch_payoff = c(0)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_payoffs(self):
        husband = self.get_player_by_role('husband')
        wife = self.get_player_by_role('wife')

        if husband.decision != wife.decision:
            husband.payoff = Constants.mismatch_payoff
            wife.payoff = Constants.mismatch_payoff

        else:
            if husband.decision == 'Football':
                husband.payoff = Constants.football_husband_payoff
                wife.payoff = Constants.football_wife_payoff
            else:
                husband.payoff = Constants.opera_husband_payoff
                wife.payoff = Constants.opera_wife_payoff


class Player(BasePlayer):
    decision = models.CharField(
        choices=['Football', 'Opera'],
        doc="""Either football or the opera""",
        widget=widgets.RadioSelect()
    )

    def other_player(self):
        """Returns other player in group"""
        return self.get_others_in_group()[0]

    def role(self):
        if self.id_in_group == 1:
            return 'husband'
        if self.id_in_group == 2:
            return 'wife'
