from eval_utils.experiments import Experiment
from chains import get_rag_chain
perform_experiment=Experiment(get_rag_chain()).perform_experiment()

