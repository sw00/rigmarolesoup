(function ($,W,D) {
	String.prototype.linkify=function(){
		return this.replace(/[A-Za-z]+:\/\/[A-Za-z0-9-_]+\.[A-Za-z0-9-_:%&amp;;\?\/.=]+/g,function(m){
			return m.link(m);
		});
	};
	String.prototype.linkuser=function(){
		return this.replace(/[@]+[A-Za-z0-9-_]+/g,function(u){
			return u.link("http://twitter.com/"+u.replace("@",""));
		});
	};
	String.prototype.linktag=function(){
		return this.replace(/[]+[A-Za-z0-9-_]+/,function(t){
			return t;
		});
	};

	$.getJSON(
		'http://search.twitter.com/search.json?q=from:settface&callback=?', 
		{},
		function(data){
			var tweets = data.results;	

			for (var i=0; i<tweets.length; i++){
				var tweet = tweets[i];
				tweet.timestamp = new Date(tweet.created_at);
				tweet.url = '//twitter.com/' + tweet.from_user + '/status/' + tweet.id_str;

				var $item = $('<li>').html(
					'<span class="entypo"><a href="'+ tweet.url + '">&#62217;</a></span>' + tweets[i].text.linkify().linkuser().linktag().replace(/<a/g,'<a target="_blank"'));
				$('#activity').append($item);
			}
		}); 
})(jQuery, window, document);
