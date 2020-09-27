from slack_cleaner2 import SlackCleaner
import time, re
from credentials import SLACK_TOKEN
from collections import defaultdict
from pprint import pprint

s = SlackCleaner(SLACK_TOKEN, sleep_for=1)

deleted = 0
retained = 0
first_lines = defaultdict(int)
for msg in s.c.slackbot.msgs(after="20200802"):
    if re.match("push_day_old_data.py", msg.text) is not None:
        time.sleep(1)
        msg.delete()
        deleted += 1
    else:
        first_line = msg.text.split('\n')[0][:100]
        first_lines[first_line] += 1
        print(msg.text)
        print("="*80)
        retained += 1

for f,c in first_lines.items():
    print(c,f)
    print("-"*80)
print(f"Deleted {deleted} Slackbot messages and kept {retained} messages.")
