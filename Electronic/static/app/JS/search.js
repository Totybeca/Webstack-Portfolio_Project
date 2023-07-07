function performSearch() {
    var searchTerm = $('#search-input').val();
    
    // Perform AJAX request to retrieve search results
    $.ajax({
      url: '/search/',  // Replace with the actual URL for your search endpoint
      method: 'GET',
      data: { search_term: searchTerm },
      success: function(response) {
        // Handle the search results returned from the server
        // Update the DOM with the search results
        $('#search-results').html(response);
      },
      error: function(error) {
        // Handle any errors that occur during the AJAX request
        console.log(error);
      }
    });
  }
  