import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Commercial Credit Risk Dashboard", layout="wide")
st.title("Commercial Credit Risk & Industry Stability")
st.markdown("Automated B2B risk modeling using UK Companies House registry data.")

@st.cache_data
def load_data():
    return pd.read_csv('regional_risk_rank.csv')

df = load_data()

st.sidebar.header("Territory Filter")
regions = ['All'] + sorted(df['region'].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Select Region (Postcode Prefix)", regions)

if selected_region != 'All':
    filtered_df = df[df['region'] == selected_region]
else:
    filtered_df = df

st.markdown("---")
st.subheader("Risk vs. Market Size Matrix")
st.markdown("Identify industries with high market opportunity and low historical default rates.")

fig = px.scatter(
    filtered_df,
    x="total_companies",
    y="failure_rate_pct",
    color="regional_risk_rank",
    hover_name="industry_description",
    hover_data=["region", "total_dissolved"],
    color_continuous_scale="Reds_r",
    labels={
        "total_companies": "Total Active Companies (Market Size)",
        "failure_rate_pct": "Historical Failure Rate (%)",
        "regional_risk_rank": "Risk Rank"
    }
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("Top High-Risk Sectors")
st.markdown("The top 5 most volatile industries based on regional historical dissolution data.")

hit_list = filtered_df[filtered_df['regional_risk_rank'] <= 5].sort_values(by=['region', 'regional_risk_rank'])
st.dataframe(
    hit_list[['region', 'regional_risk_rank', 'industry_description', 'total_companies', 'failure_rate_pct']],
    use_container_width=True,
    hide_index=True
)
