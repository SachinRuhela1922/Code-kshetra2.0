Job-Candidate Matching System

This project matches candidates to employers based on the job description, salary expectations, education, experience, and work location. The employer's profile is fetched from a Google Docs document, while the candidates' profiles are stored in a CSV file.

Features:

- Employer Profile Fetching: Retrieves job specifications and requirements from a Google Docs document.
- Candidate Profile Matching: Compares candidates' profiles (stored in a CSV) against the job requirements and ranks them based on the match.
- Profile URL: Each candidate's profile includes a URL for their detailed profile (e.g., LinkedIn).
- Ranking System: Candidates are ranked based on the match to the employer's job description, location, salary, education, and experience.

Prerequisites

Before running the project, ensure that you have the following:

1. Python 3.6 or later installed on your machine.
2. Google Cloud Project: You need a Google Cloud project with the Google Docs API enabled.
3. Google Cloud Credentials: Download the `credentials.json` file from Google Cloud Console and place it in the project directory.
4. CSV File: A CSV file containing candidate profiles (more on this below).
5. Required Python Libraries: The project uses several Python libraries for interacting with the Google Docs API and processing data. These must be installed before running the script.

Dependencies

Install the following Python libraries by running the command:

pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib pandas

Setting Up Google Docs API

To use the Google Docs API, follow these steps:

1. Go to the Google Developers Console (https://console.developers.google.com/).
2. Create a new project.
3. Enable the Google Docs API in the API library for your project.
4. Under Credentials, create OAuth 2.0 credentials.
5. Download the `credentials.json` file and place it in the root directory of this project.

Candidate CSV File Format

Create a CSV file (e.g., `candidate_profiles.csv`) that contains the following columns:

- Name: The candidate's name.
- Job Description: A brief description of the job the candidate is looking for.
- Location: Candidate's preferred work location.
- Salary: Candidate's expected salary.
- Education: Candidate's educational qualifications.
- Experience: Candidate's years of experience.
- Profile URL: A link to the candidate's full profile (e.g., LinkedIn).

Example CSV:

Name,Job Description,Location,Salary,Education,Experience,Profile URL
John Doe,Software Developer,New York,75000,Bachelor's,3,https://www.linkedin.com/in/johndoe
Jane Smith,Data Analyst,Remote,80000,Master's,4,https://www.linkedin.com/in/janesmith
...

Employer Profile

The employer profile is fetched from a Google Docs document. Make sure your Google Docs document contains the following details for each employer:

- Job Description
- Location
- Salary
- Education
- Experience

Replace the employer_doc_id in the code with your Google Docs document ID (found in the URL of the document).

Running the Script

1. Download the `credentials.json` file from Google Cloud Console and place it in your project directory.
2. Prepare your Candidate CSV file as described above and save it as `candidate_profiles.csv`.
3. Replace the Employer Document ID: Update the code with your employer Google Docs document ID (find it in the URL).
4. Run the Python script:

python job_candidate_matching.py

5. Script Execution: The script will:
   - Fetch the employer's profile from Google Docs.
   - Load the candidate profiles from the CSV file.
   - Rank candidates based on their match to the employer’s job description and requirements.
   - Print the candidates' names, profile URLs, and their match scores.

Example Output

Top Candidates for Employer:
John Doe - Score: 5
Profile URL: https://www.linkedin.com/in/johndoe
Candidate Profile: {'Name': 'John Doe', 'Job Description': 'Software Developer', 'Location': 'New York', 'Salary': 75000, 'Education': "Bachelor's", 'Experience': 3, 'Profile URL': 'https://www.linkedin.com/in/johndoe'}

Jane Smith - Score: 4
Profile URL: https://www.linkedin.com/in/janesmith
Candidate Profile: {'Name': 'Jane Smith', 'Job Description': 'Data Analyst', 'Location': 'Remote', 'Salary': 80000, 'Education': "Master's", 'Experience': 4, 'Profile URL': 'https://www.linkedin.com/in/janesmith'}

...

Customizing the Script

- Job Matching Criteria: You can modify the matching logic in the code to adjust how the script evaluates job descriptions, locations, salary, education, and experience.
- Google Docs Document: Ensure that the Google Docs document contains sections that have the necessary employer details (Job Description, Salary, etc.).

Contributing

Feel free to fork this repository and submit pull requests for improvements.

- Bug fixes
- Feature enhancements
- Code optimizations

License

This project is open source and available under the MIT License.
