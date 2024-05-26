import glob
import os
from pathlib import Path

from asyncflows import AsyncFlows


async def main():
    document_paths = glob.glob("./arxiv_cs/pdf/*/*.pdf")
    pdf_filepaths = document_paths[0:300]
    

    # Load the chatbot flow
    flow = AsyncFlows.from_file("paperbot.yaml").set_vars(
        pdf_filepaths=pdf_filepaths,
    )

    # Get the user's query via CLI interface (swap out with whatever input method you use)
    try:
        interests = input("What kind of papers are you interested in?\n>>>")
    except EOFError:
        return

    # Set the query and conversation history
    query_flow = flow.set_vars(
        interests=interests,
    )

    # Run the flow and get the result
    result = await query_flow.run()
    print(result)
    # print(pdf_filepaths)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())