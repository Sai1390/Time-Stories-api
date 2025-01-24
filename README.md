# Time Stories API

A simple Python-based API that scrapes the latest stories from [time.com](https://time.com) and serves them as a JSON response through a custom API endpoint.

## Features
- Dynamically fetches the latest 6 stories from `time.com`.
- Extracts story titles and links using regex.
- Provides an easy-to-use custom API endpoint: `http://localhost:8000/getTimeStories`.
- Lightweight and runs locally with minimal dependencies.

## Example Output
When you access the API at `http://localhost:8000/getTimeStories`, it returns a JSON response like this:

```json
[
    {
        "title": "Who Is Handing Trump All Those Executive Orders? Meet Will Scharf",
        "link": "https://time.com/7209704/trump-staff-secretary-will-scharf-executive-orders-binders/"
    },
    {
        "title": "Trump to Visit Disaster-Struck California and North Carolina",
        "link": "https://time.com/7209700/trump-los-angeles-wildfires-north-carolina-hurricane-helene-trip-visit/"
    },
    {
        "title": "Trump Executive Order Calls for AI Development ‘Free From Ideological Bias’",
        "link": "https://time.com/7209689/trump-ai-ideological-bias-executive-order/"
    },
    {
        "title": "Trump Declassifies JFK, RFK, and MLK Assassination Docs",
        "link": "https://time.com/7209648/trump-orders-declassification-documents-jfk-rfk-mlk-kennedy-king-assassinations/"
    },
    {
        "title": "Senate Confirms John Ratcliffe to Lead CIA",
        "link": "https://time.com/7209622/john-ratcliffe-cia-confirmed-trump-senate/"
    },
    {
        "title": "Column: Business Can Sow Climate Optimism",
        "link": "https://time.com/7209398/business-climate-optimism-drive-action/"
    }
]

Steps to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/time-stories-api.git
cd time-stories-api
Run the Python server:

bash
Copy
Edit
python time_api_server.py
Access the API:

Open your browser or use a tool like curl or Postman to visit: http://localhost:8000/getTimeStories.
