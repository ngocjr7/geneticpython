"""
# Problem: roulette_wheel_selection.py
# Description: 
# Created by ngocjr7 on [2020-03-31 14:55:40]
"""
from __future__ import absolute_import

from .selection import Selection
from ...individual import Individual

from typing import List, Union
from bisect import bisect_right
from itertools import accumulate
import random
from random import Random

class RouletteWheelSelection(Selection):
    def __init__(self):
        pass

    def select(self, size: int, 
            population: List[Individual], 
            rand : Random = Random(), 
            is_unique = False) -> List[Individual]:

        fits = [float(indv.objective) for indv in population]
        max_fit = max(fits)
        fits = [(max_fit - e_fit + 1) for e_fit in fits]
        sum_fit = sum(fits)
        wheel = list(accumulate([i/sum_fit for i in fits]))

        selected = [True] * len(population)
        
        selected_indvs = []

        for _ in range(size):
            idx = bisect_right(wheel, rand.random())
            while is_unique and not selected[idx] and idx > -len(selected):
                idx -= 1
                
            if idx == -len(selected):
                idx = rand.randint(0, len(selected)-1)

            selected_indvs.append(population[idx])
            selected[idx] = False

        return selected_indvs