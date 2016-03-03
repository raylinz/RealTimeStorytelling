import redis
import json
import time
import sys

conn = redis.Redis()

while 1:

    keys = conn.keys()

    if len(keys) == 0 :
        continue

    values = conn.mget(keys)

    try:
        deltas = [float(v) for v in values]
    except TypeError:
        print keys
        continue

    if len(deltas):
        rate = float(len(deltas)) / (sum(deltas)
    else:
        rate = 0

    print json.dumps({"rate":rate})
    sys.stdout.flush()

    time.sleep(0.5)
