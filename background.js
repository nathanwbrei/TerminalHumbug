
// Background.js receives the JSON of humbug messages
chrome.extension.onMessage.addListener(
  function(request, sender, sendResponse) {
  	if (request.data) {
  		console.log("Background.js has received a scraping!");
    	var r = new XMLHttpRequest();
    	r.open('POST', 'http://localhost:5000/humbug', true);
    	r.send(request.data);
    }
  });