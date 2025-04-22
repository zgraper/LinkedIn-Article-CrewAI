import os
import yaml
import streamlit as st
from decouple import config
from crewai import Crew
from crewai_tools import WebsiteSearchTool
from langchain_openai import ChatOpenAI

from agents import load_agents
from tasks import load_tasks

# Load environment variables
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

# Initialize tools (if additional tool setup needed)
# WebsiteSearchTool is configured in agents by name

# Load and instantiate Agents and Tasks
agents = load_agents("config/agents.yaml")
tasks = load_tasks("config/tasks.yaml", agents=agents)

# Streamlit app setup
st.set_page_config(page_title="CrewAI LinkedIn Article Generator")
st.title("CrewAI LinkedIn Article Generator")

# Sidebar inputs
with st.sidebar:
    st.header("Article Parameters")
    topic = st.text_input("Topic of the article")
    num_resources = st.number_input("Number of resources", min_value=1, max_value=20, value=5)
    tone = st.selectbox("Tone", ["Friendly", "Formal", "Analytical"])
    audience_level = st.selectbox("Audience Level", ["Beginner", "Intermediate", "Expert"])
    word_count = st.number_input("Target Word Count", min_value=100, max_value=5000, value=800)
    additional_instructions = st.text_area("Additional Instructions")
    generate = st.button("Generate Article")

# Orchestrate CrewAI run
if generate:
    inputs = {
        "topic": topic,
        "num_resources": num_resources,
        "tone": tone,
        "audience_level": audience_level,
        "word_count": word_count,
        "additional_instructions": additional_instructions,
    }
    crew = Crew(agents=list(agents.values()), tasks=tasks, verbose=False)
    result = crew.kickoff(inputs=inputs)
    final = result.get("final_article") if isinstance(result, dict) else result

    st.subheader("Generated Article")
    st.markdown(final or "*No output returned.*")