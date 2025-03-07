#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

# from scrum_project.crew import ScrumProject
from src.scrum_project.crew import ScrumProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    print("\n🚀 ¡Ejecutando el equipo SCRUM! 🚀")
    
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        # ScrumProject().crew().kickoff(inputs=inputs)
        resultado = ScrumProject().crew().kickoff(inputs=inputs)
        print("\n=== 🚀 RESULTADO DEL EQUIPO SCRUM ===")
        print(resultado)
        print("\n✅ ¡Ejecución completada con éxito!")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        ScrumProject().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ScrumProject().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs"
#     }
#     try:
#         ScrumProject().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()  # 🔥 Llamamos a la función para que se ejecute