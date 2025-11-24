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