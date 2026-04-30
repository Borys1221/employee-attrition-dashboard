# Employee Attrition Analysis
**Why do employees leave — and what can HR do about it?**

An end-to-end HR analytics project built with Python and vanilla JavaScript.
Analyses 1,470 employee records to identify the strongest drivers of attrition.

🔗 **[Live Dashboard](https://borys1221.github.io/employee-attrition-dashboard/)**

---

## Key Findings

| Finding | Attrition Rate |
|---|---|
| Employees working overtime | 30.5% vs 10.4% without |
| Low salary band | 29.3% vs 10.3% high salary |
| Under 30 years old | 27.9% |
| First year at company | 34.9% |
| Sales Representative role | 39.8% |
| Overall baseline | 16.1% |

**Bottom line:** Overtime and low compensation are the primary drivers.
Early-tenure employees under 30 in Sales are at highest risk.

---

## Dashboard Sections

- **KPI Overview** — attrition rate, avg income, overtime and salary risk
- **Where attrition is highest** — by department and job role
- **Why employees leave** — satisfaction, age, income, tenure segments
- **Heatmaps** — age × income and income × tenure intersections
- **Practical takeaways** — decision-ready findings for HR teams

---

## Tech Stack

- **Python** — data processing and dashboard generation
- **JavaScript / HTML / CSS** — interactive dashboard (no frameworks)
- **GitHub Pages** — live deployment

---

## Run Locally

```bash
python app.py
```
Open: `http://127.0.0.1:8765/index.html`

---

## Project Structure

├── generate_dashboard.py   # Data processing + HTML generation
├── app.py                  # Local development server
├── index.html              # Live dashboard (GitHub Pages entry point)
├── hr_clean.csv            # Cleaned HR dataset (1,470 records)
└── requirements.txt        # Standard library only — no dependencies

---

## About

Built as part of a data analytics portfolio.
Focus: translating raw HR data into actionable business insights.

**Author:** Borys Borysov
[LinkedIn](https://linkedin.com/in/borys-borysov) · [Portfolio](https://github.com/Borys1221)
