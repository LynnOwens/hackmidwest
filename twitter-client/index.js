require('dotenv').config()
const { TwitterClient } = require('twitter-api-client')

const fs = require('fs');
const express = require('express');



const app = express();
const port = 5000;
app.use(express.static('../twitter-client'));

//Idiomatic expression in express to route and respond to a client request
app.get('/', (req, res) => { //get requests to the root ("/") will route here
    res.sendFile('input_term.html', { root: '../hackmidwest/website/templates' }); //server responds by sending the index.html file to the client's browser
    //the .sendFile method needs the absolute path to the file, see: https://expressjs.com/en/4x/api.html#res.sendFile 
});

app.listen(port, () => { //server starts listening for any attempts from a client to connect at port: {port}
    console.log(`Now listening on port ${port}`);
});

const twitterClient = new TwitterClient({
    apiKey: process.env.TWITTER_API_KEY,
    apiSecret: process.env.TWITTER_API_SECRET,
    accessToken: process.env.TWITTER_ACCESS_TOKEN,
    accessTokenSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET
})

function handleFormSubmission() {
    var inputValue = document.getElementById("term").value;
    console.log(inputValue)

    let params = {
        q: inputValue,
        count: 4
    };

    searchTwitterAndSaveData(params);

    // return inputValue;
}

const searchTwitterAndSaveData = (params) => {
    let data = '';
    twitterClient.tweets.search(params).then(tweet => {
        data = JSON.stringify(tweet);

        // write JSON string to a file
        fs.writeFile('twitter-client/tmp/data.json', data, (err) => {
            if (err) {
                throw err;
            }
            console.log("JSON data is saved.");
        });
    }).catch(e => {
        console.error(e)
    })
};