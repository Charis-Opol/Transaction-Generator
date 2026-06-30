import random


class RiskEngine:

    """
    Controls how borrowers become
    more or less risky over time.
    """

    def __init__(self):

        pass

    def monthly_health_change(

        self,

        health,

        occupation,

        month

    ):

        change = random.uniform(

            -0.03,

            0.03

        )

        if month in [2,5,9]:

            change -= 0.04

        if month == 12:

            change -= 0.06

        if occupation == "Farmer":

            if month in [3,4,5]:

                change += 0.08

            if month in [8,9,10]:

                change += 0.06

        health += change

        health = max(

            0,

            min(

                1,

                health

            )

        )

        return health