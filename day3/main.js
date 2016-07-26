function addListItem(text){
  list = document.querySelector('ul');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}

addListItem("new item");