# EdTech Student Applications Funnel Analysis & Personalisation Opportunities

**Self-directed project** built to demonstrate the kind of work I’d love to do at Unifrog.

## Project Goal
Understand student behaviour on a simulated careers/university application platform, identify where they drop off, predict successful completion, and surface actionable personalisation opportunities — directly relevant to Unifrog’s mission of helping young people make better choices and submit stronger applications.

## What I Built
- **Synthetic Dataset**: Generated realistic student event data with funnel stages (Login → Browse → View Details → Start Application → Complete).
- **SQL Exploration**: Funnel conversion rates and segment analysis.
- **Python Analysis**: Data wrangling + Logistic Regression model (AUC ~0.80) to predict application completion. Key predictors: prior engagement, sessions, and session duration.
- **Power BI Dashboard**: Interactive, product-facing dashboard with funnel visualisation, slicers, KPIs, and clear recommendations for the Product team.

## Key Insights & Recommendations
- Highest drop-off occurs at the 'Start_Application' stage.
- Prior engagement score is the strongest predictor of success.
- Mobile users and students from State schools show higher friction.
- **Recommendation**: Implement targeted reminders and simplified flows for low-engagement students to improve completion rates.

## Tech Stack
- Python (pandas, scikit-learn)
- SQL
- Power BI

## How to Explore
1. Clone the repo
2. Run `python generate_dataset.py`
3. Run `python analysis.py`
4. Open the `.pbix` file in Power BI Desktop

**Live Dashboard** (may require login): [View here](https://app.powerbi.com/reportEmbed?reportId=be70e4af-b03e-4474-943d-2b95c63aa883)

Screenshots of Dashboard
<img width="1710" height="1107" alt="Screenshot 2026-06-29 at 15 22 25" src="https://github.com/user-attachments/assets/93d86b63-24f0-4dbc-b5b5-2b738c978ec4" />
<img width="1710" height="1107" alt="image" src="https://github.com/user-attachments/assets/6193d703-e3c1-4267-a4ee-4e3def1618db" />
<img width="1710" height="1107" alt="Screenshot 2026-06-29 at 15 22 38" src="https://github.com/user-attachments/assets/9a31ca50-0a30-437b-96ec-698abb3ff0d2" />

Built with genuine interest in Unifrog’s work on student progression and data-driven product decisions. Happy to walk through it in more detail!
