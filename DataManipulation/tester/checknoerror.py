import smartsheet 
import logging 

#Initialize Client
access_token = "voaya5lwe6gzccnw2ebc64rzif"
access_token = "nioc9o1toi4mimk9b5mvskkivz"
access_token = "pz9jqn9hta59a47iha94wlxlhr"
ss_client = smartsheet.Smartsheet(access_token)

# Check that there are no errors
ss_client.errors_as_exceptions(True)

# Requesting Sheets
ss_client.Sheets.get_sheet_as_csv(3585229588850564,"/Users/shockedbunny/Projects/Hackathon/DevMatch/DataManipulation/tester")
ss_client.Sheets.get_sheet_as_csv(5351320140965764,"/Users/shockedbunny/Projects/Hackathon/DevMatch/DataManipulation/tester")




