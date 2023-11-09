const API_KEY = 'd3ae3db05f803191603e794a5154bdf4'
let WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather?'

const callUserCoords = () => {
    let coords = {}
    if (!"geolocation" in navigator) return

    // Promise 
    // pending : 비동기작업이 끝나기를 대기중
    // fulfilled : 비동기작업이 성공적으로 끝남, resolve()
    // rejected :  비동기작업이 실패, reject()
    return new Promise((resolve, reject)=>{
        navigator.geolocation.getCurrentPosition( position => {
            coords.lat = position.coords.latitude
            coords.log = position.coords.longitude
            resolve(coords) // Promise의 상태를 fulfilled 변경, resolve의 매개변수로 넘어간 '
                            // 값을 then 블록의 매개변수로 전달
        
        }, (error)=>{
            console.error('현재위치를 받아오지 못했습니다.')
            reject(error) // Promise의 상태를 rejected로 바꾸고 reject함수의 매개변수로 전달된
                          // 값을 catch 블록의 콜백함수 매개변수로 전달
        });
    })
}

// async : 내부에서 await 키워드를 사용할 수 있다.
// async fnc는 반환하는 값이 있을 경우 Promise 객체로 반환한다.

const loadWeather = async () => {
    // callUserCoords가 fullfilled 또는 rejected 가 되기를 기다림
    // fullfilled 가 되면 coords에 resolve() 함수의 매개변수로 전달했던 값을 담아줌
   
    try {
        coords = await callUserCoords();
        res = await call_weather_api(coords);
        document.querySelector('.txt_weather').innerHTML = res.main.temp + 'ºC @ ' + res.name;
    } catch (error) {
        console.error(error)
    }
}

const call_weather_api = async (coords)  => {
    console.log(coords)

    let WEATHER_PARAM = 
    `lat=${coords.lat}&lon=${coords.log}&appid=${API_KEY}&units=metric&lang=kr`

    const response = await fetch(WEATHER_API + WEATHER_PARAM);
    return response.json()
}

loadWeather()