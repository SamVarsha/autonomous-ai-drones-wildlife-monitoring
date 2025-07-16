import csv

detections = [
    ['Deer', '12:01:34', 'X:10, Y:15'],
    ['Elephant', '12:03:10', 'X:18, Y:25']
]

with open('detections_log.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Animal', 'Timestamp', 'Location'])
    writer.writerows(detections)
