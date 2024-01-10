// Wait for the document to be ready before executing the script
$(document).ready(function() {
  
  // Add a new element to the list when DIV#add_item is clicked
  $('#add_item').click(function() {
    $('<li>Item</li>').appendTo('ul.my_list');
  });

  // Remove the last element from the list when DIV#remove_item is clicked
  $('#remove_item').click(function() {
    $('ul.my_list li:last-child').remove();
  });

  // Clear all elements from the list when DIV#clear_list is clicked
  $('#clear_list').click(function() {
    $('ul.my_list').empty();
  });

});

