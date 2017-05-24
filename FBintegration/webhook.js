const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const server = app.listen(process.env.PORT || 4000, () => {
  console.log('Express server listening on port %d in %s mode', server.address().port, app.settings.env);
});


//facebook validation

app.get('/', (req, res) => {
  console.log('checking');
  if (req.query['hub.mode'] === 'subscribe' && req.query['hub.verify_token'] === 'tuxedo_cat') {
    console.log("Validating webhook");
    res.status(200).send(req.query['hub.challenge']);
  } else {
    console.error("failed");
    res.status(403).end();
  }
});

/* Handling all messenges */
app.post('/', (req, res) => {
  console.log(req.body);
  if (req.body.object === 'page') {
    req.body.entry.forEach((entry) => {
      entry.messaging.forEach((event) => {
        if (event.message && event.message.text) {
//	  console.log(event.message);
//	  console.log(event.message.text);
          sendMessage(event);
        }
      });
    });
    res.status(200).end();
  }
});

//sending messages

const request = require('request');

function sendMessage(event) {
  let sender = event.sender.id;
  let text = event.message.text;

  request({
    url: 'https://graph.facebook.com/v2.6/me/messages',
    qs: {access_token: 'EAAGeBZBDgxFUBANENmy0tRI8vg3xig2fdprAO305W3dqZBCbTcnVT0Eu9H2tio9YgaD69NlRjNB2VwR6po2BIqzD7QojZBpzDGn672gwf38TFV2MV9F1s1zvoSIpF9xPV6vtmPxrovbNg4u0hcqZBNtSZCb7hdZAQqZBYf7OQYSsgZDZD'},
    method: 'POST',
    json: {
      recipient: {id: sender},
      message: {text: text}
    }
  }, function (error, response) {
    if (error) {
        console.log('Error sending message: ', error);
    } else if (response.body.error) {
        console.log('Error: ', response.body.error);
    }
  });
}
