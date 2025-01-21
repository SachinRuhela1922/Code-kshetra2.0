import os
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import re


# Google Docs API Authentication
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

def authenticate_google_docs_api():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('docs', 'v1', credentials=creds)


# Fetch Employer Profile from Google Docs
def get_employer_profile(doc_id):
    service = authenticate_google_docs_api()
    document = service.documents().get(documentId=doc_id).execute()
    employer_data = {}

    for element in document['body']['content']:
        if 'paragraph' in element:
            text = ''
            for text_run in element['paragraph']['elements']:
                if 'textRun' in text_run:
                    text += text_run['textRun']['content']
            # Extract relevant details using regular expressions or keywords
            if 'Job Description' in text:
                employer_data['Job Description'] = text
            elif 'Location' in text:
                employer_data['Location'] = text
            elif 'Salary' in text:
                employer_data['Salary'] = text
            elif 'Education' in text:
                employer_data['Education'] = text
            elif 'Experience' in text:
                employer_data['Experience'] = text

    return employer_data


# Match Candidates with Employers based on Profile
def match_candidates_with_employers(employer_data, candidate_data):
    matches = []
    for candidate in candidate_data:
        score = 0
        
    
        if employer_data['Job Description'].lower() in candidate['Job Description'].lower():
            score += 1

        
        if employer_data['Location'].lower() in candidate['Location'].lower():
            score += 1
        
      
        if int(candidate['Salary']) >= int(employer_data['Salary']):
            score += 1
        
        if employer_data['Education'].lower() in candidate['Education'].lower():
            score += 1

        
        if int(candidate['Experience']) >= int(employer_data['Experience']):
            score += 1

        # Store score and candidate info
        matches.append({
            'Candidate Name': candidate['Name'],
            'Score': score,
            'Profile URL': candidate['Profile URL'],  # Include Profile URL
            'Candidate Profile': candidate
        })
    
    # Sort candidates by score in descending order
    sorted_matches = sorted(matches, key=lambda x: x['Score'], reverse=True)
    return sorted_matches


# Load Candidate Data (assuming a CSV format for candidate profiles)
def load_candidate_data(csv_file_path):
    return pd.read_csv(csv_file_path).to_dict(orient='records')


# Example Usage:
def main():
    # Employer Profile Google Doc ID
    employer_doc_id = '1ENqNtgBGfeJNrKCx1swQ78msMuqaNVEQfdGv6PwmQds'
    employer_data = get_employer_profile(employer_doc_id)
    print(f"Employer Profile: {employer_data}")
    
    
    candidate_data = load_candidate_data('candidate_profiles.csv')  # Replace with your CSV file path
    
    matches = match_candidates_with_employers(employer_data, candidate_data)

    
    print("Top Candidates for Employer:")
    for match in matches:
        print(f"{match['Candidate Name']} - Score: {match['Score']}")
        print(f"Profile URL: {match['Profile URL']}")
        print(f"Candidate Profile: {match['Candidate Profile']}\n")


if __name__ == '__main__':
    main()
