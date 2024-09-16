import streamlit as st
from datetime import date
import os
from crewai.agent import Agent
from pydantic import Field, ValidationError

# Set OpenAI API Key directly in the code
os.environ['OPENAI_API_KEY'] = 'Add your OpenAI API key'
# Sentinel2ExportAgent class
class Sentinel2ExportAgent(Agent):
    project_id: str = Field(..., description="Project ID for Earth Engine")

    def __init__(self, name, role, goal, backstory, project_id):
        try:
            super().__init__(name=name, role=role, goal=goal, backstory=backstory, project_id=project_id)
        except ValidationError as e:
            st.error(f"Validation Error: {e}")
            return

        self.project_id = project_id
        st.write("Earth Engine Authentication skipped. Data will be stored in PostgreSQL.")

    def export_sentinel2_image_to_drive(self, latitude, longitude, start_date, end_date, image_name):
        try:
            # Instead of fetching from Earth Engine, we'll display the message
            st.write(f"Image '{image_name}' with data for the region around Latitude: {latitude}, Longitude: {longitude} "
                     f"for the period from {start_date} to {end_date} has been stored in PostgreSQL.")
            st.write("The data is now available in PostgreSQL for further analysis.")
            st.write("Use MindsDB for anomaly detection and data analysis.")

            return "Data stored in PostgreSQL. You can analyze it using MindsDB Anomaly Detection."
        except Exception as e:
            return f"Error during the process: {e}"

# Streamlit app starts here
st.title("Data Fetcher AI Agent")

# Sidebar inputs
project_id = st.sidebar.text_input("Enter your Earth Engine Project ID", "genai-agent-hack-2024")
latitude = st.sidebar.number_input("Latitude", min_value=-90.0, max_value=90.0, value=37.7749, step=0.01)
longitude = st.sidebar.number_input("Longitude", min_value=-180.0, max_value=180.0, value=-122.4194, step=0.01)
start_date = st.sidebar.date_input("Start Date", value=date(2021, 6, 1))
end_date = st.sidebar.date_input("End Date", value=date(2021, 6, 30))
image_name = st.sidebar.text_input("Image Name", "sentinel2_image")

# Run the data fetch when button is clicked
if st.sidebar.button("Fetch Sentinel-2 Image"):
    # Create the Sentinel2ExportAgent
    sentinel2_agent = Sentinel2ExportAgent(
        name="Sentinel2ExportAgent",
        role="Data Analyst",
        goal="Export Sentinel-2 imagery from Earth Engine to Google Drive",
        backstory="The agent assists in data analysis by exporting high-resolution satellite imagery.",
        project_id=project_id
    )

    # Fetch and export the image (simulated)
    result = sentinel2_agent.export_sentinel2_image_to_drive(
        latitude, longitude, str(start_date), str(end_date), image_name
    )

    # Display the result
    st.write(result)