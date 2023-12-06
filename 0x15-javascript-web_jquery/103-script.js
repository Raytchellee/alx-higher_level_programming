$(document).ready(function () {
  $('input#btn_translate').click(printHello);
  $('input#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        printHello();
      }
    });
  });
});

function printHello () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  const lang = $('input#language_code').val();
  const link = url + lang;
  $.get(link, function (res) {
    $('div#hello').text(res.hello);
  });
}
