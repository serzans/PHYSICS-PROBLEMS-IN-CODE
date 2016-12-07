import numpy as np



#  


EBITDA={2010:1644.0,2011:1644.0,2012:1644.0}

print EBITDA


# Enterprise value
EV=EBITDA*M

# Bank fee percentage of EV
Fee_percentage=0.015

# Bank fees
Fees=Fee_percentage*EV

# Total Uses
Total_Uses=EV+Fees


# Debt capital structure
# Senior debt percentage
SD_percentage=0.30

# Mezzanine debt perceentage
Mez_percentage=0.20

# Equity percentage
EqV_percentage=1-SD_percentage-Mez_percentage



# Senior debt
SD=SD_percentage*EV

# Mezzanine debt
Mez=Mez_percentage*EV

# Equity
EqV=EqV_percentage*EV






FCC=1.1

# Entry multiple
M_entry=7.0

# Exit multiples
M_exit=[6.0,7.0,8.0]





