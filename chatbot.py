from transformers import pipeline

# Load the model (use an appropriate task and model for your needs)
# chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
chatbot = pipeline("text2text-generation", model="google/flan-t5-large")

def generate_response(prompt):
    try:
        # Generate a response with the model
        response = chatbot(prompt, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        return f"Error: {str(e)}"
