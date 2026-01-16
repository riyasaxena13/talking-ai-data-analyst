# 🤖 Talking AI Data Analyst

**Talking AI Data Analyst** is an **interactive AI-powered Streamlit application** that allows users to perform **automated data analysis** on CSV datasets with ease. The app provides **visualizations, summary statistics, automated insights, and text-to-speech functionality**, making data exploration faster, smarter, and more intuitive. Ideal for students, data enthusiasts, and professionals looking for a **quick way to understand their data without manual effort**.


## 🌟 Key Features

- **Data Preview**: View the first few rows of your dataset.
- **Summary Statistics**: Descriptive statistics for numerical and categorical columns.
- **Visualizations**:
  - Histograms for numeric columns
  - Correlation heatmap
  - Bar charts for categorical columns
- **Automated Profiling Report**: Generate a full EDA report using `ydata-profiling`.
- **Automated Insights**:
  - Mean, min, max for numeric columns
  - Missing values detection
  - Most common values for categorical columns
- **AI Q&A**: Ask structured questions like:
  - "Highest Product ID"
  - "Average Quantity"
  - "Total Orders"
  - "Most Common Product"
- **Text-to-Speech**: Listen to insights directly from the app.
- **Export Options**:
  - Download insights as **TXT**
  - Download insights as **PDF report**

---

## 🛠️ Technologies & Libraries Used

- Python
- Streamlit
- Pandas
- Seaborn & Matplotlib
- Plotly Express
- YData Profiling (`ydata-profiling`)
- pyttsx3 (Text-to-Speech)
- ReportLab (PDF generation)

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/talking-ai-data-analyst.git


Navigate to the project folder: cd talking-ai-data-analyst
Install dependencies: pip install -r requirements.txt
Run the Streamlit app:streamlit run app.py


