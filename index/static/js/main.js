ActivityApp = (function ($) {
	$.getJSON(
		'http://search.twitter.com/search.json?q=from:settface&callback=?', 
		{},
		function(data){
			window.tweets = data.results;
			var tweets = data.results;	
			var max = tweets.length < 3 ? tweets.length : 3;

			for (var i=0; i<max; i++){
				var tweet = tweets[i];
				tweet.timestamp = new Date(tweet.created_at);
				tweet.url = '//twitter.com/' + tweet.from_user + '/status/' + tweet.id_str;

				var $item = $('<li>').html(
					'<span class="entypo"><a href="'+ tweet.url + '">&#62217;</a></span>' + tweets[i].text);
				$('#activity').append($item);
			}
		});
})(jQuery);
