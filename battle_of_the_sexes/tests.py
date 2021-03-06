# -*- coding: utf-8 -*-
from __future__ import division

import random

from otree.common import Currency as c, currency_range

from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield (views.Introduction)

        yield (
            views.Decide, {"decision": random.choice(['Football', 'Opera'])}
        )

        # results
        yield (views.Results)
