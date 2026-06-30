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