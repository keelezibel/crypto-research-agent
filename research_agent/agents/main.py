from dotenv import load_dotenv
from graph.state import AgentState
from langchain_core.messages import HumanMessage
from research_agent.agents.nodes.sample_agent import sample_agent
from langgraph.graph import END, StateGraph

# Load environment variables from .env file
load_dotenv()


def start(state: AgentState):
    """Initialize the workflow with the input message."""
    return state


def create_workflow():
    """Create the workflow with selected analysts."""
    workflow = StateGraph(AgentState)
    workflow.add_node("start_node", start)
    workflow.add_node("sample_agent", sample_agent)

    workflow.add_edge("start_node", "sample_agent")
    workflow.add_edge("sample_agent", END)

    workflow.set_entry_point("start_node")
    return workflow


def run(
    show_reasoning: bool = False,
):
    workflow = create_workflow()
    agent = workflow.compile()

    final_state = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="",
                ),
            ],
            "data": {},
            "metadata": {
                "show_reasoning": show_reasoning,
            },
        },
    )

    return {
        "response": final_state["data"]["analyst_signals"],
    }


if __name__ == "__main__":
    run()
