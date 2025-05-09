Dataguy Documentation
=====================

Welcome to **DataGuy** — a Python package designed to simplify data science workflows using Large Language Models (LLMs).
It helps with intelligent data wrangling, analysis, and visualization for small-to-medium datasets.

Features
--------

- **Automated Data Wrangling**: Clean and preprocess your data using LLM-generated code.
- **AI-Powered Data Visualization**: Describe a plot in words, and let DataGuy build it.
- **Intelligent Data Analysis**: Use natural language prompts to guide statistical summaries or comparisons.
- **Customizable Workflows**: Integrate with `pandas`, `matplotlib`, and more.
- **Safe Code Execution**: Built-in sandboxing to guard against untrusted code execution.
How It Works
============

DataGuy is an intelligent assistant for data exploration and analysis, powered by large language models (LLMs).
This section explains how DataGuy interprets your input, generates code, handles errors, and delivers results.

Overview
--------

The workflow consists of the following steps:

1. **Model Selection**
   DataGuy decides whether your input should be interpreted as a request for a description, a plot, or a code transformation. It selects the appropriate LLM mode accordingly.

2. **Context Building**
   A conversational context is created to track previous prompts, results, and errors. This ensures coherent interactions and allows for iterative improvements.

3. **Prompt Generation**
   Based on your task, DataGuy builds one of three prompt types:

   - **Text mode** for dataset summaries or explanations
   - **Image mode** for understanding uploaded visualizations
   - **Code mode** for generating and executing data operations

4. **LLM Interaction**
   The selected model writes Python code (e.g., `pandas`, `matplotlib`) or produces a natural language response. If execution fails, DataGuy resubmits the failed code with the error message for refinement.

5. **Safe Code Execution**
   Generated code is sandboxed and evaluated in a restricted environment to prevent dangerous operations.

6. **Caching and Retry Logic**
   Past results are cached to avoid duplicate computation. Failed executions are corrected automatically by feeding context back into the model.

Visual Workflow
---------------

.. mermaid::

   graph TD
     A[User Prompt] --> B[Model Selection]
     B --> C[Prompt Builder]
     C --> D[LLM Request]
     D --> E[Code or Text Generation]
     E --> F[Safe Execution]
     F --> G[Output (Chart, Summary, etc.)]

Example Usage
-------------

.. code-block:: python

   from dataguy import DataGuy

   # Create the assistant
   dg = DataGuy()

   # Load a dataset
   dg.load("sales.csv")

   # Ask a question or request a plot
   dg.ask("Describe this dataset")
   dg.ask("Show a bar chart of sales by region")

   # DataGuy interprets the request and responds with a chart or summary


Installation
------------

Install DataGuy via pip:

.. code-block:: bash

   pip install dataguy

Quickstart
----------

.. code-block:: python

   from dataguy import DataGuy
   dg = DataGuy("data.csv")
   dg.describe()
   dg.visualize("a bar chart of sales by category")

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   how_it_works
   api/index
   changelog


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
