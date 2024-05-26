
from asyncflows.actions.base import Action, BaseModel
from asyncflows.actions.transformer import  Outputs
from asyncflows.models.config.model import BiEncoderModelType
from typing import Any

class SdbInputs(BaseModel):
    embeds: list[Any]
    documents: list[Any]

class SdbWrite(Action[SdbInputs, Outputs]):
    name = "sdb_write"

    async def run(self, inputs: SdbInputs) -> Outputs:
        from surrealdb import Surreal

        db = Surreal("ws://localhost:8000")
        await db.connect()
        await db.signin({"user": "root", "pass": "root"})
        await db.use("tmp", "tmp")



        for (e,d) in zip(inputs.embeds, inputs.documents):
            self.log.info("document:", doc=d)
            db.create("chunk", {"doc":d, "embed":e})

        return Outputs(
            result=[],
        )