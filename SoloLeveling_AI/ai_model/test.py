import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.models import Sequential

# Define the model architecture
model = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_length),
    LSTM(units=128),
    Dense(units=vocab_size, activation='softmax')
])

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(X_train, y_train, batch_size=128, epochs=10)

# Generate text from the trained model
seed_text = "The quick brown fox"
for i in range(10):
    x = tokenizer.texts_to_sequences([seed_text])[0]
    x = tf.keras.preprocessing.sequence.pad_sequences([x], maxlen=max_length-1, padding='pre')
    predicted = model.predict_classes(x)
    output_word = ""
    for word,index in tokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    seed_text += " " + output_word
print(seed_text)
