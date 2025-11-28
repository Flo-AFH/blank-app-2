import streamlit as st

st.title("Using Streamlit in Codespaces")
st.write(
    "There are a few steps to follow to set up Codespaces to run streamlit!"
)

# getting a github account set up first
with st.expander("1st: If you don't have one yet: make a GitHub account"):
    # can I put this image in the title of the expander? 
    # st.image('https://pngimg.com/uploads/github/github_PNG40.png')
    "Go to https://github.com/ and click on Sign up for GitHub"
    st.image("/workspaces/blank-app-2/images/GitHub.png")
    """Fill in mail, password and a Username and create your account.  
You will be prompted to enter a code that was sent to your mail so make sure to choose a mail address that you can easily access.  
You now have a GitHub account! 
"""


# now explanation on how to get streamlit working in codespaces    
with st.expander("2nd: Use Streamlit Community Cloud to use Codespaces"):
    "*You can also refer to this website for documentation: https://docs.streamlit.io/get-started/installation/community-cloud*"
    "**Open https://share.streamlit.io/**"
    'Click on :blue-background[Continue to Sign in] and then on :blue-background[Continue with GitHub]'
    st.image('https://js2iiu.com/wp-content/uploads/2025/05/68_01-934x1024.png')
    st.write('Use your GitHub account credentials to sign in and authenticate the sign-up. ' \
    '  When prompted click on "I accept".')

"Now you might either be in a :red[new environment] "
st.image('https://docs.streamlit.io/images/streamlit-community-cloud/deploy-empty-new-app.png')
"or you might see some more windows that :blue[ask for your input]"
st.image('https://docs.streamlit.io/images/streamlit-community-cloud/GitHub-auth1-none.png')



# have the two options
with st.expander('A :red[new evironment] opened for you'):
    ''
    # if this then need to set up the github access with more steps 



with st.expander('You are :blue[prompted for more input]'):
    '''In this case you can just click :blue-background[Authorize streamlit] for public 
    repositories (under repositories you see **Public repositories**)  
    After this you can choose if you want to add authorization for private repositories too 
    (note that now under repositories you see **Public and Private**)'''
    # if this just click on authorize and if they want also authorize for the second one 



# also making github account


# load project data here
# what can they take from collab and put here? And how?
# examples: matplotlib figure, altair figure
# --> need the terminal (3 lines to the left, terminal, new terminal)
#     in terminal: pip install matplotlib 
#     then can import

# also add where they can see it in github and how to commit?
