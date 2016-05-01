$(window).load(function() {

  function hideDescription() {
    $('#description').css({
      'display': 'none'
    });
  };

	function showSearchMessage() {
		$('#searchMessage').css({
			'display': 'inline'
		});
	};

	function hideSearchMessage() {
		$('#searchMessage').css({
			'display': 'none'
		});
	};

	function showTweetColumns() {
		$('#positiveTweets').css({
			'display': 'inline'
		});
		$('#negativeTweets').css({
			'display': 'inline'
		});
	}

	function clearTweetResults() {
    $('#positiveResults').empty();
    $('#negativeResults').empty();
	}

	$('#sumbit').click(function() {
		var term = $('#searchTerm').val();
		var url = '/tweets?search=' + encodeURIComponent(term);
    hideDescription();
		showSearchMessage();

		$.get(url, function(data, status) {
			hideSearchMessage();
      clearTweetResults();
			showTweetColumns();

			data = JSON.parse(data);

			if (data) {

				for (var i = 0; i < data.length; i++) {
					var result = data[i];

					var column = 'negativeResults';
					if (result['positive']) {
						column = 'positiveResults';
					}

					twttr.widgets.createTweet(
							result['id'],
							document.getElementById(column), {
								theme: 'light'
							})
						.then(function(el) {
							console.log("Tweet has been displayed.")
						});

				}
			};
		})
	});
});
