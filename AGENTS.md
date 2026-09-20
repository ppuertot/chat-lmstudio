# AGENTS

## What is an *Agent* in LM Studio?

An **agent** is a lightweight, reusable component that encapsulates a specific task or workflow. Think of it as a function with context – you give it input, and it produces output while maintaining internal state if needed.

### Core concepts
| Concept | Description |
|---------|-------------|
| **Skill** | A library‑like bundle of tools (Python functions, shell commands, etc.) that an agent can invoke. |
| **Prompt** | The text template or instruction the agent uses to generate a response with its language model. |
| **State** | Optional persistent data stored in LM Studio’s key‑value store; useful for multi‑turn conversations or long‑running tasks. |

### How to create an Agent
1. **Define a skill** – write a Python function, register it as a skill, and expose it via the `lmstudio` SDK.
2. **Write a prompt** – craft a prompt that calls the skill using the `{skill_name}` syntax.
3. **Instantiate the agent** in your application code:
   ```python
   from lmstudio import Agent
   agent = Agent(
       name="my_agent",
       prompt=MY_PROMPT,
       skills=[my_skill],
   )
   ```
4. **Run the agent** – call `agent.run(input_text)` and get the model output.

### Example: A Simple Summarizer Agent
```python
# summarizer.py
from lmstudio import Skill, Agent

summarize = Skill(
    name="summarize",
    function=lambda text: "This is a summary of the provided text."
)

PROMPT = (
    "You are a helpful assistant that summarizes long passages.
    \nInput:\n{input_text}\n\nSummary:\n"
)

summarizer_agent = Agent(name="summarizer", prompt=PROMPT, skills=[summarize])
```

### Running the Agent from the CLI
```bash
lmstudio agent run summarizer "Here is a long paragraph that needs summarizing."
```

> **Tip** – Use `lmstudio agent list` to see all registered agents.

---
## Best Practices
| Practice | Why it matters |
|----------|----------------|
| Keep skills small and focused | Easier to test and maintain. |
| Document prompts clearly | Reduces ambiguity for the model. |
| Persist state only when necessary | Avoids bloated storage usage. |

---
## Resources
- [LM Studio Documentation](https://lmstudio.ai/docs)
- [Python SDK Reference](https://lmstudio.ai/sdk/python)
- [Community Forum](https://community.lmstudio.ai) | Feel free to ask questions or share your agent designs!
