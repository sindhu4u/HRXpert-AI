import os
from relevant_skills_agent import get_relevant_skills
from screening_agent import evaluate_resume
from email_sender_agent import send_shortlist_email
from ocr_agent import extract_text_and_hyperlinks_from_pdf
from ner_agent import extract_resume_entities

def main():
    # Step 1: Get resume file names from the user
    resume_files = input("Enter the resume file names (comma-separated): ").strip().split(",")
    
    extracted_resumes = []  # List to store extracted resume details

    for file in resume_files:
        file = file.strip()
        print(f"\nProcessing {file}...")
        
        # Extract text and hyperlinks from the resume
        extracted_text, hyperlinks = extract_text_and_hyperlinks_from_pdf(file)
        
        # Perform Named Entity Recognition (NER) to extract email and skills
        extracted_info = extract_resume_entities(extracted_text, hyperlinks)
        
        # Ensure extracted_info contains the expected keys
        extracted_resumes.append(extracted_info)

    # Step 2: Get HR input for job role
    job_role = input("\nEnter the job role for screening: ").strip()
    
    # Step 3: Fetch skills required for the job role
    required_skills = get_relevant_skills(job_role).split("\n")
    print(f"\nGenerated skills for {job_role}: {', '.join(required_skills)}")
    
    # Step 4: Confirm or modify the skills
    confirmation = input("\nAre these skills correct? (yes/no): ").strip().lower()
    if confirmation != "yes":
        required_skills = input("Enter the correct skills (comma-separated): ").strip().split(",")
    
    shortlisted_candidates = []  # Store candidates who match the job criteria

    # Step 5: Screen resumes based on required skills
    for candidate in extracted_resumes:
        candidate_skills = candidate[1]
        print(f"\nScreening {candidate[0]}'s resume...")
        
        screening_result, classification = evaluate_resume(job_role, candidate_skills, required_skills)
        print(f"Screening Result for {candidate[0]}: {screening_result}")
        
        # Step 6: Ask HR to approve the shortlisted candidates
        if classification == "Valid":
            approve = input(f"Approve {candidate[0]} for an interview? (yes/no): ").strip().lower()
            if approve == "yes":
                shortlisted_candidates.append(candidate)
    
    # Step 7: Send emails to shortlisted candidates
    for candidate in shortlisted_candidates:
        email = candidate[0]
        response = send_shortlist_email(email, f"Interview Invitation for {job_role}", job_role)
        print(response)
    
    print("\nScreening process completed.")

if __name__ == "__main__":
    main()
