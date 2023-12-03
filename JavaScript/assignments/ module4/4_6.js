'use strict';

document.querySelector('form').addEventListener(
    'submit',
    async function(evt) {
        evt.preventDefault();
        let query = document.querySelector('#query').value;
        let url = `https://api.chucknorris.io/jokes/search?query=${query}`;
        let response = await fetch(url);
        let jsonData = await response.json();
        console.log(jsonData);
        let result = document.querySelector('#result');
        for (let item of jsonData.result) {
            let article = document.createElement('article');
            let p = document.createElement('p');
            p.innerHTML = item.value;
            article.appendChild(p);
            result.appendChild(article);
        }
    }
);
