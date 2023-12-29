# Simple Function Calling System

This project implements a lightweight function calling system based on sentence embeddings and cosine similarity. It allows users to define functions represented by sentences and map user input to the most similar function.
This system was designed to run on a CPU with very low overhead.

## Key Features

- **Local and CPU-Based**: Runs on CPU using a small SentenceTransformers model, making it accessible for local function calling.
- **Fast Response**: Each function call takes less than a second, approximately 0.05 seconds per call on a test machine, enabling quick response times.
- **Easy Extension**: Simple addition of sentences enables the definition of new functions without complex configurations.

## Usage

1. **Define Functions**: Add sentences to the `functions_to_embed` list to define your functions.
2. **Run**: Execute `main()` to start the REPL loop.
3. **Input Sentences**: Enter sentences via the REPL loop to find the most similar function, and observe the top matching function printed. Inquiries like "is it snowing" or "what's the weather." Will trigger the weather function.
4. **Exit**: Type `exit` to quit the program.

## Performance

On a test machine, the system achieves quick response times of approximately 0.05 seconds per function call using CPU resources. This provides efficient performance compared to running separate models for each call.

## Customization

- **Change Embedding Model**: Modify `SentenceTransformer()` to change the sentence embeddings model.
- **Adjust Threshold**: Adapt the similarity threshold in `util()` to refine function matching.
- **Add More Functions**: Add sentences to the `functions_to_embed` list to define your functions.

## Next Steps

### Potential Improvements

1. **Database Integration**: Incorporate a database for persistence of functions and metadata.
2. **Client/Server Architecture**: Develop a scalable architecture using a client/server model.
3. **Chatbot Implementation**: Extend the system to create a chatbot using the function calling system, including weather-related inquiries.

---
