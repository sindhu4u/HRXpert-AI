import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 0.75,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-pro-exp-02-05",
  generation_config=generation_config,
  system_instruction="List out the top 10 skills only for the given Job Role that the Resume of the candidate applying for that Job Position must have as a list of the names of the technologies alone.",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Full Stack Developer\nList the names alone",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here are 10 key skills, listed by name only, that should ideally be on a Full Stack Developer's resume:\n\n1.  JavaScript\n2.  HTML\n3.  CSS\n4.  React\n5.  Angular\n6.  Node.js\n7.  Python\n8.  SQL\n9.  Git\n10. REST\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Data Scientist.\nList the names alone",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here are 10 key skills, listed by name only, for a Data Scientist resume:\n\n1.  Python\n2.  SQL\n3.  Machine Learning\n4.  Statistics\n5.  R\n6.  Data Visualization\n7.  Deep Learning\n8.  Big Data\n9.  Cloud Computing\n10. Data Wrangling\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "AI Engineer\nList the names alone\n\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here are 10 key skills, listed by name only, for an AI Engineer resume:\n\n1.  Python\n2.  Machine Learning\n3.  Deep Learning\n4.  TensorFlow\n5.  PyTorch\n6.  Natural Language Processing (NLP)\n7.  Computer Vision\n8.  Cloud Computing (AWS/Azure/GCP)\n9.  Big Data\n10. Reinforcement Learning\n",
      ],
    },
  ]
)
Role="Frontend Developer"
response = chat_session.send_message(Role +"\nList the names alone")

print(response.text)