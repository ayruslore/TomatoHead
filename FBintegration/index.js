var express = require('express');
var ConversationV1 = require('watson-developer-cloud/conversation/v1');

var app = express();

var contexts = [];

app.get('/smssent', function (req, res) {
  var message = req.query.Body;
  var number = req.query.From;
  var twilioNumber = req.query.To;

  var context = null;
  var index = 0;
  var contextIndex = 0;
  contexts.forEach(function(value) {
    console.log(value.from);
    if (value.from == number) {
      context = value.context;
      contextIndex = index;
    }
    index = index + 1;
  });

  console.log('Recieved message from ' + number + ' saying \'' + message  + '\'');

  var conversation = new ConversationV1({
    username: '32c747a9-3590-469b-89a8-78a87d17aa4a',
    password: 'sbH852xySFhx',
    version_date: ConversationV1.VERSION_DATE_2017_04_04
  });

  console.log(JSON.stringify(context));
  console.log(contexts.length);

  conversation.message({
    input: { text: message },
    workspace_id: '0d76e1dd-b2e8-4a65-bbf4-68d72c5b2d11',
    context: context
   }, function(err, response) {
       if (err) {
         console.error(err);
       } else {
         console.log(response.output.text[0]);
         if (context == null) {
           contexts.push({'from': number, 'context': response.context});
         } else {
           contexts[contextIndex].context = response.context;
         }

         var intent = response.intents[0].intent;
         console.log(intent);
         if (intent == "done") {
           //contexts.splice(contexts.indexOf({'from': number, 'context': response.context}),1);
           contexts.splice(contextIndex,1);
           // Call REST API here (order pizza, etc.)
         }

         var client = require('twilio')(
           'ACb879a3e6e52da2fa7d84ffa4eb8f430d',
           'd8ef0c4030fcf1e2c704df809bcdb1c5'
         );

         client.messages.create({
           from: twilioNumber,
           to: number,
           body: response.output.text[0]
         }, function(err, message) {
           if(err) {
             console.error(err.message);
           }
         });
       }
  });

  res.send('');
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
