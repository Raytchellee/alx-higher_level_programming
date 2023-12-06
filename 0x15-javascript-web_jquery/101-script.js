$(document).ready(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>item</li>');
  });
  $('div#remove_item').click(function () {
    $('ul.my_list li').last().remove();
  });
  $('div#clear_list').click(function () {
    $('ul.my_list li').remove();
  });
});
