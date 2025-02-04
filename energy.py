import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Load Data
def load_data():
    file_path = r"C:\Users\HARISH KARTHICK\OneDrive\Desktop\ABINAYA\Energy_consumption.csv"
    df = pd.read_csv(file_path, parse_dates=["Timestamp"])
    return df


def main():
    st.title("Energy Consumption Alert System")

    df = load_data()

    # Sidebar for threshold selection
    st.sidebar.header("Settings")
    threshold = st.sidebar.slider("Energy Consumption Alert Threshold", min_value=int(df['EnergyConsumption'].min()),
                                  max_value=int(df['EnergyConsumption'].max()), value=80)

    # Display dataset
    st.subheader("Dataset Overview")
    st.dataframe(df.head())

    # Plot energy consumption over time
    st.subheader("Energy Consumption Over Time")
    fig, ax = plt.subplots()
    ax.plot(df['Timestamp'], df['EnergyConsumption'], label='Energy Consumption', color='b')
    ax.axhline(y=threshold, color='r', linestyle='--', label='Alert Threshold')
    ax.set_xlabel("Time")
    ax.set_ylabel("Energy Consumption")
    ax.legend()
    st.pyplot(fig)

    # Alert System
    st.subheader("Consumption Alerts")
    high_usage = df[df['EnergyConsumption'] > threshold]
    if not high_usage.empty:
        st.warning("High energy consumption detected at the following times:")
        st.dataframe(high_usage[['Timestamp', 'EnergyConsumption']])
    else:
        st.success("Energy consumption is within normal limits.")

    # Recommendations
    st.subheader("Energy Saving Tips")
    st.write("- Optimize HVAC usage by maintaining a moderate temperature.")
    st.write("- Reduce lighting usage when not necessary.")
    st.write("- Increase reliance on renewable energy sources where possible.")


if __name__ == "__main__":
    main()
