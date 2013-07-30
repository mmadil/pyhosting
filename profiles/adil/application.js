jQuery(document).ready(function(){

  $('#about').click(function() {
    $('.about').show("fast");
    $('.contact').hide();
    $('.tech').hide();
  });
  $('#tech').click(function() {
    $('.tech').show("fast");
    $('.about').hide();
    $('.contact').hide();
  });
  $('#contact').click(function() {
    $('.contact').show("fast");
    $('.about').hide();
    $('.tech').hide();
  });

});
