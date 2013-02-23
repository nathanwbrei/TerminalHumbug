
function scrape() {

	// Retrieve ALL messages from DOM
	// Thanks @thomasballinger
	var data_jq = $('.message_row, .recipient_row').map(function(i, x){
		return {
			name : jQuery.makeArray($(x).find('.sender_name').map(function(i, x){return x.innerText})),
			message : jQuery.makeArray($(x).find('.message_content').map(function(i, x){return x.innerText})),
			time : jQuery.makeArray($(x).find('.message_time').map(function(i, x){return x.innerText})),
			stream : jQuery.makeArray($(x).find('.stream_label').map(function(i, x){return x.innerText})),
			subject : jQuery.makeArray($(x).find('.narrows_by_subject').map(function(i, x){return x.innerText}))
		};})

	data = jQuery.makeArray(data_jq);

	// If we found some new DOM nodes
	if (scrape.old_length < data.length) {

		// Slice them free
		delta = data.slice(scrape.old_length, data.length);
		scrape.old_length = data.length;

		var s = JSON.stringify(delta);
		console.log("Scraper.js: "+ delta.length+" new objects." );

		// Send delta to background.js, which isn't origin-sandboxed
		// http://developer.chrome.com/extensions/messaging.html
		chrome.extension.sendMessage({data: s});
	}
}

scrape.old_length = 0;
setInterval(scrape,1000);