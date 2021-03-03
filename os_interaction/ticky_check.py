""""#!/usr/bin/env python3"""

import re
import os
from collections import defaultdict
import operator
import csv


def analyze_syslog(syslog):
    with open(syslog) as f:
        lines = f.readlines()

        error_freqs = defaultdict(int)
        per_user = {}
        for line in lines:
            msg = find_error_message(line)
            if msg is not None:
                error_freqs[msg[1]] += 1
                per_user = increment_count(per_user, msg[2], 1)
                continue
            msg = find_info_message(line)
            if msg is not None:
                per_user = increment_count(per_user, msg[3], 0)

    error_freq_sorted = {e: f for e, f in sorted(error_freqs.items(), key=operator.itemgetter(1), reverse=True)}
    per_user_sorted = {user: count for user, count in sorted(per_user.items())}
    return error_freq_sorted, per_user_sorted


def find_error_message(line):
    error_pattern = r"ERROR ([\w ']+) \(([\w\.]+)\)"
    return re.search(error_pattern, line)


def find_info_message(line):
    info_pattern = r"INFO ([\w ']+) \[#(\d+)\] \(([\w\.]+)\)"
    return re.search(info_pattern, line)


def print_dictionaries(error_dictionaries):
    for msg, count in error_dictionaries[0].items():
        print(f'{msg}: {count}')
    print('--------------------------------')
    for user, count in error_dictionaries[1].items():
        print(f'{user}: {count}')


def print_error_count(error_dictionaries):
    error_description_count = 0
    for count in error_dictionaries[0].values():
        error_description_count += count

    error_id_count = 0
    for count in error_dictionaries[1].values():
        error_id_count += count[1]

    print(f'error_description_count: {error_description_count}')
    print(f'error_id_count: {error_id_count}')


def increment_count(pu_dict, key, index):
    if key not in pu_dict.keys():
        if index == 0:
            pu_dict[key] = [1, 0]
        else:
            pu_dict[key] = [0, 1]
        return pu_dict

    counts = pu_dict[key]
    counts[index] += 1
    pu_dict[key] = counts
    return pu_dict


def make_error_msg_csv(error_dictionary):
    location = os.path.join(os.getcwd(), 'error_message.csv')
    with open(location, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Error', 'Count'])
        for msg, count in error_dictionary.items():
            writer.writerow([msg, str(count)])


def make_user_statistics_csv(per_user):
    location = os.path.join(os.getcwd(), 'user_statistics.csv')
    with open(location, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Username', 'INFO', 'ERROR'])
        for user, msgs in per_user.items():
            writer.writerow([user, msgs[0], msgs[1]])


def main():
    syslog_location = os.path.join(os.getcwd(), 'syslog.log')
    error_dictionaries = analyze_syslog(syslog_location)

    # print_dictionaries(error_dictionaries)
    # print_error_count(error_dictionaries)

    make_error_msg_csv(error_dictionaries[0])
    make_user_statistics_csv(error_dictionaries[1])


main()

