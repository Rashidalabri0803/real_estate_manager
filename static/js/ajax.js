function loadPropertyDetails(pk){
  $.ajax({
    url: '/properties/${pk}/,
    method: 'GET',
    success: function(data){
      $('#property-details').html(data);
    }
  });
}