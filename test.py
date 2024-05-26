from asyncflows import Action, BaseModel, Field, AsyncFlows

async def main():
    print("starting main")
    username = input("what's your name:\n>>>")
    flow = AsyncFlows.from_file("./test.yaml").set_vars(
        username = username
    )
    res = await flow.run()
    print(res)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
