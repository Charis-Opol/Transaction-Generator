"""
transaction_generator.py

Generates realistic Ugandan mobile money transaction data
for hybrid LSTM-FNN credit risk prediction.

Author: Charis Opol
"""

from datetime import datetime
import uuid
import random

import pandas as pd
from tqdm import tqdm

from borrower_generator import BorrowerGenerator
from seasonality import SeasonalityEngine
from risk_engine import RiskEngine

from constants import (
    CHANNELS,
    NETWORKS,
    OCCUPATION_BEHAVIOUR,
    MERCHANT_BEHAVIOURS
)

from config import (
    NUM_BORROWERS,
    START_YEAR,
    MIN_TRANSACTIONS,
    MAX_TRANSACTIONS
)


class TransactionGenerator:

    def __init__(self):

        self.borrowers = BorrowerGenerator().generate(NUM_BORROWERS)

        self.seasonality = SeasonalityEngine()

        self.risk = RiskEngine()

        self.transactions = []

    ############################################################
    # Borrower State
    ############################################################

    def initialise_state(self, borrower):

        return {

            "balance": random.randint(
                50000,
                500000
            ),

            "health": random.uniform(
                0.55,
                0.95
            ),

            "last_transaction": None,

            "monthly_income":
                borrower["monthly_income"],

            "defaulted": False

        }

    ############################################################
    # Transaction ID
    ############################################################

    def transaction_id(self):

        return uuid.uuid4().hex.upper()[:18]

    ############################################################
    # Timestamp
    ############################################################

    def random_timestamp(
            self,
            borrower,
            transaction_type,
            year,
            month):

        occupation = borrower["occupation"]

        profile = OCCUPATION_BEHAVIOUR[
            occupation
        ]

        if transaction_type == "Received":

            if random.random() < 0.75:

                day = random.choice(
                    profile["income_days"]
                )

            else:

                day = random.randint(
                    1,
                    28
                )

        else:

            day = random.randint(
                1,
                28
            )

        hour = random.randint(
            7,
            20
        )

        minute = random.randint(
            0,
            59
        )

        second = random.randint(
            0,
            59
        )

        return datetime(
            year,
            month,
            day,
            hour,
            minute,
            second
        )

    ############################################################
    # Transaction Type
    ############################################################

    def choose_transaction_type(
            self,
            borrower,
            state,
            month):

        occupation = borrower["occupation"]

        profile = OCCUPATION_BEHAVIOUR[
            occupation
        ]

        receive_probability = profile[
            "income_probability"
        ]

        receive_probability *= state[
            "health"
        ]

        season = self.seasonality.get_factors(
            month
        )

        if occupation == "Farmer":

            receive_probability *= (
                season.harvest_multiplier
            )

        receive_probability = min(
            receive_probability,
            0.95
        )

        if random.random() < receive_probability:

            return "Received"

        return "Sent"

    ############################################################
    # Amount
    ############################################################

    def transaction_amount(
            self,
            borrower,
            transaction_type,
            month):

        occupation = borrower[
            "occupation"
        ]

        profile = OCCUPATION_BEHAVIOUR[
            occupation
        ]

        season = self.seasonality.get_factors(
            month
        )

        if transaction_type == "Received":

            base = profile[
                "base_income"
            ]

            base *= season.harvest_multiplier

        else:

            base = profile[
                "base_expense"
            ]

            base *= season.spending_multiplier

        amount = random.lognormvariate(
            0,
            0.45
        )

        amount *= base

        return int(
            max(
                amount,
                1000
            )
        )

    ############################################################
    # Network
    ############################################################

    def choose_network(
            self,
            occupation):

        profile = OCCUPATION_BEHAVIOUR[
            occupation
        ]

        preferred = profile[
            "preferred_network"
        ]

        if random.random() < 0.80:

            return preferred

        return random.choice(
            NETWORKS
        )

    ############################################################
    # Channel
    ############################################################

    def choose_channel(
            self,
            occupation):

        profile = OCCUPATION_BEHAVIOUR[
            occupation
        ]

        preferred = profile[
            "preferred_channel"
        ]

        if random.random() < 0.70:

            return preferred

        return random.choice(
            CHANNELS
        )

    ############################################################
    # Merchant Category
    ############################################################

    def merchant_category(
            self,
            transaction_type):

        return random.choice(
            MERCHANT_BEHAVIOURS[
                transaction_type
            ]
        )
        
    ############################################################
    # Balance Update
    ############################################################

    def update_balance(
            self,
            balance,
            amount,
            transaction_type):

        if transaction_type == "Received":

            balance += amount

        else:

            balance -= amount

        return max(balance, 0)

    ############################################################
    # Create Transaction
    ############################################################

    def create_transaction(
            self,
            borrower,
            state,
            month):

        transaction_type = self.choose_transaction_type(
            borrower,
            state,
            month
        )

        timestamp = self.random_timestamp(
            borrower,
            transaction_type,
            START_YEAR,
            month
        )

        amount = self.transaction_amount(
            borrower,
            transaction_type,
            month
        )

        balance_before = state["balance"]

        balance_after = self.update_balance(
            balance_before,
            amount,
            transaction_type
        )

        state["balance"] = balance_after

        occupation = borrower["occupation"]

        transaction = {

            "borrower_id": borrower["borrower_id"],

            "transaction_id": self.transaction_id(),

            "timestamp": timestamp,

            "year": timestamp.year,

            "month": timestamp.month,

            "day": timestamp.day,

            "day_of_week": timestamp.strftime("%A"),

            "hour": timestamp.hour,

            "transaction_type": transaction_type,

            "amount": amount,

            "balance_before": balance_before,

            "balance_after": balance_after,

            "occupation": occupation,

            "district": borrower["district"],

            "region": borrower["region"],

            "gender": borrower["gender"],

            "age": borrower["age"],

            "education": borrower["education"],

            "marital_status": borrower["marital_status"],

            "household_size": borrower["household_size"],

            "monthly_income": borrower["monthly_income"],

            "loan_amount": borrower["loan_amount"],

            "loan_term_months":
                borrower["loan_term_months"],

            "interest_rate":
                borrower["interest_rate"],

            "loan_cycle":
                borrower["loan_cycle"],

            "sacco_member":
                borrower["sacco_member"],

            "risk_profile":
                borrower["risk_profile"],

            "network":
                self.choose_network(
                    occupation
                ),

            "channel":
                self.choose_channel(
                    occupation
                ),

            "merchant_category":
                self.merchant_category(
                    transaction_type
                ),

            "harvest_season":
                self.seasonality.get_factors(
                    month
                ).harvest_multiplier > 1,

            "school_fees_season":
                self.seasonality.get_factors(
                    month
                ).school_fees,

            "christmas_season":
                self.seasonality.get_factors(
                    month
                ).christmas,

            "rainy_season":
                self.seasonality.get_factors(
                    month
                ).rainy_season,

            "financial_health":
                round(
                    state["health"],
                    3
                ),

            "default_label":
                1 if state["health"] < 0.35 else 0

        }

        return transaction

    ############################################################
    # Simulate One Month
    ############################################################

    def simulate_month(
            self,
            borrower,
            state,
            month):

        monthly_transactions = []

        number_transactions = random.randint(
            MIN_TRANSACTIONS,
            MAX_TRANSACTIONS
        )

        for _ in range(number_transactions):

            transaction = self.create_transaction(
                borrower,
                state,
                month
            )

            monthly_transactions.append(
                transaction
            )

        return monthly_transactions

    ############################################################
    # Simulate One Borrower
    ############################################################

    def simulate_borrower(
            self,
            borrower):

        borrower_transactions = []

        state = self.initialise_state(
            borrower
        )

        for month in range(1, 13):

            state["health"] = self.risk.monthly_health_change(

                state["health"],

                borrower["occupation"],

                month

            )

            borrower_transactions.extend(

                self.simulate_month(

                    borrower,

                    state,

                    month

                )

            )

        return borrower_transactions
    

    ############################################################
    # Generate Dataset
    ############################################################

    def generate(self):

        print("\nGenerating synthetic mobile money transactions...\n")

        self.transactions = []

        for _, borrower in tqdm(
                self.borrowers.iterrows(),
                total=len(self.borrowers),
                desc="Borrowers"):

            borrower_transactions = self.simulate_borrower(
                borrower
            )

            self.transactions.extend(
                borrower_transactions
            )

        df = pd.DataFrame(
            self.transactions
        )

        df = df.sort_values(
            [
                "borrower_id",
                "timestamp"
            ]
        ).reset_index(drop=True)

        return df

    ############################################################
    # Export CSV
    ############################################################

    def export_csv(
            self,
            dataframe,
            filename="uganda_mobile_money_master.csv"):

        dataframe.to_csv(
            filename,
            index=False
        )

        print(
            f"\nCSV exported successfully -> {filename}"
        )

    ############################################################
    # Export Excel
    ############################################################

    def export_excel(
            self,
            dataframe,
            filename="uganda_mobile_money_master.xlsx"):

        dataframe.to_excel(
            filename,
            index=False
        )

        print(
            f"Excel exported successfully -> {filename}"
        )

    ############################################################
    # Generate + Export
    ############################################################

    def run(self):

        df = self.generate()

        print("\nDataset Summary")
        print("------------------------")
        print(f"Rows : {len(df):,}")
        print(f"Columns : {len(df.columns)}")
        print(
            f"Borrowers : {df['borrower_id'].nunique():,}"
        )

        print(
            f"Transactions : {len(df):,}"
        )

        print()

        self.export_csv(df)

        self.export_excel(df)

        return df
    
############################################################
# Main
############################################################

if __name__ == "__main__":

    generator = TransactionGenerator()

    dataset = generator.run()

    print("\nPreview\n")

    print(dataset.head())

    print("\nFinished.")