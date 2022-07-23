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
    count: 1
};


const args = JSON.stringify(process.argv.slice(2));
let tweetSearchTerm = args.split('=')[1].slice(0, -2)

params.q = tweetSearchTerm;
console.log('You are searching for tweets by: ' + params.q)



let data = '';

twitterClient.tweets.search(params).then(tweet => {
    data = JSON.stringify(tweet);

    // write JSON string to a file
    fs.writeFile('./tmp/data.json', data, (err) => {
        if (err) {
            throw err;
        }
        console.log("JSON data is saved.");
    });
}).catch(e => {
    console.error(e)
})