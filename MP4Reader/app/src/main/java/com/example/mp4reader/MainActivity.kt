package com.example.mp4reader

import android.os.Bundle
import android.widget.VideoView
import android.media.MediaPlayer
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val videoView = VideoView(this)
        setContentView(videoView)

        // Load placeholder MP4 from raw folder
        val videoUri = "android.resource://" + packageName + "/" + R.raw.sample_video
        videoView.setVideoPath(videoUri)
        videoView.setOnPreparedListener { mp: MediaPlayer -> mp.isLooping = true }
        videoView.start()
    }
}
