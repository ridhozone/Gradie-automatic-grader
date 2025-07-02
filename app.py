import streamlit as st
from utils.style import style_code
from utils.helper import extract_texts
from gradie import Koreksi


st.set_page_config(
    page_title="Gradie - instant grading", page_icon=":material/social_leaderboard:"
)
st.html(style_code)

st.title("Gradie :material/social_leaderboard:")
st.subheader("Automated Student Assessment")

tab1, tab2, tab3 = st.tabs(["Gradie", "How-To", "About"])

with tab1:
    st.write("")
    with st.container(border=True, key="main_container"):
        c1, c2 = st.columns(2, gap="medium")

        with c1:
            kunci_jawaban = st.file_uploader(
                ":material/vpn_key: Upload kunci jawaban",
                key="kunci",
                type=["pdf", "docx", "txt"],
            )

        with c2:
            jawaban_siswa = st.file_uploader(
                ":material/person_book: Upload jawaban siswa",
                key="siswa",
                type=["pdf", "docx", "txt"],
                accept_multiple_files=True,
            )

        button = st.button("Auto Grade", type="primary", use_container_width=True)

    st.write("")

    with st.container(border=True):
        if button:
            if not kunci_jawaban or not jawaban_siswa:
                st.toast(
                    ":material/notifications_active: Please upload both the answer key and student answers first."
                )
                st.write(":material/rubric: Grading results will be displayed here!")

            else:
                with st.spinner("Waitig..."):
                    kunci_text = extract_texts(
                        filename=kunci_jawaban.name, content=kunci_jawaban.read()
                    )

                    siswa_texts = ""
                    for siswa in jawaban_siswa:
                        siswa_text = extract_texts(
                            filename=siswa.name, content=siswa.read()
                        )
                        siswa_texts += siswa_text + "\n\n"

                    hasil = Koreksi(kunci_text, siswa_texts)

                st.success(":material/rubric: Here are the grading results:")
                st.dataframe(
                    [
                        {"Name": s["nama"], "Score": s["nilai"]}
                        for s in hasil["hasil_nilai"]
                    ]
                )
                st.toast(
                    ":material/notifications_active: Grading completed successfully!"
                )

        else:
            st.write(":material/rubric: Grading results will be displayed here!")

with tab2:
    st.write("")
    with st.container(border=True, key="howto"):
        st.markdown(
            """
            ### How to Use the App

            This app helps teachers **automatically grade students' answers** using simple CSV uploads.

            1. **Prepare the Answer Key & Student Answers File**  
            - Format: `.pdf, docx, txt`  
            - Must contain two columns: `No` and `Answer`

            3. **Upload the Files**  
            - Use the **Drag & Drop** in **Upload** section to upload both files  
            - Ensure both files are correctly formatted

            4. **Click 'Auto Grade' Button**  
            - The system will automatically compare each student's answers with the answer key  
            - A table of scores will be displayed

            5. **Download the Results**  
            - You can download the full recap as a `.csv` file

            > :material/info: Make sure your files follow the format to avoid processing errors.
            """
        )

with tab3:
    st.write("")
    with st.container(border=True, key="about"):
        st.markdown(
            """
            ### About the App

            This is an AI-assisted tool designed to help teachers **automatically grade students' answers** by comparing them to an uploaded answer key.

            **Key Features**
            - **Upload answer key and student responses**
            - **Automatic comparison** of each student's answers
            - **Score calculation** based on correct answers
            - **Result table recap** of all student scores
            - **Export to CSV** in one click

            ---

            **Benefits**
            - Saves grading time  
            - Reduces manual errors  
            - Simple and user-friendly for all teachers

            > Built as part of an educational automation project.
            """
        )
