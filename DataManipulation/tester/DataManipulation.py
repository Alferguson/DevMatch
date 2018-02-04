import smartsheet 
import logging 

#Initialize Client
access_token = "voaya5lwe6gzccnw2ebc64rzif"
access_token = "nioc9o1toi4mimk9b5mvskkivz"
access_token = "pz9jqn9hta59a47iha94wlxlhr"
ss_client = smartsheet.Smartsheet(access_token)

# Check that there are no errors
ss_client.errors_as_exceptions(True)


logging.basicConfig(filename='rwsheet.log', level=logging.INFO)

# Requesting Sheets
ss_client.Sheets.get_sheet_as_csv(6072805927217028,"/Users/shockedbunny/Projects/Hackathon/DevMatch/DataManipulation/tester")
ss_client.Sheets.get_sheet_as_csv(5351320140965764,"/Users/shockedbunny/Projects/Hackathon/DevMatch/DataManipulation/tester")

# Extracting Data From Data Base for Matching


# Matching Algorithm 


#Creating New Sheet With Results
sheet_spec = ss_client.models.Sheet({
  'name': 'Finalized Groups',
  'columns': [{
      'title': 'Name',
      'type': 'TEXT_NUMBER',
#     'type': 'CHECKBOX',
#     'symbol': 'STAR'
    }, {
      'title': 'GROUP NUMBER',
      'primary': True,
      'type': 'TEXT_NUMBER'
    }
  ]
})
response = ss_client.Home.create_sheet(sheet_spec)
new_sheet = response.result
an = response
# Getting Information about Data
SheetID_to_share = an.data.id
print "Sheet Id for Manipulation: " + str(an.data.id)
print "/////////////"
print "Server Response: " + str(an.request_response)

