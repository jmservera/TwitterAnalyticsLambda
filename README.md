# Twitter Analytics Lambda

A [lambda architecture](https://en.wikipedia.org/wiki/Lambda_architecture) using Azure managed services for Twitter Analytics.

Uses [Tweepy](https://github.com/tweepy/tweepy) inside a small Docker web app that will be run inside a Web App for Linux Containers in Azure, connected to an Event Hubs to partition the data an analyze it with a Stream Analytics query that uses a Machine Learning endpoint to get sentiment from the tweets.
The ASA output goes to PowerBI to show the information in realtime.

