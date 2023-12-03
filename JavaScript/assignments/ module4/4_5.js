'use strict';

async function randomJoke() {
    let joke = await fetch('https://api.chucknorris.io/jokes/random');
    let jsonData = await joke.json();
    console.log(jsonData.value);
}
randomJoke();
