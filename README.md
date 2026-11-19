# AI Agent & Tool Calling — Module 05

An AI Agent prototype built for **Module 05: AI Agents, Tools & Automation** during my Generative AI internship at **Codomax Digital Solutions**.

## Agent Execution Loop
`Understand Task → Decide Action → Use Tool → Process Result → Respond`

## Key Concepts Covered
* **Agent vs. Chatbot:** Uses decision logic and external tools rather than single-turn text generation alone.
* **Tool / Function Calling:** Routes tasks to deterministic helper functions (`calculator_tool`, `internship_status_tool`).
* **State & Memory:** Tracks task history across runs.
* **Safety & Guardrails:** Restricts arithmetic input characters and avoids unsafe code execution.
