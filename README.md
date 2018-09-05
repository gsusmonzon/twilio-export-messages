
# twilio-export-messages
python script to export twilio message logs en masse


- Input account_sid and auth_pass with your credentials. Check Twilio API Explorer if unsure.
- To run the script in terminal: `python twilio.py`

Known issue: if inbound messages contain emojis or strange characters the csv writing throws an error. Fixed this by filtering to only write outbound messages. If you have a fix please PR it.