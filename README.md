# HRXpert AI

## Description
HRXpert AI is an AI-driven HR automation tool designed to streamline and optimize HR tasks such as resume screening, offer letter issuance, payroll processing, onboarding, and HR reporting. By leveraging a multi-agent AI approach with LangGraph or LangFlow, HRXpert AI automates repetitive HR processes, allowing HR professionals to focus on strategic decision-making.

## Problem Statement
HR professionals spend up to 40% of their time on administrative tasks like resume screening, offer letter creation, payroll processing, and onboarding. Manual processes slow hiring, increase operational costs, and reduce efficiency. HRXpert AI addresses these inefficiencies by automating HR workflows with AI-driven decision-making, significantly reducing manual effort and improving overall HR operations.

## Setup
### Prerequisites
1. Install Python 
2. Create a `.env` file and add your API keys:
   ```sh
   GEMINI_API_KEY=your_api_key_here
   ```

### Running HRXpert AI
1. Ensure all dependencies are installed.
2. Place the resume files in the project directory.
3. Run the main script:
   ```sh
   python main.py
   ```
4. Follow the prompts to perform Resume Screening.

### Workflow Execution
1. **Resume Extraction**: The tool extracts text from resumes using OCR (for PDFs and images) and processes structured text for Word documents.
2. **NER Processing**: Named Entity Recognition extracts candidate details (name, job title, email, LinkedIn, GitHub, etc.).
3. **HR Skill Verification**: HR confirms the skills required for the job role.
4. **Candidate Screening**: The system evaluates resumes based on job role criteria.
5. **HR Approval**: HR reviews and approves shortlisted candidates.
6. **Email Notification**: Approved candidates receive an automated interview invitation.

---

## Impact & Benefits
- **Reduces Hiring Time by 50%**: Faster screening and shortlisting.
- **Cuts Operational Costs by 30%**: Less manual effort required.
- **Improves Hiring Accuracy**: AI-driven evaluation ensures better candidate selection.
- **Scalability**: Adaptable for large-scale HR operations.

## Future Enhancements
- **Integration with HRMS & ATS**: Seamless workflow with HR management systems.
- **Expanded AI Capabilities**: More advanced models for resume parsing and candidate evaluation.
- **Cloud Deployment**: Scalability for enterprise-level usage.

---

### Contribution
We welcome contributions to enhance HRXpert AI. Feel free to submit pull requests or open issues for bug reports and feature requests.


---

## License
HRXpert AI is open-source under the MIT License. See `LICENSE` for details.

