import streamlit as st
from send_email import send_email
import pandas

st.set_page_config(page_title="Home", layout="wide")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
        </style>
        """, unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Home", "Contact Me"])

with tab1:
    col1, col2 = st.columns([0.4, 0.6])

    with col1:
        st.image("images/photo.png")

    with col2:
        st.title("About Me")
        content = """
            Hey there! I'm Crystal, a passionate Python developer with 5+ years under my belt. 
            I kicked things off by diving into online courses, and since then I've put my skills to the test at a 
            startup in Sweden. 
            
            When I'm not coding away, I love working on personal projects (check them out below!).

            Here's the gist:

            Python pro: 5+ years of experience, honed through online learning, professional work, and personal projects.\n
            Startup experience: Built an automated testing suite as a Software Developer at a Swedish startup.\n
            Always learning: Constantly expanding my skills and tackling new challenges.
        
            Want more info?
            Feel free to send me an email!
            Looking forward to hearing from you soon!
            """
        st.write(content)

    st.divider()

    col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

    df = pandas.read_csv("data.csv", sep=";")
    with col3:
        half = int(len(df) / 2) + 1
        for index, row in df[:half].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"], width=100)
            st.write(f"[Source Code]({row['url']})")

    with col4:
        for index, row in df[half:].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"], width=100)
            st.write(f"[Source Code]({row['url']})")

with tab2:
    st.header("Contact Me")

    with st.form(key="email_forms"):
        user_name = st.text_input(label="user_name", label_visibility="collapsed", placeholder="Name")
        user_email = st.text_input(label="user_email", label_visibility="collapsed", placeholder="Email Address")
        raw_message = st.text_area(label="raw_message", label_visibility="collapsed", placeholder="Message...")
        subject = f"New email from {user_name}"

        message = f"""{raw_message} \n {user_email}
        """

        button = st.form_submit_button("Submit")
        if button:
            send_email(subject, message)
            st.info("Thank you for your email. I will reach out soon!")
