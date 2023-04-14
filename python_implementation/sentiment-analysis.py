import tkinter as tk
from tkinter import ttk
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Setting up your subscription key and endpoint for the Sentiment Analytics Cognitive service
subscription_key = "your-subscription-key"
endpoint = "your-endpoint"

# Authenticating the client
credentials = AzureKeyCredential(subscription_key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credentials)

#Defining the function to categorize the sentiment score
def categorize_text(score):
    if score == 1:
        print('Positive')
    elif score == 0:
        print('Negative')
    elif score > 0.4 and score < 0.6:
        print('Neutral')

# Defining the function to analyze the sentiment
def analyze_sentiment():
    # Get the text from the input field
    text = input_field.get("1.0", "end-1c")
    
    # Call the Sentiment Analytics Cognitive service to get the sentiment score
    response = client.analyze_sentiment(documents=[text])[0]
    score = response.sentiment_scores.positive
    
    # Update the output label with the sentiment score and record it
    score = output_label.config(text=f"Sentiment score: {score:.2f}")
    
    #Calling the text score categoring fucntion
    categorize_text(score)

# Create the main window and set the title
window = tk.Tk()
window.title("Sentiment Analysis")

# Create the input field and label
input_label = ttk.Label(window, text="Enter text:")
input_label.pack(side="top", padx=10, pady=5)
input_field = tk.Text(window, height=10, width=50)
input_field.pack(side="top", padx=10, pady=5)

# Create the analyze button and bind it to the analyze_sentiment function
analyze_button = ttk.Button(window, text="Analyze", command=analyze_sentiment)
analyze_button.pack(side="top", padx=10, pady=5)

# Create the output label
output_label = ttk.Label(window, text="")
output_label.pack(side="top", padx=10, pady=5)

# Start the main event loop
window.mainloop()
