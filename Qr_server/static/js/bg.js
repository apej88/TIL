const call_unsplash_api = async () =>{
    const ACCESS_KEY = '-0YX-Fhv9lDBYnEDsecjpY1k8yhPnQuM6riSVKVaaho'
    let apiURL = 'https://api.unsplash.com/photos/random?'

    apiURL += 'orientation=landscape&query=landscape'
    let response  = await fetch(apiURL
                , {headers:{Authorization: `Client-ID ${ACCESS_KEY}`}})

    return response.json()
}

const createUnsplashToken = async () => {
    let bg = await call_unsplash_api()

    // 배경이미지 url, 배경이미지 장소정보, 만료일자
    let bgURL = bg.urls.full;
    let bgLocation = bg.location.name?bg.location.name:'Our final day...'
    let expirationDate = new Date();
    expirationDate.setDate(expirationDate.getDate()+1);

    let unsplashToken = {
        url:bgURL,
        location:bgLocation,
        expirationOn:expirationDate.getTime()
    }

    localStorage.setItem('unsplashToken', JSON.stringify(unsplashToken));
    return unsplashToken;
}

(async () => {

    // localStorage에서 토큰을 가져옴
    let unsplashToken = JSON.parse(localStorage.getItem('unsplashToken'))

    // 현재시간
    let now = new Date().getTime();

    // token이 없거나 토큰이 만료되었다면
    if(!unsplashToken || unsplashToken.expirationOn < now){
        unsplashToken = await createUnsplashToken();
    }

    document.querySelector('body').style.backgroundImage = 
        `url(${unsplashToken.url})`;
    
    bgLocation.innerHTML = unsplashToken.location;

})()