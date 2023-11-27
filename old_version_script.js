// 가입된 사용자 정보 (예제를 위해 간단히 하드코딩)
const registeredUsers = [
    { username: 'user1', password: 'pass1' },
    { username: 'user2', password: 'pass2' },
    // ... 추가 사용자 정보
];

function login() {
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const username = usernameInput.value;
    const password = passwordInput.value;

    // 사용자 인증 확인
    const authenticatedUser = registeredUsers.find(user => user.username === username && user.password === password);

    if (authenticatedUser) {
        alert('로그인 성공!');
        // 로그인에 성공하면 여기에서 추가 작업 수행
        login_success();
    } else {
        alert('잘못된 사용자명 또는 비밀번호');
    }

    // 폼 초기화
    usernameInput.value = '';
    passwordInput.value = '';
}

function login_success() {
    window.location.href = 'login_success.html';
  }
