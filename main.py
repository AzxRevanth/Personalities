# from dotenv import load_dotenv
# load_dotenv()
import os
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from crewai import Task, Crew
from agents import (
    intp, entp, infj, enfj, estj, istj,
    entj, intj, enfp, infp, isfj, esfj,
    esfp, istp, isfp, estp, neutral
)
from memory import retrieve_memory

AGENT_DESCRIPTIONS = {
    "intp": (intp, "Analyze logically and question assumptions"),
    "entp": (entp, "Challenge ideas and explore alternatives"),
    "infj": (infj, "Respond with values and long-term human impact"),
    "enfj": (enfj, "Encourage and guide with people-focused advice"),
    "estj": (estj, "Provide decisive, practical direction"),
    "istj": (istj, "Provide careful, methodical steps"),
    "entj": (entj, "Set direction and focus on execution"),
    "intj": (intj, "Propose a strategic, long-term solution"),
    "enfp": (enfp, "Generate creative and optimistic possibilities"),
    "infp": (infp, "Respond with empathy and values"),
    "isfj": (isfj, "Focus on reliability and proven methods"),
    "esfj": (esfj, "Consider group needs and social impact"),
    "esfp": (esfp, "Respond based on real-world experience"),
    "istp": (istp, "Break down the problem and solve practically"),
    "isfp": (isfp, "Respond calmly with authenticity"),
    "estp": (estp, "Focus on fast action and opportunities"),
}


def run_council(username: str, question: str, selected_agents: dict):
    tasks = []
    outputs = {}
    agents_used = []

    past_notes = retrieve_memory(username, question)

    for key, value in selected_agents.items():
        if value:
            agent, description = AGENT_DESCRIPTIONS[key]
            task = Task(
                description=description,
                agent=agent,
                expected_output="A clear and relevant response"
            )
            tasks.append(task)
            agents_used.append(agent)
            outputs[key] = task

    if not tasks:
        return {"final": "Please select at least one personality."}

    if len(tasks) > 1:
        memory_context = "\n".join(f"- {n}" for n in past_notes)
        synth_task = Task(
            description=(
                "Combine all selected perspectives into one clear, concise answer. "
                "Use the following past knowledge if relevant:\n"
                f"{memory_context}\n\n"
                "Resolve conflicts and provide 2–3 actionable steps."
            ),
            agent=neutral,
            context=tasks,
            expected_output="A balanced final answer"
        )
        tasks.append(synth_task)
        agents_used.append(neutral)

    crew = Crew(
        agents=agents_used,
        tasks=tasks,
        process="sequential",
        verbose=False
    )

    final_output = crew.kickoff()

    result = {k: t.output for k, t in outputs.items()}

    result["final"] = (
        list(outputs.values())[0].output
        if len(outputs) == 1
        else final_output
    )

    return result
