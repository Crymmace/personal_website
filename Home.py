import streamlit as st
from send_email import send_email
import pandas

st.set_page_config(layout="wide")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
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
            Hello!
            My name is Crystal!

            I started learning Python about 5 years ago through the use of online courses. 
            Since then I've worked as a temporary Software Developer for a startup in Sweden. 
            I have a handful of side projects that I've worked on in my free time that you can check out below!. 
            I'm dedicated, I work hard, and I love what I do.

            If you'd like what you see, feel free to reach out!
            Hope to hear from you soon!
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
