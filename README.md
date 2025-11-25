*LANGCHAIN

=======

##MODULE 1
###LESSON 1
this lesson included learning:
-Creating prompts using SystemMessage and HumanMessage

-Invoking LLMs using .invoke()

-Streaming model outputs with .stream()

-Understanding how tracing works using @traceable- Helps you track, debug, and visualize every step your LLM workflow takes,Uses the @traceable decorator to automatically log each function run.,

-Loading data from files and using context in prompts

- tool calling - Allows the LLM to decide when to call a function/tool instead of generating text, The LLM outputs a structured JSON object specifying:
Which tool to call
Arguments for that tool

Lesson 2

1. LLM Runs for Chat Models

LLM runs capture every interaction with a chat model. They record the prompt, model settings, and final output. This makes it easy to debug model behavior, compare responses, and understand how an LLM produced its answer.

2. Handling Streaming LLM Runs

Streaming lets the model send outputs in small chunks. LangSmith logs each chunk and then combines them into a final message using a reduce_fn(). This helps visualize step-by-step generation and improves responsiveness.

3. Retriever Runs + Documents

Retriever runs show how your system searches for information. They log the user’s query and the documents returned. Each document includes page_content and metadata, helping you diagnose whether retrieval is correct and improving RAG systems.

Lesson 3

Alternative Tracing Methods
You can trace your LangChain/LangGraph runs using different backends like LangSmith, console logs, file-based logs, or in-memory tracers. Each method captures inputs, outputs, errors, and execution flow for debugging or monitoring.

Tracing Context Manager
A simple with block that automatically traces everything inside it. Great for debugging a specific part of your code without enabling global tracing.

wrap_openai
Wraps the OpenAI client so even direct OpenAI API calls (outside LangChain/LangGraph) appear in your traces. Ensures all LLM usage is captured consistently.

RunTree (Advanced)
A low-level API for building custom trace trees manually. You can add events, metadata, child traces, and control the whole trace structure. Useful for complex or highly customized pipelines.

Lesson 4
Group Traces Into Threads 

Threading lets us group multiple related traces under a single conversation or workflow. Each run inside the thread shares the same thread ID, making it easy to track context, follow history, and analyze entire sessions as one logical unit. This is useful for chat apps, multi-step pipelines, and any workflow where several traces belong to the same user interaction.



***MODULE 2

Lesson 1

This code loads environment variables, creates a LangSmith dataset, and uploads a list of example question–answer pairs. It then defines a minimal RAG-style function (langsmith_rag) that retrieves a simple context snippet and generates a short answer. Finally, we can call langsmith_rag(question) to run the example end-to-end.


Lesson 2 

Evaluators 

Evaluators are tools used to automatically score the quality of model outputs. They compare a model’s response against expected answers or criteria such as accuracy, relevance, clarity, or semantic similarity. Evaluators help benchmark, debug, and improve LLM applications by providing consistent, repeatable scoring.

LLM-as-a-Judge Evaluators

LLM-as-a-Judge evaluators use another language model to grade responses. Instead of hand-crafted rules, the evaluator LLM reads the question, the reference answer, and the model output, then assigns a score (e.g., 1–10). This approach is flexible, scalable, and works well for subjective tasks like semantic similarity, reasoning quality, or explanation clarity.

LESSON 3 

This project builds a small RAG pipeline using the Perplexity API and evaluates it with LangSmith. A Perplexity-powered langsmith_rag function retrieves context, generates answers, and logs runs. A LangSmith dataset is created with custom Q/A examples.
Evaluators score model outputs, and evaluate() runs experiments across full datasets, versions, splits, selected examples, repetitions, concurrency, and metadata.
This setup lets you measure and compare the performance of your RAG system easily.
The model used by us is sonar pro.

LESSON 4 

Experiments evaluate a Perplexity-based RAG pipeline using LangSmith.
Model responses are compared to reference answers using two evaluators: semantic similarity and conciseness.
Traces show how the evaluator interprets each submission and assigns a numeric similarity score.
Dashboard charts reveal how scores vary across dataset examples, with some cases (e.g., #6) showing noticeable drops.
Running experiments across dataset versions, splits, and repetitions highlights how different configurations affect model quality.

=======

MODULE 3

LESSON 1

Experiments evaluate a Perplexity-based RAG pipeline using LangSmith.
Model responses are compared to reference answers using two evaluators: semantic similarity and conciseness.
Traces show how the evaluator interprets each submission and assigns a numeric similarity score.
Dashboard charts reveal how scores vary across dataset examples, with some cases (e.g., #6) showing noticeable drops.
Running experiments across dataset versions, splits, and repetitions highlights how different configurations affect model quality.

Lesson 2

This project builds a small RAG workflow using Perplexity (sonar-pro) for generation and LangSmith for storing and evaluating results.
A prompt is hydrated with a question, language, and an attachment (/mnt/data/Lesson 1.ipynb), then sent to Perplexity. 
The model’s output is saved to a LangSmith dataset (Perplexity-RAG-Results) for later evaluation and comparison. 
This setup enables tracking for RAG-style applications.

Lesson 3

Prompt Engineering Workflow sses a simple LangChain-style prompt template with variables.
Hydrates the prompt using real inputs, including the attached notebook:
/mnt/data/prompt_engineering_lifecycle.ipynb
Sends the hydrated messages to Perplexity (sonar-pro) for generation.
Creates or reuses a LangSmith dataset (Perplexity-RAG-Results).
Logs each input + output pair to LangSmith for tracking and evaluation.
Demonstrates the core steps of prompt engineering:
prompt design → hydration → model call → experiment logging.

Lesson 4

Here we talk about prompt canvas. On Langchain website, we cannot use any key other than open ai and since I use Perplexity, I run the code in my jupyter notebook to create a prompt and run the input using python. 

LANGGRAPH

MODULE 1 

LESSON 1 
We discovered that LangGraph enables us to combine the flexibility of agents with the dependability of fixed control flows (chains). It makes it possible to create partially autonomous, structured, and customizable AI systems. No code in the video hence no jupyter notebook updated.

LESSON 2 

We developed a function to monitor textual differences and timestamps each time a node updates after learning about graph states.

What has altered: Node outputs and the State type now include user_name, mood, last_updated, diff, and previous_graph_state. To make graph.invoke function, a minimal graph runner was implemented, and duplicate cells were swapped out for a single biased decide mood.

LESSON 3

this one was on chains. We learnt how to use the langgraph studio UI in the browser and visualise the node in the UI by entering the graph state here itself.

Lesson 4

This is on router. We learnt how graph can route between direct LLM response and tool execution by inspecting model output and using conditional edges, also learnt using a ToolNode and the tools_condition enables the model to request structured tool calls which are executed and inserted back into message stream.

LESSON 5

I learned how to use MessageState with tool binding, how to inspect the output in Langsmith, and how a ReAct style loop allows the mdoel call toold to observe tool outputs and reason further by feeding tool response back into the assistant node.

LESSON 6&7

We learnt how to add memory to the agent.

