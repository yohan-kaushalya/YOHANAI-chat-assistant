# YOHANAI-chat-assistant
### 🤖 yohanAI - Modular Assistant Platform

**yohanAI** is a high-performance, responsive, and custom-styled modular AI assistant system built from scratch using **Python**, **Streamlit**, and the native **Google GenAI SDK**. It features a futuristic cyber-themed UI/UX layout optimized for contextual prompting, real-time file vector embeddings, and token-streaming response deliveries. 

### 🚀 Architectural Blueprint & Key Features

* **Advanced Multi-Modal File Context Injection:** Secure transient storage pipelines (tempfile abstractions) allow users to upload large files (PDF, TXT, CSV, Images) directly into Gemini's cloud storage context API for dynamic retrieval operations.
* **Real-Time Data Token Streaming:** Asynchronous stream generators (generate_content_stream) feed backend predictions directly to the canvas placeholder layers instantly without freezing execution frames.
* **Cyberpunk UI Customizations:** Embedded specific dynamic inline stylesheets (style.css) and background grid animation modules (scripts.js) overriding traditional standard UI templates.
* **Adaptive Execution Core:** Live control panels providing modular selections of varied backend intelligence versions paired with strict temperature control knobs.

### 🛠️ Stack Architecture

* **Core Framework:** Python 3.10+
* **Interface Engine:** Streamlit Framework
* **Language Intelligence Layer:** Google GenAI client module (google-genai)
* **Environment Context Architecture:** Python-dotenv configuration parser

### ⚙️ How to Deploy Locally

### 1. Initialize Repository Environment

bash

git clone https://github.com/YOUR_USERNAME/yohanAI.git
cd yohanAI

Use code with caution.

### 2. Configure Local Decoupled Keys

Create a file named .env in the root structure directory and populate your authenticated credentials: 

env

GEMINI_API_KEY=your_secured_gemini_api_token_here

Use code with caution.

### 3. Installation of Platform Dependencies

Execute the system compilation command via terminal: 

bash

pip install -r requirements.txt

Use code with caution.

### 4. Boot the Local Server Engine

bash

streamlit run main.py

Use code with caution.

*(Note: Ensure your primary startup script containing load_custom_styles_and_scripts() is named accurately inside the boot layer)* 

### 📄 Repository Blueprint Structure

* main.py - Core presentation script layout and execution router.
* ai_backend.py - Encapsulated Gemini assistant driver implementation logic.
* style.css / scripts.js - Embedded responsive presentation layer assets.
* requirements.txt - Fixed application dependency map.
