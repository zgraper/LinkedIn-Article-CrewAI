import yaml
from crewai import Task

def load_tasks(config_path: str = "config/tasks.yaml", agents: dict = None) -> list[Task]:
    """
    Load and instantiate Task objects based on the tasks.yaml configuration.

    Each task entry in tasks.yaml must include:
      - name
      - description
      - agent
      - expected_output
      - (optional) depends_on
    """
    with open(config_path) as f:
        cfg = yaml.safe_load(f).get("tasks", [])

    tasks = []
    for entry in cfg:
        name            = entry["name"]
        description     = entry.get("description", "")
        expected_output = entry.get("expected_output", "")
        agent_name      = entry["agent"]
        agent           = agents.get(agent_name) if agents else None

        params = {
            "name": name,
            "description": description,
            "expected_output": expected_output,
            "agent": agent,
        }
        # include dependencies if specified
        if entry.get("depends_on"):
            params["depends_on"] = entry["depends_on"]

        task = Task(**params)
        tasks.append(task)

    return tasks
