import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.title("Let's work with our data!")

st.header('First we have to load our data!')

# If students are unsure how to use this I add the code for them as well
with st.expander(label='Code to use for this'):
    'In streamlit we can work normally, so we load the data the same way we would do in a normal notebook:'
    st.code("heart = pd.read_csv('https://raw.githubusercontent.com/LUCE-Blockchain/Databases-for-teaching/refs/heads/main/Framingham%20Dataset.csv')")
    'To see the output you can then also call it as before. In my instance I named my dataset "heart" so if I want the output I will write:'
    st.code('heart')


# TODO: add that they might have to use pip install for some modules (can open a bash terminal and use pip install *module name*)

heart = pd.read_csv('https://raw.githubusercontent.com/LUCE-Blockchain/Databases-for-teaching/refs/heads/main/Framingham%20Dataset.csv')

"Simply by calling our dataframe after loading it we have a nice view of it even with the option of scrolling through!"

heart

"We can explore the dataframe just how we would in a notebook!"
st.code('st.write(heart.describe())')
st.write(heart.describe())
"However do make sure to take out anything that is unnecessary for your final presentation to not have the report too cluttered."

#st.write(heart.columns)


st.header('Next we can have a look at making graphs in streamlit using matplotlib')

with st.expander('Using matplotlib in streamlit'):
    'First make sure that you have all necessary modules **installed**!'
    with st.expander('Using the terminal'):
        '''You can open a new terminal by clicking the three lines on the top left of your screen (under the VScode logo)'
         and then clicking on *Terminal* and *New Terminal*.   
         Now a new bash Terminal should have opened that you can use to install the modules as described below.'''
    'You might need to use the bash terminal with:'
    st.code("pip install matplotlib")
    'After that make sure to also **import** the module in your script!'

    "The code for actually making the plots can be taken over from your colab file"
    "You might for example use:"
    st.code('''vc = heart.loc[heart.PERIOD == 1].educ.value_counts()
        fig, ax = plt.subplots(figsize=(12, 4))

        ax.bar(vc.index, 
            vc.values);''', language='python')
    "To get the output of the graph you then have to have the following installed:"
    st.code("pip install streamlit[charts]")
    " and you have to use " 
    st.code('st.pyplot(fig=[Your figure name here, e.g. fig])')
    'This should give you the graph you see below!'

vc = heart.loc[heart.PERIOD == 1].educ.value_counts()
fig, ax = plt.subplots(figsize=(12, 4))

ax.bar(vc.index, # values for the x-axis
       vc.values); # values for the y-axis

st.pyplot(fig=fig)


# making a plot in altair 
st.header('Now for using altair to make graphs in streamlit')

with st.expander('Using altair in streamlit'):
    'Again make sure that you have all necessary modules **installed** and make sure to also **import** the module in your script!'

    "The code for making the plots can be taken over from colab if you used altair there before."
    "You might for example use:"
    st.code('''alt_chart = alt.Chart(heart).mark_bar().encode(
    x='AGE',
    y='count()'
    )''', language='python')
    "To get the output of the graph you then have to have the following installed:"
    st.code("pip install streamlit[charts]")
    " and you have to use " 
    st.code('st.altair_chart([Your chart name here, e.g. alt_chart])')
    'This should give you the graph you see below!'
alt_chart = alt.Chart(heart).mark_bar().encode(
    x='AGE',
    y='count()'
)
st.altair_chart(alt_chart)


# load project data here
# what can they take from collab and put here? And how?
# examples: matplotlib figure, altair figure
# --> need the terminal (3 lines to the left, terminal, new terminal)
#     in terminal: pip install matplotlib 
#     then can import