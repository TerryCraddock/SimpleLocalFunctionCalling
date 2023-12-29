# Import necessary libraries
import time  # Library to work with time
from sentence_transformers import SentenceTransformer  # Library for sentence embeddings
from sklearn.metrics.pairwise import cosine_similarity  # Library for cosine similarity calculation

# Load the pre-trained Sentence Transformer model
model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2', device="cpu")

# List of functions or sentences to embed for comparison
functions_to_embed = [
    "weather rain rainy raining rains rainstorm snow snowing snowy sun sunny sunshine fog foggy fogged cloud cloudy storm stormy windy hail hailing hailstorm sleet sleeting mist misty temperature cold hot humidity humid",
    "Set reminder alert alarm timer",
    "Delete reminder alert alarm timer"
]

# Function to get embeddings of input sentences
def get_sentence_embeddings(sentences):
    embeddings = model.encode(sentences)
    return embeddings

# Function to calculate similarity scores between source embedding and a list of embeddings
def get_similarity_scores(source_embedding, embeddings):
    similarity_scores = cosine_similarity([source_embedding], embeddings).flatten()
    return similarity_scores

# Utility function to perform specific actions based on similarity scores
def util(max_score, max_score_index):
    if max_score < 0.20:
        print("No specific function needed. Let's chat!")
    else:
        if max_score_index == 0:
            print("Checking weather")
        elif max_score_index == 1:
            print("Setting a timer")
        elif max_score_index == 2:
            print("Deleting a timer")

# Main function
def main():
    # Get embeddings for the predefined functions/sentences
    embeddings = get_sentence_embeddings(functions_to_embed)

    # Start an interactive loop to receive user input
    while True:
        source_sentence = input("Enter a source sentence (or 'exit' to quit): ")
        if source_sentence.lower() == 'exit':
            break
        
        start_time = time.time()  # Get the current time before the function call

        # Get embedding for the user's input sentence
        source_embedding = model.encode(source_sentence)

        # Calculate similarity scores between the user's input and predefined functions
        scores = get_similarity_scores(source_embedding, embeddings)
        max_score = max(scores)
        max_score_index = scores.tolist().index(max_score)

        print(f'Max score: {max_score}')
        print(f'Max score index: {max_score_index}')

        # Perform specific action based on the calculated similarity scores
        util(max_score, max_score_index)

        end_time = time.time()  # Get the current time after the function call
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Elapsed time: {elapsed_time} seconds")

# Ensure the main function is called when the script is run
if __name__ == "__main__":
    main()  # Call the main function when the script is run
