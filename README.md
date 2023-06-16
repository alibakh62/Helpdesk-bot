# Helpdesk-bot
This is a simple implementation of a helpdesk bot using the `langchain` library and OpenAI API. This project is meant to showcase how to use LLMs to read the helpdesk instructions of a company and answer questions about it.

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


