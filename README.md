# UK Business Risk Dashboard 🇬🇧📊

[![Live App](https://img.shields.io/badge/Live-Streamlit-00B4D8?style=for-the-badge)](INSERT_YOUR_STREAMLIT_URL_HERE)

## 👋 What is this?
I built this project to get hands-on experience handling massive, messy, real-world datasets instead of just using clean Kaggle files. I wanted to see if I could use data to figure out which industries in the UK are the riskiest to start a business in (or for a bank to lend money to).

To do this, I used the official UK Companies House dataset—a massive 5-million-row CSV containing info on every registered company in the country. I built a pipeline to clean it, load it into a database, run SQL analytics on it, and capped it off with an interactive web app.

![Dashboard Screenshot](INSERT_IMAGE_LINK_HERE) *(Upload a screenshot to github and paste the link here)*

## 🧠 What I Learned & Built

1. **Wrangling Giant CSVs (Python & Pandas):** The raw file was over 5 million rows. It was way too big to open in Excel and had tons of corrupted lines. I wrote a Python script using Pandas to process the data in chunks and bypass the broken rows so it wouldn't crash my machine.
2. **Database Design (PostgreSQL):** I loaded the raw data into a staging table, then wrote SQL scripts to split the massive 55-column flat file into a proper Star Schema (`fact_company`, `dim_industry`, `dim_location`) so it would run efficiently.
3. **Advanced SQL:** I used CTEs and Window Functions (like `RANK() OVER`) to dynamically calculate the historical failure rate of different industries across different regions.
4. **Web App Deployment (Streamlit):** I didn't want the data to just sit in a database, so I used Python, Streamlit, and Plotly to build a dark-mode dashboard that lets users filter and interact with the results in real time.

## 💻 Tech Stack
* **Database:** PostgreSQL, SQL
* **Data Pipeline:** Python, Pandas, SQLAlchemy
* **Frontend:** Streamlit, Plotly Express
* **Data Source:** [UK Companies House Free Data](https://download.companieshouse.gov.uk/en_output.html)

## 🚀 Want to run it yourself?

If you want to run the frontend dashboard locally on your machine:

1. Clone this repo:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/commercial-credit-risk-model.git](https://github.com/YOUR_USERNAME/commercial-credit-risk-model.git)
