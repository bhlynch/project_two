// Show that we've loaded the JavaScript file
console.log("Loaded main.js");

// Query the endpoint that returns a JSON ...
d3.json("/fires").then(function (data) {

    // ... and dump that JSON to the console for inspection
    console.log(data); 

});