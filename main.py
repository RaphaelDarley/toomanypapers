from asyncflows import Action, BaseModel, Field, AsyncFlows
import glob


async def user_add():
    user_id = 1
    interests = "alternatives to transformers"


async def main():
    print("starting main")
    document_paths = glob.glob("./arxiv_cs/pdf/*/*.pdf")
    document_paths = document_paths[0:1]

    # Load the chatbot flow
    flow = AsyncFlows.from_file("pdf_process.yaml").set_vars(
        pdf_filepaths=document_paths,
    )

    # Keep track of the conversation history
    conversation_history = []

    # Run the flow
    while True:
        # Get the user's query via CLI interface (swap out with whatever input method you use)
        try:
            message = input("Ask me anything: ")
        except EOFError:
            break

        # Set the query and conversation history
        query_flow = flow.set_vars(
            message=message,
            conversation_history=conversation_history,
        )
        
        # Run the flow and get the result
        result = await query_flow.run()
        print(result)
        
        # Update the conversation history
        conversation_history.extend(
            [
                f"User: {message}",
                f"Assistant: {result}",
            ]
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())