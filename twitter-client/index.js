require('dotenv').config()
const { TwitterClient } = require('twitter-api-client')
const fs = require('fs');

const twitterClient = new TwitterClient({
    apiKey: process.env.TWITTER_API_KEY,
    apiSecret: process.env.TWITTER_API_SECRET,
    accessToken: process.env.TWITTER_ACCESS_TOKEN,
    accessTokenSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET
})

const params = {
    q: `UberConf`,
    count: 4
};

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