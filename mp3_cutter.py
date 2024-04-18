from time import sleep
import sys

def loadbar(iteration, total, prefix="", suffix="", decimals=1, length=100, fill="卐"):
    percent = 100 * (iteration / float(total))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + "-" * (length - filled_length)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, format(percent, f".{decimals}f"), suffix))
    sys.stdout.flush()

items = list(range(0, 50))
total_items = len(items)

loadbar(0, 1, prefix="Progress:", suffix="Complete", length=total_items)
for i, item in enumerate(items):
    sleep(0.1)
    loadbar(i + 1, total_items, prefix="Progress:", suffix="Complete", length=total_items)
