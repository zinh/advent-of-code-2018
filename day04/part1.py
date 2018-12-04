import re
import datetime

def parse_input(file_name):
    # events chronologically sorted
    events = []
    p = re.compile(r'\[(\d+)\-0*(\d+)\-0*(\d+) 0*(\d+):0*(\d+)\] (.+)')
    with open('input') as f:
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

current_guard = events[0]['guard_id']
last_event = events[0]
for event in events[1:]:
    timestamp = event[0]
    event_type = event[1]
    if event_type['action'] == 'start':
        guard_id = event[1]['guard_id']
        current_guard = guard_id
    elif event_type['action'] == 'asleep':
        pass
    elif event_type['action'] == 'wake':
        pass
    last_event = event
print(parse_input('input')[0:20])
