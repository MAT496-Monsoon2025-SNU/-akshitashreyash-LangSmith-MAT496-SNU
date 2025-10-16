# -akshitashreyash-LangSmith-MAT496-SNU
module 1 - LangGraph
---
Video 1: Motivation

Concepts Learned

Understood the control flow of LangGraph applications.

Control flow can be manual or LLM-driven.

The more autonomy given to the LLM, the less reliable the results — LangGraph bridges this reliability gap.

Notes

No code executed in this video.
-----------

-Video 2: Simple Graph-

Concepts Learned

Learned the structure of a LangGraph, consisting of nodes and edges.

Studied conditional edges and graph states.

Built a graph using the StateGraph() builder.

Changes Implemented

Modified conditional nodes to analyze the user’s mood based on input text.

Node selection now depends on input semantics (e.g., text in all caps → angry tone).

Added five conditional nodes in total.

Prefixed a custom string to the initial graph state.

Commit Summary

-------------------
Video 3: Studio

Concepts Learned

Set up and ran a local LangSmith Studio development server.

Visualized graph execution directly in the browser interface.

Changes Implemented

Updated simple.py to match the customized graph from Video 2.

Executed and visualized the run in Studio.

Saved the studio visualization as a PNG in the Module 1 folder.

Commit Summary

png
------------------
Video 4: Chain

Concepts Learned

Revisited tool calling concepts.

Integrated tools into graphs through chains where messages represent nodes.

Changes Implemented

Created a custom tool-calling function for retrieving quotes by category.

Modified the initial message list for testing.

Commit Summary

----------------------------------
Video 5: Router

Concepts Learned

Understood the Router node concept.

In a Chain, the LLM calls a tool and ends; in a Router, the LLM decides whether to call a tool or proceed directly to the end node.

Changes Implemented

Integrated the quote retrieval tool from the Chain module.

Modified router.py with the new tool-calling logic.

Ran and visualized the updated router in LangSmith Studio.

Commit Summary

p
---------------------------------------------
Video 6: Agent

Concepts Learned

Built an Agent using the ReAct principle, where outputs loop back as inputs until completion.

Practiced iterative reasoning within tool-calling nodes.

Changes Implemented

Replaced arithmetic functions with string manipulation tools (reverse text, prefix text, etc.).

Adjusted user prompts accordingly.

Tested and traced the agent successfully in LangSmith Studio.

Commit Summary

