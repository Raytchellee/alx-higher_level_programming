$('document').ready(function () {
  const link = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('input#btn_translate').click(function () {
    $.get(link + $.param({ lang: $('input#language_code').val() }), function (res) {
      $('div#hello').html(res.hello);
    });
  });
});
