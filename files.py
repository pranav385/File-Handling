import streamlit as st
import pandas as pd


st.subheader("Uploading the CSV File")

# For loading CSV file we have 2 ways

# 1st ways
# Uploading the CSV file as it is 
df=st.file_uploader("Upload the CSV file : ") # By this we can upload any file

df=st.file_uploader("Upload the CSV file : ",type=['csv','xlsx']) # By this we can only upload csv and xlsx file

# Now the file is uploaded, now we see how we can extract data from uploaded file

if df is not None:    # By this code if we upload the file then the data is show in our webpage in raw format
    st.dataframe(df) 

# To display the data in csv format we import pandas 

st.subheader("Loading the CSV File")


df1=pd.read_csv("Products.csv")
# st.write(df) # this will also work to display the data in the format as it is in the file  

# st.table(df1) # This will also work to display the data in table format

# There are chances that some time file not exist then ideally what we do is when we are reading the data frame
# we will write if df is not None: then we will display it as a table by st.table(df1)
if df1 is not None:
    st.table(df1.head())


st.subheader("For showing image directly")

# there are two ways to display images. 
# 1st is we can upload the image and show it
# 2nd We can directly show an image of our choice

# First see how we can directly show image of our choice

st.image("img.png")

# for uploading the image
st.subheader("Uploading the image")

img=st.file_uploader('Please Upload the image',type=['png','jpeg'])

if(img is not None):     # Here if the image is uploaded then we will show it by this
    st.image(img)


st.subheader("Working with Videos")

videoFile=st.file_uploader("Upload your video and share it with the world",type=['mkv','mp4'])

if videoFile is not None:
    st.video(videoFile)
    st.video(videoFile,start_time=4) # if we do this then our video by default start from 4 sec


st.subheader("Directly uploading the video file")

st.video('vid.mp4')

st.video('vid.mp4',start_time=4)


st.subheader("Uploading the audio ")

audioFile=st.file_uploader("Upload your audio file",type=['mp3','wav'])

if audioFile is not None:
    st.audio(audioFile)
    st.audio(audioFile.read()) # from both the audio file will run
    st.audio(audioFile,start_time=50)


