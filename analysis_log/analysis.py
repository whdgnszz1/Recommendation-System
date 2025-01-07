import re
import datetime
import matplotlib.pyplot as plt

memory_pattern = re.compile(
    r'^\[([\d/]+\s+\d{2}:\d{2}:\d{2}),INFO\]\[LCPLATFORM\].*total memory=(\d+)MB,\s+used memory=(\d+)MB, free memory=(\d+)MB'
)

gc_start_pattern = re.compile(r'collection full-gc start')
gc_finish_pattern = re.compile(r'collection full-gc finished')

times = []
total_mem = []
used_mem = []
free_mem = []

removed_mem_times = []
removed_mem_values = []

in_gc = False
before_gc_used = None
next_memory_is_after_gc = False

with open('log_20250105.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # GC 시작 이벤트 감지
        if gc_start_pattern.search(line):
            in_gc = True
            if used_mem:
                before_gc_used = used_mem[-1]
            else:
                before_gc_used = None
            continue

        # GC 완료 이벤트 감지
        if gc_finish_pattern.search(line) and in_gc:
            in_gc = False
            next_memory_is_after_gc = True
            continue

        # 메모리 상태 라인 감지
        match = memory_pattern.search(line)
        if match:
            dt_str = match.group(1)
            total_str = match.group(2)
            used_str = match.group(3)
            free_str = match.group(4)

            dt = datetime.datetime.strptime(dt_str, '%Y/%m/%d %H:%M:%S')
            total_val = int(total_str)
            used_val = int(used_str)
            free_val = int(free_str)

            times.append(dt)
            total_mem.append(total_val)
            used_mem.append(used_val)
            free_mem.append(free_val)

            if next_memory_is_after_gc and before_gc_used is not None:
                removed_memory = before_gc_used - used_val
                removed_mem_times.append(dt)
                removed_mem_values.append(removed_memory)
                next_memory_is_after_gc = False
            continue

plt.figure(figsize=(14, 10))

# 첫 번째 서브플롯: 전체, 사용, 여유 메모리
plt.subplot(2, 1, 1)
plt.plot(times, total_mem, label='Total Memory (MB)', color='blue', linestyle='--')
plt.plot(times, used_mem, label='Used Memory (MB)', color='red', marker='o')
plt.plot(times, free_mem, label='Free Memory (MB)', color='green', marker='x')

plt.title("LCPLATFORM GC Memory Usage Over Time")
plt.xlabel("Time")
plt.ylabel("Memory (MB)")
plt.gcf().autofmt_xdate()
plt.grid(True)
plt.legend()

# 두 번째 서브플롯: 제거된 메모리
plt.subplot(2, 1, 2)
plt.bar(removed_mem_times, removed_mem_values, width=0.01, color='purple', label='Removed Memory (MB)')  # width는 조정 필요
plt.title("Memory Removed by GC Over Time")
plt.xlabel("Time")
plt.ylabel("Removed Memory (MB)")
plt.gcf().autofmt_xdate()
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
