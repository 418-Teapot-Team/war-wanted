# War Wanted
This task was done by team TEAPOT 418 for BEST hackathon, which involves developing a website to help coordinating work to search losted people.
The backend stack for this project is Python Flask, and the frontend stack is Vue.js, Tailwind.css.
Below, you will find all the necessary information and descriptions related to the project.

## Description
Project involves creating of two systems - public and closed.
Public system is designed for volunteers and searchers. Using it they can add a person they found and all the data about them.

After adding the person found, it goes to 2 ML models that identifies and compare the person with the ones we have in database wanted.
If the found person has matches it appears in the closed system, where the responsible person from the government side has to review it and eigther approve or deny the exact match.

> The public website is available at: http://34.107.31.175:3003/
> The closed system is available at: http://34.107.31.175:3001/
> The website REST API is available at: http://34.107.31.175:8001/
> The ML models service is available at: http://34.107.31.175:8003/


## Local setup
- Before running you should create a .env file with all the credential (sample is availabe in backend directory)
- Start the docker-compose using the next command:
`docker compose --env-file=path/to/.env up`


## Key features

### ML models:
- *Face Recognition* - is used to search for person match from the database of wanted people. Model is also retrained each time new record added, making it more accurate.
- *Field Comparison* - is used to compare the values of the fields and decide the similarity of two persons

### External API
- We allow government services to communicate with our system using closed API
