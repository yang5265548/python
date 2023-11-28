for (let i = 0; i < 3; i++) {
  let li = document.createElement('li');

  switch (i) {
    case 0:
      li.innerText = 'First item';
      break;
    case 1:
      li.innerText = 'Second item';
      li.classList.add('my-item');
      break;
    case 2:
      li.innerText = 'Third item';
      break;
  }
  document.querySelector('#target').appendChild(li);
}

// document.querySelector('#target').addClass('my-list');