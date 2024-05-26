from asyncflows.actions.base import Action, BaseModel
from asyncflows.actions.transformer import  Outputs
from asyncflows.models.config.model import BiEncoderModelType
from typing import Any

import numpy as np
from pydantic import ConfigDict

class EmbedInputs(BaseModel):
    model: BiEncoderModelType = "sentence-transformers/all-mpnet-base-v2"
    documents: list[Any]
    texts: None | list[str] = None

class EmbedOutputs(BaseModel):
    model_config: Any = ConfigDict(
        arbitrary_types_allowed=True,
    )

    embeds: Any = None
    documents: list[Any]

class Embed(Action[EmbedInputs, EmbedOutputs]):
    name = "embed"

    async def run(self, inputs: EmbedInputs) -> EmbedOutputs:
        from infinity_emb import AsyncEmbeddingEngine, EngineArgs
        model = inputs.model
        assert(inputs.texts is not None)

        args = EngineArgs(model_name_or_path=model)
        engine = AsyncEmbeddingEngine.from_args(args)
        await engine.astart()
        embeddings, _ = await engine.embed(sentences=inputs.texts)

        out = [(e,d) for (e,d) in zip(embeddings,inputs.documents)]
        return EmbedOutputs(
            embeds=np.asfarray(embeddings).tolist(),
            documents=inputs.documents
        )

        return Outputs(
            result=out,
        )