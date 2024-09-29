import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('car_rental_data.csv')
    return data

# Load car rental data
car_data = load_data()

# Streamlit app title
st.title("Car Rental Recommendation System")

# Sidebar for user inputs
st.sidebar.header("Filter your car search")

# Create filter options
category_filter = st.sidebar.selectbox('Category', car_data['Category'].unique())
fuel_type_filter = st.sidebar.selectbox('Fuel Type', car_data['Fuel Type'].unique())
price_filter = st.sidebar.slider('Price Per Day (INR)', int(car_data['Price Per Day (INR)'].min()), int(car_data['Price Per Day (INR)'].max()))
seats_filter = st.sidebar.selectbox('Number of Seats', car_data['Number of Seats'].unique())
air_conditioning_filter = st.sidebar.selectbox('Air Conditioning', ['Yes', 'No'])

# Filter dataset based on user input
filtered_data = car_data[
    (car_data['Category'] == category_filter) &
    (car_data['Fuel Type'] == fuel_type_filter) &
    (car_data['Price Per Day (INR)'] <= price_filter) &
    (car_data['Number of Seats'] == seats_filter) &
    (car_data['Air Conditioning'] == air_conditioning_filter)
]

# Display filtered results
st.subheader(f"Available {category_filter} Cars:")
st.write(filtered_data[['Car Name', 'Features', 'Price Per Day (INR)', 'Safety Rating']])

# Display car details for selected cars
if not filtered_data.empty:
    st.subheader("Car Details")
    for index, row in filtered_data.iterrows():
        st.write(f"**Car Name**: {row['Car Name']}")
        st.write(f"**Features**: {row['Features']}")
        st.write(f"**Price Per Day**: {row['Price Per Day (INR)']} INR")
        st.write(f"**Safety Rating**: {row['Safety Rating']} / 5")
        st.write("---")
else:
    st.write("No cars found matching your criteria.")
