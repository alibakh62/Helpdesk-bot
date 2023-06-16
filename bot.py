import os
import json
import argparse
from pathlib import Path
from pprint import pprint
from langchain.document_loaders import JSONLoader
from langchain.indexes import VectorstoreIndexCreator
from dotenv import load_dotenv

load_dotenv()


# Define a function to generate metadata for each document.
def generate_metadata(sample, metadata):
    # Extract 'Time', 'URL', and 'MainTask' from the sample and add them to the metadata.
    metadata["Time"] = sample["Time"]
    metadata["URL"] = sample["URL"]
    metadata["MainTask"] = sample["MainTask"]
    return metadata


def main(query):
    # Create the JSONLoader.
    loader = JSONLoader(
        file_path="../data/sample.json",
        jq_schema=".[] | {Time: .Time, URL: .URL, MainTask: .MainTask, Steps: [.Steps[] | {Description: .Description, Headline: .Headline, Links: .Links}]}",
        metadata_func=generate_metadata,
        text_content=False,
    )

    # Load the documents.
    docs = loader.load()

    # Create the vectorstore
    index = VectorstoreIndexCreator().from_loaders([loader])

    # query the vectorstore
    results = index.query(query)
    pprint(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query the bot.")
    parser.add_argument(
        "--query", type=str, help="The query to ask the bot", required=True
    )

    args = parser.parse_args()

    main(args.query)
