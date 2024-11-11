import streamlit as st

# Title and Description
st.title("Your App Title")
st.write("This is a brief description of your app. Explain what it does here.")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.write("You can add elements here, like inputs or navigation links.")
st.sidebar.selectbox("Choose a section", ["Home", "Settings", "About"])

# Main Content
st.header("Main Content Section")
st.write("This is the main area where your app’s content will go.")

# Example Inputs
text_input = st.text_input("Enter some things:")
st.write("You entered:", text_input)

number_input = st.number_input("Select a numbers : ", min_value=0, max_value=100, value=50)
st.write("Selected number:", number_input)

# Example Button
if st.button("Submit"):
    st.write("Button clicked!")

# Display DataFrame (Optional)
import pandas as pd
df = pd.DataFrame({
    'Column A': [1, 2, 3],
    'Column B': ['X', 'Y', 'Z']
})
st.write("Sample Data Table:")
st.dataframe(df)

# Footer
st.markdown("---")
st.write("Developed by [Your Name]")

# Run this script using: `streamlit run your_script.py`
