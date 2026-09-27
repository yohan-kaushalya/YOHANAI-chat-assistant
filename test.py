
import streamlit as st
from app import GeminiAssistant  


st.set_page_config(page_title="yohanAI - Modular Assistant", page_icon="🤖", layout="wide")


def load_custom_styles_and_scripts():
    
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

   
    with open("scripts.js", "r", encoding="utf-8") as f:
        st.markdown(f"<script>{f.read()}</script>", unsafe_allow_html=True)


load_custom_styles_and_scripts()


st.title("🤖 yohanAI - MADE YOUR FUTURE")
st.caption("grow your mind ,choose your path")
st.caption("powered by yohan kaushalya")

@st.cache_resource
def get_assistant():
    return GeminiAssistant()

try:
    assistant = get_assistant()
except Exception as e:
    st.error(str(e))
    st.stop()


if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_gemini_file" not in st.session_state:
    st.session_state.uploaded_gemini_file = None

with st.sidebar:
    st.header("📄 Document Upload")
    uploaded_file = st.file_uploader(
        "PDF, TXT, CSV, PNG, JPG, JPEG files upload only", 
        type=["pdf", "txt", "csv", "png", "jpg", "jpeg"]
    )

    if uploaded_file and st.session_state.uploaded_gemini_file is None:
        with st.spinner("File is loading and uploading to yohanAI..."
                        ):
            try:
                gemini_file = assistant.upload_file_to_gemini(uploaded_file)
                st.session_state.uploaded_gemini_file = gemini_file
                st.success(f"✓ '{uploaded_file.name}' successfully uploaded to yohanAI.")
            except Exception as e:
                st.error(str(e))

    if st.session_state.uploaded_gemini_file:
        st.info("Active File attached!")
        if st.button("Remove File"):
            st.session_state.uploaded_gemini_file = None
            st.rerun()

    
    st.markdown("---")
    st.header("⚙️ AI Settings")

    model_choice = st.selectbox(
        "select the AI model:",
        ["gemini-flash-lite-latest", " gemini-3-flash-preview","gemini-3.1-pro-preview","gemini-pro-latest","gemini-3.5-flash-lite","gemini-3.5-flash-preview","gemini-3.5-flash-lite-preview","gemini-3.5-pro-preview","gemini-3.5-flash-lite","Gemini 3.1 Flash Lite"]
    )

    creativity = st.slider("Creativity Level (Temperature):", 0.0, 1.0, 0.7)

    st.markdown("---")
    if st.session_state.messages:
        chat_text = "\n\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
        
        st.download_button(
            label="📥 Download Chat",
            data=chat_text,
            file_name="yohanAI_chat_history.txt",
            mime="text/plain",
            use_container_width=True  
        )

    if st.button("Clear Chat History",use_container_width=True):
        st.session_state.messages = []
        st.rerun()


for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="ai-msg">🤖 <b>yohanAI:</b><br>{msg["content"]}</div>', unsafe_allow_html=True)




st.write("💡 Quick Prompts:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📄 Summarize Document"):
        st.session_state.preset_prompt = "Summarize the uploaded document in simple terms."

with col2:
    if st.button("💻 Explain Code Concept"):
        st.session_state.preset_prompt = "Please explain the concept of async/await in Python."

with col3:
    if st.button("✍️ Write an Essay"):
        st.session_state.preset_prompt = "Write a short essay on the future of AI technology."



if prompt := st.chat_input("enter your message here..."):
  
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-msg">{prompt}</div>', unsafe_allow_html=True)

    message_placeholder = st.empty()
    full_response = ""

    stream_gen = assistant.generate_response_stream(
        prompt=prompt,
        gemini_file=st.session_state.uploaded_gemini_file
    )

    for chunk_text in stream_gen:
        full_response += chunk_text
        message_placeholder.markdown(f'<div class="ai-msg">🤖 <b>yohanAI:</b><br>{full_response}▌</div>', unsafe_allow_html=True)

    message_placeholder.markdown(f'<div class="ai-msg">🤖 <b>yohanAI:</b><br>{full_response}</div>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": full_response})