// Wait for the document to be ready before executing the script
$(document).ready(function() {

  // Set up click event handler for INPUT#btn_translate
  $('#btn_translate').click(function() {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Make an AJAX request to the API to fetch the translation
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      success: function(response) {
        // Display the translation in DIV#hello
        $('#hello').text(response.hello);
      },
      error: function() {
        // Handle errors, if any
        $('#hello').text('Translation not available for the provided language code.');
      }
    });
  });

});

