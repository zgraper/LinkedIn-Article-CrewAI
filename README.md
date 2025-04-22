# CrewAI LinkedIn Article Generator

A Streamlit‑powered interface that leverages CrewAI agents to research a topic, draft multiple parallel article versions in different styles, and compile a polished, LinkedIn‑ready post.

---

## 🚀 Features

- **Automated Research**  
  Uses `WebsiteSearchTool` to fetch the top N recent, reputable sources on your topic.

- **Parallel Drafting**  
  Three distinct writer agents generate drafts in “friendly,” “formal,” or “analytical” styles.

- **Editorial Merge & Proofreading**  
  An editor agent compiles the best sections, proofreads, and fact‑checks against original URLs.

- **Live Preview**  
  Instant rendering of your final article in the Streamlit UI, ready to copy into LinkedIn.

- **Config‑Driven**  
  Easily tweak agent behavior, task pipelines, and rate limits via YAML under `config/`.

---

## 🧰 Prerequisites

- **Python** 3.9+  
- **OpenAI API key** (set in your `.env` as `OPENAI_API_KEY`)  
- **Replit** (for hosted deployment) or any machine that can run Streamlit

---

## 📦 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your‑username/crewai‑linkedin‑generator.git
   cd crewai‑linkedin‑generator
   ```

2. **Create & activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set you OpenAI key**
   Create a file named `.env`
   ```ini
   OPENAI_API_KEY=sk‑your_api_key_here
   ```

---

## ⚙️ Configuration

All agent behaviors and task definitions live under `config/`:

    `config/agents.yaml`
    Defines each agent’s role, LLM model, temperature, attached tools, and rate limits.

    `config/tasks.yaml`
    Defines each task’s name, description, agent assignment, dependencies, and expected output schema.

You can adjust temperature, add or remove agents, tweak prompts, or update rate limits without touching any Python code.

---

## ▶️ Running the App

**Locally**
```bash
streamlit run main.py \
  --server.address=0.0.0.0 \
  --server.port=8501
```
Then open http://localhost:8501 in your browser.

**One Replit**
1. Add a file named `.replit` with:
   ```toml
   run = "streamlit run main.py --server.address=0.0.0.0 --server.port=$PORT"
   ```

2. Ensure your `.env` contains `OPENAI_API_KEY`.

3. Click **Run** in the Replit UI.

---

## 📁 Project Structure

```bash
.
├── .env                    # Your OpenAI API key
├── .replit                 # (Replit) custom run command
├── config/
│   ├── agents.yaml         # Agent definitions & parameters
│   └── tasks.yaml          # Task pipelines & expected outputs
├── main.py                 # Streamlit interface & Crew kickoff
├── agents.py               # load_agents() → Agent instances
├── tasks.py                # load_tasks()  → Task instances
├── utils.py                # (optional) shared helpers & rate‑limiters
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🔧 Troubleshooting

  **Tool import errors**
  `ImportError: cannot import name 'WebsiteSearchTool'`
  Ensure you're importing `crewai_tools`, not `crewai.tools`.

  **YAML parse errors**
  Watch your indentation—each task field (name, agent, description, expected_output) must be indented 4 spaces under its list item.

  **502 on Replit**
  Make sure Streamlit binds to `0.0.0.0` and the `$PORT` via your `.replit` or `.streamlit/config.toml`.

---

## 🤝 Contributing

1. Fork the repo

2. Create a feature branch (`git checkout -b feat/awesome-agent`)

3. Commit your changes (`git commit -m "Add new SEO agent"`)

4. Push (`git push origin feat/awesome-agent`)

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License. See LICENSE for details.

---

```CSS

Feel free to tweak any section—especially the configuration details and troubleshooting tips—to match your setup or personal preferences!
```
