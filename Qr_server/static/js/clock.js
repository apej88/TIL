const clock = document.querySelector('.clock__txt');

const getTime = () => {
    const now = new Date();
    const month = now.getMonth() + 1;
    const date = now.getDate();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();
    const time = `${hours < 10 ? `0${hours}`:hours}:
                ${minutes < 10 ? `0${minutes}`:minutes}:
                ${seconds < 10 ? `0${seconds}`:seconds}`;
    
    clock.innerHTML = time;
}

getTime()
setInterval(getTime,1000)