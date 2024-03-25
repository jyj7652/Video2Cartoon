import cv2

# 동영상 파일 경로
video_path = 'video2cartoon.mp4'

# 동영상을 읽어올 VideoCapture 객체 생성
cap = cv2.VideoCapture(video_path)

# VideoWriter 객체 생성을 위한 동영상 정보 획득
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# VideoWriter 객체 생성
out = cv2.VideoWriter('cartoon_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (frame_width, frame_height))

while cap.isOpened():
    # 프레임 읽어오기
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 엣지 검출
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    # 컬러 이미지를 만화처럼 보이도록 스타일 변환
    color = cv2.bilateralFilter(frame, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    # 결과 동영상 저장
    out.write(cartoon)

    # 화면에 출력
    cv2.imshow('Cartoon Video', cartoon)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 객체 해제
cap.release()
out.release()
cv2.destroyAllWindows()
