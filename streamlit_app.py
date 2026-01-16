import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import pyttsx3
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ==============================
# Page Config
# ==============================
st.set_page_config(page_title="Talking AI Analyst", layout="wide")
st.title("🤖 Talking AI Data Analyst")

# ==============================
# File Upload
# ==============================
uploaded_file = st.file_uploader("📂 Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # ==============================
    # Data Preview
    # ==============================
    st.subheader("👀 Data Preview")
    st.dataframe(df.head())

    # ==============================
    # Summary Statistics
    # ==============================
    st.subheader("📊 Summary Statistics")
    st.write(df.describe(include="all"))

    num_cols = df.select_dtypes(include="number").columns
    cat_cols = df.select_dtypes(exclude="number").columns

    # ==============================
    # Visualizations
    # ==============================
    if len(num_cols) > 0:
        st.subheader("📈 Histogram")
        st.plotly_chart(px.histogram(df, x=num_cols[0]), use_container_width=True)

    if len(num_cols) > 1:
        st.subheader("🔥 Correlation Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    if len(cat_cols) > 0:
        st.subheader("📊 Categorical Bar Chart")
        counts = df[cat_cols[0]].value_counts().reset_index()
        counts.columns = [cat_cols[0], "Count"]
        st.plotly_chart(
            px.bar(counts, x=cat_cols[0], y="Count", text="Count"),
            use_container_width=True
        )

    # ==============================
    # Profiling Report
    # ==============================
    st.subheader("📑 Automated Profiling Report")
    profile = ProfileReport(df, explorative=True)
    st_profile_report(profile)

    # ==============================
    # Automated Insights
    # ==============================
    st.subheader("🧠 Automated Insights")
    insights = []

    for col in num_cols:
        insights.append(
            f"📌 Column '{col}' has mean {df[col].mean():.2f}, "
            f"min {df[col].min()}, max {df[col].max()}."
        )

    missing = df.isnull().sum()
    for col, val in missing.items():
        if val > 0:
            insights.append(f"📌 Column '{col}' has {val} missing values.")

    for ins in insights:
        st.write(ins)

    # ==============================
    # Text to Speech
    # ==============================
    engine = pyttsx3.init()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔊 Read Insights"):
            for i in insights:
                engine.say(i)
            engine.runAndWait()

    with col2:
        if st.button("⏹️ Stop"):
            engine.stop()

    # ==============================
    # Download Insights TXT
    # ==============================
    st.download_button(
        "📥 Download Insights (TXT)",
        "\n".join(insights),
        file_name="insights.txt"
    )

    # ==============================
    # Export PDF
    # ==============================
    st.subheader("📄 Export Insights")

    if st.button("Download PDF Report"):
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, "Automated Data Insights Report")

        y = height - 100
        c.setFont("Helvetica", 11)

        for text in insights:
            c.drawString(50, y, text)
            y -= 20
            if y < 50:
                c.showPage()
                y = height - 50

        c.save()
        buffer.seek(0)

        st.download_button(
            "📥 Download PDF",
            buffer,
            file_name="data_insights.pdf",
            mime="application/pdf"
        )

    # ==============================
    # SMART AI Q&A (CORRECT LOGIC)
    # ==============================
    st.subheader("❓ Ask AI About Your Data")

    question = st.text_input(
        "Ask like: Highest Product ID, Average Quantity, Total Orders"
    )

    if st.button("Get AI Answer"):
        q = question.lower()

        try:
            if "highest product" in q:
                answer = df["Product ID"].max()

            elif "average quantity" in q:
                answer = round(df["Quantity"].mean(), 2)

            elif "total orders" in q:
                answer = df["Order ID"].nunique()

            elif "most common product" in q:
                answer = df["Product ID"].mode()[0]

            else:
                answer = "I can answer only structured data questions."

            st.success(f"🤖 Answer: {answer}")

        except Exception as e:
            st.error(f"Error: {e}")

else:
    st.info("👆 Upload a CSV file to start")














