# import google.generativeai as genai

# # client = genai.Client(api_key="AIzaSyD8FrLR6bmeG6NFEztRtvdfoPH-FGIkaHc")

# genai.configure(api_key = "AIzaSyD8FrLR6bmeG6NFEztRtvdfoPH-FGIkaHc")
# model = genai.GenerativeModel("gemini-pro")

# response = model.generate_content("Explain how AI works")

# # response = client.models.generate_content(
# #     model="gemini-2.0-flash",
# #     contents="Explain how AI works",
# # )

# print(response.text)






# models = genai.list_models()
# 
# for model in models:
    # print(f"{model.name} - {model.supported_generation_methods}")


import google.generativeai as genai

api = "AIzaSyD8FrLR6bmeG6NFEztRtvdfoPH-FGIkaHc"

genai.configure(api_key= api)

# Use correct model name
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Explain how AI works?")
print(response.text)


