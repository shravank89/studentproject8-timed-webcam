import streamlit as st
import cv2
from datetime import datetime


st.title("Timed Webcam")

if st.button("Open Video"):
    streamlit_image = st.image([])
    video = cv2.VideoCapture(0)

    while 1:
        now = datetime.now()
        current_date = now.strftime("%A,%d-%m-%Y")
        current_time = now.strftime("%H:%M:%S")
        check, frame = video.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.putText(img=frame, text=current_date, org=(25, 400), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=current_time, org=(25, 440), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2, color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)
        streamlit_image.image(frame)



