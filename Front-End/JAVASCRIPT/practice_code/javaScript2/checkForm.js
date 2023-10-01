// checkForm.js : 폼 유효성 확인

window.onload = function(){
    // 폼의 유효성 확인
    // 폼의 [회원가입] 버튼 눌렀을 때 : submit 이벤트가 발생 / 처리
    document.getElementById('joinForm').onsubmit = function(){
        // 성명 입력하지 않은 경우 알림창 출력
        let name = document.getElementById('name');
        let id = document.getElementById('id');
        let password = document.getElementById('password');
        let passwordCheck = document.getElementById('passwordCheck');
        let job = document.getElementById('job');

        if(name.value == ""){
            // 성명을 입력하지 않으면
            alert("성명을 입력하세요.");
            name.focus();
            // 성명 입력란에 포커스
            return false;
        }

        if(id.value == ""){
            alert("아이디를 입력하세요.");
            id.focus();
            return false;
        }

        if(id.value.length<6||id.value.length>10){
            alert("아이디를 6~10자로 입력하세요.");
            id.value = "";
            id.focus();
            return false;
        }
        
        if(password.value == ""){
            alert("비밀번호를 입력하세요.");
            password.focus();
            return false;
        }
        
        if(password.value != passwordCheck.value){
            alert("비밀번호 확인이 일치하지 않습니다.");
            passwordCheck.value = "";
            passwordCheck.focus();
            return false;
        }
        // 옵션메뉴
        // if(job.vale == "") 이렇게 사용해도 됨.
        // 직업선택 value에 아무것도 안넣어줘서 사용 가능.
        if(job.selectedIndex == 0){
            alert("직업을 선택해주세요.");
            job.focus();
            return false;
        }
        // 라디오 체크
        let chk = false;
        for(let i=0 ; i<joinForm.emailRcv.length ; i++){
            if(joinForm.emailRcv[i].checked == true){
                chk = true; // 하나라도 체크되면 true로 설정
            }
        }
        if(chk == false){
            alert("이메일 수신여부를 선택하세요.");
            return false;
        }

        // 체크박스
        let agreement1 = document.getElementById('agreement1');
        let agreement2 = document.getElementById('agreement2');
        if(agreement1.checked == false || agreement2.checked == false){
            alert("모두 동의해주세요.");
            return false;
        }
    }; //onsubmit

};//window.onload