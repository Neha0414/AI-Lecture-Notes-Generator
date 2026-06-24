
import os
import subprocess
import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Lecture Notes Generator",
    page_icon="🎓",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stButton > button {
    width: 100%;
    height: 3em;
    font-size: 18px;
    border-radius: 10px;
}

.stDownloadButton > button {
    width: 100%;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("🎓 AI Lecture Notes")
st.sidebar.success("Ready to Process Lectures")

# =========================
# HEADER
# =========================

st.markdown("""
<h1 style='text-align:center;'>
🎓 AI Lecture Notes Generator
</h1>

<p style='text-align:center;color:gray;font-size:18px;'>
Upload a lecture recording and generate study notes, quizzes, and flashcards.
</p>
""", unsafe_allow_html=True)

st.info(
    "🚀 Upload a lecture recording and generate study material instantly."
)

# =========================
# FILE UPLOAD
# =========================

uploaded_file = st.file_uploader(
    "📁 Upload MP3 File",
    type=["mp3"]
)

if uploaded_file:

    os.makedirs("audio", exist_ok=True)

    file_path = os.path.join(
        "audio",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Audio uploaded successfully!")
    st.write(f"Saved as: {file_path}")

    if st.button("🚀 Generate Notes, Quiz & Flashcards"):

        try:

            progress = st.progress(0)

            with st.spinner("🎤 Converting speech to text..."):
                subprocess.run(
                    ["python", "speech_to_text.py"],
                    check=True
                )

            progress.progress(33)

            with st.spinner("📖 Generating notes..."):
                subprocess.run(
                    ["python", "generate_notes.py"],
                    check=True
                )

            progress.progress(66)

            with st.spinner("📝 Generating quiz and flashcards..."):
                subprocess.run(
                    ["python", "generate_quiz.py"],
                    check=True
                )

                subprocess.run(
                    ["python", "generate_flashcards.py"],
                    check=True
                )

            progress.progress(100)

            st.success("🎉 Generation Complete!")

            # =========================
            # READ GENERATED FILES
            # =========================

            notes = ""
            quiz = ""
            flashcards = ""

            if os.path.exists("notes/notes.txt"):
                with open(
                    "notes/notes.txt",
                    "r",
                    encoding="utf-8"
                ) as f:
                    notes = f.read()

            if os.path.exists("quizzes/quiz.txt"):
                with open(
                    "quizzes/quiz.txt",
                    "r",
                    encoding="utf-8"
                ) as f:
                    quiz = f.read()

            if os.path.exists("flashcards/flashcards.txt"):
                with open(
                    "flashcards/flashcards.txt",
                    "r",
                    encoding="utf-8"
                ) as f:
                    flashcards = f.read()

            # =========================
            # TABS
            # =========================

            tab1, tab2, tab3 = st.tabs(
                [
                    "📚 Notes",
                    "❓ Quiz",
                    "🧠 Flashcards"
                ]
            )

            # =========================
            # NOTES
            # =========================

            with tab1:

                st.markdown("## 📚 Study Notes")
                st.markdown("---")

                st.markdown(notes)

                st.download_button(
                    "📥 Download Notes",
                    notes,
                    file_name="notes.txt"
                )

            # =========================
            # QUIZ
            # =========================

            with tab2:

                st.markdown("## ❓ Quiz Questions")
                st.markdown("---")

                # st.text_area(
                #     "",
                #     quiz,
                #     height=500,
                #     label_visibility="collapsed"
                # )
                st.markdown(quiz, unsafe_allow_html=False)

                st.download_button(
                    "📥 Download Quiz",
                    quiz,
                    file_name="quiz.txt"
                )

            # =========================
            # FLASHCARDS
            # =========================

            with tab3:

                st.markdown("## 🧠 Flashcards")
                st.markdown("---")

                # st.text_area(
                #     "",
                #     flashcards,
                #     height=500,
                #     label_visibility="collapsed"
                # )
                st.markdown(flashcards)

                st.download_button(
                    "📥 Download Flashcards",
                    flashcards,
                    file_name="flashcards.txt"
                )

        except Exception as e:

            st.error(f"❌ Error: {e}")

