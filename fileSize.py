import os

def average_size(*filenames: str) -> float:

    total_bytes = 0
    count = 0
    for name in filenames:
        if not os.path.exists(name):
            print(f"Warning: '{name}' not found, skipping.")
            continue
        if not os.path.isfile(name):
            print(f"Warning: '{name}' is not a regular file, skipping.")
            continue
        try:
            size = os.path.getsize(name)
        except OSError as e:
            print(f"Warning: cannot access '{name}': {e}")
            continue
        total_bytes += size
        count += 1

    if count == 0:
        print("No valid files provided.")
        return 0.0

    avg_kb = (total_bytes / count) / 1024.0
    avg_kb_rounded = round(avg_kb)
    print(f"Average size: {avg_kb_rounded} KB")
    return avg_kb

if __name__ == "__main__":
    average_size("test.txt", "hello.mp3")
