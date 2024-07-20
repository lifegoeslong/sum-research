import matplotlib.pyplot as plt

def analyze_trace(trace_file):
    read_count = 0
    openat_count = 0
    close_count = 0
    write_count = 0
    total_count = 0

    with open(trace_file, 'r') as file:
        for line in file:
            if "read(" in line:
                read_count += 1
            elif "openat(" in line:
                openat_count += 1
            elif "close(" in line:
                close_count += 1
            elif "write(" in line:
                write_count += 1
            total_count += 1

    read_percent = (read_count / total_count) * 100
    openat_percent = (openat_count / total_count) * 100
    close_percent = (close_count / total_count) * 100
    write_percent = (write_count / total_count) * 100

    return (read_count, read_percent, openat_count, openat_percent, close_count, close_percent, write_count, write_percent)

def plot_bar_chart(read_count, read_percent, openat_count, openat_percent, close_count, close_percent, write_count, write_percent):
    labels = ['read', 'openat', 'close', 'write']
    counts = [read_count, openat_count, close_count, write_count]
    proportions = [read_percent, openat_percent, close_percent, write_percent]

    fig, ax = plt.subplots(figsize=(8, 6))

    # Bar chart for calling counts
    ax.bar(labels, counts, color=['blue', 'orange', 'green', 'purple'], label='Calling Count')
    for i, count in enumerate(counts):
        ax.text(i, count + 0.01 * max(counts), str(int(count)), ha='center', va='bottom', fontsize=9)

    # Bar chart for proportions
    ax.bar(labels, proportions, color=['lightblue', 'peachpuff', 'lightgreen', 'lavender'], bottom=0, label='Proportion')
    for i, prop in enumerate(proportions):
        ax.text(i, prop + 0.01 * max(proportions), f"{prop:.2f}%", ha='center', va='bottom', fontsize=9)

    ax.set_title('Calling Counts and Proportions of read, openat, close, and write')
    ax.set_xlabel('System Call')
    ax.set_ylabel('Count and Proportion')
    ax.legend()
    plt.show()

# Example usage
read_count, read_percent, openat_count, openat_percent, close_count, close_percent, write_count, write_percent = analyze_trace('trace.txt')
plot_bar_chart(read_count, read_percent, openat_count, openat_percent, close_count, close_percent, write_count, write_percent)
