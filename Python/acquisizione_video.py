import imageio.v2 as imageio
import numpy as np

def analizza_video(file_video, max_frame=10):
    video = imageio.get_reader(file_video)
    risultati = []

    for i, frame in enumerate(video):
        if i >= max_frame:
            break

        # Dimensioni frame
        h, w, _ = frame.shape

        # Centro del frame (approccio semplice)
        cx = w // 2
        cy = h // 2

        risultati.append({
            "frame": i,
            "cx": cx,
            "cy": cy,
            "width": w,
            "height": h
        })

    video.close()
    return risultati
