const form = document.querySelector('#source');
const p = document.querySelector('#target');
form.addEventListener('submit', evt => {
  evt.preventDefault();

  const firstName = document.getElementsByName('firstname')[0].value;
  const lastName = document.getElementsByName('lastname')[0].value;

  p.innerHTML = 'your name is ' + firstName + ' ' + lastName;
});