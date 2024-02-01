import streamlit as st

st.header("Introduction")
intro = '''
During a continuous manufacturing process, we want to know whether the process is in control or not and to know if there is any presence of variation. Variation may be due to chance or assignable causes. Control charts help to detect the causes during a process. It prevents us from manufacturing defective product and further. For example, variation can be in material properties, improper test procedure, etc.
Control chart was introduced by Dr. Walter A. Shewhart to control and monitor the process variation. This chart is also known as the Shewhart chart.
'''
st.write(intro)

st.subheader("What is a Control Chart?")
ans1 = '''
A control chart is a graph which displays all the process data in order sequence. It consists of a centre line, the upper limit and lower limit. Centre line of a chart represents the process average. Control limits (upper & lower) which are in a horizontal line below and above the centre line depicts whether the process is in control or out of control. Control limits are based on process variation.
'''
st.write(ans1)

st.subheader("Types of Control Chart")
ans2 = '''
There are various types of control chart used for different types of data and for specific purposes. Selecting the right type of chart is the first priority. Let us discuss some of the charts which can be used for the following types of data.

1.Attribute data – When your data is in the form of an attribute or count form of data we will use control charts like

    ● P chart

    ● U chart

    ● C chart

    Attribute data are the number of defects, defective units, etc.

2.Numerical data – When your data is in the form of a continuous type of
data we will use control charts like

    ● X bar chart

    ● R bar chart

    ● S bar chart

    Examples like measurement of length, weight, temperature, etc.

'''
st.write(ans2)

eg = '''
Examples:

Suppose in a bolt manufacturing industry, an automation inspection examines samples of bolts for severe cracks that make the bolts unusable. For each sample, analysts record the number of bolts inspected and the number of bolts rejected.
§ Another example, suppose in a beverage manufacturing industry a quality inspector wants to investigate whether the quantity of beverage is consistent over time. To collect data, a quality analyst records the quantity from a sample of certain bottles.
'''
st.write(eg)

st.subheader("When to use a control chart?")
ans3 = '''
● To examine whether the process is stable or not.

● To understand the process variation over time.

● When you need to find out any variation occurs and fixed it
instantaneously.

● To find out whether the process is within the statistical control or not (Due to chance or assignable casue)
'''
st.write(ans3)

st.subheader("Benefits")
ans4 = '''
● Gives the visual representation of the ongoing in a process.

● Easy to understand and to interpret.

● Helps in decision making for process improvement goals.

● Identification of cause’s type of variation in a process.
'''
st.write(ans4)

st.subheader("Example")
eg1 = '''
A LCD manufacturer wants to monitor the number of dead pixels on 21-inch LCD screens. Technicians record the number of dead pixels for each screen. Each subgroup has a different number of screens. The manufacturer uses a U chart to monitor the average number of dead pixels per screen.
'''
st.write(eg1)
st.image('/Users/lordvoldemort/Desktop/MIN303/proj/Control-Chart.png', use_column_width=True)