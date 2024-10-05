from .llms import eval_llm
from .prompts import PROMPT
from langsmith.evaluation import LangChainStringEvaluator
from langsmith.schemas import Run, Example


def prepare_data(run: Run, example: Example):
    data= {
        "prediction": run.outputs["output"],
        "reference": example.outputs["answer"],
        "input": example.inputs["input"],
        "chat_history":example.inputs["chat_history"]
    }
    return data

qa_evaluator = LangChainStringEvaluator("qa", config={"llm": eval_llm, "prompt": PROMPT},prepare_data=prepare_data)



def evaluate_length(run: Run, example: Example) -> dict:
    prediction = run.outputs.get("output") or ""
    required = example.outputs.get("answer") or ""
    score = int(len(prediction) < 2 * len(required))
    return {"key":"length", "score": score}