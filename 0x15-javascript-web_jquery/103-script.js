// Wait for the document to be ready before executing the script
$(document).ready(function() {

  // Set up click event handler for INPUT#btn_translate
  $('#btn_translate').click(fetchTranslation);

  // Set up keypress event handler for INPUT#language_code
  $('#language_code').keypress(function(event) {
    // Check if the pressed key is ENTER (key code 13)
    if (event.which === 13) {
      fetchTranslation();
    }
  });

  // Function to fetch and display translation
  function fetchTranslation() {
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
  }

});

