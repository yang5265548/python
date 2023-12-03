const form = document.querySelector('form');
form.addEventListener('submit', async function(evt) {
  evt.preventDefault();
  const value_from_input = document.querySelector('#query').value;
  console.log(value_from_input);
  const response = await fetch(
      `https://api.tvmaze.com/search/shows?q=${value_from_input}`);
  const jsonData = await response.json();
  console.log(jsonData)
  for (let i = 0; i < jsonData.length; i++) {
    const name = jsonData[i].show.name;
    const summary = jsonData[i].show.summary;
    const url = jsonData[i].show.url;
    const article = document.createElement('article');
    const h2 = document.createElement('h2');
    h2.innerText = name;
    const a = document.createElement('a');
    a.href = url;
    a.target = '_blank';
    a.innerText='link';
    const image = document.createElement('img');

    // image.src = jsonData[i].show.image?.medium || 'https://via.placeholder.com/210x295?text=Not%20Found';
    image.src = jsonData[i].show.image?jsonData[i].show.image.medium : '';
    image.alt = name;
    const div = document.createElement('div');
    div.innerHTML = summary;
    const result = document.createElement('div');
    result.innerHTML = '';
    result.id = 'result';
    article.appendChild(h2);
    article.appendChild(a);
    article.appendChild(image);
    article.appendChild(div);
    result.appendChild(article);
    document.querySelector('body').appendChild(result);
  }

});
