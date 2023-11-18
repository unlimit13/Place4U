position=0;
function success({coords, timestamp}){
    const latitude = coords.latitude;   // 위도
    const longitude = coords.longitude; // 경도
    
    alert(`위도: ${latitude}, 경도: ${longitude}`);
}
function getUserLocation() {
    if (!navigator.geolocation) {
        throw "위치 정보가 지원되지 않습니다.";
    }
    navigator.geolocation.getCurrentPosition(success)
    
}
getUserLocation();