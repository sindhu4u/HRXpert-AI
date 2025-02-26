import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-pro-exp-02-05",
  generation_config=generation_config,
  system_instruction="You will be given the skills you need to look for in the resume and also the skills a candidate applying for a position has. Infer if the candidate's Resume is valid or not for the job and possesses that skill.",
)


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
                "JavaScript\nHTML\nCSS\nReact\nAngular\nNode.js\nPython\nSQL\nGit\nREST",  # Removed numbering and extra spacing
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
                "Python\nSQL\nMachine Learning\nStatistics\nR\nData Visualization\nDeep Learning\nBig Data\nCloud Computing\nData Wrangling", # Removed numbering and extra spacing
            ],
        },
        {
            "role": "user",
            "parts": [
                "AI Engineer\nList the names alone",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Python\nMachine Learning\nDeep Learning\nTensorFlow\nPyTorch\nNatural Language Processing (NLP)\nComputer Vision\nCloud Computing (AWS/Azure/GCP)\nBig Data\nReinforcement Learning", # Removed numbering and extra spacing
            ],
        },


        # Example 1: Full Stack Developer (Valid)
        {
            "role": "user",
            "parts": [
                "Job Role: Full Stack Developer\nRequired Skills: JavaScript, HTML, CSS, React, Node.js, Python, SQL, Git, REST\nCandidate Skills: JavaScript, HTML, CSS, React, Node.js, Python, SQL, Git, REST, Docker, Kubernetes"
            ],
        },
        {
            "role": "model",
            "parts": [
                "Classification: Valid\nReasoning: The candidate possesses all the required skills (JavaScript, HTML, CSS, React, Node.js, Python, SQL, Git, REST) and even has additional relevant skills (Docker, Kubernetes)."
            ],
        },

        # Example 2: Full Stack Developer (Not Valid)
        {
            "role": "user",
            "parts": [
                "Job Role: Full Stack Developer\nRequired Skills: JavaScript, HTML, CSS, React, Node.js, Python, SQL, Git, REST\nCandidate Skills: Java, C++, Spring, Hibernate, MySQL, Git"
            ],
        },
        {
            "role": "model",
            "parts": [
                "Classification: Not Valid\nReasoning: The candidate lacks several crucial required skills. While they have Git and SQL (MySQL), they are missing JavaScript, HTML, CSS, React, Node.js, and Python.  Their Java/Spring/Hibernate experience, while valuable, doesn't align with the core requirements of this specific Full Stack Developer role."
            ],
        },

        # Example 3: AI Engineer (Valid)
        {
            "role": "user",
            "parts": [
                "Job Role: AI Engineer\nRequired Skills: Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, Natural Language Processing (NLP), Computer Vision, Cloud Computing (AWS/GCP/Azure)\nCandidate Skills: Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, NLP, Computer Vision, AWS, Scikit-learn"
            ],
        },
        {
            "role": "model",
            "parts": [
                "Classification: Valid\nReasoning: The candidate has all the essential skills, including Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, NLP, Computer Vision, and Cloud Computing (AWS). The addition of Scikit-learn further strengthens their profile."
            ],
        },

        # Example 4: AI Engineer (Not Valid)
        {
            "role": "user",
            "parts": [
                "Job Role: AI Engineer\nRequired Skills: Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, Natural Language Processing (NLP), Computer Vision, Cloud Computing (AWS/GCP/Azure)\nCandidate Skills:  R, Statistical Modeling, Data Analysis, SQL, Tableau"
            ],
        },
        {
            "role": "model",
            "parts": [
                "Classification: Not Valid\nReasoning: The candidate's skills are more aligned with a Data Analyst or Data Scientist role. While they have valuable skills like R, Statistical Modeling, Data Analysis, SQL, and Tableau, they are missing core AI Engineering skills like Python, Deep Learning, TensorFlow, PyTorch, NLP, and Computer Vision."
            ],
        },

         # Example 5: Full Stack Developer (Valid - Partial Match with Explanation)
        {
            "role": "user",
            "parts": [
                "Job Role: Full Stack Developer\nRequired Skills: JavaScript, HTML, CSS, React, Node.js, Python, SQL, Git, REST\nCandidate Skills: JavaScript, HTML, CSS, React, Node.js, Git, REST"
            ],
        },
        {
            "role": "model",
            "parts": [
                "Classification: Valid \nReasoning: The candidate possesses most of the required front-end and back-end skills (JavaScript, HTML, CSS, React, Node.js, Git, REST) but is missing Python and SQL. While not a perfect match, they could be considered for further evaluation or a more specialized front-end role.  Further investigation is recommended to assess their potential to learn Python and SQL quickly."
            ],
        },


    ]
)
prompt=job_role+required_skills+candidate_skills
response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)