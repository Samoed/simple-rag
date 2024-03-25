from typing import Optional

from llama_index.llms.llama_cpp import LlamaCPP

from rag.config import LLM_PATH

_model: Optional[LlamaCPP] = None


def get_llm() -> LlamaCPP:
    """Get the LLM model."""
    global _model

    if _model is not None:
        return _model

    _model = LlamaCPP(
        model_path=LLM_PATH,
        temperature=0.1,
        max_new_tokens=256,
        context_window=3900,
        generate_kwargs={},
        model_kwargs={"n_gpu_layers": 0},
        verbose=True,
    )

    return _model
