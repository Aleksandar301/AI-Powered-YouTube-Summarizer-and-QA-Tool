from llm import get_llm

if __name__ == "__main__":
    # Initialize the LLM with your model
    llm = get_llm(model_name="llama2")  # replace with your local Ollama model if different

    # Example context and question
    context = "Python is a popular programming language known for its readability and simplicity."
    question = "What is Python?"

    # Generate answer
    answer = llm.generate_answer(context, question)
    print("LLM Answer:")
    print(answer)
