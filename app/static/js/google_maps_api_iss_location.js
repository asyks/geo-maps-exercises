(function($) { // creating local namespace and use 'no conflict' mode
  $(document).ready(function() {

    var map;

    function initialize(latitude, longitude) {
      var issLatLng = new google.maps.LatLng(latitude, longitude);
      var mapOptions = {zoom: 4, center: issLatLng};
      map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
      var marker = new google.maps.Marker({
        position: issLatLng,
        map: map,
        title: 'These are the coordinates the ISS is currently orbiting above'
      });
    }

    $.ajax({
      url: "/ajax/iss/",
      type: "GET",
      success: function(iss_data) {
        google.maps.event.addDomListener(
          window,
          'load',
          initialize(iss_data['latitude'], iss_data['longitude'])
        );
      }
    });

  });
}(jQuery));
