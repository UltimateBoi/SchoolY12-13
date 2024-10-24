import concurrent.futures
from datetime import datetime

def slow_loop():
    startTime = datetime.now()
    i = 1
    while i <= 10:
        print(f"Question {i}")
        for j in range(100001):
            print(f"   Question {i}.{j}")
        i += 1
    endTime = datetime.now()
    totalTime = endTime - startTime
    totalTimeSeconds = totalTime.total_seconds()
    print(f"{round(totalTimeSeconds, 6)}s")
    with open("times.txt", "a") as f:
        f.writelines(f"Slow Loop took {totalTime}s\n")

def print_questions(i):
    results = []
    results.append(f"Question {i}")
    for j in range(100001):
        results.append(f"   Question {i}.{j}")
    return results

def main():
    startTime = datetime.now()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(print_questions, i) for i in range(1, 11)]
        for future in concurrent.futures.as_completed(futures):
            results = future.result()
            for line in results:
                print(line)
    endTime = datetime.now()
    totalTime = endTime - startTime
    totalTimeSeconds = totalTime.total_seconds()
    print(f"{round(totalTimeSeconds, 6)}s")
    with open("times.txt", "a") as f:
        f.writelines(f"Fast Loop took {totalTime}s\n")
    slow_loop()

if __name__ == "__main__":
    main()