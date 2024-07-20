def analyze_trace(trace_file):
    rt_sigprocmask_count = 0
    rt_sigaction_count = 0
    total_count = 0

    with open(trace_file, 'r') as file:
        for line in file:
            if "rt_sigprocmask" in line:
                rt_sigprocmask_count += 1
            elif "rt_sigaction" in line:
                rt_sigaction_count += 1
            total_count += 1

    rt_sigprocmask_percent = (rt_sigprocmask_count / total_count) * 100
    rt_sigaction_percent = (rt_sigaction_count / total_count) * 100

    print(f"rt_sigprocmask count: {rt_sigprocmask_count}")
    print(f"rt_sigprocmask percentage: {rt_sigprocmask_percent:.2f}%")
    print(f"rt_sigaction count: {rt_sigaction_count}")
    print(f"rt_sigaction percentage: {rt_sigaction_percent:.2f}%")

# Example usage
analyze_trace('trace.txt')
