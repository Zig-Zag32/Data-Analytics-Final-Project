#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# Load data
repair_types = pd.read_csv("repair_types.csv")
technicians = pd.read_csv("technicians.csv")
upcoming_repairs = pd.read_csv("upcoming_repairs.csv")

# Strip whitespace
repair_types.columns = repair_types.columns.str.strip()
technicians.columns = technicians.columns.str.strip()
upcoming_repairs.columns = upcoming_repairs.columns.str.strip()

# Merge on repair_name since that worked for your data
upcoming_repairs_merged = upcoming_repairs.merge(
    repair_types[['repair_name', 'time_in_minutes']],
    on='repair_name',
    how='left'
)

# Sort by severity
if 'severity' not in upcoming_repairs_merged.columns:
    raise ValueError("No 'severity' column found.")

upcoming_repairs_merged = upcoming_repairs_merged.sort_values(by='severity', ascending=False).reset_index(drop=True)

def time_to_minutes(t):
    h, m, s = t.split(':')
    return int(h)*60 + int(m) + int(float(s))

if 'start_time' not in technicians.columns or 'end_time' not in technicians.columns:
    raise ValueError("Technicians must have 'start_time' and 'end_time' columns.")

# Calculate technician available time
technicians['start_min'] = technicians['start_time'].apply(time_to_minutes)
technicians['end_min'] = technicians['end_time'].apply(time_to_minutes)
technicians['available_minutes'] = technicians['end_min'] - technicians['start_min']

if 'employee_id' not in technicians.columns:
    raise ValueError("No 'employee_id' column in technicians.")

# Print technicians available minutes
print("Technicians available minutes:")
print(technicians[['employee_id', 'employee_name', 'start_time', 'end_time', 'available_minutes']])

# Create a dictionary of technician capacities
technician_capacity = {row['employee_id']: row['available_minutes'] for _, row in technicians.iterrows()}

# Print first few repairs to see required time
print("First few repairs:")
print(upcoming_repairs_merged[['repair_id', 'repair_name', 'time_in_minutes']].head())

assignments = []
for _, repair in upcoming_repairs_merged.iterrows():
    required_time = repair.get('time_in_minutes', None)
    assigned_tech = None

    # If required_time is NaN, continue
    if pd.isna(required_time):
        assignments.append(None)
        continue

    # Attempt assignment
    for tech_id, remaining_time in technician_capacity.items():
        if remaining_time >= required_time:
            assigned_tech = tech_id
            technician_capacity[tech_id] -= required_time
            break
    
    assignments.append(assigned_tech)

upcoming_repairs_merged['employee_id'] = assignments

# Check if any assignments were made
print("Sample assignments (first 5):")
print(upcoming_repairs_merged[['repair_id', 'employee_id']].head())

# Save results
final_cols = ['repair_id', 'severity', 'repair_name', 'employee_id']
upcoming_repairs_merged[final_cols].to_csv("upcoming_repairs_assigned.csv", index=False)

print("Check 'upcoming_repairs_assigned.csv' for results.")

