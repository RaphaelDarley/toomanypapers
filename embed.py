import glob
from asyncflows import Action, BaseModel, Field, AsyncFlows
from asyncflows.actions.base import Action, BaseModel
import my_actions.extract_pdf_custom as extract_pdf_custom
from asyncflows.actions.transformer import BaseTransformerInputs, Outputs
from asyncflows.models.config.model import BiEncoderModelType, CrossEncoderModelType
import numpy as np
from typing import Any


async def main():
    print("starting main")

    document_paths = glob.glob("./arxiv_cs/pdf/*/*.pdf")
    pdf_filepaths = document_paths[0:20]

    flow = AsyncFlows.from_file("./embed.yaml").set_vars(
        pdf_filepaths=pdf_filepaths
    )
    res = await flow.run()
    # print(res)
    return


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
