import os
import cv2
import uuid
import streamlit as st

from ultralytics import YOLOv10


def save_upload_file(upload_file, save_folder):
    os.makedirs(save_folder, exist_ok=True)
    if upload_file:
        new_filename = str(uuid.uuid4()) + ".jpg"
        save_path = os.path.join(save_folder, new_filename)
        with open(save_path, 'wb+') as f:
            data = upload_file.read()
            f.write(data)

        return save_path
    else:
        st.markdown('### :warning: :red[Image not found!]')


@st.cache_data(max_entries=1000)
def process_image_and_show_result(image_path, model_path):
    # Process image
    img_size = 640
    conf_threshold = 0.3
    model = YOLOv10(model_path)
    result = model.predict(source=image_path,
                           imgsz=img_size,
                           conf=conf_threshold)
    result = result[0].plot()
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    # Show image result
    st.markdown('**Detection result**')
    col1, col2 = st.columns([0.5, 0.5], gap='large')

    with col1:
        st.image(image_path, caption='Your image')
    with col2:
        st.image(result, caption='Result by Yolov10')


def setup_layout():
    st.set_page_config(
        page_title="AIO-Project Module 1",
        layout="wide"
    )
    col1, col2 = st.columns([0.45, 0.55], gap='large')
    with col1:
        st.title(':memo: AIO-Project - Module 1')
    with col2:
        st.title(
            ':helmet_with_white_cross: :green[YOLOv10] - Helmet Detection Demo')

    uploaded_img = st.file_uploader(
        '__Input your image__', type=['jpg', 'jpeg', 'png'])
    st.divider()

    if uploaded_img:
        model_path = "models/best.pt"
        save_folder = "images"
        uploaded_img_path = save_upload_file(uploaded_img, save_folder)

        try:
            process_image_and_show_result(uploaded_img_path, model_path)

        finally:
            os.remove(uploaded_img_path)
            os.rmdir(save_folder)
    else:
        st.markdown('### :warning: :red[Please insert an image!]')


def main():
    setup_layout()


if __name__ == '__main__':
    main()
