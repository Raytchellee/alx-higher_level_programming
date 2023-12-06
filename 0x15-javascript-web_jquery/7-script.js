$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (value) {
  $('div#character').text(value.name);
});
