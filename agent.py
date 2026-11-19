import datetime
import json

# ==========================================================
# Module 05: AI Agents, Tools & Automation
# Flow: Understand Task -> Decide Action -> Use Tool -> Process Result -> Respond
# ==========================================================


def calculator_tool(expression: str) -> str:
    """Safely evaluates basic arithmetic expressions."""
    allowed = set("0123456789+-*/(). ")
    if not expression or not set(expression).issubset(allowed):
        return "Error: Unsupported characters in math expression."
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as exc:
        return f"Error: {exc}"


def internship_status_tool(topic: str = "") -> str:
    """Returns current internship module progress state."""
    state = {
        "completed_or_reviewed": ["Module 01", "Module 02", "Module 03", "Module 04"],
        "active_module": "Module 05 - AI Agents, Tools & Automation",
        "next_module": "Module 06 - GenAI Capstone Project",
        "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
    }
    return json.dumps(state, indent=2)


TOOLS = {
    "calculator": calculator_tool,
    "internship_status": internship_status_tool,
}


class SimpleAIAgent:
    def __init__(self, name: str = "TaskAgent"):
        self.name = name
        self.memory: list[dict] = []

    def decide_action(self, task: str) -> tuple[str | None, str]:
        """Decides which tool to call based on the task."""
        lower = task.lower()
        if any(op in lower for op in ["calculate", "compute", "what is ", "5/7", "71%"]) and any(
            ch.isdigit() for ch in lower
        ):
            # Extract simple math expression if present
            cleaned = "".join(ch for ch in lower if ch in "0123456789+-*/(). ")
            expr = cleaned.strip()
            if expr:
                return "calculator", expr
        if any(word in lower for word in ["module", "progress", "status", "next"]):
            return "internship_status", task
        return None, task

    def run(self, task: str) -> str:
        # 1. Understand Task & 2. Decide Action
        tool_name, tool_input = self.decide_action(task)

        # 3. Use Tool & 4. Process Result
        if tool_name and tool_name in TOOLS:
            raw_result = TOOLS[tool_name](tool_input)
            observation = f"[Tool: {tool_name} | Input: {tool_input}] -> {raw_result}"
        else:
            observation = "[No external tool needed] -> Handled directly from agent memory/instructions."

        # 5. Respond & update state/memory
        response = f"{self.name} Response for '{task}':\n{observation}"
        self.memory.append({"task": task, "observation": observation})
        return response


if __name__ == "__main__":
    agent = SimpleAIAgent("CodomaxHelperAgent")
    sample_tasks = [
        "What is my current module status and what comes next?",
        "Calculate (5 / 7) * 100",
        "Explain how an agent differs from a plain chatbot.",
    ]
    for t in sample_tasks:
        print("=" * 60)
        print(agent.run(t))
