import streamlit as st
import pandas as pd
import openpyxl
import datetime

if "page" not in st.session_state:
    st.session_state.page = 1

# Define the content for each page
page_contents = {
    1: "Page 1 Content",
    2: "Page 2 Content",
}

# Streamlit app
st.title("Control Chart Maker")

# Step 1: Welcome and Project Name

if st.session_state.page == 1:
    # st.write(page_contents[st.session_state.page])

    st.header("Welcome!")


    # Step 2: First Choice
    st.header("Type of Control Chart")
    first_option = st.selectbox("Select among the options:", ["Attribute", "Variable"])

    # Step 3: Second Choice
    if first_option == "Variable":
        st.header("Choose the sample size")
        second_option = st.selectbox("Select among the options:", ["Small", "Large"])
    else:
        st.header("Choose the type")
        second_option_1 = st.selectbox("Select among the options:", ["Defective","Defects"])
        second_option_2 = st.selectbox("Select whether n is varying or constant:", ["Constant","Varying"])

    st.header("Select the Control Chart")
    if first_option == "Variable":
        if second_option == "Small":
            third_option = st.selectbox("Select among the options", ["X-R"])
        else:
            third_option = st.selectbox("Select among the options", ["X-S"])
    else:
        if second_option_1 == "Defective":
            third_option = st.selectbox("Select among the options", ["P","nP"])
        else:
            third_option = st.selectbox("Select among the options", ["C","U"])



    if st.button("Next Page"):
        st.session_state.page += 1
        st.experimental_rerun()

        # Reset to the first page when you reach the last page
        if st.session_state.page > len(page_contents):
            st.session_state.page = 1



if st.session_state.page == 2:
    # give the path of excel file
    file_path = "/Users/lordvoldemort/Desktop/MIN303/proj/testing.xlsx"

    
    df = pd.read_excel(file_path, sheet_name="Sheet1")
    


    df.reset_index(inplace=True, drop=True)

    # Define the number of rows and columns to display
    max_rows = st.slider("Maximum Rows to Display", 1, df.shape[0], value=df.shape[0])
    max_columns = st.slider("Maximum Columns to Display", 1, df.shape[1], value=df.shape[1])

    # Slice the DataFrame to limit rows and columns
    sliced_df = df.iloc[:max_rows, :max_columns]

    # Display the sliced DataFrame
    st.dataframe(sliced_df)

    st.sidebar.header("Options")
    options_form = st.sidebar.form("options_form")
    date = options_form.date_input("DATE")
    date = date.strftime('%Y-%m-%d')
    val = options_form.number_input("VALUE",step=1)
    add_data = options_form.form_submit_button()

    if add_data:
        
        new_data = {"DATE":date, "VALUE":val}

        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index= True)
        df.to_excel(file_path, sheet_name="Sheet1", index=False)
        st.experimental_rerun()


    if st.button("Previous Page"):
        st.session_state.page -= 1
        st.experimental_rerun()

        # Reset to the first page when you reach the last page
        if st.session_state.page > len(page_contents):
            st.session_state.page = 1

