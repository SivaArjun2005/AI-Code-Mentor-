import streamlit as st
from agent import CodeMentorAgent

st.set_page_config(page_title="AI Code Mentor", page_icon="👨‍💻", layout="wide")

st.title("👨‍💻 AI Code Mentor")
st.write("Debug, explain, and optimize code.")

# User inputs
code_input = st.text_area("Paste your code here:", height=200, placeholder="e.g., for i in range(5) print(i)")
task = st.text_input("What should I do? (e.g., Debug, Explain, Optimize)")

if st.button("Ask Mentor"):
    if code_input.strip() and task.strip():
        agent = CodeMentorAgent()
        prompt = f"Here is some code:\n{code_input}\n\nTask: {task}\nExplain clearly and fix if needed."
        response = agent.run(prompt)

        st.subheader("💡 Mentor's Response:")
        st.write(response)
