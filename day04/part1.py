import re
import datetime

def parse_input(file_name):
    # events chronologically sorted
    events = []
    p = re.compile(r'\[(\d+)\-0*(\d+)\-0*(\d+) 0*(\d+):0*(\d+)\] (.+)')
    with open(file_name) as f:
        for line in f:
            parsed = p.match(line).groups()
            year, month, day, hour, minute = [int(p) for p in parsed[:-1]]
            t = datetime.datetime(year, month, day, hour, minute)
            command = parsed[-1]
            events.append([t, parse_action(command)])
    events.sort(key=lambda event: event[0])
    return events

def parse_action(text):
    if text == 'falls asleep':
        return {'action': 'asleep'}
    if text == 'wakes up':
        return {'action': 'wake'}
    p = re.compile(r'Guard #(\d+) begins shift')
    guard_id, = p.match(text).groups()
    return {'action': 'start', 'guard_id': guard_id}

def max_minute(dates):
    time_ranges = [time_range for date in dates.values() for time_range in date]
    t = {i: 0 for i in range(0, 60)}
    for time_range in time_ranges:
        m = (time_range[1] - time_range[0]).seconds // 60
        start_min = time_range[0].minute
        for minute in range(start_min, start_min + m):
            t[minute] += 1
    return max(t.items(), key=lambda x: x[1])

events = parse_input('input1')
current_guard = events[0][1]['guard_id']
last_event = events[0]
guards = {}
for event in events[1:]:
    timestamp = event[0]
    event_type = event[1]
    if event_type['action'] == 'start':
        current_guard = event[1]['guard_id']
    elif event_type['action'] == 'wake':
        sleep_since = last_event[0]
        date = datetime.datetime(sleep_since.year, sleep_since.month, sleep_since.day)
        guard = guards.setdefault(current_guard, {})
        d = guard.setdefault(date, [])
        d.append([sleep_since, timestamp])
    last_event = event

# Part 1
# Get guard with longest sleep
sleeps = []
for guard_id in guards.keys():
    total_sleep = sum([(date[1] - date[0]).seconds for dates in guards[guard_id].values() for date in dates]) // 60
    sleeps.append([guard_id, total_sleep])

guard_id, total_sleep = max(sleeps, key=lambda s: s[1])
print(guard_id)
 most minute
print(max_minute(guards[guard_id]))

# Part 2
guard_with_min = [(guard, max_minute(time_ranges)) for guard, time_ranges in guards.items()]
print(max(guard_with_min, key=lambda x: x[1][1]))
