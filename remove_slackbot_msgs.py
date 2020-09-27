from slack_cleaner2 import SlackCleaner
import time, re
from credentials import SLACK_TOKEN
s = SlackCleaner(SLACK_TOKEN, sleep_for=1)

deleted = 0
retained = 0
for msg in s.c.slackbot.msgs(after="20200802"):
    if re.match("push_day_old_data.py", msg.text) is not None:
        time.sleep(1)
        msg.delete()
        deleted += 1
    else:
        print(msg.text)
        retained += 1

print(f"Deleted {deleted} Slackbot messages and kept {retained} messages.")
