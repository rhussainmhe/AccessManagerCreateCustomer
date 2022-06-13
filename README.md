# Create access manager customer with modified roses name and XID

## Prereqs:
1. Chromedriver
2. Update executable path for Chromedriver on line 14 of CreateDistrict.py

## How to run

1. Update roses.py with your roses name/pw and connected pw
2. Run CreateDistrict.py
3. Enter Oracle ID
4. Double check returned values before entering them in Access Manager create page

## Sample return:

Enter Oracle ID: 999999
Loaded connected login page
Logged into connected
https://connected.mcgraw-hill.com/connected/support.accountSearch.do?accountName=&oksAccountId=182481
Roses name: Made up Roses name
Loaded roses login page
Logged into roses
Loaded roses search page
Searching oracle name Made up Roses name
Found roses name
Found manage link
Found district name + state: Made up Roses name Nashville, Alabama
Loaded manage educational identity search page
Searching district in manage educational identity
Found district
--------------------------------------------------------
Does the oracle id you entered match what was returned?
Entered: 999999 Returned: 999999
--------------------------------------------------------
If yes create new access manager customer using below info

Access Manager Name:     Made up Roses name (AL) 999999
XID:                     (hidden)
