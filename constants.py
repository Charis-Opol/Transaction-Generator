"""
Constants used throughout the simulator.
"""

DISTRICTS = [
    "Kampala",
    "Mukono",
    "Wakiso",
    "Jinja",
    "Gulu",
    "Mbarara",
    "Mbale",
    "Arua",
    "Lira",
    "Masaka",
    "Kabale",
    "Soroti"
]

REGIONS = {
    "Central":["Kampala","Mukono","Wakiso","Masaka"],
    "Eastern":["Jinja","Mbale","Soroti"],
    "Northern":["Gulu","Lira","Arua"],
    "Western":["Mbarara","Kabale"]
}

OCCUPATIONS = {
    "Farmer":0.35,
    "Trader":0.25,
    "Boda Rider":0.12,
    "Salaried":0.18,
    "Shop Owner":0.06,
    "Casual Worker":0.04
}

NETWORKS = [
    "MTN",
    "Airtel"
]

CHANNELS = [
    "USSD",
    "Agent",
    "Mobile App"
]

MERCHANT_TYPES = [
    "School Fees",
    "Groceries",
    "Fuel",
    "Agriculture",
    "Medical",
    "Utility",
    "Rent",
    "Savings",
    "Business Stock",
    "Personal Transfer"
]

OCCUPATION_BEHAVIOUR = {

    "Farmer":{

        "income_frequency":0.45,

        "base_transaction_size":60000,

        "seasonality":True,

        "income_bias":"seasonal"

    },

    "Trader":{

        "income_frequency":0.90,

        "base_transaction_size":45000,

        "seasonality":False,

        "income_bias":"daily"

    },

    "Salaried":{

        "income_frequency":0.25,

        "base_transaction_size":85000,

        "seasonality":False,

        "income_bias":"monthly"

    },

    "Boda Rider":{

        "income_frequency":0.95,

        "base_transaction_size":25000,

        "seasonality":True,

        "income_bias":"daily"

    },

    "Shop Owner":{

        "income_frequency":0.80,

        "base_transaction_size":70000,

        "seasonality":False,

        "income_bias":"business"

    },

    "Casual Worker":{

        "income_frequency":0.55,

        "base_transaction_size":35000,

        "seasonality":True,

        "income_bias":"irregular"

    }
}

OCCUPATION_BEHAVIOUR = {

    "Farmer": {
        "income_days":[10,20],
        "income_probability":0.45,
        "expense_probability":0.55,
        "base_income":90000,
        "base_expense":35000,
        "preferred_channel":"Agent",
        "preferred_network":"MTN"
    },

    "Trader": {
        "income_days":[1,2,3,4,5,6],
        "income_probability":0.75,
        "expense_probability":0.65,
        "base_income":60000,
        "base_expense":45000,
        "preferred_channel":"USSD",
        "preferred_network":"MTN"
    },

    "Salaried": {
        "income_days":[28],
        "income_probability":0.15,
        "expense_probability":0.40,
        "base_income":250000,
        "base_expense":55000,
        "preferred_channel":"App",
        "preferred_network":"Airtel"
    },

    "Boda Rider": {
        "income_days":[1,2,3,4,5,6,7],
        "income_probability":0.80,
        "expense_probability":0.70,
        "base_income":40000,
        "base_expense":28000,
        "preferred_channel":"USSD",
        "preferred_network":"MTN"
    },

    "Shop Owner": {
        "income_days":[1,2,3,4,5,6],
        "income_probability":0.82,
        "expense_probability":0.75,
        "base_income":70000,
        "base_expense":60000,
        "preferred_channel":"Agent",
        "preferred_network":"MTN"
    },

    "Casual Worker": {
        "income_days":[2,4,6],
        "income_probability":0.40,
        "expense_probability":0.55,
        "base_income":45000,
        "base_expense":30000,
        "preferred_channel":"USSD",
        "preferred_network":"Airtel"
    }

}

MERCHANT_BEHAVIOURS = {

    "Received":[

        "Salary",
        "Crop Sales",
        "Business Income",
        "Family Support",
        "Loan Disbursement",
        "Savings Withdrawal"

    ],

    "Sent":[

        "School Fees",
        "Fuel",
        "Groceries",
        "Medical",
        "Rent",
        "Utilities",
        "Business Stock",
        "Savings Deposit",
        "Personal Transfer"

    ]

}