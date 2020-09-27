from slack_cleaner2 import SlackCleaner
import time, re
from credentials import SLACK_TOKEN
from collections import defaultdict
from pprint import pprint

s = SlackCleaner(SLACK_TOKEN, sleep_for=1)

deleted = 0
retained = 0
first_lines = defaultdict(int)
chars = 100
for msg in s.c.slackbot.msgs(after="20200802"):
    if re.match("push_day_old_data.py", msg.text) is not None: # or re.match("fetch_terminals.py: No 'Location' field found for terminal with ID 55141", msg.text) is not None:
        time.sleep(1)
        msg.delete()
        deleted += 1
    else:
        first_line = msg.text.split('\n')[0][:chars]
        first_lines[first_line] += 1
        print(msg.text)
        print("="*80)
        retained += 1

for f,count in sorted(first_lines.items(), key=lambda item: item[1]):
    print(f"{count:>5}: {f}")
    print("-"*(chars+7))
print(f"Deleted {deleted} Slackbot messages and kept {retained} messages.")
