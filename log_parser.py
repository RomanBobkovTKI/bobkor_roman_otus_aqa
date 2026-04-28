import re
import json
import os
import argparse
from collections import Counter
from heapq import nlargest

LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<date>.*?)\] '
    r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>.*?)" '
    r'(?P<status>\d+) (?P<size>\d+) '
    r'"(?P<referer>.*?)" "(?P<agent>.*?)" (?P<duration>\d+)'
)


def parse_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        return match.groupdict()
    return None


def process_file(filepath):
    total_requests = 0
    methods = Counter()
    ips = Counter()
    longest_requests = []

    with open(filepath, 'r') as f:
        for line in f:
            parsed = parse_line(line)
            if not parsed:
                continue

            total_requests += 1

            method = parsed['method']
            ip = parsed['ip']
            duration = int(parsed['duration'])

            methods[method] += 1
            ips[ip] += 1

            longest_requests.append({
                "ip": ip,
                "date": f"[{parsed['date']}]",
                "method": method,
                "url": parsed['url'],
                "duration": duration
            })

    top_ips = dict(ips.most_common(3))
    top_longest = nlargest(3, longest_requests, key=lambda x: x['duration'])

    result = {
        "top_ips": top_ips,
        "top_longest": top_longest,
        "total_stat": dict(methods),
        "total_requests": total_requests
    }

    return result


def save_and_print(result, filename):
    json_name = filename + ".json"

    with open(json_name, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"\n📊 Статистика для {filename}")
    print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Файл или директория с логами")

    args = parser.parse_args()

    if os.path.isfile(args.path):
        result = process_file(args.path)
        save_and_print(result, args.path)

    elif os.path.isdir(args.path):
        for file in os.listdir(args.path):
            full_path = os.path.join(args.path, file)

            if os.path.isfile(full_path):
                result = process_file(full_path)
                save_and_print(result, full_path)

    else:
        print("❌ Неверный путь")


if __name__ == "__main__":
    main()