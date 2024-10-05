from langsmith import evaluate
from .evaluators import evaluate_length,qa_evaluator




class Experiment:

    def __init__(self,app):
        self.app=app
    models_prefixes=[
       ( "gpt-4-turbo","openai-4"),
        ("gpt-4-turbo","strict-openai-4"),
       ( "gpt-3.5-turbo","openai-3.5"),

    ]
    dataset_name = "FindInFiles Example Dataset"

    def langsmith_app_2(self,inputs):
        output = self.app.invoke(inputs)
        return {"output": output}

    def perform_experiment(self): 
        evaluate_result=evaluate(
             self.langsmith_app_2,
            data=self.dataset_name, # The data to predict and grade over
            evaluators=[evaluate_length,qa_evaluator], # The evaluators to score the results
            experiment_prefix="my-app-experiment",# A prefix for your experiment names to easily identify them
        )


