import yaml
from crewai import Agent
from crewai_tools import WebsiteSearchTool
from langchain_openai import ChatOpenAI

# Mapping of available tools
TOOLS = {
    "WebsiteSearchTool": WebsiteSearchTool(),
}


def load_agents(config_path: str = "config/agents.yaml") -> dict:
    """
    Load and instantiate Agent objects based on the agents.yaml configuration.

    Returns:
        dict: A mapping from agent name to Agent instance.
    """
    with open(config_path) as f:
        cfg = yaml.safe_load(f).get("agents", {})

    agents = {}
    for name, info in cfg.items():
        # Initialize the LLM
        llm_cfg = info.get("llm", {})
        llm = ChatOpenAI(
            model_name=llm_cfg.get("model_name", "gpt-3.5-turbo"),
            temperature=llm_cfg.get("temperature", 0.7),
        )

        # Attach any configured tools
        tool_objs = []
        for tool_name in info.get("tools", []):
            tool = TOOLS.get(tool_name)
            if tool:
                tool_objs.append(tool)

        # Instantiate the Agent
        agent = Agent(
            role=info.get("role", ""),
            backstory=info.get("backstory", ""),
            goal=info.get("goal", ""),
            llm=llm,
            tools=tool_objs,
            allow_delegation=info.get("allow_delegation", False),
            verbose=info.get("verbose", False),
        )
        agents[name] = agent

    return agents