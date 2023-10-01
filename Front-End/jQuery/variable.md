## jQuery 변수
- 변수명 앞에 $ 붙임
- let $box1 = $(‘#box1’); // 아이디 선택자로 찾아옴
    - let 객체;
    - 객체이므로 jQuery 메소드 사용 가능
    - $box1.css(‘color’, ‘red’);
- let $divLen =$(‘div’).length; // div 태그 개수 저장
    - 객체가 아닌 값을 저장할 경우에는 $ 붙이지 않아도 됨
    - let divLen = $(‘div’).length;