# ⚡ Electrical Equipment Maintenance Optimization
Group: George Zack, Saqlain Anjum, Ki Hwang

## **Overview**
This project aims to **optimize** the assignment of upcoming electrical equipment repairs to a team of technicians. By leveraging available data about work orders, technician schedules, and repair characteristics, we seek to allocate tasks more efficiently, reduce the risk of severe failures, and maximize the effectiveness of the maintenance team. The ultimate goal is to support executive decision-making for maximizing company revenue while ensuring long-term sustainability of our infrastructure. 🌱

**Key Objectives:**
1. **Optimal Technician Scheduling:**  
   Ensure each technician’s schedule is fully utilized and that repairs don’t spill over into subsequent workdays, making the most of their on-duty time. 🛠️
   
2. **Impactful Hardware Failures Insight:**  
   Identify which repairs are most critical by severity or frequency to guide investment in preventative measures and infrastructure improvements. 🔧
   
3. **Efficient Repair Assignments:**  
   Assign upcoming repairs to the right technicians, matching their availability, skills, and time constraints to reduce downtime and increase operational efficiency. 🚀

## **Datasets**

The project utilizes three primary datasets:

1. **`repair_types.csv`**  
   - **Columns:**
     - `repair_id`: Unique identifier for each repair type
     - `repair_name`: Name or category of the repair
     - `repair_value`: Metric indicating how the repair reduces fire risk
     - `time_in_minutes`: Estimated time required to complete the repair

2. **`technicians.csv`**  
   - **Columns:**
     - `employee_name`: Technician’s name
     - `employee_id`: Unique identifier for each technician
     - `start_time`: Start of shift (HH:MM:SS)
     - `end_time`: End of shift (HH:MM:SS)
     - `number_of_days`: Number of days per week the technician works

3. **`upcoming_repairs.csv`**  
   - **Columns:**
     - `repair_id`: Unique identifier for the upcoming repair
     - `severity`: Severity rating (0 to 1)
     - `repair_name`: The type of upcoming repair (matches `repair_types`)
     - `employee_id`: Assigned technician ID, if any (may be null)

## **Approach for the Backend Script**

1. **Data Preparation & Cleaning:**  
   - Strip whitespace from column headers  
   - Validate presence of required columns (`severity`, `start_time`, `end_time`, `employee_id`)

2. **Merging & Prioritizing Repairs:**  
   - Merge `upcoming_repairs` with `repair_types` to determine required time  
   - Sort repairs by severity (highest first) to address the most critical tasks early ⏱️

3. **Calculating Technician Availability:**  
   - Convert `start_time`/`end_time` into total available minutes  
   - Create a dictionary to track each technician’s remaining available minutes

4. **Assigning Repairs:**  
   - Iterate over the sorted `upcoming_repairs` list  
   - Assign repairs to a technician with sufficient available time  
   - Reduce that technician’s available time accordingly 🎯

5. **Results:**  
   - Output assignments to `upcoming_repairs_assigned.csv` including `repair_id`, `severity`, `repair_name`, and `employee_id`

## **How to Run**

**Prerequisites:**
- Python 3.x  
- Pandas library (`pip install pandas`)

**File Structure:**  
Place the following files in the same directory:
- `repair_types.csv`
- `technicians.csv`
- `upcoming_repairs.csv`

**Execution:**  
```bash
python assign_repairs.py
```

## **Final Results and Visualization using Qlik**
1. **Severity and Priority Dashboard**
2. **Repair Task Assignment Dashboard**
