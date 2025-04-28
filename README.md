✈️ Air Schedule Formatter
This Streamlit app is designed to quickly format pasted air schedules into clean HTML tables for easy copying and pasting by contact center agents. Additionally, it takes the content from a provided schedule and creates a DOT script agents can use when quoting flights. 

🚀 What It Does
  - Accepts a pasted air schedule (e.g., flight details from booking system or directly from air department).
  - Formats the pasted text into a properly structured HTML table.
  - Makes it faster and easier for agents to copy and share flight schedules.

⚠️ Important — Formatting Requirements
  - As this tool was developed to parse very specific regex, the pasted air schedule must follow the defined regex formats for the tool to work correctly.
    - Text must be consistently structured (e.g., consistent number of columns, expected line breaks, no missing data).
    - Unexpected variations (extra spaces, missing fields, inconsistent delimiters, etc.) will cause the formatter to fail or produce incorrect HTML.

💬 Tip: If the tool fails to format properly, double-check the pasted content for any inconsistencies or formatting errors.
