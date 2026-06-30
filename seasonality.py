"""
Seasonality engine for Uganda.

This module models how income and spending vary throughout
the year depending on occupation and local economic events.
"""

from dataclasses import dataclass


@dataclass
class SeasonalFactors:

    harvest_multiplier: float

    spending_multiplier: float

    rainy_season: bool

    school_fees: bool

    christmas: bool

    january_recovery: bool


class SeasonalityEngine:

    def __init__(self):

        self.harvest_months = [3,4,5,8,9,10]

        self.school_fee_months = [2,5,9]

        self.rainy_months = [3,4,5,10,11]

        self.christmas_month = 12

        self.january = 1

    def get_factors(self, month):

        harvest = month in self.harvest_months

        school = month in self.school_fee_months

        rainy = month in self.rainy_months

        christmas = month == self.christmas_month

        january = month == self.january

        harvest_multiplier = 1.0
        spending_multiplier = 1.0

        if harvest:
            harvest_multiplier = 1.7

        if school:
            spending_multiplier += 0.35

        if christmas:
            spending_multiplier += 0.60

        if january:
            spending_multiplier -= 0.20

        return SeasonalFactors(
            harvest_multiplier,
            spending_multiplier,
            rainy,
            school,
            christmas,
            january
        )