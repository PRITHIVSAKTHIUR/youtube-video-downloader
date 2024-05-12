from youtube_video import download_youtube_video
import gradio as gr

def app(video_link):
    video_path = download_youtube_video(video_link)
    return video_path

interface = gr.Interface(
    fn=app,
    inputs=gr.Textbox(label="Enter YouTube link 🔗 To Download Video⬇️ "),
    outputs=gr.Video(label = "video_path")
)

interface.launch(debug=True)