import json
import os
import time
import random

backend = r'C:\Users\bliss\arki-system\backend'
agents_file = r'C:\Users\bliss\arki-system\backend\agents\agents.json'
orchestration_file = r'C:\Users\bliss\arki-system\backend\orchestration.json'
logs_dir = r'C:\Users\bliss\arki-system\backend\logs'
dashboard_file = os.path.join(logs_dir, 'dashboard.html')

os.makedirs(logs_dir, exist_ok=True)

with open(agents_file, 'r', encoding='utf-8') as f:
    agents = json.load(f)

revenue_summary = {}

for agent in agents:
    name = agent['Name']
    layer = agent['Layer']
    tasks = agent['Tasks']
    revenue = agent['RevenueImpact']

    total_revenue = 0
    for task in tasks:
        task_id = random.randint(1000,9999)
        task_revenue = random.randint(50,500)  # simulated revenue per task
        total_revenue += task_revenue

        log_file = os.path.join(logs_dir, f"{layer}_{name}_log.txt")
        with open(log_file, 'a', encoding='utf-8') as log:
            log.write(f"[{time.strftime('%H:%M:%S')}] Agent {name} ({layer}) executing task {task} | RevenueImpact: {revenue} | Revenue: | TaskID:{task_id}\n")
        time.sleep(random.uniform(0.1,0.5))

    revenue_summary[name] = total_revenue

# Create simple dashboard HTML
html_content = "<html><head><title>Arkiyalink Dashboard</title></head><body>"
html_content += "<h1>Arkiyalink Agent Revenue Dashboard</h1>"
html_content += "<table border='1'><tr><th>Agent</th><th>Total Revenue</th></tr>"
for agent, rev in revenue_summary.items():
    html_content += f"<tr><td>{agent}</td><td></td></tr>"
html_content += "</table></body></html>"

with open(dashboard_file, 'w', encoding='utf-8') as f:
    f.write(html_content)
