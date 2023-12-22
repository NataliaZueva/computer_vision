import cv2


def process_video(video, image):
    img_count = 0
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    now_frame = 0
    while frames != now_frame:
        flag, frame = video.read()
        now_frame = video.get(cv2.CAP_PROP_POS_FRAMES)

        if flag:
            frame = cv2.resize(frame, (image.shape[1], image.shape[0]))
            if is_similar_template(image, frame):
                img_count += 1
                if img_count % 10 == 0:
                    print(img_count)

    return img_count


def is_similar_template(img, frame):
    img_thresh = get_thresh(img)
    frame_thresh = get_thresh(frame)
    val = cv2.matchTemplate(frame_thresh, img_thresh, cv2.TM_CCOEFF_NORMED)
    return val > 0.9


def get_thresh(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY)
    return thresh


img = cv2.imread('img.jpg')
video = cv2.VideoCapture("output.avi")
count = process_video(video, img)
print(f"Count image: {count}")
