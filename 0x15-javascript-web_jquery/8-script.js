const link = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(link, function (res) {
  for (const item of res.results) {
    $('ul#list_movies').append(`<li>${item.title}</li>`);
  }
});
