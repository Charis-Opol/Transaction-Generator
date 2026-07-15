import random


class RiskEngine:

    def monthly_health_change(

        self,

        health,

        occupation,

        month

    ):

        health += random.uniform(

            -0.07,

            0.05

        )

        if month in [2,5,9]:

            health -= random.uniform(

                0.04,

                0.08

            )

        if month == 12:

            health -= random.uniform(

                0.08,

                0.15

            )

        if occupation == "Farmer":

            if month in [3,4]:

                health += random.uniform(

                    0.10,

                    0.18

                )

            if month in [9,10]:

                health += random.uniform(

                    0.08,

                    0.15

                )

        if occupation == "Casual Worker":

            health += random.uniform(

                -0.08,

                0.03

            )

        if random.random() < 0.07:

            health -= random.uniform(

                0.15,

                0.30

            )

        return max(

            0.05,

            min(

                health,

                1

            )

        )

    def default_probability(

        self,

        borrower,

        state

    ):

        score = 0

        if state["health"] < 0.70:

            score += 1

        if state["health"] < 0.55:

            score += 2

        if state["health"] < 0.40:

            score += 3

        debt_ratio = (

            borrower["loan_amount"]

            /

            borrower["monthly_income"]

        )

        if debt_ratio > 6:

            score += 3

        elif debt_ratio > 4:

            score += 2

        elif debt_ratio > 2:

            score += 1

        if borrower["risk_profile"] == "High":

            score += 2

        elif borrower["risk_profile"] == "Medium":

            score += 1

        if borrower["sacco_member"] == 0:

            score += 1

        if borrower["occupation"] == "Casual Worker":

            score += 2

        elif borrower["occupation"] == "Farmer":

            score += 1

        elif borrower["occupation"] == "Boda Rider":

            score += 1

        probability = min(

            0.03 +

            score * 0.04,

            0.80

        )

        return probability