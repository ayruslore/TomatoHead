var ConversationV1 = require('watson-developer-cloud/conversation/v1');
var prompt =require('prompt-sync')();
//setup conversation service wrapper

var conversation = new ConversationV1({
	username:"48c3f747-294d-4db4-8602-70dad10b4233" ,
	password:"FGxkTZmQjLoG",
	path: {workspace_id:"8b949fe3-319c-4414-a956-f839cf8f4fa3"},
	version_date: '2017-04-25'
});

//start conversation

conversation.message({},processResponse);
//conversation.message({input :{text:"i want butter chicken"}},processResponse);
 

// Process the conversation response.
function processResponse(err, response) {
  if (err) {
    console.error(err); // something went wrong
    return;
  }

  // If an intent was detected, log it out to the console.
  if (response.intents.length > 0) {
    console.log('Detected intent: #' + response.intents[0].intent);
  }
  
  // Display the output from dialog, if any.
  if (response.output.text.length != 0) {
      console.log(response.output.text[0]);
  }

  // Prompt for the next round of input.
    var newMessageFromUser = prompt('>> ');
    // Send back the context to maintain state.
    conversation.message({
      input: { text: newMessageFromUser },
      context : response.context,
    }, processResponse)
}