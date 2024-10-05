from langsmith import Client

client = Client()

# Define dataset: these are your test cases
dataset_name = "FindInFiles Example Dataset"
dataset = client.create_dataset(dataset_name)

try:

    client.create_examples(
        inputs=[
            {"input": "What is National Rail's Days Out Guide?","chat_history":[]},
            {"input": "What types of offers are included in the Days Out Guide?","chat_history":[]},
            {"input": "How does using the Days Out Guide benefit the environment?","chat_history":[]},    

        ],
        outputs=[
            {"answer": "National Rail's Days Out Guide is a program that offers 2FOR1 and other special discounts on attractions when you travel by train."},
            {"answer": "Using the Days Out Guide and traveling by train helps reduce your carbon footprint compared to other modes of transportation."},
            {"answer": "The Days Out Guide includes offers for theme parks, museums, theatre tickets, football stadium tours, hotels, restaurants, and more."}

        ],
        dataset_id=dataset.id,
    )
except:
    pass