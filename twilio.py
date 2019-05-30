import csv
import requests
import codecs

account_sid = ""
auth_pass = ""

results_per_page = 1000
num_pages = 1000
start_date = "2010-04-01"

page = 0
base_url = "https://api.twilio.com"
initial_page = "/" + start_date + "/Accounts/" + account_sid + "/Messages.json?PageSize=" + str(results_per_page)
next_page = None
write_header = True

csv_file = codecs.open('export.csv', 'w')
csvwriter = csv.writer(csv_file)

while page < num_pages:

  if page == 0:
    response = requests.get(base_url + initial_page, auth=(account_sid, auth_pass)).json()
  else:
    response = requests.get(base_url + next_page, auth=(account_sid, auth_pass)).json()

  next_page = response['next_page_uri']
  data = response['messages']

  print("On page: " + str(page))
  page += 1

  for message in data:

    if write_header:
      header = message.keys()
      csvwriter.writerow(header)
      write_header = False

    csvwriter.writerow([s.encode('utf-8') if type(s) is unicode else s for s in message.values()])


  if next_page == None:
    print("No more pages")
    break

csv_file.close()
print("Done!")
