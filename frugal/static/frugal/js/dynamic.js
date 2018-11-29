 $(document).ready(function() {
        
      var max_fields = 3; //maximum input boxes allowed
      var wrapper = $("form table:first"); //Fields wrapper
      var add_button = $(".add_field_button"); //Add button ID
      var remove_button = $(".remove_field_button");
 
      var x = 1; //initlal text box count
      $(add_button).click(function(e){ //on add input button click
        
      e.preventDefault();
      if(x < max_fields)
      { //max input box allowed
        x++; //text box increment
        
        $(wrapper).append('<tr id="row'+x+'"><td><input id="Recognized_Body'+x+'" class="form-control" name="Recognized_Body'+x+'" required="required" type="text" /></td>'+
        ' <td><input id="Registration_Number'+x+'" class="form-control" name="Registration_Number'+x+'" required="required" type="text" /></td></tr>'); //add input box
          
      }
      });

      $(remove_button).click(function(e){ //on add input button click
        
        e.preventDefault();
        if(x > 1)
        { //max input box allowed
          var row = $("tr#row"+x)
          x--; //text box increment
          row.remove()
          
        }
        });

        });
    