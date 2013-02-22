
// Background.js receives the JSON of humbug messages
chrome.extension.onMessage.addListener(
  function(request, sender, sendResponse) {
  	if (request.data) {
  		console.log("Background.js has received a scraping!");
    	sendResponse({farewell: "Thanks from background.js"});
    	var r = new XMLHttpRequest();
    	r.open('POST', 'http://localhost:5000/humbug', true);
    	r.send(request.data);
    }
  	else {
  		console.log("Background.js received something, but something didn't work.");
  	}
  });