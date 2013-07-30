jQuery(document).ready(function(){

  $('#about').click(function() {
    $('.about').show("fast");
    $('.nav a').last().removeClass("active");
    $('.nav a').first().next().removeClass("active");
    $('.nav a').first().addClass("active");
    $('.contact').hide();
    $('.tech').hide();
  });
  $('#tech').click(function() {
    $('.tech').show("fast");
    $('.nav a').first().removeClass("active");
    $('.nav a').last().removeClass("active");
    $('.nav a').first().next().addClass("active");
    $('.about').hide();
    $('.contact').hide();
  });
  $('#contact').click(function() {
    $('.contact').show("fast");
    $('.nav a').first().removeClass("active");
    $('.nav a').first().next().removeClass("active");
    $('.nav a').last().addClass("active");
    $('.about').hide();
    $('.tech').hide();
  });

});
