# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
import os
st.set_page_config(page_title="Personalities")

st.markdown(
    "<h1 style='text-align:center'>A Council of <span style='color:red'>Personalities</span></h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center'><em>Ask different personalities a question</em></p>",
    unsafe_allow_html=True
)

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
st.write("Please enter your OpenAI API key to proceed.")

# if not openai_api_key or not openai_api_key.startswith("sk-"):
#     st.warning("Please enter your OpenAI API key.")
#     st.stop()

st.session_state["OPENAI_API_KEY"] = openai_api_key
os.environ["OPENAI_API_KEY"] = openai_api_key

from main import run_council
from memory import save_interaction

st.header("Choose personalities", divider="grey")

st.markdown(
    """
    <style>
    .personality-box {
        min-height: 260px;
        padding: 0.75rem;
        border-radius: 0.75rem;
        border: 1px solid rgba(255,255,255,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4, border=True)
with col1:
    st.markdown("<div class='personality-box'>", unsafe_allow_html=True)
    st.subheader("Analysts")
    use_intp = st.checkbox("INTP", value=True)
    use_entp = st.checkbox("ENTP", value=False)

    use_intj = st.checkbox("INTJ", value=False)
    use_entj = st.checkbox("ENTJ", value=False)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='personality-box'>", unsafe_allow_html=True)
    st.subheader("Diplomats")
    use_infj = st.checkbox("INFJ", value=True)
    use_enfj = st.checkbox("ENFJ", value=False)

    use_infp = st.checkbox("INFP", value=False)
    use_enfp = st.checkbox("ENFP", value=False)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='personality-box'>", unsafe_allow_html=True)
    st.subheader("Sentinels")
    use_estj = st.checkbox("ESTJ", value=True)
    use_istj = st.checkbox("ISTJ", value=False)

    use_isfj = st.checkbox("ISFJ", value=False)
    use_esfj = st.checkbox("ESFJ", value=False)
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='personality-box'>", unsafe_allow_html=True)
    st.subheader("Explorers")
    use_istp = st.checkbox("ISTP", value=True)
    use_estp = st.checkbox("ESTP", value=False)

    use_isfp = st.checkbox("ISFP", value=False)
    use_esfp = st.checkbox("ESFP", value=False)
    st.markdown("</div>", unsafe_allow_html=True)


selected_agents = {
    "intp": use_intp,
    "entp": use_entp,
    "infj": use_infj,
    "enfj": use_enfj,
    "estj": use_estj,
    "istj": use_istj,

    "intj": use_intj,
    "entj": use_entj,

    "infp": use_infp,
    "enfp": use_enfp,

    "isfj": use_isfj,
    "esfj": use_esfj,

    "istp": use_istp,
    "estp": use_estp,

    "isfp": use_isfp,
    "esfp": use_esfp,
}


st.markdown(
    """
    <h2 style="text-align:center">Ask a question</h2>
    <hr style="opacity:0.4">
    """,
    unsafe_allow_html=True
)


outer_left, center, outer_right = st.columns([1, 6, 1])

with center:
    input_col, button_col = st.columns([5, 1])

    question = input_col.text_input(
        "",
        placeholder="Type your question here..."
    )

    ask_clicked = button_col.button("Ask", use_container_width=True)

if ask_clicked:
    if not question.strip():
        st.error("Please enter a question.")
        st.stop()
    if not any(selected_agents.values()):
        st.warning("Please select at least one personality.")
        st.stop()

    if question.strip():
        with st.spinner("Thinking..."):
            try:
                result = run_council(question, selected_agents)
            except Exception as e:
                st.error("Something went wrong.")
                st.exception(e)
                st.stop()

    st.subheader("Final Answer")
    st.write(result["final"])

    for key, enabled in selected_agents.items():
        if enabled and key in result:
            with st.expander(key.upper()):
                st.write(result[key])

    save_interaction(question, result["final"])