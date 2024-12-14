# Football Injury Rehab Chatbot

This repository contains a simple chatbot designed to provide rehabilitation advice for football-related injuries using Google's Gemini API. The chatbot is built using Python and Streamlit, leveraging prompt engineering to tailor responses for football players seeking recovery and injury management guidance.

---

## Features
- Provides advice for football-related injuries such as recovery plans, exercises, and injury management.
- Lightweight, interactive user interface built with Streamlit.
- Utilizes prompt engineering to focus responses on football injury rehabilitation.
- No history is stored to maintain a clean, stateless interaction for each question.

---

## Prerequisites

### Software Requirements
- Python 3.8 or higher
- Virtual environment tools (e.g., `venv`, `conda`)
- Internet access to interact with the Gemini API

### Libraries Used
- `streamlit` for the user interface
- `google.generativeai` for the Gemini API integration
- `python-dotenv` for securely managing the API key

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/38832/Gemini-Bot.git
   cd Gemini-Bot
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the API Key**:
   - Create a `.env` file in the root of the project.
   - Add the following line to the `.env` file, replacing `<YOUR_API_KEY>` with your Gemini API key:
     ```
     GOOGLE_API_KEY=<YOUR_API_KEY>
     ```

---

## Running the Application

1. **Start the Streamlit Server**:
   ```bash
   streamlit run app.py
   ```

2. **Access the Application**:
   - Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. **Ask Questions**:
   - Enter football injury-related questions, such as:
     - "What are the best recovery exercises for an ACL tear?"
     - "How do I manage a sprained ankle after football practice?"
     - "What stretches can I do for hamstring injuries?"

---

## File Structure

```
Gemini-Bot/
├── app.py               # Main application file
├── requirements.txt     # Required Python libraries
├── .env.example         # Example file for API key configuration
├── README.md            # Project documentation
└── venv/                # Virtual environment (not included in the repo)
```

---

## Customization

### Prompt Engineering
The chatbot uses prompt engineering to tailor responses. You can modify the prompt in the `get_gemini_response` function within `app.py` to customize the chatbot’s behavior. For example:

```python
football_prompt = (
    "You are a highly specialized rehabilitation assistant for football players. "
    "Provide detailed advice for recovery, rehabilitation exercises, and injury management. "
    "Question: " + question
)
```

---

## Limitations
- The chatbot does not store session history.
- It depends on the Gemini API for all responses, so it requires an active API key and internet connection.
- Responses are generated based on the model’s training and may not always be medically accurate. Always consult a professional for serious injuries.

---

## Future Enhancements
- Add session storage for user interactions.
- Enable integration with external resources or databases for enhanced knowledge.
- Fine-tune a custom model using specialized rehabilitation datasets.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
- [Google Gemini API](https://developers.google.com/generative-ai)
- [Streamlit Documentation](https://docs.streamlit.io)
- OpenAI for inspiring the use of large language models.


