
// Runs when extension installed.
chrome.runtime.onInstalled.addListener(function() {
  // chrome.contextMenus.create({
  //   "id": "sampleContextMenu",
  //   "title": "Sample Context Menu",
  //   "contexts": ["selection"]
  // });
});


// Runs on web navigation.
chrome.webNavigation.onCompleted.addListener(function({errorOccured, url, parentFrameId}) {
  alert(`this is the motherfucking url: ${url}`)
  sendUrlToServer(url)
}, 
// event filter: {url: [{urlMatches : 'https://www.google.com/'}]}
);

function sendUrlToServer(url) {
  fetch('http://localhost:8000/urls', {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'omit',
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow',
    referrer: 'no-referrer', // no-referrer, *client
    body: JSON.stringify({
      url: url
    }), // body data type must match "Content-Type" header
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    console.log(JSON.stringify(myJson));
    alert(JSON.stringify(myJson));
  }).catch(err => {
    console.log(err)
    alert(err);
  })
}