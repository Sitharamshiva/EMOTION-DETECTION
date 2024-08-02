import streamlit as st
import pickle

# Load the trained model
with open(r"C:\Users\shiva\LINEAR ALGEBRA\model.pkl", 'rb') as model_file:
    model = pickle.load(model_file)

# Define the label to image path mapping
label_to_image = {
"sad": r"C:\Users\shiva\Downloads\—Pngtree—sad emoji_7258455.png",
"joy":r"C:\Users\shiva\Streamlit_elite_20\streamlit\joy.png",
"love":r"C:\Users\shiva\Streamlit_elite_20\streamlit\love.png",
"anger":r"C:\Users\shiva\Downloads\—Pngtree—angry emoji vector icon_3720389.png",
"fear":r"C:\Users\shiva\Streamlit_elite_20\streamlit\fear.png",
"surprise":r"C:\Users\shiva\Streamlit_elite_20\streamlit\surprse.png"
}

# Set the title of the Streamlit app
st.title("Emotion Detection")

# Text input
input_text = st.text_area("Enter some text:")

# Button to trigger prediction
if st.button("DETECT"):
    if input_text:
        # Predict the emotion
        predicted_label = model.predict([input_text])[0]
        image_path = label_to_image.get(predicted_label, None)  # Get the image path

        # Display the predicted emotion and corresponding image
        if image_path:
            st.write(f"Predicted Emotion: {predicted_label}")
            st.image(image_path, use_column_width=True)
        else:
            st.write(f"Predicted Emotion: {predicted_label}")
    else:
        st.write("Please enter some text.")