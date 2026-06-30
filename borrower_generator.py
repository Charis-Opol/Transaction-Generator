from faker import Faker
import random
import pandas as pd

from constants import DISTRICTS
from constants import REGIONS
from constants import OCCUPATIONS

fake = Faker()

class BorrowerGenerator:

    def __init__(self, seed=42):

        Faker.seed(seed)
        random.seed(seed)

    def choose_region(self, district):

        for region, districts in REGIONS.items():

            if district in districts:
                return region

        return "Central"

    def generate_risk_profile(self):

        score = round(random.uniform(0,1),2)

        if score > 0.75:
            return "Low"

        elif score > 0.45:
            return "Medium"

        return "High"

    def generate_income(self, occupation):

        if occupation == "Farmer":

            return random.randint(
                200000,
                1200000
            )

        if occupation == "Trader":

            return random.randint(
                400000,
                2500000
            )

        if occupation == "Boda Rider":

            return random.randint(
                300000,
                1800000
            )

        if occupation == "Shop Owner":

            return random.randint(
                600000,
                5000000
            )

        if occupation == "Salaried":

            return random.randint(
                700000,
                6000000
            )

        return random.randint(
            150000,
            800000
        )

    def generate(self,
                 number_of_borrowers=3000):

        borrowers=[]

        occupations=list(OCCUPATIONS.keys())
        weights=list(OCCUPATIONS.values())

        for i in range(number_of_borrowers):

            occupation=random.choices(
                occupations,
                weights=weights
            )[0]

            district=random.choice(DISTRICTS)

            borrower={

                "borrower_id":f"B{i+1:05d}",

                "age":random.randint(20,68),

                "gender":random.choice(
                    ["Male","Female"]
                ),

                "district":district,

                "region":self.choose_region(
                    district
                ),

                "occupation":occupation,

                "monthly_income":
                self.generate_income(
                    occupation
                ),

                "marital_status":
                random.choice(
                    [
                        "Single",
                        "Married",
                        "Widowed"
                    ]
                ),

                "household_size":
                random.randint(1,8),

                "education":
                random.choice(
                    [
                        "Primary",
                        "Secondary",
                        "Diploma",
                        "Degree"
                    ]
                ),

                "sacco_member":
                random.choice([0,1]),

                "loan_amount":
                random.choice(
                    [
                        300000,
                        500000,
                        800000,
                        1000000,
                        1500000,
                        2000000,
                        3000000,
                        5000000
                    ]
                ),

                "loan_term_months":
                random.choice(
                    [
                        6,
                        12,
                        18,
                        24
                    ]
                ),

                "interest_rate":
                random.choice(
                    [
                        0.18,
                        0.20,
                        0.22,
                        0.25
                    ]
                ),

                "loan_cycle":
                random.randint(
                    1,
                    5
                ),

                "risk_profile":
                self.generate_risk_profile()

            }

            borrowers.append(
                borrower
            )

        return pd.DataFrame(
            borrowers
        )


if __name__ == "__main__":

    generator=BorrowerGenerator()

    borrowers=generator.generate()

    print(
        borrowers.head()
    )

    print()

    print(
        borrowers.shape
    )