import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Load CPU utilization log data from JSON file
CPU_UTILIZATION_FILE = "cpu_utilization_log.json"

def load_cpu_utilization_log(file_path):
    with open(file_path, 'r') as f:
        logs = json.load(f)
    
    df = pd.DataFrame(logs)
    df['time'] = pd.to_datetime(df['time'])  # Convert time to datetime format
    return df

# Load the log data
df_cpu_utilization = load_cpu_utilization_log(CPU_UTILIZATION_FILE)

# Remove the "None" scheduler
df_cpu_utilization = df_cpu_utilization[df_cpu_utilization['scheduler'] != 'None']

# Set up Seaborn for better style
sns.set(style="whitegrid")

# Pivot the data to create a matrix of schedulers vs. time
pivot_df = df_cpu_utilization.pivot_table(index='scheduler', columns='time', values='CPU Utilization')

# Create a heatmap of the utilization
plt.figure(figsize=(16, 8))
sns.heatmap(pivot_df, cmap="magma", cbar_kws={'label': 'CPU Utilization (%)'})


# Title and labels
plt.title('CPU Utilization Heatmap for Schedulers Over Time')
plt.xlabel('Time')
plt.ylabel('Scheduler')

# Format the x-axis timestamp
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%M-%d'))

plt.tight_layout()
plt.show()
