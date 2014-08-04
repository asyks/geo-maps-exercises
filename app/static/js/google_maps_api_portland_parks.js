(function($) { // creating local namespace and use 'no conflict' mode
  $(document).ready(function() {

    const ua_latitude = 45.525368;
    const ua_longitude = -122.685879;
    var map;

    function initialize(portland_basketball_parks) {
      var uaLatLng = new google.maps.LatLng(ua_latitude, ua_longitude);
      var mapOptions = {zoom: 13, center: uaLatLng};
      map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
      $(portland_basketball_parks).each(function() {
        thing = $(this)
        park_lat_lng = new google.maps.LatLng($(this).attr('loc')['lat'], $(this).attr('loc')['lon']);
        park_name = $(this).attr('Property');
        var marker = new google.maps.Marker({position: park_lat_lng, map: map, title: park_name});
      });
    }

    $.ajax({
      url: "/ajax/hoops/",
      type: "GET",
      success: function(portland_basketball_parks) {
        google.maps.event.addDomListener(window, 'load', initialize(portland_basketball_parks));
      }
    });

  });
}(jQuery));
