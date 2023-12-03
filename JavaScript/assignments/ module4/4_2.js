const form = document.querySelector('form');
form.addEventListener('submit', async function(evt) {
      evt.preventDefault();
      const value_from_input = document.querySelector('#query').value;
      const response = await fetch(
          `https://api.tvmaze.com/search/shows?q=${value_from_input}`);
      const jsonData = await response.json();
      console.log(jsonData);
    },
);