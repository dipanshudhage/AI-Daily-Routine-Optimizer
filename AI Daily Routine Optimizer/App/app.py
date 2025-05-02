import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

st.set_page_config(page_title="Smart Daily Routine Optimizer", page_icon="🧠", layout="wide")
st.title("🧠 Smart AI-Free Daily Routine Optimizer")
st.markdown("Generate a practical and balanced routine based on your priorities and energy cycle. ⚙️")

# --- Sidebar Inputs ---
st.sidebar.header("🔧 Customize Your Day")

wake_time = st.sidebar.time_input("⏰ Wake-up Time", value=datetime.time(7, 0))
sleep_time = st.sidebar.time_input("😴 Sleep Time", value=datetime.time(22, 0))

task_options = [
    "Study", "Exercise", "Work", "Relax", "Reading", "Social",
    "Entertainment", "Learning", "Nap", "Household", "Break"
]

selected_tasks = st.sidebar.multiselect(
    "🏆 Select Priorities (Pick up to 8)",
    task_options,
    default=["Study", "Exercise", "Relax", "Reading"]
)

focus_time = st.sidebar.radio("🧠 Peak Focus Time", ["Morning", "Afternoon", "Evening"])
include_breaks = st.sidebar.checkbox("☕ Include Short Breaks", value=True)
include_naps = st.sidebar.checkbox("💤 Include Power Nap", value=False)

# --- Time Calculations ---
start_dt = datetime.datetime.combine(datetime.date.today(), wake_time)
end_dt = datetime.datetime.combine(datetime.date.today(), sleep_time)
if end_dt <= start_dt:
    end_dt += datetime.timedelta(days=1)

total_minutes = int((end_dt - start_dt).total_seconds() // 60)
available_slots = total_minutes // 60  # 1-hour granularity

# --- Core Routine Logic ---
def generate_routine(tasks, focus_time, breaks, naps):
    routine = []
    task_pool = tasks.copy()
    
    fixed_slots = []
    if breaks:
        fixed_slots += [11, 15, 18]  # Morning, Afternoon, Evening breaks
    if naps:
        fixed_slots += [14]  # Post-lunch nap
    
    slot_plan = []
    task_hours = {task: 1 for task in task_pool}
    remaining_hours = available_slots - len(fixed_slots)

    # Add remaining time smartly to tasks
    while remaining_hours > 0:
        for task in task_pool:
            if remaining_hours == 0:
                break
            task_hours[task] += 1
            remaining_hours -= 1

    focus_map = {
        "Morning": list(range(8, 12)),
        "Afternoon": list(range(13, 16)),
        "Evening": list(range(17, 20))
    }

    current_hour = wake_time.hour
    used_slots = 0

    while used_slots < available_slots:
        hour_str = f"{(current_hour % 24):02d}:00"

        if current_hour in fixed_slots:
            if naps and current_hour == 14:
                routine.append((hour_str, "Nap"))
            else:
                routine.append((hour_str, "Break"))
        else:
            selected = None
            for task, hours in sorted(task_hours.items(), key=lambda x: -x[1]):
                if hours > 0:
                    # Prioritize focus-time tasks
                    if (task in ["Study", "Work", "Learning"]) and current_hour in focus_map[focus_time]:
                        selected = task
                        break
                    if not selected:
                        selected = task
            if selected:
                routine.append((hour_str, selected))
                task_hours[selected] -= 1
            else:
                routine.append((hour_str, "Free Slot"))

        current_hour += 1
        used_slots += 1

    return routine

# --- UI Output ---
if st.sidebar.button("📅 Generate My Smart Routine"):
    routine = generate_routine(selected_tasks, focus_time, include_breaks, include_naps)
    
    st.subheader("📋 Your Personalized Smart Schedule")
    for time, task in routine:
        st.write(f"**{time}** → {task}")

    st.subheader("📊 Time Distribution")
    df = pd.DataFrame(routine, columns=["Time", "Task"])
    pie_data = df["Task"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(pie_data.values, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

    st.subheader("📥 Download Schedule")
    buffer = StringIO()
    for time, task in routine:
        buffer.write(f"{time} → {task}\n")
    st.download_button("Download as .txt", buffer.getvalue(), file_name="optimized_schedule.txt")

    st.success("✅ Schedule Generated Successfully!")

    st.subheader("💡 Suggestions")
    if "Study" in selected_tasks:
        st.markdown("📚 Use Pomodoro: 25 mins study + 5 min break.")
    if "Exercise" in selected_tasks:
        st.markdown("🏋️ Early exercise can boost focus and energy.")
    if include_naps:
        st.markdown("💤 15–20 min naps post-lunch improve productivity.")
