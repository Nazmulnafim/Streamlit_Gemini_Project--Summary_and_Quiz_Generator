import streamlit as st
from PIL import Image
from api_calling import note_generator, audio_transcription, quiz_generator


st.title("Note Summary :green_book: and Quiz Generator", width=400)
st.markdown("Upload upto 3 images to generate notes and quiz.")
st.divider()

with st.sidebar:
    st.header("Controls")
    pictures = st.file_uploader(
        "Upload your photos here",
        type= ['jpg', 'jpeg', 'png'],
        accept_multiple_files= True
    )
    if pictures:
        if (len(pictures) <= 3):
            col = st.columns(len(pictures))
            for i, img in enumerate(pictures):
                col[i].image(img)
        else:
            st.warning("You can upload 3 photos max.")

    # converting pictures to PIL pictures to work with gemini

    pil_pictures = []
    for pic in pictures:
        pil_pic = Image.open(pic)
        pil_pictures.append(pil_pic)
        print(type(pil_pic))
    


    # else:
    #     st.error("No picture is uploaded")

    difficulty = st.selectbox("Enter the difficulty of your quiz", options= ["Easy", "Medium", "Hard"], index=None,placeholder="Choose difficulty level")

    button_pressed = st.button("Click the Button to inititate AI", type="primary")


if button_pressed:
    if not pictures:
        st.error("No picture is uploaded")
    if not difficulty:
        st.error("Difficulty Level is not selected")
    if pictures and difficulty:
    
        # note
        with st.container(border= True):
            st.subheader("Your Note")
        
            with st.spinner("AI is generating summary for you", show_time=True):
                generated_note = note_generator(pil_pictures)
                st.markdown(generated_note)

        # audio
        with st.container(border= True):
            st.subheader("Audio Transcript")

            # clearing markdown 
            generated_note = generated_note.replace("#", "")
            generated_note = generated_note.replace("*", "")
            generated_note = generated_note.replace("-", "")
            
            with st.spinner("Audio transcription is being generated...", show_time=True):
                note_to_audio = audio_transcription(generated_note)
                st.audio(note_to_audio)
       
        # quiz
        with st.container(border= True):
            st.subheader("Your Quiz")

            with st.spinner("Quiz is being generated...", show_time=True):
                quizes = quiz_generator(pil_pictures, difficulty)
                st.markdown(quizes)



