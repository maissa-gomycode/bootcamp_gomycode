
# LCEL Pipeline with Gemini 2.5 Flash

## Description
This project implements a three-step LCEL pipeline using LangChain and Gemini 2.5 Flash.

## Pipeline
1. Decomposition: Generates up to three numbered sub-questions.
2. Answering: Answers each sub-question using batch() for concurrent execution.
3. Synthesis: Combines the answers into a concise three-line summary.

## LCEL Usage
The pipe operator (|) connects prompts, the Gemini model and output parsers. RunnableLambda handles custom processing, while RunnablePassthrough.assign() preserves intermediate results.

## Testing
The pipeline is tested with two different questions and includes a unit test to verify the maximum of three sub-questions.

Model: gemini-2.5-flash
