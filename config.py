"""
Global configuration for the synthetic mobile money data generator.
"""

RANDOM_SEED = 42

# Population
NUM_BORROWERS = 3000
#NUM_BORROWERS = 10
#NUM_BORROWERS = 100
#NUM_BORROWERS = 1000
#NUM_BORROWERS = 5000

# Simulation period
START_YEAR = 2025
MONTHS = 12

# Average transactions per borrower each month
MIN_TRANSACTIONS = 10
MAX_TRANSACTIONS = 30

# Loan defaults
DEFAULT_RATE = 0.18

# Export
EXPORT_CSV = True
EXPORT_EXCEL = True

# Currency
CURRENCY = "UGX"