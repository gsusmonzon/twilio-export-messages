import csv
import requests

account_sid = ""
auth_pass = ""

results_per_page = 1000
num_pages = 500
start_date = "2010-04-01"

base_url = "https://api.twilio.com"
initial_page = "/" + start_date + "/Accounts/" + account_sid + "/Messages.json?PageSize=" + str(results_per_page)

response = requests.get(base_url + initial_page, auth=(account_sid, auth_pass)).json()
next_page = response['next_page_uri']

page = 0
data = response['messages']

# print response['previous_page_uri']
# print response

if not next_page == None:
  while page < num_pages:
    response = requests.get(base_url + next_page, auth=(account_sid, auth_pass)).json()

    next_page = response['next_page_uri']

    print "On page: " + str(page)

    data = data + response['messages']
    page += 1

    if next_page == None:
      print "No more pages"
      break

csv_file = open('export.csv', 'w')
csvwriter = csv.writer(csv_file)

count = 0

for message in data:

  if count == 0:
    header = message.keys()
    csvwriter.writerow(header)
    count += 1

  #only include outbound sms because inbound ascii/emojis throws csv writer errors
  if message.values()[2] == "outbound-api":
    csvwriter.writerow(message.values())

csv_file.close()

print "Done!"