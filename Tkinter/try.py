# from transformers import pipeline

# generator = pipeline("text-generation", model="gpt2")
# prompt = "What is the Capital of india?"
# output = generator(prompt, max_length=50, num_return_sequences=1, truncation = True)

# print(output[0]['generated_text'])

# from transformers import pipeline

# generator = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta")  # More accurate for Q&A
# prompt = "Q: What is the capital of India?\nA:"
# output = generator(prompt, max_new_tokens=50, do_sample=False)

# print(output[0]['generated_text'])

