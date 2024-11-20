import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Load the data from a JSON file

with open('scheduler_log.json', 'r') as f:
    data = json.load(f)


# Convert data to a DataFrame
df = pd.DataFrame(data)

# Convert 'time' to datetime
df['time'] = pd.to_datetime(df['time'])

# Visualize events per scheduler
event_counts = df.groupby(['scheduler', 'event']).size().unstack(fill_value=0)

# Bar plot for events per scheduler
event_counts.plot(kind='bar', figsize=(10, 6))
plt.title('Event Counts by Scheduler')
plt.xlabel('Scheduler')
plt.ylabel('Event Count')
plt.xticks(rotation=0)
plt.legend(title='Event')
plt.tight_layout()
plt.show()

# Create a timeline plot
fig, ax = plt.subplots(figsize=(12, 6))
for scheduler, group in df.groupby('scheduler'):
    ax.plot(group['time'], [scheduler] * len(group), 'o-', label=scheduler)

# Format the timeline
ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))
plt.title('Scheduler Event Timeline')
plt.xlabel('Time')
plt.ylabel('Scheduler')
plt.legend(title='Scheduler')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
