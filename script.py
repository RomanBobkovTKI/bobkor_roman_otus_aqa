import subprocess
from collections import defaultdict
from datetime import datetime

def get_ps_output():
    result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, text=True)
    return result.stdout.splitlines()

def parse_ps(lines):
    users = set()
    user_process_count = defaultdict(int)
    total_processes = 0

    total_cpu = 0.0
    total_mem = 0.0

    max_cpu = (0.0, "")
    max_mem = (0.0, "")

    for line in lines[1:]:
        parts = line.split(None, 10)
        if len(parts) < 11:
            continue

        user = parts[0]
        cpu = float(parts[2])
        mem = float(parts[3])
        command = parts[10]

        users.add(user)
        user_process_count[user] += 1
        total_processes += 1

        total_cpu += cpu
        total_mem += mem

        if cpu > max_cpu[0]:
            max_cpu = (cpu, command)

        if mem > max_mem[0]:
            max_mem = (mem, command)

    return {
        "users": users,
        "user_process_count": user_process_count,
        "total_processes": total_processes,
        "total_cpu": total_cpu,
        "total_mem": total_mem,
        "max_cpu": max_cpu,
        "max_mem": max_mem
    }

def format_command(cmd):
    return cmd[:20]

def generate_report(data):
    lines = []

    lines.append("Отчёт о состоянии системы:")
    lines.append(f"Пользователи системы: {', '.join(sorted(data['users']))}")
    lines.append(f"Процессов запущено: {data['total_processes']}\n")

    lines.append("Пользовательских процессов:")
    for user, count in data['user_process_count'].items():
        lines.append(f"{user}: {count}")

    lines.append("")
    lines.append(f"Всего памяти используется: {data['total_mem']:.1f}%")
    lines.append(f"Всего CPU используется: {data['total_cpu']:.1f}%")

    lines.append(f"Больше всего памяти использует: {format_command(data['max_mem'][1])}")
    lines.append(f"Больше всего CPU использует: {format_command(data['max_cpu'][1])}")

    return "\n".join(lines)

def save_report(report):
    now = datetime.now().strftime("%d-%m-%Y-%H:%M-scan.txt")
    with open(now, "w", encoding="utf-8") as f:
        f.write(report)
    return now

def main():
    lines = get_ps_output()
    data = parse_ps(lines)
    report = generate_report(data)

    print(report)
    filename = save_report(report)
    print(f"\nОтчёт сохранён в файл: {filename}")

if __name__ == "__main__":
    main()