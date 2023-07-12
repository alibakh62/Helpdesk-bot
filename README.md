# Helpdesk-bot
With the advent of LLMs, many companies are looking to utilize them in their workflows, mainly through the automation of their processes. One of the areas in which LLMs could be very helpful is the Customer Service department which handles customer queries. Usually, companies prefer to handle first-tier inquiries through a bot system so that less traffic is routed to the human customer support agents. This brings down the costs and also could increase customer satisfaction as support through bots is usually faster (if done right).

Without using LLMs, one must create a rule-based solution with a rule for every possible customer query. This method is doomed to fail (or at least not work as expected) mainly due to two reasons:

- It's very tedious work to create such systems where one has to define the logic the bot must follow manually. Also, every time there's an update in a company's internal processes, someone has to make sure that it's also defined for the bot, which can be easily missed.
- Same question could be said differently. Therefore, simple intent detection based on keywords won't work.

A potential solution that could address these issues elegantly is to use an instruction-tuned LLM (e.g., ChatGPT) that uses the company's internal customer support documents as context to answer customer inquiries.

This is a simple implementation of a helpdesk bot using the `langchain` library and OpenAI API. This project is meant to showcase how to use LLMs to read the helpdesk instructions of a company and answer questions about it.

I used the WikiHow dataset as an example of context data. It's the closest dataset to the helpdesk documents. The dataset contains many JSON files, and each file contains an instruction to complete a task.

The following future steps are under development now:

- Add support for handling different types of files such as .docx, .pdf, etc.
- Add a chatbot UI.
- Create API endpoints.
- Containerize for simpler deployment.

# Installation & Setup
To install the project, clone the repository and navigate to the project directory.

I highly recommend to use a virtual environment to install the dependencies. To create a virtual environment, run the following command:
```bash
python -m venv venv
```

To install the dependencies, run the following command:
```bash
pip install -r requirements.txt
```

**Note:** You also need to rename the `.env.example` file to `.env` and add your OpenAI API key to the file.

# Usage
To run the bot, run the following command:
```bash
python bot.py --query "<your query>"
```

As an example of an instruction data, I downloaded WikiHow data that contains instructions on how to do various tasks.

Here's an example of the bot output answering the question "How to install MS Office on Linux?":
```bash
(' You can install MS Office on Linux by using Wine, a compatibility layer for '
 'running Windows applications on non-Windows POSIX-compliant operating '
 'systems. To do this, you need to install Wine on Ubuntu, open Wine '
 'configuration, select the Libraries tab, override riched20 DLL, select '
 'native load order, apply the load order change, run the installation '
 'executable, and then install the office suite as if you were running Windows '
 'machine.')
```

Change the file name to `wikiHow0.json` to get the bot to answer other different questions. You can download the file from [here](https://drive.google.com/file/d/1uHBrFv-JI4BhcrmGXV_a9bS3W-RweXfn/view?usp=sharing).


