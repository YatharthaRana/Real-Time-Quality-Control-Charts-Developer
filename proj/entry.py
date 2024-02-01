import streamlit as st
import pandas as pd
import openpyxl
import datetime
import os

from st_pages import Page, show_pages

st.set_page_config(
    page_title="Control Chart",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

show_pages(
    [
        Page("/Users/lordvoldemort/Desktop/MIN303/proj/entry.py", "Home", "🏠"),
        Page("pages/know_more.py", "Learn about Control Charts", ":books:"),
        Page("pages/team.py","Know about the Team","😎")
    ]
)

if "page" not in st.session_state:
    st.session_state.page = 1

# Define the content for each page
page_contents = {
    1: "Page 1 Content",
    2: "Page 2 Content",
}

# Streamlit app
st.title("Quality Quill")
stg = "Made with ❤️ by Team Niyantran"
st.write(stg)




if st.session_state.page == 1:
    # st.write(page_contents[st.session_state.page])

    # st.header("Welcome!")



    # Step 2: First Choice
    st.subheader("Type of Control Chart")
    first_option = st.selectbox("Select among the options:", ["Attribute", "Variable"])

    # Step 3: Second Choice
    if first_option == "Variable":
        st.subheader("Choose the sample size")
        second_option = st.selectbox("Select among the options:", ["Small", "Large"])
    else:
        st.subheader("Choose the type")
        second_option_1 = st.selectbox("Select among the options:", ["Defective","Defects"])
        second_option_2 = st.selectbox("Select whether sample size is varying or constant:", ["Constant","Varying"])

    st.subheader("Select the Control Chart")
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

    data_to_share = {"third_option": third_option}
    df_storing = pd.DataFrame(data_to_share,index=[0])
    df_storing.to_csv("/Users/lordvoldemort/Desktop/MIN303/proj/shared_data.csv", index=False)


    if st.button("Next Page"):
        st.session_state.page =2
        st.rerun()

        # Reset to the first page when you reach the last page
        if st.session_state.page > len(page_contents):
            st.session_state.page = 1


if st.session_state.page == 2:

    df_recieved = pd.read_csv("shared_data.csv")

    top = df_recieved["third_option"][0]
    file_path = "/Users/lordvoldemort/Desktop/MIN303/proj/charts/FINAL-CONTROL-CHART.xlsx"
    if top == "X-R":
        df = pd.read_excel(file_path, sheet_name="X CHART",header = 2)
        col_val_lim = 6
        columns_included = ['VALUE','UCL(AVG+3*SD)','LCL(AVG-3*SD)','AVERAGE']
        shname = "X CHART"
    elif top == "P":
        df = pd.read_excel(file_path,sheet_name="P CHART",header = 2)
        col_val_lim = 7
        columns_included = ['Proportion Defective','Upper Control Limit','Lower Control Limit','Control Limit ']
        shname = "X CHART"

    df.reset_index(drop=True, inplace=True)

    # Define the number of rows and columns to display
    max_rows = st.slider("Maximum Rows to Display", 1, df.shape[0], value=df.shape[0])
    max_columns = st.slider("Maximum Columns to Display", 1, col_val_lim, value=col_val_lim)

    # Slice the DataFrame to limit rows and columns
    sliced_df = df.iloc[:max_rows, :max_columns]

    # Display the sliced DataFrame
    st.dataframe(sliced_df)

    st.sidebar.header("Options")
    options_form = st.sidebar.form("options_form")
    serial_no = options_form.number_input("Serial No", step=1)
    val = options_form.number_input("VALUE",step=1)
    add_data = options_form.form_submit_button()

    if add_data:
        new_data = {"S.NO.":serial_no, "VALUE":val}
        if serial_no in df["S.NO."].tolist():
            # Update the existing row
            df.loc[df["S.NO."] == serial_no, "VALUE"] = val
            df.to_excel(file_path, sheet_name=shname, index=False)
            st.experimental_rerun()
        else:
            # Add a new row
            new_data = {"Serial No": serial_no, "VALUE": val}
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            df.to_excel(file_path, sheet_name=shname, index=False)
            st.experimental_rerun()

    
    df_selected = df[columns_included]
    st.line_chart(df_selected)

    st.subheader("Open Excel")

    # Specify the path to the specific Excel file you want to open.
    excel_file_path = "/Users/lordvoldemort/Desktop/MIN303/proj/charts/FINAL-CONTROL-CHART.xlsx"  # Replace with the actual file path.

    if st.button("Open Excel File"):
        if os.path.exists(excel_file_path):
            # Specify the path to the Excel application on your computer (for Windows).
            excel_path = "/Applications/Microsoft Excel.app"  # Replace with the actual path to Excel.
            
            if os.path.exists(excel_path):
                os.system(f'open -a "{excel_path}" "{excel_file_path}"')
            else:
                st.error("Excel not found at the specified path. Please check the path.")
        else:
            st.error("The specified Excel file does not exist. Please check the file path.")

    st.subheader("Go Back") 
    if st.button("Previous Page"):
        st.session_state.page = 1
        st.rerun()

        # Reset to the first page when you reach the last page
        if st.session_state.page > len(page_contents):
            st.session_state.page = 1
