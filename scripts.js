document.getElementById('start-button').addEventListener('click', () => {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('video-feed').src = "/video_feed";
});

document.getElementById('video-feed').onload = () => {
    document.getElementById('loading').style.display = 'none';
};
