import csv

def filter_logs(file_path, ip_range, methods, min_response_time):
    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ip = row['ip']
            method = row['method']
            response_time = float(row['response_time'])
            if ip in ip_range and method in methods and response_time >= min_response_time:
                yield row


def analyze_logs(file_path, ip_range, methods, min_response_time):
    unique_ips = set()
    method_counts = {method: 0 for method in methods}
    total_response_time = 0
    log_count = 0

    for log in filter_logs(file_path, ip_range, methods, min_response_time):
        ip = log['ip']
        method = log['method']
        response_time = float(log['response_time'])

        unique_ips.add(ip)
        method_counts[method] += 1
        total_response_time += response_time
        log_count += 1

    avg_response_time = total_response_time / log_count if log_count else 0

    return {
        'Unique IPs': len(unique_ips),
        'Method Counts': method_counts,
        'Average Response Time': avg_response_time
    }

def main_menu():
    while True:
        print("\nServer Log Analysis Menu")
        print("1. Analyze logs")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter log file path: ")
            ip_range = input("Enter IP range (e.g., '192.168.1.1-192.168.1.100'): ").split('-')
            methods = input("Enter HTTP methods (comma-separated, e.g., 'GET,POST'): ").split(',')
            min_response_time = float(input("Enter minimum response time: "))

            stats = analyze_logs(file_path, ip_range, methods, min_response_time)
            print("\nAnalysis Results:")
            print(f"Unique IPs: {stats['Unique IPs']}")
            print(f"HTTP Methods Count: {stats['Method Counts']}")
            print(f"Average Response Time: {stats['Average Response Time']:.2f} seconds")
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()