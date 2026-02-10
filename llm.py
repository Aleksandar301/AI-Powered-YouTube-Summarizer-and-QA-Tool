# llm.py
import ollama

class LocalLLM:
    def __init__(self, model_name):
        """
        Initializes the local Ollama model.
        model_name: the name of the model pulled locally via Ollama
        """
        self.model_name = model_name

    def generate_answer(self, context: str, query: str) -> str:
        """
        Generates an answer using the Ollama local model.
        """
        prompt = f"Use the following context to answer the question:\n{context}\n\nQuestion: {query}\nAnswer:"

        # Run Ollama model via the Python API
        response = ollama.chat(model=self.model_name, messages=[{"role": "user", "content": prompt}])
        # returns the model's text output
        return response['message']['content']

# Optional helper
def get_llm(model_name):
    return LocalLLM(model_name)
