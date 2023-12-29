import time
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2', device="cpu")
functions_to_embed = [
    "weather rain rainy raining rains rainstorm snow snowing snowy sun sunny sunshine fog foggy fogged cloud cloudy storm stormy windy hail hailing hailstorm sleet sleeting mist misty temperature cold hot humidity humid",
    "Set reminder alert alarm timer",
    "Delete reminder alert alarm timer"
]

def get_sentence_embeddings(sentences):
    embeddings = model.encode(sentences)
    return embeddings

def get_similarity_scores(source_embedding, embeddings):
    similarity_scores = cosine_similarity([source_embedding], embeddings).flatten()
    return similarity_scores

def util(max_score, max_score_index):
    if max_score < 0.20:
        print("No function needed we can chat.")
    else:
        if max_score_index == 0:
            print("Checking weather")
        elif max_score_index == 1:
            print("Setting Timer")
        elif max_score_index == 2:
            print("Deleting Timer")

def main():
    embeddings = get_sentence_embeddings(functions_to_embed)

    while True:
        source_sentence = input("Enter a source sentence (or 'exit' to quit): ")
        if source_sentence.lower() == 'exit':
            break
        
        start_time = time.time()  # Get the current time before the function call
        source_embedding = model.encode(source_sentence)

        scores = get_similarity_scores(source_embedding, embeddings)
        max_score = max(scores)
        max_score_index = scores.tolist().index(max_score)

        print(f'Max score: {max_score}')
        print(f'Max score index: {max_score_index}')

        util(max_score, max_score_index)
        end_time = time.time()  # Get the current time after the function call
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Elapsed time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()  # Call the main function when the script is run
