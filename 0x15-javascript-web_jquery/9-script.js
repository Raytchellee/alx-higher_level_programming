$(document).ready(function () {
  const link = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(link, function (res) {
    $('div#hello').text(res.hello);
  });
});
