function getLatitudeLongitude() {

<<<<<<< HEAD
    var address = document.getElementById('id_City').value;
    
    //getLatitudeLongitude(address)
    address = address || 'TamilNadu';
   
    // Initialize the Geocoder
    var geocoder = new google.maps.Geocoder();
    if (geocoder) {
        
        geocoder.geocode({
            'address': address
            }, function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                document.getElementById('id_latitude').value = results[0].geometry.location.lat();
                document.getElementById('id_longitude').value = results[0].geometry.location.lng();
                loadMap();
            }
        });
    }
    
}
   

function loadMap(){
     
    
    var map = new GMap2(document.getElementById("map"));
    map.addControl(new GLargeMapControl());
    map.addControl(new GMapTypeControl());
      
                    
    var lat = document.getElementById('id_latitude').value;
    var lng = document.getElementById('id_longitude').value;
    map.setCenter(new GLatLng(lat,lng), 12);
   
    GEvent.addListener(map, "click", function(overlay, point){
        
        map.clearOverlays();
        if (point) {
            map.addOverlay(new GMarker(point));
            map.panTo(point);
            document.getElementById("id_latitude").value = point.lat();
            document.getElementById("id_longitude").value = point.lng();
                        
        }
        var lat = parseFloat(document.getElementById("id_latitude").value);
        var lng = parseFloat(document.getElementById("id_longitude").value);
        var latlng = new google.maps.LatLng(lat, lng);
        var geocoder = new google.maps.Geocoder();
        
        geocoder.geocode({ 'latLng': latlng }, function (results, status) {
    
            if (status == google.maps.GeocoderStatus.OK) {
                if (results[1]) {
                    msg = results[1].formatted_address
                    document.getElementById("id_Address").value = msg
                }
            }
        });
    });


   
   

}
// arrange for our onload handler to 'listen' for onload events
if (window.attachEvent) {
window.attachEvent("onload", function() {
getLatitudeLongitude();
});
} else {
window.addEventListener("load", function() {
getLatitudeLongitude();
}, false);
}
=======
                var address = document.getElementById('id_City').value;
                
                //getLatitudeLongitude(address)
                address = address || 'TamilNadu';
               
                // Initialize the Geocoder
                var geocoder = new google.maps.Geocoder();
                if (geocoder) {
                    
                    geocoder.geocode({
                        'address': address
                        }, function (results, status) {
                        if (status == google.maps.GeocoderStatus.OK) {
                            document.getElementById('id_latitude').value = results[0].geometry.location.lat();
                            document.getElementById('id_longitude').value = results[0].geometry.location.lng();
                            loadMap();
                        }
                    });
                }
                
            }
               
            
            function loadMap(){
                 
                
                var map = new GMap2(document.getElementById("map"));
                map.addControl(new GLargeMapControl());
                map.addControl(new GMapTypeControl());
                  
                                
                var lat = document.getElementById('id_latitude').value;
                var lng = document.getElementById('id_longitude').value;
                map.setCenter(new GLatLng(lat,lng), 12);
               
                GEvent.addListener(map, "click", function(overlay, point){
                    
                    map.clearOverlays();
                    if (point) {
                        map.addOverlay(new GMarker(point));
                        map.panTo(point);
                        document.getElementById("id_latitude").value = point.lat();
                        document.getElementById("id_longitude").value = point.lng();
                                    
                    }
                    var lat = parseFloat(document.getElementById("id_latitude").value);
                    var lng = parseFloat(document.getElementById("id_longitude").value);
                    var latlng = new google.maps.LatLng(lat, lng);
                    var geocoder = new google.maps.Geocoder();
                    
                    geocoder.geocode({ 'latLng': latlng }, function (results, status) {
                
                        if (status == google.maps.GeocoderStatus.OK) {
                            if (results[1]) {
                                msg = results[1].formatted_address
                                document.getElementById("id_Address").value = msg
                            }
                        }
                    });
                });
            
            
               
               
          
        }
        // arrange for our onload handler to 'listen' for onload events
        if (window.attachEvent) {
            window.attachEvent("onload", function() {
            getLatitudeLongitude();
            });
        } else {
            window.addEventListener("load", function() {
            getLatitudeLongitude();
            }, false);
        }
>>>>>>> 9588477bedf939aefc5bbd253e29268449028432
