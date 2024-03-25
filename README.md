# Video2Cartoon
openCV를 이용해서 동영상을 만화 느낌 나는 영상으로 바꾸는 프로그램

## 이 프로그램을 이용해서 cartoon의 느낌이 잘 표현된 동영상과 사진

* 로켓이 발사되는 영상의 첫 장면
  
![rocket_screenshot](https://github.com/jyj7652/Video2Cartoon/assets/70854950/210a98a4-984c-4f21-8736-0aeb19f4333a)

* 고양이 동영상

  https://github.com/jyj7652/Video2Cartoon/assets/70854950/e0130e91-03a6-40ff-851f-e9151d054eb4


## 이 프로그램을 이용해서 cartoon의 느낌이 잘 표현되지 못한 동영상과 사진

* 로켓이 발사된 이후 하늘에서의 모습

  ![rocket_error](https://github.com/jyj7652/Video2Cartoon/assets/70854950/b98486f2-9d2e-430f-ba8e-6029971bac4a)


* 내 오버워치 플레이 영상

  https://github.com/jyj7652/Video2Cartoon/assets/70854950/a38dfb06-ef72-4b60-ac38-1b77f8960348

* * *

## 내가 만든 프로그램(알고리즘)의 한계점

* **일괄적인 효과 적용**   
  모든 프레임에 같은 엣지 기술을 적용하다 보니 로켓 발사의 첫 장면처럼 엣지가 잘 감지 될 수 있는 장면은
  cartoon 스타일의 영상이 제작 되지만 발사된 후에 구름속을 로켓이 지날 때는 엣지를 잘 감지하지 못하여
  거의 원본 영상과 비슷하게 되는 경우가 있었다.
* **성능 및 효율성**   
  이 코드에서 사용된 알고리즘은 비교적 단순하지만, 대규모의 동영상 또는 실시간 스트리밍에 대해서는 성능이나 효율성 면에서 충분하지 않을 수 있다.   
