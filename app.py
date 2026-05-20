import streamlit as st
from chatbot import get_response
from memory import ChatMemory

# 1. Page Configuration
st.set_page_config(
    page_title="SmartStudyBot | AI Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for a professional look
st.markdown("""
<style>
    /* Styling the main title */
    h1 {
        color: #4A90E2;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: bold;
    }
    
    /* Make the chat input box stand out */
    .stChatInputContainer {
        border-radius: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 3. Main Header
st.title("🎓 Smart AI Study Assistant")
st.markdown("**Your personal AI tutor for ML, DL, AI, Gen AI, and Agentic AI.**")
st.divider()

# 4. Initialize Memory
if "memory" not in st.session_state:
    st.session_state.memory = ChatMemory()

memory = st.session_state.memory

# 5. Sidebar Dashboard
with st.sidebar:
    # We can add a nice academic icon here
    st.markdown("<h1 style='text-align: center; font-size: 80px;'>🧠</h1>", unsafe_allow_html=True)
    st.title("About this Bot")
    st.markdown("---")
    
    st.markdown("### 📚 Topics I Cover")
    st.markdown("- **Machine Learning (ML)**")
    st.markdown("- **Deep Learning (DL)**")
    st.markdown("- **Artificial Intelligence (AI)**")
    st.markdown("- **Generative AI (Gen AI)**")
    st.markdown("- **Agentic AI**")
    
    st.markdown("---")
    st.markdown("### 📊 API Usage Limits")
    st.markdown("- **15** messages / minute")
    st.markdown("- **1,500** messages / day")
    st.caption("*(Based on Gemini Free Tier)*")

    st.markdown("---")
    st.markdown("### ⚙️ Controls")
    
    # Styled Clear button
    if st.button("🗑️ Clear Conversation", use_container_width=True, type="primary"):
        memory.clear()
        st.rerun() # Refresh the page to clear the UI
        
    st.markdown("---")
    st.caption("Powered by Gemini 2.5 Flash")

# 6. Welcome Message (only shows if chat is empty)
if len(memory.get_messages()) == 0:
    st.info("👋 Hello! I am your strict study assistant. Ask me a question to get started.")

# 7. Render Chat History with Custom Avatars
for message in memory.get_messages():
    # Set avatar based on who is talking
    avatar = "👤" if message["role"] == "user" else "🎓"
    
    with st.chat_message(message["role"], avatar=avatar):
        st.write(message["content"])

# 8. Handle New User Input
user_input = st.chat_input("Type your study question here...")

if user_input:
    # Display user's question
    memory.add_user_message(user_input)
    with st.chat_message("user", avatar="👤"):
        st.write(user_input)

    # Show a loading animation while the AI thinks!
    with st.spinner("🤖 Thinking..."):
        reply = get_response(user_input, memory.get_messages())

    # Display AI's answer
    memory.add_bot_message(reply)
    with st.chat_message("assistant", avatar="🎓"):
        st.write(reply)
